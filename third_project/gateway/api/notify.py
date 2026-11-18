import requests
from fastapi import APIRouter, HTTPException

from third_project.gateway.domain.events import Event
from third_project.gateway.infra import message_forwarder
from third_project.gateway.infra.channels import CHANNELS

router = APIRouter()


@router.post('/notify', status_code=201)
def notify(event: Event) -> None:
    failed = []
    for name in message_forwarder.forward(event.model_dump()):
        try:
            CHANNELS[name].send(event.visible_text)
        except requests.RequestException:
            failed.append(name)
    if failed:
        raise HTTPException(status_code=502, detail=f'delivery failed: {", ".join(failed)}')

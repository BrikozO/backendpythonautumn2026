from third_project.gateway import config


def forward(event: dict) -> list[str]:
    return config.ROUTES.get(event.get('source', ''), ['console'])

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

from third_project.gateway import config, router
from third_project.gateway.channels import CHANNELS


class NotifyHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path != '/notify':
            self.send_error(404, 'unknown path')
            return
        length = int(self.headers.get('Content-Length', 0))
        try:
            event = json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            self.send_error(400, 'invalid JSON')
            return
        if not isinstance(event, dict) or 'text' not in event:
            self.send_error(400, 'field "text" is required')
            return

        text = f'{event.get("source")}: {event["text"]}'
        failed = []
        for name in router.route(event):
            try:
                CHANNELS[name].send(text)
            except requests.RequestException:
                failed.append(name)
        if failed:
            self.send_error(502, f'delivery failed: {", ".join(failed)}')
            return

        self.send_response(201)
        self.end_headers()


def run() -> None:
    with HTTPServer(('', config.PORT), NotifyHandler) as httpd:
        print(f'слушаю :{config.PORT}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

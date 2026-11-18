from third_project.gateway import config


def route(event: dict) -> list[str]:
    return config.ROUTES.get(event.get('source', ''), ['console'])

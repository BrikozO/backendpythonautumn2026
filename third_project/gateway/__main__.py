import uvicorn

from third_project.gateway import server
from third_project.gateway.infra.channels import console

console.send('gateway запущен')
uvicorn.run(server.app, host='0.0.0.0', port=8000)

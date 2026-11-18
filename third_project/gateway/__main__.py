from third_project.gateway import server
from third_project.gateway.channels import console

console.send('gateway запущен')
server.run()

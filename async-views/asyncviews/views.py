import asyncio
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


# serve para demonstrar como funciona o async
# vai retornar o HttpResponse primeiro e depois a função do loop
async def async_view(request):
    # funciona para criar task para funções async
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking FTTP request')


# asyncio.get_event_loop() Ele monitora e gerencia as tarefas assíncronas, agendando quando devem ser
# executadas e lidando com eventos de I/O (como leitura de arquivos,
# solicitações de rede, etc.) de maneira não bloqueante. Ele permite que o código
# execute múltiplas tarefas de forma "concorrente", sem precisar de várias threads.

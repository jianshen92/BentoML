from starlette.applications import Starlette
from starlette.responses import StreamingResponse
from starlette.routing import Route
import asyncio
import time

async def hello(request):
    async def event_stream():
        i = 0
        while True:
            yield f"data: Hello, world! Time: {time.time()}\n\n"
            await asyncio.sleep(1)
            i += 1
            if i > 5:
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream")

routes = [
    Route("/hello", hello)
]

app = Starlette(debug=True, routes=routes)
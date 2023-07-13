# This is your Server A.
# It receives the request from the user and forwards the stream from Server B.

from starlette.responses import StreamingResponse
from starlette.applications import Starlette
import httpx
import aiohttp
import asyncio
import time

app = Starlette()

# async def event_stream(response):
#     async for line in response.aiter_lines():
#         print(line)
#         yield line.encode("utf-8") + b"\n"

async def event_stream():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8000/hello') as resp:
            async for line in resp.content.iter_any():
                ctime = f"proxytime : {time.time()}"
                yield line

@app.route("/sse")
async def sse_endpoint(request):

    return StreamingResponse(event_stream(), media_type="text/event-stream")


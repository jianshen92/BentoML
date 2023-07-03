import bentoml

class SSERunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = False

    @bentoml.Runnable.method(batchable=False)
    def predict(self, ins:str):
        # for i in range(10):
        return f"given {ins}"

async def run(ins:str):
    return f"given {ins}"

from starlette.responses import StreamingResponse
# from starlette.routing import Route
import asyncio
# import time

# async def hello():
async def event_stream():
    for i in range(5):
        yield f"{i} \n\n"
        await asyncio.sleep(1)

    # return StreamingResponse(event_stream(), media_type="text/event-stream")
     

sse_runner = bentoml.Runner(SSERunnable)

# svc = bentoml.Service("sse", runners=[sse_runner])
svc = bentoml.Service("sse")

@svc.stream(input=bentoml.io.Text(), output=bentoml.io.TextStream())
async def predict(input_text:str):
    # ret = await sse_runner.predict.async_run(input_text)
    # return await run(input_text)
    # ret = await event_stream()
    return event_stream()

import bentoml

class SSERunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = False

    @bentoml.Runnable.method()
    def predict(self, ins:str):
        # for i in range(10):
        return f"given {ins}"


sse_runner = bentoml.Runner(SSERunnable)

svc = bentoml.Service("sse", runners=[sse_runner])

@svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
async def predict(input_text:str) -> str:
    ret = sse_runner.predict.run(input_text)
    return ret


import bentoml
import asyncio

class SSERunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    @bentoml.Runnable.stream_method()
    async def count(self, input_text:str):
        for i in range(10):
            await asyncio.sleep(1)
            yield f"async {i} {input_text} \n\n"

    @bentoml.Runnable.stream_method()
    async def generate(self, prompt:str):
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        from transformers import AutoTokenizer, TextIteratorStreamer
        from threading import Thread

        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

        inputs = tokenizer(prompt, return_tensors="pt")
        streamer = TextIteratorStreamer(tokenizer)
        generation_kwargs = dict(inputs, streamer=streamer, max_new_tokens=300)
        thread = Thread(target=model.generate, kwargs=generation_kwargs)
        thread.start()

        for new_text in streamer:
            yield f"{new_text} \n\n"

sse_runner = bentoml.Runner(SSERunnable)
svc = bentoml.Service("sse", runners=[sse_runner])

@svc.stream(input=bentoml.io.Text(), output=bentoml.io.TextStream())
async def count(input_text:str):
    ret = await sse_runner.count.async_run(input_text)
    return ret

@svc.stream(input=bentoml.io.Text(), output=bentoml.io.TextStream())
async def generate(input_text:str):
    ret = await sse_runner.generate.async_run(input_text)
    async for i in ret:
        yield i 

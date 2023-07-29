#%%
import this
from typing import Any
# import anyio
# import time

# async def async_task():
#     print("Starting async task...")
#     await anyio.sleep(2)
#     print("Finished async task!")

# def sync_task():
#     print("Starting sync task...")
#     time.sleep(2)
#     print("Finished sync task!")
#     anyio.from_thread.run(async_task)

# async def main_async():
#     # This is the entry point for AnyIO's event loop.
#     # We'll start the synchronous task from here.
#     await anyio.to_thread.run_sync(sync_task)

# # def main():
# #     # We start the AnyIO event loop by running main_async()
# #     anyio.run(main_async)

# if __name__ == "__main__":
#     anyio.run(main_async)
#%%
import httpx
import asyncio

async def listen_to_sse(url: str):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            async for line in response.aiter_lines():
                print(line)

await listen_to_sse('http://localhost:8001/sse')
# %%
import aiohttp
import asyncio

async def consume_sse():
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{http://localhost:3000}/predict') as resp:
            async for line in resp.content.iter_any():
                print(line)

await consume_sse()

#%%
# %%
import aiohttp
import asyncio

async with aiohttp.ClientSession() as session:
    async with session.post(f'http://localhost:8000/s') as resp:
        async for line in resp.content.iter_any():
            print(line)

# %%
import bentoml
# from starlette.responses import StreamingResponse
# from starlette.routing import Route
import asyncio
import aiohttp
import httpx
import time


class SSERunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    @bentoml.Runnable.stream_method()
    def sync_gen(self):
        for i in range(10):
            time.sleep(1)
            yield f"sync {i} \n\n"

    @bentoml.Runnable.stream_method()
    async def async_gen(self):
        for i in range(10):
            await asyncio.sleep(1)
            yield f"async {i} \n\n"

sse_runner = bentoml.Runner(SSERunnable)
# %%
sse_runner.runner_methods

#%%
sse_runner.init_client()

#%%
await sse_runner.async_gen.async_run()

# %%
def decorator(arg1):
    print(f"Decorator factory called with {arg1}")
    def actual_decorator(function):
        print("Applying decorator")
        def wrapper(*args, **kwargs):
            print(f"Before call with {arg1}")
            function(*args, **kwargs)
            print(f"After call with {arg1}")
        return wrapper
    return actual_decorator

@decorator(1)
def say_hello():
    print("Hello!")
# %%
import attr
import typing as t
@attr.define
class SN():
    func: t.Callable

    def __set_name__(self, owner, name):
        print(f"__set_name__ called with {owner} and {name}")


def dec(func=None):
    def inner(*args, **kwargs):
        return SN(func)
    return inner


class A:
    @dec()
    def method(self):
        pass

# %%
import bentoml

# %%
from bentoml.serve import serve_http_production

# %%
serve_http_production(".",".")

# %%
from typing import Any
class YO():

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call")
        return self
    
YO()()
# %%
import aiohttp
async with aiohttp.ClientSession() as session:
    async with session.post('http://localhost:3000/stream_predict') as resp:
        async for line in resp.content.iter_any():
            print(line)
# %%
# %%
from transformers import pipeline 
generator = pipeline('text-generation', model = 'gpt2')
# %%
generator("Hello, I'm a language model", max_length = 30, num_return_sequences=3)
# %%
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
inputs = tok(["An increasing sequence: one,"], return_tensors="pt")
streamer = TextIteratorStreamer(tok)

# %%
prompt = "A step by step recipe to make bolognese pasta:"
# %%
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

async def gen(prompt:str): 
    inputs = tokenizer(prompt, return_tensors="pt")
    streamer = TextIteratorStreamer(tokenizer)
    generation_kwargs = dict(inputs, streamer=streamer, max_new_tokens=20)
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        yield new_text

# %%


generated_text = ""
for new_text in streamer:
    generated_text += new_text
    print(generated_text)
# %%
await gen(prompt)
# %%
import inspect

async def t():
    yield 1

print(type(t()))
print(inspect.iscoroutinefunction(t))
print(inspect.isgenerator(t()))
print(inspect.isasyncgen(t()))
# %%
# %%
# %%

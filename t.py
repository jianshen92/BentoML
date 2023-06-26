import anyio
import time

async def async_task():
    print("Starting async task...")
    await anyio.sleep(2)
    print("Finished async task!")

def sync_task():
    print("Starting sync task...")
    time.sleep(2)
    print("Finished sync task!")
    anyio.from_thread.run(async_task)

async def main_async():
    # This is the entry point for AnyIO's event loop.
    # We'll start the synchronous task from here.
    await anyio.to_thread.run_sync(sync_task)

# def main():
#     # We start the AnyIO event loop by running main_async()
#     anyio.run(main_async)

if __name__ == "__main__":
    anyio.run(main_async)

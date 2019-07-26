import asyncio

async def myCoroutine():
    print("my coroutine")


async def main():
    await asyncio.sleep(1)

loop = asyncio.get_event_loop()

try:
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())

    pending = asyncio.Task.all_tasks()
    print(pedding)
    loop.run_until_complete(main())
finally:
    loop.close()

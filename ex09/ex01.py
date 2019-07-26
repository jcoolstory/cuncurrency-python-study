import asyncio

async def myCoroutine():

    print("simple event loop example")

def main():

    loop = asyncio.get_event_loop()

    loop.run_until_complete(myCoroutine())
    loop.close()

if __name__ == "__main__":
    main()

import asyncio
import time

async def myWork():
    print("starting work")
    time.sleep(5)

    print("eding work")

def main():

    loop = asyncio.get_event_loop()
    loop.run_until_complete(myWork())
    loop.close()

    print(loop.is_closed())

if __name__ == "__main__":
    main()

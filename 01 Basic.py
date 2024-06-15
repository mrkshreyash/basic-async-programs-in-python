import asyncio


async def hello_world():
    print("First Hello")
    await asyncio.sleep(1)
    print("Then World !")


asyncio.run(main=hello_world())
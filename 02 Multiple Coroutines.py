import asyncio


async def say(what: str, when: int):
    await asyncio.sleep(when)
    print(what)


async def main():
    await asyncio.gather(
        say("First", 2),
        say("Second", 3),
        say("Third", 1)
    )


asyncio.run(main=main())

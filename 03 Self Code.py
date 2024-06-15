import asyncio

import requests


async def count():
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(i)


async def google():
    endpoint = "https://www.google.com"
    data = requests.get(endpoint)
    await asyncio.sleep(6)
    print(f"Google Status Code: {data.status_code}")


async def gibberish():
    await asyncio.sleep(5)
    print(f"GIBBERISH: sjdfjdfljsldfkjl")


async def main():
    await asyncio.gather(
        count(), google(), gibberish()

    )


try:
    asyncio.run(main=main())

except Exception as e:
    print(e)

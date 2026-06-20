import asyncio

async def task():

    print("Start")

    await asyncio.sleep(2)

    print("End")

asyncio.run(task())






import asyncio


async def prints(name='ruven'):
    print(name)
    await asyncio.sleep(4)
    return {"data": 1}


async def calling():
    print("Good!!")
    await asyncio.sleep(2)
#asyncio.run(calling())

async def main():
    task1 = asyncio.create_task(prints('heee'))
    await task1
    print(task1.result())

asyncio.run(main())

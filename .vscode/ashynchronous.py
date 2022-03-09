import asyncio

# async def main():
#     print('Main Complete')
#     task= asyncio.create_task(func('Async call'))
#     await asyncio.sleep(1)
#     print('Finished')

# async def func(text):
#     print(text)
#     await asyncio.sleep(10)

# asyncio.run(main())

#2nd Program

async def fetch_Data():
    print('Start Fetching')
    await asyncio.sleep(2)
    print('Done Fetching')
    return {'data':1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
    

async def main():
    task1= asyncio.create_task(fetch_Data())
    task2= asyncio.create_task(print_numbers())

    value= await task1
    print(value)
    await task2



asyncio.run(main())

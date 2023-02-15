# import time
#
#
# def fun1(x):
#     print('fun1 on...')
#     print(f'x ** 2 = {x ** 2}')
#     print('fun1 off...')
#     time.sleep(3)
#     print('fun1 end')
#
#
# def fun2(x):
#     print('fun2 on...')
#     print(f'x ** 0.5 = {x ** 0.5}')
#     print('fun2 off...')
#     time.sleep(3)
#     print('fun2 end')
#
#
# def main():
#     fun1(4)
#     fun2(4)
#
#
# print(time.strftime('%X'), ': программа запущена')
# main()
# print(time.strftime('%X'), ': программа завершена')
#


# import asyncio
# import time
#
#
# async def fun1(x):
#     print(f'x ** 2 = {x ** 2}')
#     await asyncio.sleep(2.199)
#     print('fun1 end')
#
#
# async def fun2(x):
#     print(f'x ** 0.5 = {x ** 0.5}')
#     await asyncio.sleep(2.198)
#     print('fun2 end')
#
# print(time.strftime('%X'), ': программа запущена')
#
# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     task1 = loop.create_task(fun1(4))
#     task2 = loop.create_task(fun2(4))
#     loop.run_until_complete(asyncio.wait([task1, task2]))
#
# print(time.strftime('%X'), ': программа завершена')


# import asyncio
# import time
#
#
# async def fun1(x):
#     print(f'x ** 2 = {x ** 2}')
#     time.sleep(2.199)
#     print('fun1 end')
#
#
# async def fun2(x):
#     print(f'x ** 0.5 = {x ** 0.5}')
#     time.sleep(2.198)
#     print('fun2 end')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun1(4))
#     await task1
#     await task2
#
# print(time.strftime('%X'), ': программа запущена')
# asyncio.run(main())
# print(time.strftime('%X'), ': программа завершена')




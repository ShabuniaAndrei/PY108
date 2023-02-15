# import asyncio
#
#
# async def async_func(task_no):
#     print(f'{task_no}zapusk')
#     await asyncio.sleep(1)
#     print(f'{task_no}gotovo')
#
#
# async def main():
#     task_a = loop.create_task(async_func('taskA'))
#     task_b = loop.create_task(async_func('taskB'))
#     task_c = loop.create_task(async_func('taskC'))
#     await asyncio.wait([task_a, task_b, task_c])
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     asyncio.set_event_loop(loop)
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         pass


# import asyncio
# import time
# from aiohttp import ClientSession
#
#
# async def fetch_url_data(session, url):
#     try:
#         async with session.get(url, timeout=60) as response:
#             resp = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return resp
#     return
#
#
# async def fetch_async(r):
#     url = 'httpls://www.uefa.com/uefaeuro-2020/'
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session, url))
#             tasks.append(task)
#         responses = await asyncio.gather(*tasks)
#     return responses
#
#
# if __name__ == '__main__':
#     for ntimes in [1, 10, 50, 100, 500]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(fetch_async(ntimes))
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'получено {ntimes} результатов запроса за {time.time() - start_time} секунд')
#
#
# import threading
# import time
# import random
#
#
# def worker(number):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print('i worker {}, i slept {} seconds'.format(number, sleep))
#
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#
# print('Finish')

# #
# from threading import Thread
# from time import sleep
#
#
# class CustomThread(Thread):
#     def __inti__(self, limit):
#         Thread.__init__(self)
#         self._limit = limit
#
#     def run(self):
#         for i in range(self._limit):
#             print(f'from:{i}')
#             sleep(0.5)
#
#
# cth = Thread(target=CustomThread)
# print(cth.run())
# print('stop')
# a = [1, 3, 4, 5, 6]
# s = iter(a)
# print(s.__next__())
# print(s.__next__())

# class aa:
#     def __iter__(self):
#         self.x = 0
#         return self
#
#     def __next__(self):
#         y = self.x
#         self.x = 1
#         return y
#
#
# ite = aa()
# example = iter(ite)
#
# print(next(example))
# print(next(example))
#
#
# a = [i for i in 'helloworld']
# print(a)


# class aab:
#     def __iter__(self):
#         self.x = 0
#         return self
#
#     def __next__(self):
#         y = self.x
#         while y < 6:
#             self.x += 1
#             if y == 5:
#                 break
#             return y
#
#
# ite = aab()
# example = iter(ite)
# for i in example:
#     print(i)
#
#
# elem = [2, 4, 5, 6]
#
#
# def als(num):
#     for n in num:
#         yield n
#
#
# s = (i for i in elem)
# some = als(elem)
# print(als(elem))
# print(next(some))
# print(next(some))
# print(next(some))


# def func(num):
#     return (i for i in num if i % 2 == 0)
#
#
# gen_func = func(elem)
# print(gen_func)

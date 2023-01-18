# sum = 0
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for i in range(len(numbers)):
#     sum += numbers[i]**2
# print(sum)


# s = input()
# count = 0
# str = s.split()
# for i in range(len(str)-1):
#     num = int(str[i-1] + str[i-2])
#     for n in range(len(str)-3):
#         num_2 = int(str[i-1] + str[i])
#         if num_2 == num:
#             count += 1
# print(count)


# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# num_max = max(numbers)
# ind_max = numbers.index(num_max)
# num_min = min(numbers)
# ind_min = numbers.index(num_min)
# numbers.insert(ind_max, num_min)
# del numbers[ind_max+1]
# numbers.insert(ind_min, num_max)
# del numbers[ind_min+1]
# print(*numbers)zz


#
# palindromes = [i for i in range(100, 1000) if  i % 10 == i // 100]
# print(palindromes)
# new_keywords = [m for m in keywords if len(m) >= 5]
#
# print(new_keywords)

# объявление функции
# def draw_triangle():
#     for i in range(1, 11):
#         print('*'*i)
#
# # основная программа
# draw_triangle()  # вызов функции
# объявление функции
# def print_digit_sum(num):
#     count = 0
#     while num > 0:
#         count += num%10
#         num = num//10
#     print(count)

# вызываем функцию
# print_digit_sum(int(input()))

# def sum_digits(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
#
#
# print(sum_digits(int(input())))

# return [i for i if...]
#
# def get_factors(num):
#     str = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             str.append(i)
#
#     return str
# print(get_factors(int(input())))


# def get_factors(num):
#     return [n for n in range(1, num + 1) if num % n == 0]
#
#
# n = int(input())
# print(get_factors(n))
# def get_factors(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#
#     return count
# print(get_factors(int(input())))

# def find_all(target, symbol):
#     str = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             str.append(i)
#     return str
# print(find_all(input(), input()))
# print(find_all('abcdabcaaa', 'a'))
# print(find_all('abcadbcaaa', 'e'))
# print(find_all('abcadbcaaa', 'd'))


# # объявление функции
# def merge(list1, list2):
#     return sorted(list1+list2)
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# def merge(list1, list2):
#     result = list1 + list2   # создаем результирующий список
#     result.sort()            # сортируем список встроенным методом sort()
#     return result            # возвращаем отсортированный список
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = merge(list1, list2)  # вызываем функцию слияния двух отсортированных списков
# print(list3)


# n = int(input())
# lst = []
# lst2 = []
# for i in range(n):
#     numbers1 = [int(c) for c in input().split()]
#     lst.append(numbers1)
# for k in lst:
#     for j in k:
#         lst2.append(j)
# print(sorted(lst2))


def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        flag = True
    else:
        flag = False
n = int(input())
is_prime(n)
count = 0
while is_prime:
    n += 1
    for i in range(1, n+14):
        if n % i == 0:
            count += 1
    if count == 2:
        flag = True
        break
    else:
        flag = False
print(n)

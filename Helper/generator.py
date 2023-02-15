# n, m, k, x, y, z = (int(input()) for i in range(6))
# n, m, k, x, y, z = (int(input()) for _ in 'nmkxyz')

# [num for num in range(1, amount+1)]

# [print(len(set(input().lower()))) for x in range(int(input()))]
# print(*[len(set(input().lower())) for i in range(int(input()))], sep='\n')
# for _ in range(int(input())):
#     print(len(set(input().lower())))

# print(len(set(''.join(input().lower() for _ in range(int(input()))))))

# print(len(set([word.lower().strip('.,;:-?!') for word in input().split()])))  - количество слов в строке

# print(*(sorted(list(set([int(i) for i in input().split()])&set([int(i) for i in input().split()]))))) - повтор цифр
# print(*sorted(set(input().split()) & set(input().split()), key=int))  - повтор цифр

# s1, s2, s3 = set(input().split()), set(input().split()), set(input().split()),
# print(*sorted(set(s1)&set(s2)-set(s3), key=int, reverse = True))
#
# st1, st2, st3 = (set(input().split()) for _ in '123')
# print(*sorted(st1 & st2 - st3, key=int, reverse=True))


# print('YES' if set(input()).issuperset(set(input())) else 'NO')
# print(['NO', 'YES'][set(input()) >= set(input())])
#
# digits = {int(c) for c in input()}
# Общий вид генератора множеств следующий:
# {выражение for переменная in последовательность}

# digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}   # множество заполненное только цифрами строки

# print(len(set(input().lower().strip('@*!)^?').split())))  -  количество слов в тексте
# print(*sorted(set([i.lower().strip('.,();:') for i in sentence.split()])))  - список слов в тексте


# sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'
# words = sentence.lower().replace('.', '').replace(',', '').split()
# vowels = ['a', 'e', 'i', 'o', 'u']
# consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}

# result = [user['name'] for user in users if user['phone'].endswith('8')]
# print(*(sorted([user['name'] for user in users if user['email'] == ''])))
# print(*sorted([user['name'] for user in users if 'email' not in user or user['email'] == '']))

list1 = list(map(len, ['this', 'is', 'a', 'test']))
list2 = [len(word) for word in ['this', 'is', 'a', 'test']]
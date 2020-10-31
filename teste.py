#!/usr/bin/env python
# -*- coding: utf-8 -*-

#### ex 06

# import re
# s = 'This tea is not hot'
#
# nao = re.search('not', s)
# ruim = re.search('bad', s)
#
# if ruim:
#     nao = nao.span()[0]+3
#     ruim = ruim.span()[1]
#     if nao < ruim:
#         removing = s[0:nao] + s[ruim::]
#         new_text = removing.replace('not', 'good')
#         print(new_text)
#     else:
#         print(s)
# else:
#     print(s)

##################################################################

#### ex 08

# palavras = ['aba', 'xyz', 'aa', 'x', 'bbb']
# i = 0
# itens_iguais = []
#
# while i < len(palavras):
#     a = palavras[i]
#     if len(a) >= 2 and a[0] == a[-1]:
#         itens_iguais.append(a)
#     else:
#         pass
#     i += 1
#
# print(len(itens_iguais))

##################################################################

#### ex 09

# palavras = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# i = 0
# x_list = []
# all_list = []
# while i < len(palavras):
#     if palavras[i][0] == 'x':
#         x_list.append(palavras[i])
#     else:
#         all_list.append(palavras[i])
#     i += 1
#
# final_list = (sorted(x_list)+sorted(all_list))
# print(final_list)


##################################################################

#### ex 10

# tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
#
# good_list = sorted(tuples, key=lambda x: x[-1])
#
#
# print(good_list)

##################################################################

#### ex 11


# nums = [2, 2, 3, 3, 3, 2, 2]
#
# # nums_drop = set(nums)
# # new_nums = list(nums_drop)
#
#
# new_nums = []
# last_pos = ''
#
# for i in nums:
#     if i != last_pos:
#         new_nums.append(i)
#         last_pos = i
#
#
# print(new_nums)

##################################################################

#### ex 12

# from heapq import merge
#
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
#
# print(list(merge(list1, list2)))

##################################################################

#### ex 13


# def mecanismo(texto):
#     lista = texto.read().lower()
#     a = []
#     b = []
#     c = []
#     for i in lista:
#         if i == 'a':
#             a.append(i)
#         elif i == 'b':
#             b.append(i)
#         elif i == 'c':
#             c.append(i)
#     tudo = {'a': len(a), 'b': len(b), 'c': len(c)}
#
#     return tudo
#
# texto = open("letras.txt", "r")
# tudo = mecanismo(texto)
#
#
# for key in sorted(tudo.keys()):
#     print(key , " " , tudo[key])
# #
# # print(tudo)
#
# listofTuples = sorted(tudo.items() ,  key=lambda x: x[1])
# for elem in listofTuples :
#     print(elem[0] , " " , elem[1] )

##################################################################

#### ex 14

from collections import defaultdict
import random

f = open("cronicanova.txt", "r")
texto = f.read().lower()
f.close()
palavras = ['']
palavras.extend(texto.split())
palavras.extend([''])
d = defaultdict(list)
for k, v in zip(palavras, palavras[1:]):
    d[k].append(v)

# print(d)

novo_texto = []
palavra = "eu"
for i in range(15):
    palavra = random.choice(d[palavra])
    novo_texto.append(palavra)

print(novo_texto)
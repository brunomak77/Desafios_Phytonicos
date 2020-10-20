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

# words = ['aba', 'xyz', 'aa', 'x', 'bbb']
# i = 0
# itens_iguais = []
#
# while i < len(words):
#     a = words[i]
#     if len(a) >= 2 and a[0] == a[-1]:
#         itens_iguais.append(a)
#     else:
#         pass
#     i += 1
#
# print(len(itens_iguais))

##################################################################

#### ex 09

# words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# i = 0
# x_list = []
# all_list = []
# while i < len(words):
#     if words[i][0] == 'x':
#         x_list.append(words[i])
#     else:
#         all_list.append(words[i])
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


nums = [2, 2, 3, 3, 3, 2, 2]

print(0 2)
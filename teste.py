#### ex 06
# a = 'abcde'
# b = 'xyz'
#
# # print(len(a))
# # print(len(b))
#
# moda = len(a) % 2
# sizea = len(a) / 2
# modb = len(b) % 2
# sizeb = len(b) / 2
#
# if moda != 0:
#     inia = int(sizea+1)
#     fima = int(sizea)
# else:
#     inia, fima = int(sizea), int(sizea)
#
# if modb != 0:
#     inib = int(sizeb+1)
#     fimb = int(sizeb)
# else:
#     inib, fimb = int(sizeb), int(sizeb)
#
# firsta = a[:inia]
# lasta = a[fima:]
# firstb = b[:inib]
# lastb =  b[fimb:]
#
# print(firsta)
# print(firstb)
# print(lasta)
# print(lastb)
#
# c = firsta+firstb+lasta+lastb
#
# print(c)

##################################################################

#### ex 08

words = ['aba', 'xyz', 'aa', 'x', 'bbb']
i = 0
itens_iguais = []

while i < len(words):
    a = words[i]
    if len(a) >= 2 and a[0] == a[-1]:
        itens_iguais.append(a)
    else:
        pass
    i += 1

print(len(itens_iguais))
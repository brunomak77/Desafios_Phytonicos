"""
08. match_ends

Dada uma lista de strings, retorne a itens_iguais do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    # +++ SUA SOLUÇÃO +++
    i = 0
    itens_iguais = []

    while i < len(words):
        a = words[i]
        if len(a) >= 2 and a[0] == a[-1]:
            itens_iguais.append(a)
        else:
            pass
        i += 1

    return len(itens_iguais)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
    test(match_ends, ['aac', 'beergxb', 'a', 'helloh'], 2)
    test(match_ends, ['aaasdcfasdf', 'asdfasdfe', 'abcasdfasdfa', 'hello'], 1)

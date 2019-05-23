
def descifrar(number, msg):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    b = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g',
    '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o',
    '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w',
    '24': 'x', '25': 'y', '26': 'z'}

    a = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
    'h': '8', 'i': '9','j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15',
    'p': '16', 'q': '17','r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
    'x': '24', 'y': '25', 'z': '26'}

    new_msg = ''
    for letra in msg:
        if letra not in letras:
            new_msg += letra
            continue
        temp = int(a[letra])
        temp = temp +number
        while temp > 26:
            temp %= 26
        new_msg += b[str(temp)]
    return new_msg


def cifrar():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    b = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g',
    '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o',
    '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w',
    '24': 'x', '25': 'y', '26': 'z'}

    a = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
    'h': '8', 'i': '9','j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15',
    'p': '16', 'q': '17','r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
    'x': '24', 'y': '25', 'z': '26'}

    number = int(input('quantas casas devem ser trocadas?\n>>>'))
    msg = list(str.lower(input('qual a msg?\n>>>')))
    new_msg = ''
    for letra in msg:
        if letra not in letras:
            new_msg += letra
            continue
        temp = int(a[letra])
        temp = temp +number
        while temp > 26:
            temp %= 26
        new_msg += b[str(temp)]
    return new_msg


def main():
    esc =  str.lower(input('cifrar/decifrar?\n>>>'))
    if esc == 'cifrar':
        print(cifrar())
    elif esc == 'decifrar':
        number = int(input('quantas casas devem ser trocadas?(0 pra brute force)\n>>>'))
        msg = list(str.lower(input('qual a msg?\n>>>')))
        if number == 0:
            for i in range(26):
                number = i
                print(descifrar(number, msg))
        elif 0 < number:
            print(descifrar(number, msg))
        else:
            print('deu algum erro ai vei')
    else:
        print('opção invalida, pnc!!!')

main()

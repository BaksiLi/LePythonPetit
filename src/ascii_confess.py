def convert_ascii(text, manual_return=False):
    text_ascii = ''

    for i in text:
        for j in i:
            if manual_return:
                print('{}({})'.format(text_ascii, j), end='')
                put_return = bool(input())
                if put_return:
                    text_ascii += '\n'
                    text_ascii += str(ord(j))
                else:
                    text_ascii += str(ord(j))
                    text_ascii += ' '
            else:
                text_ascii += str(ord(j))
                text_ascii += ' '
        text_ascii += ' '

    return (text_ascii)


def select_mode(menu):
    while True:
        try:
            print('Please select from the following mode: ')
            for k, v in menu.items():
                print('{}: {}'.format(v, k))
            choice = int(input(''))
            if choice not in menu:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid entry. Please try again.')
    return choice


if __name__ == "__main__":
    menu = {
        1: 'output as a line',
        2: 'output with returns manually',
    }

    text = str(input('Please enter your message: '))
    text_l = text.strip().split()  # obtain a list containing words
    mode = select_mode(menu)  # select mode from menu

    if mode == 1:
        print(convert_ascii(text_l))

    elif mode == 2:
        print(
            'Press enter to skip the current letter;\n'
            'Enter any keys to add a carriage return at the current position.'
        )
        print(convert_ascii(text_l, manual_return=True))

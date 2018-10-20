def check(wrd, inp):
    if inp == wrd:
        return True
    else:
        return False


if __name__ == "__main__":
    print('Welcome to this typing exercise.')
    while True:
        try:
            word = str(
                input('Please type in the word you\'d like to practice: '))
            f = 0
            n = int(input('the times of practice: '))
            for i in range(0, n):
                inpt = str(input('entry: '))
                if not check(word, inpt):
                    f += 1
                    print('ooops!')
            print('')
        except ValueError:
            print('Invalid entry, please try again.')
            continue
        finally:
            t = {'Number of trial: ': n, 'Failure': f}
            for x, y in t.items():
                print(x, y)
            break
    print('done!')

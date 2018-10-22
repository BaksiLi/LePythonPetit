import time

def check(wrd, inp):
    if inp == wrd:
        return True
    else:
        return False


if __name__ == "__main__":
    print('Welcome to this typing exercise.')

    while True:
        try:
            word = str(input('Please type in the word you\'d like to practice: '))
            n = int(input('the times of practice: '))
            f = 0  # failure

            if n <= 0:
                raise ValueError

            t_0 = time.time()  # count start time

            for i in range(0, n):
                entry = str(input('entry: '))
                if not check(word, entry):
                    f += 1
                    print('ooops!')

            t = round(time.time() - t_0, 2)
            accu = round((1 - f / n) * 100, 1)  # accuracy

            report =  {'Number of trial ': n, 'Failure ': f, 'Accuracy': accu, 'Time used ': t}

            print('')
            break

        except ValueError:
            print('Invalid entry, please try again.')

    for k, v in report.items():
        print('{}: {}'.format(k, v))

    print('done!')


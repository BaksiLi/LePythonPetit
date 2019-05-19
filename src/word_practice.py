import sys
import time


def analysis(failure: list, n: int):
    # TODO: use the Levenshtein Algorithm, since they may differ in length as
    # well (Hamming distance not applicable)
    print('Feature not completed so far.')

    # returns a coloured text with colour showing their failure frequencies.


if __name__ == "__main__":
    print('Welcome to this typing exercise.')

    ask_input = False
    try:
        word = sys.argv[1]
        print('The text going to practice is {}'.format(word))
    except IndexError or NameError:
        # No sys argv, then ask for input
        ask_input = True

    while True:
        try:
            if ask_input:
                word = str(
                    input("Please type in the word you'd like to practice: ")
                )
                print('The text going to practice is {}'.format(word))

            # Ask for times to practice
            n = int(input('the times of practice: '))
            if n <= 0:
                raise ValueError

            invalid_entries = []
            t_0 = time.time()  # count start time

            for i in range(0, n):
                entry = str(input('entry: '))
                if word != entry:
                    invalid_entries.append(entry)
                    print('ooops!')

            t = round(time.time() - t_0, 2)
            failure = len(invalid_entries)
            accuracy = round((1 - failure / n) * 100, 1)  # accuracy

            report = {
                'Number of trial ': n,
                'Failure ': failure,
                'Accuracy': accuracy,
                'Time used ': t,
            }

            print('')
            break

        except ValueError:
            print('Invalid entry, please try again.')

    # Print statistics
    print('...\nStatistics')
    for k, v in report.items():
        print('{}: {}'.format(k, v))

    # Ask if requires analysis
    ask_further = not bool(
        input('...\nReturn to see further analysis, other keys to exit.')
    )
    if ask_further:
        analysis(invalid_entries, n)

    print('\ndone!')
    exit()

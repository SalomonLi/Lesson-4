
import operator
import argparse

keys_job = {1 : operator.add, 2 : operator.sub, 3 : operator.mul, 4 : operator.truediv}

_help = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"


parser = argparse.ArgumentParser()
parser.add_argument('operations', help=_help, type=int, choices=[1, 2, 3, 4])
parser.add_argument('first_number', help="Enter number one.", type=int)
parser.add_argument('two_number', help="Enter number two.", type=int)
args = parser.parse_args()


def calc2(operation, a, b):
    operator = keys_job[operation]
    try:
     result = operator(a, b)
     print(result)
    except ZeroDivisionError:
        print("nie można rozdelic na 0 ")
    except KeyError:
        print(_help)
    return


if __name__ == "__main__":
    calc2(args.operations, args.first_number, args.two_number)
    while True:
        io = input("Continue Y / N\n").lower()
        if io == "n":
            exit()
        operations = int(input(f"{_help}\n"))
        first_number = int(input("Podaj perwszom liczbę:\n"))
        two_number = int(input("Podaj drugom liczbę:\n"))
        calc2(operations, first_number, two_number)



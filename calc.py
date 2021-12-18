import sys
import operator
import argparse

keys_job = {1 : operator.add, 2 : operator.sub, 3 : operator.mul, 4 : operator.truediv}

_help = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"

parser = argparse.ArgumentParser()

def parsers():
    parser.add_argument('operations', help=_help, type=int, choices=[1, 2, 3, 4])
    parser.add_argument('first_number', help="Enter number one.", type=int)
    parser.add_argument('two_number', help="Enter number two.", type=int)
    args = parser.parse_args()
    return args

def calc(args):
    try:
        print("Rezultat",keys_job[args.operations](args.first_number, args.two_number))
    except ZeroDivisionError:
        print("nie można rozdelic na 0 ")
    except KeyError:
        print(_help)



if __name__ == "__main__":
    calc(parsers())
    # print(parsers())
    while True:
        io = input("Continue Y / N\n").lower()
        if io == "n":
            exit()
        keys = int(input(f"{_help}\n"))
        a = int(input("Podaj perwszom liczbę:\n"))
        b = int(input("Podaj drugom liczbę:\n"))
        print("Rezultat\n", keys_job[keys](a, b))


import sys
import operator
import argparse

keys_job = {1 : operator.add, 2 : operator.sub, 3 : operator.mul, 4 : operator.truediv}

_help = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"

parser = argparse.ArgumentParser()

def parsers():
    parser.add_argument('operations', help=_help, type=int)
    parser.add_argument('first_number', help="Enter number one.", type=int)
    parser.add_argument('two_number', help="Enter number two.", type=int)
    args = parser.parse_args()
    return args

def calc(args):
    try:
        print("Rezultat",keys_job[args.operations](args.first_number, args.two_number))
    except ZeroDivisionError:
        print("nie mozna rozdelic na 0 ")
    except KeyError:
        print(_help)



if __name__ == "__main__":
    calc(parsers())
    while True:
        io = input("Continue Y / N\n").lower()
        if "n" == io:
            exit()
        keys = int(input(f"{_help}\n"))
        a = int(input("Podaj perwszom liczbę:\n"))
        b = int(input("Podaj drugom liczbę:\n"))
        print("Rezultat\n",keys_job[keys](a, b))








    # if len(sys.argv) > 1 < 3:
    #     # if sus.argv[1] == int and sus.argv[2] == int and sus.argv[3] == int:
    #     keys, a, b = sys.argv[1:]
    #     keys_job[keys](a,b)
    #
    # elif len(sys.argv) > 3:
    #     print("Zaduzo argumentuv")
    # elif len(sys.argv) <= 1:
    #     print("nie bylo podane zadnyh argumentuw do calkulatora")
    #
    # while True:
    #     io = input("Continue Y / N\n").lower()
    #     if "n" == io:
    #         exit()
    #     keys = int(input(
    #         "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n"))
    #     a = int(input("Podaj perwszom liczbę:\n"))
    #     b = int(input("Podaj drugom liczbę:\n"))
    #     keys_job[keys](a,b)
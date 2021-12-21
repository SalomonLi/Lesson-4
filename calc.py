
import operator
import argparse

keys_job = {1 : operator.add, 2 : operator.sub, 3 : operator.mul, 4 : operator.truediv}

_help = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('operations', help=_help, type=int, choices=[1, 2, 3, 4])
    parser.add_argument('first_number', help="Enter number one.", type=int)
    parser.add_argument('two_number', help="Enter number two.", type=int)
    args = parser.parse_args()
    parsers_resul = args.operations, args.first_number, args.two_number
    return parsers_resul

def calc2(args):
    operation, a, b = args
    operator = keys_job[operation]
    result = operator(a, b)
    return result

def input_users():
    operations = int(input(f"{_help}\n"))
    first_number = int(input("Podaj perwszom liczbę:\n"))
    two_number = int(input("Podaj drugom liczbę:\n"))
    resul = operations, first_number, two_number
    return resul

def main():
    print(calc2(parser()))
    while True:
        io = input("Continue Y / N\n").lower()
        if io.lower() == "help":
            print(_help)
            continue
        if io.lower() in {"quit", "exit", "n"}:
            raise SystemExit()
        try:
            print(calc2(input_users()))
        except ZeroDivisionError:
            print("nie mozna rozdelic na 0")
        continue


if __name__ == "__main__":
    main()



import sys

def calc(znak, a, b):
    """1 = + \ 2 = - \ 3 = * \ 4 = / """
    if znak == 1:
        print("Rezultat", a+b)
    elif znak == 2:
        if a>b:
            print("Rezultat", a-b)
        else:
            print("Rezultat", b-a)
    elif znak == 3:
        print("Rezultat", a*b)
    elif znak == 4:
        try:
            print("Rezultat", a/b)
        except ZeroDivisionError:
            print("ZeroDivisionError\n nie mozna rozdelic na 0")

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        znak, a, b = sys.argv[1:]
        calc(int(znak), int(a), int(b))
    elif len(sys.argv) <= 1:
        print("nie bylo podane zadnyh argumentuw do calkulatora")
    while True:
        io = input("Continue Y / N\n").lower()
        if "n" == io:
            exit()
        znak = int(input(
            "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n"))
        a = int(input("Podaj perwszom liczbę:\n"))
        b = int(input("Podaj drugom liczbę:\n"))
        calc(znak, a, b)

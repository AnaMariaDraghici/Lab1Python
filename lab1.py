import random

def Sum(n):
    rez=0
    i=1
    while n+1>i:
        random_number=random.randint(1,1000)
        rez=rez+random_number
        print(random_number)
        i+=i
    return rez

def Prim(n):
    i=2
    if n<2:
        return 0
    else:
        while i<n:
            if n%i == 0:
                return 0
            i+=1
    return 1

def CMMDC(n):
    m = int(input("Alege m-ul ce vrei sa il folosesti: "))
    if n == 0:
        return m
    elif m == 0:
        return n
    while m:
        n, m = m, n % m
    return n
def main():
    n = int(input("Alege n-ul ce vrei sa il folosesti: "))
    print("n =", n)

    choice = int(input("Alege ce algoritm vrei sa incepi (1 to 3):\n1. Suma a n numere naturale \n2. Verificam daca n este prim\n3. Cel mai mare divizor comun dintre n si inca un numar\n"))
    if choice == 1:
        rez = Sum(n)
        print("Suma a n numere random este:", rez)
    elif choice == 2:
        if Prim(n) != 0:
            print("Numarul",n,"este prim")
        else:
            print("Numarul",n,"nu este prim")
    elif choice == 3:
        c = CMMDC(n)
        print("Cel mai mare divizor comun este", c)
    else:
        print("NOPE. I wish you have an amazing day though!")
        return
if __name__ == "__main__":
    main()

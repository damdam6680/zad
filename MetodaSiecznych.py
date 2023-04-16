def f(x):
    return pow(x,3) - 2*x - 5


def main():
    in1 = input("podaj x1: \n")
    in2 = input("podaj x2: \n")

    x1 = int(in1)
    x2 = int(in2)

    f1 = f(int(x1))
    f2 = f(int(x2))
    

    i = input("podaj liczbe iteracji: ")
    
    i = int(i)
    ex = 0.0000000001

    while i > 0 and (abs(x1 - x2) > ex):
        if(abs(x1 - x2) < ex):
            print("Złe punkty startowe")
            return
        x0 = x1 - (f1 * ((x1 - x2)  / (f1 - f2)))
        f0 = f(x0)
        if(f0 < ex):
            print("wynik ",x0)
            return
            
        x2 = x1
        f2 = f1
        x1 = x0 
        f1 = f0

        i = i - 1

        if(i == 0):
            print("przekroczona limit obiegów")
            return

        

if __name__ == "__main__":
    main()

from sympy import Symbol, diff
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


def f(x):
    return x ** 3 - 2 * x ** 2 - 4 * x - 7
def pochodna():
    x = Symbol('x')
    temp = x ** 3 - 2 * x ** 2 - 4 * x - 7
    df = diff(temp, x)
    return df
def fp(x):
    wynik =  eval(str(pochodna()))
    return wynik

def main():
    import_or_install("sympy")
    x0 =  float(input("podaj x0:"))

    x1 = x0 -1 
    f0 = f(x0)
    i = 0
    ex = 0.0000000001

    while i < 256 and (abs(x1 - x0) > ex and (abs(f0) > ex )):
        f1 = fp(x0)
        
        if(abs(f1) < ex):
            print("Zły punkt startowy")
            return
        x1 = x0
        x0 = x0 - (f0/f1)
        f0 = f(x0)

        i = i + 1

        if(i == 0):
            print("przekorczona limit obiegow")
            return
        if(abs(x1 - x0) > ex or abs(f0) > ex):
            print("i =",i," = ",x0)   
        
                    

if __name__ == "__main__":
    main()

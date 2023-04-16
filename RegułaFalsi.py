def f(x):
    return pow(x,3) - 2*x - 5 

def main():

    ex = 0.0000000001
    n = 256
    a = int(input("podaj a:"))
    b = int(input("podaj b:"))

    fa = f(a)
    fb = f(b)


    if(fa * fb > 0):
        print("nie spełnia warunków ")
        return
    
    while True:
        x0 = ((fa * b) - (fb * a))/(fa - fb)
        if(n == 0):
            print("error")
            return
        else:
            n = n -1
        fx = f(x0)

        if(abs(fx) < ex):
            print("Wynik dla x",n," = ",fx)
            return
        if(fx * fa < 0):
            b = x0
            fb = fx
        else:
            a = x0
        fa = fx
    


main()
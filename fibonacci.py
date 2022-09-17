def fibonacci(n,memoizacion):
    global str1
    if(n in memoizacion): return memoizacion[n]

    if(n==0): return 0
    if(n==1): return 1
    memoizacion[n]= fibonacci(n-1,memoizacion) + fibonacci(n-2,memoizacion)
    str1 = str1 + " " + str(memoizacion[n])
    return memoizacion[n]

global str1
str1 = ""
memoizacion = {}
memo = {}
memo = fibonacci(5,memoizacion)
if(memo==0):
    print("Resultado: " + memo)
if(memo==1):
    print("Serie: " + str(1))
    print("Resultado" + memo)
else:
    print("Serie: " + str(1) + str1[0:len(str1)-2])
    print("Resultado: " + str1[len(str1)-2:len(str1)])

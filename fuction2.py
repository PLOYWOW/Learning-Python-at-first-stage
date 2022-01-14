def fac(x):
    if x > 1:
        print(x)
        result = x + fac(x-1)
        return result
        #return x*fac(x-1)  #6*5*fac(4)
    else:
        return 1

print(fac(3))
    




     


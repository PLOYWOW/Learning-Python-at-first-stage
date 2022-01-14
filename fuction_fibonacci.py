#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# a b c 
#   a b c
#     a b c
#         a b c
#           a b  c
#             a  b  c
#                a  b  c   
#a = 0
#b = 1
#print(a)
#print(b)
c = 0
def fib(x):
   
    # if x <= 2:
    #     if x == 1:
    #         return print("1")
    #     if x == 2:
    #         return print("1 1")
    if x == 1:
        #print("c =",c,"x =",x)
        return 0
    if x > 2: # 3 เป็นต้นไป
        c = fib(x-2)+fib(x-1)
        #print("c =",c,"x =",x)
        return c
    else: # x = 2
        #print("c =",c,"x =",x)
        return 1

#print(fib(2))

for i in range(15):
    print(fib(i+1), end = " ")

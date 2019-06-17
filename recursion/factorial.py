i=0
def fact(x):
  if x==1:
    print "base return"
    return 1
  else:
    print  x
    return x * fact(x-1)

y = 4  # or y = int(raw_input()) 
print(fact(y))


'''
Below is the recursion logic:

calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
'''

'''
Consider a stack of N number of cards which are piled up and in facing down. 
Each card has a unique number from the range 1 to N. The card is stacked in 
such a way that it exhibits the following behavior: Take the first card and 
put it under the stack without revealing. Now the next card on the top will 
have the number 1 on it. Next take 2 cards one after the other and put is under
the stack without revealing. Yes you guessed it right - the next card on the 
top will reveal a value of 2. This goes on. 
Eg. for such a series : 9,1,8,5,2,4,7,6,3,10 [for N=10] Write a program to 
generate such a series for a given N number of cards so that this behavior 
can be exercised.
'''

#!python

#Below is program for N=100

d = []
N=100
for i in range(1, N+1):
    if(i==1):
        d.append(1) #[i] = 1
    else:
        x = d[i-2] + i + 1
        if(x>N):
            break
        else:
            d.append(x)

for i in range(len(d)):
    d[i] += 1

dic = {}
k=1
for i in d:
    try:
        dic[i] = k
    except:
        dic[i] = k
    k=k+1

for i in range(1,N+1):
    try:
        print dic[i]
    except:
        print random.randint(1,N)

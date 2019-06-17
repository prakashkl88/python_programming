#!python

'''
Program to sort an array in ascending
order using selection-sort algorithm
'''

a = [0, 26, 54, 93, 17, 0, 77, 31, 44, 55, 20] 

def find_max(k):
    j = 0 
    mx = a[0]
    max_index = 0 
    for j in range(0,k):
        if(mx < a[j]):
            mx = a[j]
            max_index = j 
    return max_index

def swap(x,y):
    if(a[y] < a[x]):
        temp = a[x]
        a[x] = a[y]
        a[y] = temp

for i in range(0,len(a)):
    mi = find_max(len(a)-i-1)
    swap(mi,len(a)-i-1)

print(a)

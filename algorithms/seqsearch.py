def seqsearch1 (S, x):
    location = 0
    for i in S:
        if i == x:
            return location
        location += 1
    return 0

def seqsearch2 (S, x):
    n = len(S) - 1
    location = 1
    while(location <= n and S[location] != x):
        location += 1
    if(location > n):
        location = 0
    return location

S = [0, 10, 7, 11, 5, 13, 8]
x = 4
location = seqsearch1(S, x)
location2 = seqsearch2(S, x)
print('location =', location)
print('location2 =', location2)
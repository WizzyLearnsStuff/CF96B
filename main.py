n = int(input())

m = 10 ** 18
def brute(depth, num, num_4, num_7):
    if num_4 == num_7:
        if num >= n:
            global m
            if num < m:
                m = num
    if depth == 0:
        return
    brute(depth - 1, num * 10 + 4, num_4 + 1, num_7)
    brute(depth - 1, num * 10 + 7, num_4, num_7 + 1)
        
        
brute(10, 0, 0, 0)
print(m)

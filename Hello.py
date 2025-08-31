def find_sum(a):
    sum = 0
    for i in range(a):
        print(sum,i)
        sum += i
    return sum

print(find_sum(10))

# Can you give me a pythron script to generate fibanacci series?

def fibonacci(n):   
    a, b = 0, 1
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci(10))





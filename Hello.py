def find_sum(a):
    sum = 0
    for i in range(a):
        print(sum,i)
        sum += i
    return sum

<<<<<<< HEAD
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




=======
print('The result is:',find_sum(10))
print('Just commiting this line')
>>>>>>> 7ec9ef18ec53d94e8f0f0bc82363f84b44d7f529

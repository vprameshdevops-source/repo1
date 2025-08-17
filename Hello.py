def find_sum(a):
    sum = 0
    for i in range(a):
        print(sum,i)
        sum += i
    return sum

print(find_sum(10))
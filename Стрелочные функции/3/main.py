def carry(f):
    return lambda a: lambda b: f(a, b)
  
if __name__ == '__main__':
    avg = lambda a, b: (a + b)/2
    avg1 = carry(avg)(1) # lambda 1: ...
    print(avg1(5)) # lambda 5: f(1, 5)
    print(avg(4, 5))
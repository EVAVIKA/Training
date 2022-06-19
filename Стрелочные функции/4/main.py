if __name__ == '__main__':
    a = []
    i = 0
    while i < 1000:
        a.append(i)
        i += 1
         
    print(a)
    f = lambda a, b: a * a * b if a != 0 and b != 0 else 1
    i = 0
    while i < len(a): 
        a[i] = f(a[i], a[i - 1] if i != 0 else 1)
        i += 1
    print(a)
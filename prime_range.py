def main():
    a = int(input())
    b = int(input())
    p = []
    for num in range(a+1,b):
        if isprime(num):
            p.append(num)
    print(",".join([str(i) for i in p]))

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    main()
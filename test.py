def factorial():
    n = int(input("Enter number: "))
    ans = 1
    for i in range(1,n+1):
        ans*=i
    print(ans)
    return ans
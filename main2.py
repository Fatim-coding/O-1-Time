def OnTime(n):
    literation=0
    for i in range(1,n+1):
        literation+=1
    print("when n is ",n," literations = ", literation)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nwith every 'n' the time taken and literations will not increase linearly")
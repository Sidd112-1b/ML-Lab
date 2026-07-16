def common(L1,L2):
    L3=list(filter(lambda x: x in L2,L1))
    return L3

L1 = list(map(int, input("Enter the first list elements: ").split()))
L2 = list(map(int, input("Enter the second list elements: ").split()))

res=common(L1,L2)
print("List of common elements: \n",res)
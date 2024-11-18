def f(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True
        
arrays = [
    (["water","book","sky"]  , ["water","book","sky"]),
    ([True,False]  , [True,False,True]),
    ([5,3,1]  , [5,3,1]),
    ([3,2,1]  , [3,2]),
]

for array1, array2 in arrays:
    print("Array1:", end=" ")
    for item in array1:
        print(item, end=" ")
    print()

    print("Array2:", end=" ")
    for item in array2:
        print(item, end=" ")
    print()

    if f(array1, array2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")
    print()
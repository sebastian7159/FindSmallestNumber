def find_smallest_int(arr1):
    #return min(arr1)   the min funcition finds the minimum value in a list

    var2 = arr1[0]
    for i in range(0, len(arr1)):
        var1 = arr1[i]

        if var2 <= var1:
            res1 = var2
        else:
            var2 = var1
            res1 = var2
    return res1

print(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
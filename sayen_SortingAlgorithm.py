#Joie Sayen
#JoyOfYahweh
#Searching And Sorting Algorithm - Exercise No. 10
#Data Structures and Algorithm Analysis


def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


alist = [2,10,3,4,5,6,7,8,9,1]
quicksort(alist)
print(alist)
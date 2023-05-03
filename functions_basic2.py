#1 Countdown
def countdown(input_number):
    for i in range(input_number, 0, -1):
        print(i)

countdown(7)

#2 Print and Return
def print_and_return(a,b):
    print(a)
    return(b)

print_and_return(1,2)

#3 First Plus Length
def first_plus_length(arr):
    sum = arr[0] + len(arr)
    print(sum)
    return(sum)

first_plus_length([40,30,20,10])

#4 Values Greater than Second
new_arr = []
def values_greater_than_second(arr):
    for i in range(len(arr)):
        if len(arr) < 2:
            return(False)
        elif arr[i] > arr[1]:
            new_arr.append(arr[i])
    print(len(new_arr))
    return(new_arr)

values_greater_than_second([1,2,3,4,5])
values_greater_than_second([3])

#5 This Length that Value
arr = []
def length_value(a, b):
    for i in range(a):
        if i <= a:
            arr.append(b) 
    print(arr)
length_value(5,8)
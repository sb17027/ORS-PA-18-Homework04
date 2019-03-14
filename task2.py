"""
===================   TASK 2   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def main():
    n = int(input("Enter number of elements: "))
    numberOfOdd = 0
    numberOfEven = 0
    list_of_numbers = []

    i = 1
    while i <= n:
        newNumber = int(input("Enter new number for list: "))
        if newNumber % 2 == 0:
            numberOfEven += 1
        else:
            numberOfOdd += 1
        list_of_numbers.append(newNumber)
        i = i + 1

    print(list_of_numbers)
    print("Number of odd elements:", numberOfOdd)
    print("Number of even elements:", numberOfEven)


main()
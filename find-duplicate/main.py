def find_duplication_number(numbers):
    #your code here
    number = []
    duplicate = []
    
    for num in numbers:
        if num not in number:
            number.append(num)
        elif num in number and num not in duplicate:
            duplicate.append(num)
    print(duplicate)
    # pass

#Test case
find_duplication_number([1,1]) #[1]
find_duplication_number([1,2,3,4]) #[]
find_duplication_number([1,2,1,2,2,3,4,5,5,5,5]) #[1,2,5]
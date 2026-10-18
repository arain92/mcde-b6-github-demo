# Question 1 : Accessing List Elements 
# Extract the first, middle, and last elements without modifying the original list.
number = [10, 20, 30, 40, 50,70,80]
first = number[0]
middle = number[len(number)// 2]
last = number[-1]
print("First element:", first)
print("Middle element:", middle) 
print("Last element:", last)
#Q2. List Slicing
# Extract the first, middle, and last elements without modifying the original list.
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
last_four = numbers[-4:]
reverse_second_reverse = numbers[::-2]
print("Last four elements:", last_four)
print("Reverse every second element:", reverse_second_reverse)
#Q3 List Modification
#Replace banana with orange, add grapes at index 2, and remove cherry.
fruits = ["apple", "banana", "cherry", "mango"]
fruits[1] = "orange"  # Replace banana with orange
fruits.insert(2, "grapes")  # Add grapes at index 2
fruits.remove("cherry")  # Remove cherry
print("Modified fruits list:", fruits)
#Q4. Reverse Without reverse()
# Reverse using slicing only; preserve the original list.
numbers = [12, 45, 23, 67, 89, 34]
reversed_numbers = numbers[::-1]
print("Original list:", numbers)
print("Reversed list:", reversed_numbers)
#Q5: Q5. Second Largest Unique Number
#Find the second-largest unique number. Expected: 67.
numbers = [45, 12, 89, 34, 89, 67, 45, 23]
unique_numbers = sorted(set(numbers))  # Remove duplicates and sort
second_largest = unique_numbers[-2]  # Get the second largest
print("Second largest unique number:", second_largest)
#Q6. Rotate a List
#Rotate the list right by k using slicing. Expected: [50, 60, 10, 20, 30, 40].
numbers = [10, 20, 30, 40, 50, 60]
k = 2
rotated_numbers = numbers[-k:] + numbers[:-k]
print("Original list:", numbers)
print("Rotated list:", rotated_numbers)
#Q7. Remove Duplicates, Preserve Order
#Remove duplicates while preserving first-occurrence order.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique_numbers = list(dict.fromkeys(numbers))  # Using dict to preserve order
print("List after removing duplicates:", unique_numbers)
'''LEVEL: ADVANCED
#Q8. Flatten a Nested List'''
data = [[10, 20], [30, 40], [50, 60]]
flattened_list =data[0] + data[1] + data[2]  # Flattening the nested list
print("Flattened list:", flattened_list)

#Q9. Extract Data from a Matrix
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

main_diagonal = [
    matrix[0][0],
    matrix[1][1],
    matrix[2][2]
]

second_diagonal = [
    matrix[0][2],
    matrix[1][1],
    matrix[2][0]
]

middle_column =[
    matrix[0][1],
    matrix[1][1],
    matrix[2][1]
]
print("Main diagonal:", main_diagonal)
print("Main diagonal Sum:", sum(main_diagonal))
print("Second diagonal:", second_diagonal)
print("Second diagonal Sum:", sum(second_diagonal))
print("Middle column:", middle_column)
print("Middle column Sum:", sum(middle_column))


'''Q10.  List Transformation Challenge
Build a list of the three largest unique values ascending, then two smallest unique values descending. Expected: [25,
30, 35, 10, 5].
'''

data = [15, 5, 25, 10, 35, 20, 30]

unique_sorted = sorted(set(data))

three_largest = unique_sorted[-3:]
two_smallest_desc = unique_sorted[:2][::-1]

result = three_largest + two_smallest_desc

print("Three largest:", three_largest)
print("Two smallest descending:", two_smallest_desc)
print("Final result:", result)




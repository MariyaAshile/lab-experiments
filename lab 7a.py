def get_element_at_index(numbers):
    while True:
        try:
            index = int(input("Enter an index: "))
            element = numbers[index]
            print("Element at index", index, "is", element)
            break
        except IndexError:
            print("Error: Invalid index. Index should be within the range of the list.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer index.")

# Example usage
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter number " + str(i) + ": "))
    numbers.append(num)

get_element_at_index(numbers)

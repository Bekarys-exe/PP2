def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

example_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]
unique_list = unique_elements(example_list)
print(f"Original list: {example_list}")
print(f"List with unique elements: {unique_list}")
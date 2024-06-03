1st Q

def display_star_pattern():
    pattern = ["*", "* *", "* * *", "* * * *", "* * * * *", "* * * *", "* * *", "* *", "*"]
 for stars in pattern:
     print(stars)
display_star_pattern()

2nd Q

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i % 2 != 0:  
        print(my_list[i])
3rd Q

x = [23, 'Python', 23.98]
type_list = []
for element in x:
    type_list.append(type(element))
print(x)
print(type_list)

4th Q

def get_unique_items(input_list):
    unique_list = list(set(input_list))
    return unique_list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_items(sample_list)
print("Sample List:", sample_list)
print("Unique List:", unique_list

5th Q

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
return upper_count, lower_count
input_string = 'The quick Brow Fox'
upper_count, lower_count = count_upper_lower(input_string)
print("Input String:", input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)



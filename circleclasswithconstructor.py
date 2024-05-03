#Python program to create a class called circle with constructor which will take a list as an argument for the task and the given list is [10, 501, 22, 37, 100, 999, 87, 351]

given_list = [10, 501, 22, 37, 100, 999, 87, 351] # Given list

class Circle:
    def __init__(self, given_list):
        self.given_list = given_list

result = Circle(given_list)    # Object for the class

# Print the class circle with the list
print(result.given_list)

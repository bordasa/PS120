# # # # #Problem 1
# # # # #input: ask for 2 numbers
# # # # #output: divide first number by second number
# # # # #Rules: Handle ZeroDivisionError or ValueError

# # # # print('We are going to divide 2 numbers.')
# # # # num1 = input('What is the first number?\n')
# # # # num2 = input('What is the second number?\n')

# # # # try:
# # # #     num1 = float(num1)
# # # #     num2 = float(num2)
# # # #     result = num1 / num2
# # # # except (ZeroDivisionError, ValueError) as e:
# # # #     print('\nError!', e, '', sep='\n')
# # # # else:
# # # #     print(f'{num1} / {num2} = {result}')
# # # # finally:
# # # #     print('End')

# # # class NegativeNumberError(ValueError):
# # #     def __init__(self, message='Number must be positive.'):
# # #         super().__init__(message)

# # # num = float(input('Please input a number: \n'))

# # # if num < 0:
# # #     raise NegativeNumberError()

# # # print(f'You entered {num}')

# # def list_inverter(my_list):
# #     result = []

# #     for num in my_list:
# #         try:
# #             result.append(1 / num)

# #         except ZeroDivisionError:
# #             result.append(float('inf'))

# #         except TypeError:
# #             result.append(f'1/{num}')
    
# #     return result

# # numbers = [1, 2, 3, 4, 5]
# # test1 = [1, 2, 0, 3, 4]
# # test2 = [1, '2', 3, 4, 5]
# # test3 = [1, 'ls', 'jk', 4, 5]

# # print(list_inverter(numbers))
# # print(list_inverter(test1))
# # print(list_inverter(test2))
# # print(list_inverter(test3))

# #Problem 8
# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     try:
#         print(f'{name} is {students[name]} years old')
#     except KeyError:
#         print('Student not found.')

# get_age('John')
# get_age('Sally')

#Problem 9
numbers = [1, 2, 3, 4, 5]

def lbyl_6th_element(nums):
    if len(nums) >= 6:
        return nums[5]
    
    return None

def afnp_6th_element(nums):
    try:
        return nums[5]
    except IndexError:
        return None

print(lbyl_6th_element(numbers))
print(afnp_6th_element(numbers))


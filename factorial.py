def factorial(num):
	# your code here
    facto = num
    # range(start, stop, step), -1 makes the order move backwards
    for i in range(num - 1, 1, -1):
        # print(i)
        facto *= i
    # print(facto)
    return facto        
  
# print(factorial(8))
# print(factorial(18))
# print(factorial(45))

# print(factorial(8) == 40320) 
# print(factorial(18) == 6402373705728000)
# print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)

# python3 factorial_spec.py
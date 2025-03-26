full_name = input("enter your full name: ") #ask user to input their full name
#convert the input to snake_case
snake_case_name = '_'.join(word.lower() for word in full_name.split())
print(snake_case_name) #print the snake case name
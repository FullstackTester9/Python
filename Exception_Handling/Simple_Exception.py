"""

"""

class DemoException:
    numerator = 15
    denominator = 0 # Change this value to remove exception
    result = 0

    try:
        result = numerator / denominator # Exception occured at this line
        print(f"Division is: {result}")
    except Exception as e:
        print("Oops an error occured!!!")
        print("Error -> ", e, end='\n\n')

DemoException()

class AvoidException:
    numerator = 15
    denominator = 3 # Change this value to remove exception
    result = 0

    try:
        if denominator <= 0: # Avoid exception
            print("Denominator can not be ZERO.")
        else:
            result = numerator / denominator # Exception occured at this line
            print(f"Division is: {result}")
    except Exception as e:
        print("Oops an error occured!!!")
        print("Error -> ", e)

AvoidException()
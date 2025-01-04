def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error in a more appropriate way

result = function(10, 0) #This will now return 0 instead of throwing an error.
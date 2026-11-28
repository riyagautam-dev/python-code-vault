'''# Built-in and User-defined Exceptions in Python

## 1. What is an Exception?

An exception is an error that occurs during program execution and interrupts the normal flow of the program.

Python exceptions are mainly of two types:

1. Built-in Exceptions
2. User-defined Exceptions

---

## 2. Built-in Exceptions

Built-in exceptions are predefined exceptions provided by Python.

We do not need to create these exceptions ourselves.

### Common Built-in Exceptions

| Exception | Meaning |
|---|---|
| ZeroDivisionError | Occurs when dividing a number by zero. |
| ValueError | Occurs when a function receives an invalid value. |
| TypeError | Occurs when an operation is performed on an inappropriate data type. |
| IndexError | Occurs when accessing an invalid list index. |
| NameError | Occurs when using an undefined variable. |
| FileNotFoundError | Occurs when the requested file does not exist. |

### Example:

```python
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Output:**
```text
Cannot divide by zero
```

Here,ZeroDivisionError is a built-in exception because it is already available in Python.

---

## 3. User-defined Exceptions

User-defined exceptions are custom exceptions created by programmers according to their requirements.

We create a custom exception by defining a class that inherits from the built-in Exception class.

### Example:

```python
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("You are eligible")

except AgeError as msg:
    print(msg)
```

**Output (Input: 15):**
```text
Age must be 18 or above
```

### Explanation:

1. `class AgeError(Exception):` creates a custom exception class.
2. `pass` means the class has no additional implementation.
3. `raise` is used to generate an exception manually.
4. `except AgeError as msg` catches and handles our custom exception.

---

## 4. Difference Between Built-in and User-defined Exceptions

| Built-in Exception | User-defined Exception |
|---|---|
| Already defined in Python. | Created by the programmer. |
| Predefined exceptions. | Custom exceptions. |
| No need to create a class. | A custom exception class is created. |
| Example: ValueError | Example: AgeError |

---

## 5. Important Keywords

- **try:** Contains code that may generate an exception.
- **except:** Handles an exception.
- **raise:** Manually generates an exception.
- **Exception:** Base class used to create custom exceptions.

---

## 6. Conclusion

Built-in exceptions are provided by Python, whereas user-defined exceptions are created by programmers to handle application-specific errors.

Both types help us handle errors and make programs more reliable.
'''
# Creating a user-defined exception for young age
class TooYoungException(Exception):
    #exception is a base class which generate error

    def __init__(self, arg):  # Constructor
        self.msg = arg  # Store the error message in an object variable


# Creating a user-defined exception for old age
class TooOldException(Exception):

    def __init__(self, arg):  # Constructor
        self.msg = arg  # Store the error message in an object variable


# Main program
try:
    # Taking age input from the user
    age = int(input("Enter your age: "))

    # Checking if age is greater than 60
    if age > 60:

        # Creating an object of TooOldException
        o1 = TooOldException("Your age has already crossed 60")

        # Raising the exception manually
        raise o1

    # Checking if age is less than 19
    elif age < 19:

        # Creating an object of TooYoungException
        y1 = TooYoungException("Please wait, you are too young")

        # Raising the exception manually
        raise y1

    else:
        print("You are eligible")


# Handling TooYoungException
except TooYoungException as e:
    print(e.msg)


# Handling TooOldException
except TooOldException as e:
    print(e.msg)


# Handling invalid integer input
except ValueError:
    print("Please enter a valid integer")


# This block executes whether an exception occurs or not
finally:
    print("Inside finally block")


# Executes after successful exception handling
print("Normal terminate")
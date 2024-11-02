# if __name__ = "__main__"

# In python, the if __name__ == "__main__" condition is used to check if the current script is being run as the main program. It allows you to control the execution of code based on whether the script is being run directly or imported as a module.

# When you execute a python script directly, the special variable __name__ is set to "__main__". However, when a python script is imported as a module, the value of __name__ become the name of the module.

# By using if __name__ = "__main__", you can define a block of code that should only run when the script is executed directly.

# This is useful when you want  to include some test code or run certain functions only when the script is the main entry point.
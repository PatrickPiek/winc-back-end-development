# Report

A short, 300-word report that highlights three technical elements of your implementation that you find notable

1. Classes to separate functionality

I chose to use classes for all core functionality of the app and used the built-in `__init__` method to initialize each class instance. The main method for each class where needed is `<Class>.run()`. Where useful, I used another built-in method `__str__` for a string representation of the class. This helps to keep the functionality easy to read and alter.

Classes are stored in a `classes` directory and referenced from other files as `from classes.<Class> import <Class>`. This works by adding an empty file with the filename `__init__.py` to the `classes` directory.

2. Database class that handles generic functionality
3. Using functions.py and config.py to remain DRY

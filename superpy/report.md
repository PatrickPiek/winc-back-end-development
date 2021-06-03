# Report

Three technical elements of my implementation that are notable.

1. Classes to separate functionality

I chose to use classes for all core functionality of the app and used the built-in `__init__` method to initialize each class instance. The main method for each class where needed is `<Class>.run()`. Where useful, I used another built-in method `__str__` for a string representation of the class. This helps to keep the code easy to read.

Classes are stored in a `classes` directory and referenced from other files as `from classes.<Class> import <Class>`. This works by adding an empty file with the filename `__init__.py` to the `classes` directory.

2. Database class that handles generic functionality

I chose to write a separate `Database` class that handles reading and writing to the CSV files. If the database file is not created yet, the class creates the file from a definition stored in `config.py`. If the `databases` directory is not created yet, the class creates the directory first. When a new class instance is created, the class automatically reads the data from the database file. New data is written using the append flag `mode='a'`, so the entire file does not need to be replaced.

3. Using functions.py and config.py to remain DRY

Functions are stored in a `functions` directory and referenced from other files as `from functions.<kind> import <function>`. This works by adding an empty file with the filename `__init__.py` to the `functions` directory. Functions of the same kind are stored in the same file. There are, for example, date related functions in `date.py` and filter funtions in `filter.py`. When certain code is easy to separate from the whole and is used often, it’s best to create a separate function for it. This helps to keep the code DRY.

Most configurations data such as filenames, fieldnames and date formats are stored in `config.py`. This also helps to keep the code DRY and allows for easy changes if needed.

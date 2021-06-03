# Report

Three technical elements of my implementation that are notable.

### 1. Classes to separate functionality

Classes are used for all core functionality of the app and use the built-in `__init__` method. The main method for each class `<Class>.run()`. Where useful, the built-in `__str__` method is used for a string representation of the class. Classes help to keep the code easy to read and reusable.

Classes are stored in a `classes` directory and are referenced as `from classes.<Class> import <Class>`. This works by storing an empty `__init__.py` file in the `classes` directory.

### 2. Database class

A separate `Database` class handles reading and writing data. If the database is not created yet, the file is created from a definition in `config.py`. If the `databases` directory is not created, the class creates it.

When a new class instance is created, the class automatically reads from the database. New data is written using append `mode='a'`, so the entire file does not need to be replaced when adding data.

### 3. Using `functions.py` and `config.py` to remain DRY

Functions are stored in a `functions` directory and referenced from other files as `from functions.<category> import <function>`. This works by adding an empty file with the filename `__init__.py` to the `functions` directory. Functions of the same category are stored in the same file. There are, for example, date related functions in `date.py` and filter funtions in `filter.py`.

When certain code is easy to separate from the whole and is used often, it’s best to create a separate function for it. This helps to keep the code DRY.

Most configurations data such as filenames, fieldnames and date formats are stored in `config.py`. This also helps to keep the code DRY and allows for easy changes if needed.

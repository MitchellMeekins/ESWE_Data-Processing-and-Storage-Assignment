# ESEP: Extra Credit Assignment : Data Processing and Storage Assignment

## Overview

`InMemoryDB` is a Python in-memory key-value database that supports transactions. The following functions are supported:
- begin_transaction()
- put(key, value)
- get(key)
- commit()
- rollback()

## Setup and Running the Code

1. **Setup the Environment**:
   - This was developed with Python version 3.12.2. Ensure this is installed.

2. **Download the Files**:
   - Save `main.py` to a chosen folder.
   - Save `test.py` in the same directory as `main.py`.

3. **Run the Code**:
   In order to run either file, navigate to the chosen directory, open a terminal session in this directory, and run python -i [file_name].py
   - Included in the files are test files. If desired, you may simply run the `test.py` file to verify functionality.
   - If you would like to manually verify the functionality, run tfew he `main.py` file by using python -i main.py.
  

## Potential Assignment Modifications
- A potential modification could be to include provided test cases in order to allow for faster grading. There are a few websites where this could be used, but I would recommend simply creating test cases for 3 languages (C++, Python, and Java). This could be placed before the unit testing assignment in order to give a preview for students. Additionally, the functionality of certain functions, such as whether you could begin a transaction during a transaction, was unclear. These changes should be enough, as the assignment was not particularly bad but just a little confusing in terms of the functionality of the code.

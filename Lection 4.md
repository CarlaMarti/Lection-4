# Lection 4

## Contents

Topic 1: Recap Class 4
Topic 2: Testing
Topic 3: Code Coverage
Topic 4: Linting

## Topic 1: Recap Class 4

### Code Versioning - GitHub

- Versioning: Allows developers to track changes to
their codebase over time.
- Collaboration: It enables multiple developers to
work on the same project concurrently, managing
code modifications, merging changes, and
resolving conflicts efficiently.
- Backup: Remote code repository, hosting your
project's code and providing a secure backup
- Continuous Integration and Deployment (CI/
CD): Automated build and testing processes.
Ensure code quality, and allows for smooth
deployment to production environments.

### You gotta use GitHub (or similar) IF

- If you manage any type of data team or want to
in the future
- If you want to do any data project
- If you want to properly learn how to work on an
ML project
- If you plan on collaborating with people
- If you want to create your own product to share
on the internet

### Bringing everything together

- CLI parser (Click)

parser = analizer 

- Debugger (PDB)

- Try & Except

- Classes

### In this assignment I am recommended to go further

***Ideas:***

    - EDA (figures) = Análisis Exploratorio de DATOS
    
    - clean up dataset 

I will try it!

## Topic 2: Testing

### What does it mean to test your code?

Testing in Python refers to the process of
systematically checking and validating that
individual units of source code, such as
functions or methods, work correctly

### Why is it important to test?

- Identifies Bugs Early
- Ensures Code Quality and behaves as expected
under various conditions.
- Facilitates Refactoring (changes) knowing that
tests will catch any new errors introduced.
- Improves Reliability and Robustness of code.
- Facilitates Integration & Deployment
- Act as Documentation

Testing can save you a lot of time, and money!! Example: airline.

### Back to an example product 

Testing is important and one of the steps to ensure there is no issues with the final product.

### Test Driven Development (TDD)

First you create the test, then the code. Difficult to follow, but you are then sure that your code works properly.

### TDD Process

1. Write Test
2. Run Test (Fails)
3. Add Feature
4. Run Test (Passes or not)
5. Re-factor Code
6. Back to 4

- Better understanding of your code
- Better coverage making changes easier (More confidence)
- Reduces Bugs

### Unittest and Pytest 

Unittest and Pytest are the main Python packages that we can and will use to test our code.

- We need: A function to test and a Test for the function

### In class exercise 1

Now, let’s see this in action and build some tests together on how to ensure that
the input dataset is correctly passed 

Let’s build first a simple case scenario where we could use a test.

- First let’s create a branch named class4_tests and work there
- Functions to compute the sum and subtraction of two numbers and test that they work
correctly.
- Let’s use both

    - pytest (pip install pytest & the pytest tests (it catches all tests) in the command line)

    - unittest (no install needed + python -m unittest in the command line)

    
### In class exercise 2

Now, let’s see this in action and build some tests together on how to ensure that the input dataset is correctly passed 

## HOMEWORK: 

- Build some tests for the filtering steps performed on our dataset.
- If you build a class for filtering functions you can put that class in a different script and call it from the
main script
- (Show an example on how you can import code from other files to create scripts with independent
functionality)

! I have to do a minimum of 3 tests, 5 will be a good number

***Extra Ideas: (I tried it)***

    - EDA (figures) = Análisis Exploratorio de DATOS
    
    - clean up dataset 


How to run a test: 
    
        python -m unittest tests/test_simple_functions.py

        pytest tests/test_simple_functions.py 
        
        python -m unittest tests/test_load_dataset.py

        pytest tests/test_load_dataset.py

If you run the following all tests run:

        python -m unittest

        pytest tests


## IN CLASS NOTES about some exercises in class

We are going to follow a Test Driven Development (TDD) Process:

1. First we are writing the test (in this case in a script called test_simple_functions.py)
2. We executed the following command and we had an error (the function sum_two_nums was not found)

        python -m unittest tests/test_simple_functions.py

3. We defined the functions (called: sum_two_nums and sub_two_nums) and we execute again the same command, now it works

        Results: 

        If we put the right numbers in the test code (ex: 2+3 and then 5) it passes the test.

        If we put wrong numbers in the test code (ex: 2+3 equals 7) it doesn't pass the test. 

*Note:* We need to create a script called __init__.py so that pytest works
    
    pytest tests

Now we will do the same process with another kind of test, now with assertRaises. This test will be called test_load_dataset and the function load_dataset

pytest tests/test_load_dataset.py

python -m unittest or pytest tests (all tests will run)





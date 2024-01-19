# Lection 5

*Link to repository: * https://github.com/CarlaMarti/Lection-5
 
## Contents

Topic 1: Recap Class 4
Topic 2: Code Coverage
Topic 3: Linting
Topic 4: GitHub II. CD/CI
Topic 5: Makefile
Topic 6: Multiprocessing

## Topic 1: Recap Class 4 (Testing) 

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

## Topic 2: Code Coverage

Code coverage refers to the percentage of
your code (number of lines of your code) that
is covered by tests (that is assessed).

#### Installation and usage

pip install coverage==(look for library version)
coverage run -m unittest tests/test_filter.py
coverage report
coverage html 

## Topic 3: Linting

Linting is to run a program that analyzes Python
code for various errors and potential problems. It
checks for programmatic and stylistic errors,
helping developers maintain a clean and consistent
codebase that adheres to best practices.

**Utilities:**

- Code Quality Improvement
- Early Bug Detection
- Readability and Maintainability
- Facilitates Code Reviews

#### Flake8 & Pylint

Both are libraries to lint your code. Their messages are different so it is not bad
to use both and implement the changes they suggest

Command line 1 :
pip install flake8
flake8 folder/to/lint

Command line 2 :
pip install pylint
pylint folder/to/lint

*Note: * To do linting quicker we can also install black. pip install black + black script (show)

## Topic 4: GitHub II. CD/CI

- Continuous Improvement (CI) refers to the practice of
regularly integrating code changes from multiple developers
into a shared repository. The goal is to detect issues and conflicts early in the
development cycle and ensure that the codebase
remains stable.
- Continuous Deployment (CD) focuses on automating the
deployment of applications to various environments (e.g.,
staging, production) after passing the CI stage. It involves automating the steps required to build, test,
and deploy software, reducing manual effort and
ensuring consistent and reliable deployments.

#### Steps:

1. Version Control: Store your codebase in a GitHub repository hosted on GitHub
2. Automated Testing: Set up automated testing frameworks, such as unit tests or integration
tests, that run whenever code changes are made.
3. Continuous Integration: Use GitHub Actions to automatically build and test your code
whenever changes are pushed to the repository. This ensures that new code is integrated
smoothly with the existing codebase and helps catch any errors or conflicts.
4. Code Reviews: Encourage code reviews by peers or senior developers to ensure code quality,
adherence to best practices, and identify potential improvements.

#### Benefits:

- Faster Time to Market: Automating processes reduces manual effort and speeds up the delivery of software updates.
- Improved Code Quality: Continuous integration and automated testing catch errors early, ensuring code quality and
reducing the risk of introducing bugs.
- Collaboration and Feedback: Code reviews and feedback from peers help improve code quality and foster
collaboration among team members.
- Reliable Deployments (Less human mistakes): Automating the deployment process minimizes the risk of
configuration errors and ensures consistent deployments across environments.

## Topic 5: Makefile

Makefile is a special file used to
automate the process of
compiling and building software
by using “make”

- Every blue box is a rule
- Every rule has a target (a name) (Green
box)
- Every name can have dependencies (pink)
- Every rule and name has a command to
be run (orange boxes)

*Note: * Caution with Windows Makefile has to be installed

# Homework

*Note:* I had to modify some codes and limit the offerings in various situations so that it got the proper puntuation.

### Check Pylint grades: 
    
tests directory (10/10):

    pylint tests

scripts directory (6.32/10):

    pylint scripts


### Check flake8 comments: 

tests directory (0 comments):

    flake8 tests

scripts directory (0 comments):

    flake8 scripts

### GitHub Actions 

Activated for this branch (exercise_class_5) and had a tick (only testing).

Activated the action of linting with flake8, also got the tick (linting with flake8 too!).

### Makefile

I tried to install make (Makefile) for windows with the link you gave us but couldn't open any .sig file (the ones we had to download and open to install make).
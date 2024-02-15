"""
Module: any python file with python code in it.
Packages: A folder, it is a collection/ group of modules.

come as standard, with python
you can install them from outside sources.
you can create your own packages and modules.

modularity
"""

import math  # alias
from functions import adder
from functions import *
from dictionaries import *

"""
special variables
__name__, __file__
"""

if __name__ == "__main__":
    print(__name__)  # double under/ dunder/ special variables
    display()

# create a module, create a couple of functions in it, also call those functions in the same file.
# create another file, import the module in this. use those functions here.
# check what is happening...

# use if __name__ == '__main__' code in the module and put your function calling code under this.
# now run your main file and observe the outcome.

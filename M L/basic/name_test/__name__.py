# explain why we need to use if __name__ == "__main__":?

import pandas as pd # top level code

df = pd.DataFrame([1, 2]) # not top level

print("this is a module") # top level code
print(__name__)
print(pd.__name__)
# this is a module
# __main__
# pandas

# because we have borrowed a class from a module which we have never specified in our console

# __name__ uniquely identifies the top level module
# name is a variable, main is a value, which represents the name of top level environment

# if __name__ == "__main__":
# checking if the code we are execyting is top level or not

# when import a function from a module, it will accidentlly execute this module
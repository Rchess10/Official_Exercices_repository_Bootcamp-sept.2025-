from operator import addoperator, divideoperator  # import functions

# call functions directly
addoperator(8, 10)
divideoperator(8, 10)

# or import the module (alias to avoid colliding with stdlib operator)
import operator as op_mod
op_mod.addoperator(6, 20)
op_mod.divideoperator(6, 20)

#################################################################

# from operator import Operation  # import the class

# inst = Operation(8, 10)
# inst.addoperator()
# inst.divideoperator()

# # or import the module
# import operator as op_mod
# inst = op_mod.Operation(6, 20)
# inst.addoperator()
# inst.divideoperator()

#################################################################

import operator as myop
myop.addoperator(8, 10)


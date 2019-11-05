import operator
import fxns
from enum import Enum

class fxn_type(Enum):
    stack = 0
    single_arg = 1
    dual_arg = 2

operations = {
    '+':    (fxn_type.dual_arg, operator.add),
    '-':    (fxn_type.dual_arg, operator.sub),
    '*':    (fxn_type.dual_arg, operator.mul),
    '/':    (fxn_type.dual_arg, operator.floordiv),
    '%':    (fxn_type.dual_arg, operator.mod),
    '**':   (fxn_type.dual_arg, operator.pow),

    '!':    (fxn_type.single_arg, fxns.factorial),

    'S':    (fxn_type.stack, fxns.sum),
}

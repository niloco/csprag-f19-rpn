import operator
import fxns

dual_arg_ops = {
    '+':    operator.add,
    '-':    operator.sub,
    '*':    operator.mul,
    '/':    operator.floordiv,
    '%':    operator.mod,
    '**':   operator.pow,
}

single_arg_ops = {
    '!':    fxns.factorial,
}
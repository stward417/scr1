from enum import Enum
from random import randint

class IaluCmd(Enum):
    SCR1_IALU_CMD_ADD = 4   # op1 + op2
    SCR1_IALU_CMD_SUB = 5   # op1 - op2


def result(cmd, op1, op2) -> int:
    int_w = (2**31)-1

    print(cmd)

    if (cmd == "SCR1_IALU_CMD_ADD"):
        res = op1 + op2
        if (res < -int_w):
            res = (res + (int_w*2))+2
        elif (res > int_w):
            res = (res - (int_w*2))-2
        return res
    elif (cmd == "SCR1_IALU_CMD_SUB"):
        res = op1 - op2
        if (res < -int_w):
            res = (res + (int_w*2))+2
        elif (res > int_w):
            res = (res - (int_w*2))-2
        return res





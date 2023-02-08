import logging
import cocotb
from cocotb.triggers import RisingEdge, Timer
from random import randint

from model.alu_model import *
#import alu_model

SCR1_XLEN = 32

ialu_cmd = IaluCmd

ALU_CMD = int(cocotb.top.ALU_CMD)

@cocotb.test()
async def ialu_add_tb(dut):
    int_w = (2**31)-1

    op1 = randint(-int_w, int_w)
    op2 = randint(-int_w, int_w)

    dut._log.info("Initialize ialu")
    dut.exu2ialu_main_op1_i.value = op1
    dut.exu2ialu_main_op2_i.value = op2
    dut.exu2ialu_cmd_i.value = ALU_CMD

    await Timer(2, units="ns")

    main_res_o = result(ialu_cmd(ALU_CMD).name, op1, op2)
    res_o_value = int(dut.ialu2exu_main_res_o)
    res_o_bytes = res_o_value.to_bytes(4, byteorder='big')
    res_o_signed = int.from_bytes(res_o_bytes, byteorder='big', signed=True)

    dut._log.info("RESULT:")

    if (ialu_cmd(ALU_CMD).name == "SCR1_IALU_CMD_ADD"):
        dut._log.info("iALU Command = %s", ialu_cmd(ALU_CMD).name)
        dut._log.info("Signal: main_op1_i = %d", op1)
        dut._log.info("Signal: main_op2_i = %d", op2)
        dut._log.info("Command ADD (main_op1_i, main_op2_i) = %d", res_o_signed)
    elif (ialu_cmd(ALU_CMD).name == "SCR1_IALU_CMD_SUB"):
        dut._log.info("iALU Command = %s", ialu_cmd(ALU_CMD).name)
        dut._log.info("Signal: main_op1_i = %d", op1)
        dut._log.info("Signal: main_op2_i = %d", op2)
        dut._log.info("Command SUB (main_op1_i, main_op2_i) = %d", res_o_signed)



    assert res_o_signed == main_res_o, f"Adder result is incorrect: {res_o_signed} != {main_res_o}"



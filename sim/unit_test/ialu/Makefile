# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog

ALU_CMD ?= 4

EXTRA_ARGS += -Wno-WIDTH
EXTRA_ARGS += --trace --trace-structs

VERILOG_SOURCES += $(PWD)/../../../src/includes/scr1_arch_description.svh
VERILOG_SOURCES += $(PWD)/../../../src/includes/scr1_arch_types.svh
VERILOG_SOURCES += $(PWD)/../../../src/includes/scr1_riscv_isa_decoding.svh
VERILOG_SOURCES += $(PWD)/../../../src/includes/scr1_search_ms1.svh
VERILOG_SOURCES += $(PWD)/../../../src/core/pipeline/scr1_pipe_ialu.sv
VERILOG_SOURCES += $(PWD)/scr1_pipe_ialu_tb.sv

COMPILE_ARGS += -GALU_CMD=$(ALU_CMD)

ialu:
	$(MAKE) sim MODULE=ialu_tb TOPLEVEL=scr1_pipe_ialu_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

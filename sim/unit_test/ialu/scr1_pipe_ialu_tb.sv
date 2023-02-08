module scr1_pipe_ialu_tb #(
    parameter int ALU_CMD = 0
    ) (
`ifdef SCR1_RVM_EXT
    // Common
    input   logic                           clk,                        // IALU clock
    input   logic                           rst_n,                      // IALU reset
    input   logic                           exu2ialu_rvm_cmd_vd_i,      // MUL/DIV command valid
    output  logic                           ialu2exu_rvm_res_rdy_o,     // MUL/DIV result ready
`endif // SCR1_RVM_EXT

    // Main adder
    input   logic [`SCR1_XLEN-1:0]          exu2ialu_main_op1_i,        // main ALU 1st operand
    input   logic [`SCR1_XLEN-1:0]          exu2ialu_main_op2_i,        // main ALU 2nd operand
    input   type_scr1_ialu_cmd_sel_e        exu2ialu_cmd_i,             // IALU command
    output  logic [`SCR1_XLEN-1:0]          ialu2exu_main_res_o,        // main ALU result
    output  logic                           ialu2exu_cmp_res_o,         // IALU comparison result

    // Address adder
    input   logic [`SCR1_XLEN-1:0]          exu2ialu_addr_op1_i,        // Address adder 1st operand
    input   logic [`SCR1_XLEN-1:0]          exu2ialu_addr_op2_i,        // Address adder 2nd operand
    output  logic [`SCR1_XLEN-1:0]          ialu2exu_addr_res_o         // Address adder result
    );

scr1_pipe_ialu dut(
    .clk(clk),
    .rst_n(rst_n),
    .exu2ialu_rvm_cmd_vd_i(exu2ialu_rvm_cmd_vd_i),
    .ialu2exu_rvm_res_rdy_o(ialu2exu_rvm_res_rdy_o),
    .exu2ialu_main_op1_i(exu2ialu_main_op1_i),
    .exu2ialu_main_op2_i(exu2ialu_main_op2_i),
    .exu2ialu_cmd_i(exu2ialu_cmd_i),
    .ialu2exu_main_res_o(ialu2exu_main_res_o),
    .ialu2exu_cmp_res_o(ialu2exu_cmp_res_o),
    .exu2ialu_addr_op1_i(exu2ialu_addr_op1_i),
    .exu2ialu_addr_op2_i(exu2ialu_addr_op2_i),
    .ialu2exu_addr_res_o(ialu2exu_addr_res_o));

`ifdef COCOTB_SIM
initial begin
  $dumpfile ("ialu.vcd");
  $dumpvars;
end
`endif

endmodule

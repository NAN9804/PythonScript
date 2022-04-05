from datetime import datetime
import sys

"""
本模块用于生成verilog文件模板

快捷指令 python P:\PythonScript\CustomVerilogScript\vTmpl_gen.py -name
用户需要在预期生成verilog文件的路径中打开命令行，输入“python py程序存放路径\vTmpl_gen.py *module_name”命令，即可生成如下所示的.v文件模板：
//////////////////////////////////////////////////////////////////////////////////
// 
// Create Date:   20xx-xx-xx xx:xx
// Project Name:  project_name
// Module Name:   module_name
// Engineer:      NAN
// 
// Version:       1.0
// Description: 
//
// Modification History:
// Date                   Change Descripton
// -------------------------------------------------------------------------------
// 20xx-xx-xx             Initial
//
//////////////////////////////////////////////////////////////////////////////////

`default_nettype none
module module_name 
#(  parameter A = 2 ,
    parameter B = 3 )
(
    input  wire                 clk,
    input  wire                 rst_n,
    input  wire  [31:0]         I_pc_cmd,
    output wire  [31:0]         O_FrmData
); 

//-----------------------------declaration---------------------------------//

//--------------------------logic and connections--------------------------//

//----------------------------instantiation--------------------------------//

endmodule
`default_nettype wire
"""
__author__ = 'NAN'

nowtime = datetime.now().strftime('%Y-%m-%d %H:%M')
nowdate = datetime.now().strftime('%Y-%m-%d')
modulename = sys.argv[1]
project_name = ' '

def verilog_template():
    """
    生成verilog模板的内容字符
    """
    edge = '/'*90
    comment = '// '
    vtemplate = (
                edge + '\n' + 
                comment + '\n' + 
                '// Create Date:   ' + nowtime + '\n' + 
                '// Project Name:  ' + project_name + '\n' + 
                '// Module Name:   ' + modulename + '\n' +          #当输入参数为ModuleName.v时,改为filename
                '// Engineer:      NAN' + '\n' +
                comment + '\n' +
                '// Version:       1.0' + '\n' +
                '// Description: ' + '\n' +
                comment + '\n' +
                '// Modification History:' + '\n' +
                '// Date                   Change Descripton' + '\n' +
                comment + '-'*87 + '\n' +
                comment + nowdate + '             Initial' + '\n' +
                comment + '\n' +
                edge + '\n' + '\n'
                '`default_nettype none' + '\n' +
                'module ' + sys.argv[1] +  '\n' +
                '#(  parameter A = 2 ,' + '\n' +
                '    parameter B = 3 )' + '\n' +
                '(' + '\n' +
                '    input  wire                 clk,' + '\n' +
                '    input  wire                 rst_n,' + '\n' +
                '    input  wire  [31:0]         I_,' + '\n' +
                '    output wire  [31:0]         O_' + '\n' +
                '); ' + '\n' + '\n' +
                '//-----------------------------declaration---------------------------------//' + '\n' + '\n' +
                '//--------------------------logic and connections--------------------------//' + '\n' + '\n' +
                '//----------------------------instantiation--------------------------------//' + '\n' + '\n' +
                'endmodule' + '\n' +
                '`default_nettype wire'
                )
                
    return vtemplate

if __name__ == '__main__':
    filename = modulename + '.v'
    with open(filename,'w') as file_object:
        vtemplate =verilog_template()
        file_object.write(vtemplate)
    #当输入参数为ModuleName.v时
    # filename = sys.argv[1] 
    # vtemplate =verilog_template()
    # print(vtemplate)

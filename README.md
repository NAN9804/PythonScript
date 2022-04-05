# vTmpl.py
程序用于生成verilog代码模板，需要在“vTmpl.py”所在路径中打开命令行，
并输入命令“ python vTmpl.py module_name ”，
其中*module_name参数为用户定义的verilog模块名。
执行命令后即可得到同名.v文件

# vInst_gen.py
程序用于例化verilog模块，需要在“vInst_gen.py”所在路径中打开命令行，
并输入命令“ python vInst_gen.py module_name.v ”，
其中*module_name参数为需要例化的verilog文件名。

规范：
1.每个参数定义前面都要有parameter

# vTb_gen.py
程序用于生成verilog测试模块，需要在“vTb_gen.py”所在路径中打开命令行，
并输入命令“ python vTb_gen.py module_name.v ”，
其中*module_name参数为需要生成测试模块的verilog文件名。

# eXdc_gen.py
程序用于从Excel中提取信息生成.xdc文件
1.Excel命名方式：“xxx_constr.xlsx”；
2.存放管脚约束信息的sheet命名为“xdc_sourcefile”，B列存放PROT_NAME，C列存放PACKAGE_PIN，D列存放IOSTANDARD，
三列中有一列空行就会跳过这一管脚；
3.生成的xdc文件名：“constr.xdc”。
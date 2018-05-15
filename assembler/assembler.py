code_in = open("/Users/laumitt/Documents/Computer Internals/Code/assembly.txt", "r+")
code_out = open("/Users/laumitt/Documents/Computer Internals/Code/machine.txt", "r+")
operations = {
    'add' : hex(0), # addition
    'sub' : hex(1), # subtraction
    'ort' : hex(2), # or test
    'xor' : hex(3), # xor test
    'equ' : hex(4), # equal test
    'les' : hex(5), # less than
    'gre' : hex(6), # greater than
    # 7 doesn't exist
    'jum' : hex(8), # unconditional jump
    'eqj' : hex(9), # jump if equal to
    'lej' : hex(10), # jump if less than
    'grj' : hex(11), # jump if greater than
    'rms' : hex(12), # ram store
    'rml' : hex(13), # ram load
    'rgs' : hex(14)  # register store
    # 15 doesn't exist
}
names = {
    'add' : 'addition',
    'sub' : 'subtraction',
    'ort' : 'or test',
    'xor' : 'xor test',
    'equ' : 'equal test',
    'les' : 'less than test',
    'gre' : 'greater than test',
    # 7 doesn't exist
    'jum' : 'unconditional jump',
    'eqj' : 'jump if equal to',
    'lej' : 'jump if less than',
    'grj' : 'jump if greater than',
    'rms' : 'ram store',
    'rml' : 'ram load',
    'rgs' : 'register store'
    # 15 doesn't exist
}
com_error = None
len_error = None
arg_error = None
error_exist = None
error = []
line_num = 0
assembly = []
machine = []
command_text = None
command_hex = None
command_name = None
test_flag = None
debug_flag = None

def debug(debug_flag):
    print("Debug? Y/N")
    debug = input()
    if debug == "Y" or debug == "y":
        print("Debug flags active")
        debug_flag = True
    else:
        print("Debug flags inactive")
        debug_flag = False
    return debug_flag

def run_tests(test_flag, code_in, debug_flag):
    print("Run tests? Y/N")
    test_flag = input()
    if test_flag == "Y" or test_flag == "y":
        code_in = open("/Users/laumitt/Documents/Computer Internals/Code/test_assembly.txt", "r+")
    else:
        code_in = open("/Users/laumitt/Documents/Computer Internals/Code/assembly.txt", "r+")
    if debug_flag == True:
        print("received {} (line 71)".format(test_flag))
    return code_in

def read_input(code_in, line_num, assembly, debug_flag):
    assembly.append(line.split())
    if debug_flag == True:
        print("Append {} to assembly array line {} (line 77)".format(line.split(), line_num))

def translate_command(assembly, command_hex, line_num, com_error, names, debug_flag, error):
    command_text = assembly[line_num][0]
    command_hex = operations[command_text]
    command_name = names[command_text]
    if debug_flag == True:
        print("Command: {}, assembly: {}, hex: {} (line 84)".format(command_name, command_text, command_hex))
    if command_hex == None:
        com_error = "Not a valid command"
        error.append("Command error: Not a valid command")
    return command_hex, com_error, error, error_exist

def check_length(assembly, command_hex, line_num, len_error, error_exist, debug_flag, error):
    if debug_flag == True:
        print("Checking length (line 93)")
    if command_hex not in [hex(8), hex(9), hex(10), hex(11), hex(12), hex(13), hex(14)]:
        if debug_flag == True:
            print("Command not jum, eqj, lej, grj, rms, rml, or rgs (line 96)")
        if len(assembly[line_num]) != 4:
            if len(assembly[line_num]) < 4:
                len_error = "Too few arguments: {} given, 4 required".format(len(assembly[line_num]))
            elif len(assembly[line_num]) > 4:
                len_error = "Too many arguments: {} given, 4 required".format(len(assembly[line_num]))
            else:
                print("No length error")
                len_error = None
    elif command_hex == hex(8):
        if debug_flag == True:
            print("Command is jum (line 107)")
        if len(assembly[line_num]) != 2:
            if len(assembly[line_num]) < 2:
                len_error = "Too few arguments: {} given, 2 required".format(len(assembly[line_num]))
            elif len(assembly[line_num]) > 2:
                len_error = "Too many arguments: {} given, 2 required".format(len(assembly[line_num]))
            else:
                print("No length error")
                len_error = None
    elif command_hex in [hex(9), hex(10), hex(11), hex(12), hex(13), hex(14)]:
        if debug_flag == True:
            print("Command is eqj, lej, grj, rms, rml, or rgs (line 118)")
        if len(assembly[line_num]) != 3:
            if len(assembly[line_num]) < 3:
                len_error = "Too few arguments: {} given, 3 required".format(len(assembly[line_num]))
            elif len(assembly[line_num]) > 3:
                len_error = "Too many arguments: {} given, 3 required".format(len(assembly[line_num]))
            else:
                print("No length error")
                len_error = None
    return len_error

def translate_args(assembly, command_hex, line_num, arg_error, machine, error_exist, debug_flag):
    if debug_flag == True:
        print("Translating arguments (line 131)")
    if command_hex == hex(0): # addition
        reg_in_one = assembly[line_num][1]
        reg_in_two = assembly[line_num][2]
        reg_out_one = assembly[line_num][3]
        reg_one_hex = hex(int(reg_in_one[1:]))
        reg_two_hex = hex(int(reg_in_two[1:]))
        reg_out_hex = hex(int(reg_out_one[1:]))
        machine.append([command_hex, reg_one_hex, reg_two_hex, reg_out_hex])
        if debug_flag == True:
            print(str([command_hex, reg_one_hex, reg_two_hex, reg_out_hex]) + " (line 141)")
    elif command_hex == hex(1): # subtraction
        reg_in_one = assembly[line_num][1]
        reg_in_two = assembly[line_num][2]
        reg_out_one = assembly[line_num][3]
        reg_one_hex = hex(int(reg_in_one[1:]))
        reg_two_hex = hex(int(reg_in_two[1:]))
        reg_out_hex = hex(int(reg_out_one[1:]))
        machine.append([command_hex, reg_one_hex, reg_two_hex, reg_out_hex])
        if debug_flag == True:
            print(str([command_hex, reg_one_hex, reg_two_hex, reg_out_hex]) + " (line 151)")
    elif command_hex == hex(2): # or test
        test_val = assembly[line_num][1]
        reg_in = assembly[line_num][2]
        reg_in_out = assembly[line_num][3]
        test_val_hex = hex(int(test_val))
        reg_in_hex = hex(int(reg_in[1:]))
        reg_in_out_hex = hex(int(reg_in_out[1:]))
        machine.append([command_hex, test_val_hex, reg_in_hex, reg_in_out_hex])
        if debug_flag == True:
            print(str([command_hex, test_val_hex, reg_in_hex, reg_in_out_hex]) + " (line 161)")
    elif command_hex == hex(3): # xor test
        test_val = assembly[line_num][1]
        reg_in = assembly[line_num][2]
        reg_in_out = assembly[line_num][3]
        test_val_hex = hex(int(test_val))
        reg_in_hex = hex(int(reg_in[1:]))
        reg_in_out_hex = hex(int(reg_in_out[1:]))
        machine.append([command_hex, test_val_hex, reg_in_hex, reg_in_out_hex])
        if debug_flag == True:
            print(str([command_hex, test_val_hex, reg_in_hex, reg_in_out_hex]) + " (line 171)")
    elif command_hex == hex(4): # equal test
        reg_in_one = assembly[line_num][1]
        reg_in_two = assembly[line_num][2]
        reg_out_one = assembly[line_num][3]
        reg_one_hex = hex(int(reg_in_one[1:]))
        reg_two_hex = hex(int(reg_in_two[1:]))
        reg_out_hex = hex(int(reg_out_one[1:]))
        machine.append([command_hex, reg_one_hex, reg_two_hex, reg_out_hex])
        if debug_flag == True:
            print(str([command_hex, reg_one_hex, reg_two_hex, reg_out_hex]) + " (line 181)")
    elif command_hex == hex(5): # less than test
        reg_in_one = assembly[line_num][1]
        reg_in_two = assembly[line_num][2]
        reg_out_one = assembly[line_num][3]
        reg_one_hex = hex(int(reg_in_one[1:]))
        reg_two_hex = hex(int(reg_in_two[1:]))
        reg_out_hex = hex(int(reg_out_one[1:]))
        machine.append([command_hex, reg_one_hex, reg_two_hex, reg_out_hex])
        if debug_flag == True:
            print(str([command_hex, reg_one_hex, reg_two_hex, reg_out_hex]) + " (line 191)")
    elif command_hex == hex(6): # greater than test
        reg_in_one = assembly[line_num][1]
        reg_in_two = assembly[line_num][2]
        reg_out_one = assembly[line_num][3]
        reg_one_hex = hex(int(reg_in_one[1:]))
        reg_two_hex = hex(int(reg_in_two[1:]))
        reg_out_hex = hex(int(reg_out_one[1:]))
        machine.append([command_hex, reg_one_hex, reg_two_hex, reg_out_hex])
        if debug_flag == True:
            print(str([command_hex, reg_one_hex, reg_two_hex, reg_out_hex]) + " (line 203)")
    elif command_hex == hex(7): # nonexistent
        arg_error = "Invalid Command (0x7)"
        if debug_flag == True:
            print("Tried to translate nonexistent commant hex(7) (line 205)")
    elif command_hex == hex(8): # unconditional jump
        jump_to = assembly[line_num][1]
        if len(jump_to) == 1:
            jump_to = "0" + jump_to
        jump_to_hex = "0x" + jump_to
        machine.append([command_hex, jump_to_hex, hex(0)])
        if debug_flag == True:
            print(str([command_hex, jump_to_hex, hex(0)]) + " (line 213)")
    elif command_hex == hex(9): # if equal jump
        reg_in = assembly[line_num][1]
        jump_to = assembly[line_num][2]
        if len(jump_to) == 1:
            jump_to = "0" + jump_to
        reg_in_hex = hex(int(reg_in[1:]))
        jump_to_hex = "0x" + jump_to
        machine.append([command_hex, reg_in_hex, jump_to_hex])
        if debug_flag == True:
            print(str([command_hex, reg_in_hex, jump_to_hex]) + " (line 223)")
    elif command_hex == hex(10): # if less than jump
        reg_in = assembly[line_num][1]
        jump_to = assembly[line_num][2]
        if len(jump_to) == 1:
            jump_to = "0" + jump_to
        reg_in_hex = hex(int(reg_in[1:]))
        jump_to_hex = "0x" + jump_to
        machine.append([command_hex, reg_in_hex, jump_to_hex])
        if debug_flag == True:
            print(str([command_hex, reg_in_hex, jump_to_hex]) + " (line 233)")
    elif command_hex == hex(11): # if greater than jump
        reg_in = assembly[line_num][1]
        jump_to = assembly[line_num][2]
        if len(jump_to) == 1:
            jump_to = "0" + jump_to
        reg_in_hex = hex(int(reg_in[1:]))
        jump_to_hex = "0x" + jump_to
        machine.append([command_hex, reg_in_hex, jump_to_hex])
        if debug_flag == True:
            print(str([command_hex, reg_in_hex, jump_to_hex]) + " (line 243)")
    elif command_hex == hex(12): # ram store
        reg_add = assembly[line_num][1]
        ram_add = assembly[line_num][2]
        reg_add_hex = hex(int(reg_add[1:]))
        ram_add_hex = "0x" + ram_add
        machine.append([command_hex, reg_add_hex, ram_add_hex])
        if debug_flag == True:
            print(str([command_hex, reg_add_hex, ram_add_hex]) + " (line 251)")
    elif command_hex == hex(13): # ram load
        ram_add = assembly[line_num][1]
        reg_add = assembly[line_num][2]
        ram_add_hex = "0x" + ram_add
        reg_add_hex = hex(int(reg_add[1:]))
        machine.append([command_hex, ram_add_hex, reg_add_hex])
        if debug_flag == True:
            print(str([command_hex, ram_add_hex, reg_add_hex]) + " (line 259)")
    elif command_hex == hex(14): # register store
        input_val = assembly[line_num][1]
        reg_add = assembly[line_num][2]
        input_val_hex = "0x" + input_val
        reg_add_hex = hex(int(reg_add[1:]))
        machine.append([command_hex, input_val_hex, reg_add_hex])
        if debug_flag == True:
            print(str([command_hex, input_val_hex, reg_add_hex]) + " (line 269)")
    elif command_hex == hex(15): # nonexistent
        arg_error = "Invalid Command (0x15)"
        if debug_flag == True:
            print("Tried to translate invalid command hex(15) (line 271)")
    else:
        arg_error = "Undefined Command (must be between 0x0 and 0x15)"
        if debug_flag == True:
            print("Undefined command (line 275)")
    if arg_error != None:
        error_exist = True
    return arg_error

def display_error(assembly, line_num, com_error, len_error, arg_error, debug_flag):
    if com_error != None or len_error != None or arg_error != None:
        if com_error != None:
            print("Command error on line {}: {}".format(line_num, com_error))
            print("Input: {}".format(assembly[line_num]))
        elif len_error != None:
            print("Length error on line {}: {}".format(line_num, len_error))
            print("Input: {}".format(assembly[line_num]))
        elif arg_error != None:
            print("Argument error on line {}: {}".format(line_num, arg_error))
            print("Input: {}".format(assembly[line_num]))
    elif debug_flag == True:
        print("No errors (line 292)")

def write_output(machine, code_out, debug_flag):
    code_out.write("v2.0 raw \n")
    i = 0
    if debug_flag == True:
        print("(line 298)")
        print("Machine Array:")
    for line_num, line in enumerate(machine):
        print(line)
        for y in line:
            out = y.split('x')[1]
            code_out.write(out)
            i += len(out)
            if i % 4 == 0:
                code_out.write("\n")

if __name__ == "__main__":
    print("--------" + '\n' + "Initializing" + '\n' + "--------")
    debug_flag = debug(debug_flag)
    if debug_flag == True:
        print("debug() ran (line 313)")
    code_in = run_tests(test_flag, code_in, debug_flag)
    if debug_flag == True:
        print("run_tests() ran (line 316)")
    for line in code_in:
        read_input(code_in, line_num, assembly, debug_flag)
        if debug_flag == True:
            print("read_input() ran (line 320)")
        command_hex, com_error, error, error_exist = translate_command(assembly, command_hex, line_num, com_error, names, debug_flag, error)
        if com_error != None or len_error != None or arg_error != None:
            error_exist = True
            if debug_flag == True:
                print("Error exists (line 343)")
            break
        if debug_flag == True:
            print("translate_command() ran (line 328)")
            print("command_hex = {} and com_error = {}".format(command_hex, com_error))
        len_error = check_length(assembly, command_hex, line_num, len_error, error_exist, debug_flag, error)
        if com_error != None or len_error != None or arg_error != None:
            error_exist = True
            if debug_flag == True:
                print("Error exists (line 334)")
            break
        if debug_flag == True:
            print("check_length() ran (line 337): {}".format(len_error))
        arg_error = translate_args(assembly, command_hex, line_num, arg_error, machine, error_exist, debug_flag)
        if com_error != None or len_error != None or arg_error != None:
            error_exist = True
            if debug_flag == True:
                print("Error exists (line 342)")
            break
        if debug_flag == True:
            print("translate_args() ran (line 345)")
        display_error(assembly, line_num, com_error, len_error, arg_error, debug_flag)
        if debug_flag == True:
            print("display_error() ran (line 348)")
        if com_error != None or len_error != None or arg_error != None:
            error_exist = True
            if debug_flag == True:
                print("Error exists (line 352)")
            break
        line_num +=1
        if debug_flag == True:
            print("line_num counted up (line 356)")
        if error_exist != True:
            print("{} translation successful".format(command_name))
        print("-------")
    if error_exist != True:
        write_output(machine, code_out, debug_flag)
        if debug_flag == True:
            print("write_output() ran (line 363)")
        code_out.close()
        if debug_flag == True:
            print("code_out closed (line 366)")
            code_out = open("/Users/laumitt/Documents/Computer Internals/Code/machine.txt")
            print("code_out reopened (line 368)")
            final = code_out.read()
            print("code_out read (line 370)")
            print("--------" + '\n' + "Output" + '\n'+ final + "--------")
        print("Translation complete" + '\n' + "--------")
    if error_exist == True:
        if com_error != None:
            print("Error: {}".format(com_error))
        if len_error != None:
            print("Error: {}".format(len_error))
        if arg_error != None:
            print("Error: {}".format(arg_error))

code_in = open("assembly.txt", "r+")
code_out = open("machine.txt", "r+")
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

line_num = 0
assembly = []
machine = []
debug_flag = None
error_type = "No error"
error_list = []
command_text = None
command_hex = None
command_name = None

def debug(debug_flag):
    print("Debug? Y/N")
    debug = input()
    if debug == "Y" or debug == "y":
        print("Debug active")
        debug_flag = True
    else:
        print("No debug")
        debug_flag = False
    return debug_flag

def run_tests(debug_flag, code_in):
    print("Run tests? Y/N")
    test = input()
    if test == "Y" or test == "y":
        code_in = open("test_assembly.txt", "r+")
        if debug_flag == True:
            print("Using test code as input")
    else:
        code_in = open("assembly.txt", "r+")
        if debug_flag == True:
            print("Using example code as input")
    return code_in

def read_input(debug_flag, code_in, line_num, assembly):
    for line in code_in:
        assembly.append(line.split())
        if debug_flag == True:
            print("Appending {} to assembly line {}".format(line.split(), line_num))
        line_num += 1

def translate_command(debug_flag, assembly, operations, names, command_hex, command_name, line_num, error_list):
    command = assembly[line_num][0]
    command_hex = operations[command]
    command_name = names[command]
    if command_hex == None:
        error_type = "Command error: "
        error = "Not a valid command"
        error_list.append("Error of type: {}, {}".format(error_type, error))
        if debug_flag == True:
            print("Error of type: {}, {}".format(error_type, error))
    if debug_flag == True:
        print("Command: {}, assembly: {}, hex: {}".format(command_name, command, command_hex))
    return command_hex, command_name

if __name__ == "__main__":
    debug_flag = debug(debug_flag)
    if debug_flag == True:
        print("debug ran")
        print("Debug flag: {}".format(debug_flag))
    code_in = run_tests(debug_flag, code_in)
    if debug_flag == True:
        print("run_tests ran")
        print("Input code: {}".format(code_in.read()))
    #for line in code_in:
    read_input(debug_flag, code_in, line_num, assembly)
    if debug_flag == True:
        print("read_input ran")
    command_hex, command_name = translate_command(debug_flag, assembly, operations, names, command_hex, command_name, line_num, error_list)

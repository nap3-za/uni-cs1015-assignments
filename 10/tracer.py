# Tracer Debugger
# 04 May 2024


print("***** Program Trace Utility *****")


program_name = input("Enter the name of the program file: ")
program = open(program_name, "r")
program_contents = program.readlines()
program.close()

reverse = False
if program_contents[0] == '"""DEBUG"""\n':
	reverse = True
	del program_contents[0]
else:
	program_contents.insert(0, '"""DEBUG"""\n')

i = 0
while i < len(program_contents):
	line = program_contents[i]

	if line[0:4] == "def " and line[-3:-1] == "):":
		if reverse:
			del program_contents[i+1]
		else:
			function_name = line[4:line.find("(")]
			program_contents.insert(i+1, '    """DEBUG"""' + f";print('{function_name}')\n")
	i += 1


# Write the new contents
program = open(program_name, "w")
program.writelines(program_contents)
program.close()


if reverse:
	print("Program contains trace statements\nRemoving...Done")
else:
	print("Inserting...Done")
f = open('using_python_for_automation\inputFile.txt', 'r')
passFile = open('using_python_for_automation\PassFile.txt', 'w')
failFile = open('using_python_for_automation\FailFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()

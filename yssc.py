#!/usr/bin/python3
"""Convert statements that make sense to yices scripts"""

def write_file(filename):
    filename = filename + '.smt'
    new_file = open(filename,'w')
    var1 = varlist[0]
    var2 = varlist[1]
    var3 = varlist[2]
    var4 = varlist[3]
    text = """
(benchmark {0}
:extrapreds (({1}) ({2}) ({3}) ({4}))
:formula
{5}
)
""".format(filename,var1,var2,var3,var4,commands)
    new_file.write(text)
    endmessage = 'Succesfully wrote {0}'.format(filename)
    print(endmessage)


def read_file(name):
    file = open(name)
    text = file.read()
    textlist = text.split('\n')
    vars = []
    for line in textlist:
        if str(line).startswith('vars:'):
            varline = str(line)
            varlist = varline.split(' ')
            del varlist[0]
        elif str(line).startswith('formula:'):
            cmdline = str(line)
            cmdlist = cmdline.split(' ')
            del cmdlist[0]
            if 'V' in cmdlist:
                Vpos = cmdlist.index('V')
                cmdlist[Vpos] = 'or'
            elif '-->' in cmdlist:
                imppos = cmdlist.index('-->')
                cmdlist[imppos] = 'implies'
            elif '<->' in cmdlist:
                iffpos = cmdlist.index('<->')
                cmdlist[iffpos] = 'make_bi-implication!'


    commands = '(' + cmdlist[1] + ' ' + cmdlist[0].strip('(') + ' ' + cmdlist[2].strip(')') + ')'
    
    return text,varlist,commands



choice = input('Please choose the file you wish to convert\n')
text,varlist,commands = read_file(choice)
write_file(choice)





import parser.AgentScriptCCLoader as scc
import generator.AgentGenerator as ag

import os.path

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('USAGE: singlecc.py <program.ascript>')
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print('File %s not existing' % filename)
            exit(1)

        program = scc.parse_file(filename)
        if len(program.parsing_errors) > 0:
            for error in program.parsing_errors:
                print(error)
            exit(1)

        name = os.path.splitext(os.path.basename(filename))[0]

        generator = ag.Generator(name, program)
        pyprogram = generator.generate()

        print(pyprogram)
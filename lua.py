"""Usage:
    lua.py
    lua.py [-t]
    lua.py [-d] [<script>]

Arguments:
    <script>  Lua script to be run

Options:
    -h --help   show this help message
    -d --debug  print debug info
    -t --test   run in testing mode

"""

from interpreter import Interpreter
import interpreter
import parser
from docopt import docopt


def main():
    # while True:
    # s = input()

    s = "12 / 6 - 2 * 4"

    ast = parser.parse(s, debug=False)
    print("AST:", ast)
    interpreter = Interpreter(ast)
    result = interpreter.run()
    print(result)


if __name__ == "__main__":
    args = docopt(__doc__)

    # if a script is specified, we try to run it
    if args["<script>"]:
        with open(args["<script>"]) as f:
            script = f.read()
        ast = parser.parse(script, args["--debug"])

        if not ast:
            raise SystemExit
        lua_interpreter = interpreter.Interpreter(ast)

        try:
            result = lua_interpreter.run()
            print(result)
            raise SystemExit
        except RuntimeError:
            pass

    # otherwise enter interactive mode
    else:
        while True:
            try:
                if args["--test"]:
                    line = input()
                else:
                    line = input("> ")
            except EOFError:
                raise SystemExit
            ast = parser.parse(line, args["--debug"])

            if not ast:
                raise SystemExit

            lua_interpreter = interpreter.Interpreter(ast)

            try:
                result = lua_interpreter.run()
                print(result)
            except RuntimeError:
                pass

    main()

import sys

def main():
    # Check if we should read from args, or stdin
    if len(sys.argv) != 2:
        print("Usage: bashsmash <option>")
        print(" Options:")
        print("  Use a - (dash) to specify that this script should read from stdin")
        print("  Use anything in double quotes to pass bash code directly in via the program args")
        exit(0)

    # Read correctly
    if sys.argv[1] == "-":
        raw_program = input()
    else:
        raw_program = sys.argv[1]

    # List of functions we need
    functions = {
        "printf": lambda args: f"/???/??n/???n?f {args};",
    }

    def constructChar(char: str) -> str:
        char = str(oct(ord(char)))[2:]
        output = ""

        # iterate through each oct digit and build
        for dig in char:
            args = '"" '* int(dig)
            output += f"`__ {args}`"
        
        return output


    # program prefix and suffix
    prefix = "__() {" + functions["printf"]("${#}") + "}; $("
    suffix = ");"

    # Program
    program = ""

    # Build the program. One char at a time
    for char in raw_program:
        # Yes, we do need every single backslash
        program += functions["printf"](f"\"\\\\\\\\{constructChar(char)}\"")


    # Join the program and prefix
    output = prefix + functions["printf"]("$(" + program + ")") + suffix

    # Print out the result
    print(output)

# Weird python thing for starting a program
if __name__ == "__main__":
    main()
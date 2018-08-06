import sys
import prog4_1
import prog4_2


def main():
    print("Assignment #4-3, Brandon Baniqued, brandon.baniqued@gmail.com")
    with open(sys.argv[1], mode='r') as f:  # Open file designated in command line argument
        lines = [x.strip() for x in f.readlines()]  # Separate lines into list
        lines = [x for x in lines if len(x) > 0]  # Remove empty lines
        readTokens = []
        for x in lines:  # Tokenize each line
            readTokens.append(prog4_1.Tokenize(x))
        for x in readTokens:
            prog4_1.Parse(x)  # Parse each line

        StackM = prog4_2.StackMachine()
        lineNo = 0

        try:  # Attempt to execute operations
            while lineNo < len(readTokens):  # that are read from lines
                current = readTokens[lineNo]
                out = StackM.Execute(current)
                if out is not None:
                    print(out)
                lineNo = StackM.currentLine
                if (lineNo < 0):
                    print("Trying to execute invalid line: " + str(lineNo))
                    break
            print("Program terminated correctly")

        except IndexError as e:
            print("Line " + str(StackM.currentLine) + ": '" + current + "' caused " + e + ".")


if __name__ == "__main__":
    main()

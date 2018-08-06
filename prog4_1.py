def Tokenize(x):      #Takes a string and divides it up into a list
    validTokens = ["add","push","pop","sub","mul","div","mod","skip","save","get"]
    tokens = x.split()
    tokens = [x for x in tokens if len(x) > 0]
    data = []
    for i in range(0,len(tokens)):
        tok = tokens[i]
        if(tok not in validTokens):
            try:
                float(tok)
            except ValueError:
                print("Unexpected token: " + tok)
        data.append(tok)
    return data

def Parse(tokens):  #Takes Tokenized list and makes sure the syntax is correct
    twoPiece = ["push","save","get"]
    onePiece = ["pop","add","sub","mul","div","mod","skip"]
    for i in range(0,len(tokens)-1):
        tok = tokens[i]
        try:
            float(tok)
        except ValueError:
            pass
        else:
            continue
        if(not(tok in onePiece or tok in twoPiece)):
            raise ValueError("Parse error at: " + tok)
        if(tok in onePiece):
            try:
                float(tokens[i+1])
            except ValueError:
                continue
            else:
                raise ValueError("Parse error at: " + tok)
        if(tok in twoPiece):
            if(i+1 == len(tokens)):
                raise ValueError("Parse error at: " + tok)
            try:
                float(tokens[i+1])
            except ValueError:
                raise ValueError("Parse error at: " + tok)
    return 1


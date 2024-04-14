from myparser import MyParser

if __name__ == "__main__":
    parser = MyParser()
    while True:
        # getting input and parse while 'ctrl+d' pressed
        try:
            s = input('Input Exp >>>> ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(f"Result Is -> { {result} }\n")

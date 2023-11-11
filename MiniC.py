from MiniCParser import parser

def read_input():
    result = ''
    while True:
        data = input('Mini-C> ')
        if data == 'exit;':
            break
        if data:
            result += data + '\n'
        else:
            break
    return result.rstrip()  

# Main
while True:
    data = read_input()
    if data == 'exit;':
        break
    if not data:
        continue
    try:
        # Split the input data by newlines and process each statement separately
        statements = data.split('\n')
        for statement in statements:
            tree = parser.parse(statement)
            print(tree)
    except Exception as e:
        print(e)
        continue

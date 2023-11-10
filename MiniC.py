from MiniCParser import parser

def read_input():
    result = ''
    while True:
        data = input('Mini-C> ').strip()
        if data == 'exit;':
            break
        if data:
            result += data + '\n'  # Add a newline after each statement
        else:
            break
    return result.strip()

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
            if isinstance(tree, list) and tree[0] in ['if', 'while']:
                print(tree)
            else:
                print([tree])
    except Exception as e:
        print(e)
        continue

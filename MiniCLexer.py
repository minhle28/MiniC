import ply.lex as lex

# List of token names
tokens = (
    'ID',
    'NUM',
    'OPTR',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'ASSIGN',
    'SEMI',
    'IF',
    'WHILE',
)

# Regular expression rules for simple tokens
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMI = r';'
t_IF = r'if'
t_WHILE = r'while'
t_OPTR = r'>=|<=|==|>|<|\+|\-|\*'

# Define a rule for ID token
def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    return t

# Define a rule for NUM token
def t_NUM(t):
    r'[+-]?[0-9]+(\.[0-9]*)?'
    t.value = float(t.value)  # Convert to float type
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Rule for error handling
def t_error(t):
    print(f"Unrecognized character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
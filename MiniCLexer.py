import ply.lex as lex

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

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_SEMI = r';'
t_IF = r'if'
t_WHILE = r'while'
t_OPTR = r'>=|<=|==|>|<|\+|\-|\*'

ID_to_tokenKey = {
		'while' : 'WHILE',	
		'if'		: 'IF',	
		}

def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    t.type = ID_to_tokenKey.get( t.value, 'ID' )
    return t

def t_NUM(t):
    r'[+-]?[0-9]+(\.[0-9]*)?'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Unrecognized character '{t.value[0]}'")
    #t.lexer.skip(1)
    return t

lexer = lex.lex()

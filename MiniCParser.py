import ply.yacc as yacc
from MiniCLexer import tokens

# Parsing rules
def p_program(p):
    'program : stmtlist'
    p[0] = p[1]
    print('program:', p[0])

def p_stmt_block(p):
    'stmt : LBRACE stmtlist RBRACE'
    p[0] = p[2]
    print('stmt_block:', p[0])

def p_stmt_if(p):
    'stmt : IF LPAREN expr RPAREN stmt'
    p[0] = ['if', [p[3], p[5]]]
    print('stmt_if:', p[0])

def p_stmt_while(p):
    'stmt : WHILE LPAREN expr RPAREN stmt'
    p[0] = ['while', p[3], p[5]]
    print('stmt_while:', p[0])

def p_stmtlist_single(p):
    'stmtlist : stmt'
    p[0] = p[1]
    print('stmtlist_single:', p[0])

def p_stmtlist_multiple(p):
    'stmtlist : stmtlist stmt'
    p[0] = p[1] + p[2]
    print('stmtlist_multiple:', p[0])

def p_expr_id(p):
    'expr : ID'
    p[0] = ['id', p[1]]
    print('expr_id:', p[0])

def p_expr_num(p):
    'expr : NUM'
    p[0] = ['num', p[1]]
    print('expr_num:', p[0])

def p_stmt_expr_semi_assign(p):
    'stmt : ID ASSIGN expr SEMI'
    p[0] = [['id', p[1]], '=', p[3]]
    print('stmt_expr_semi_assign:', p[0])

def p_stmt_expr_semi_num(p):
    'stmt : ID ASSIGN NUM SEMI'
    p[0] = [['id', p[1]], '=', ['num', p[3]]]
    print('stmt_expr_semi_num:', p[0])

def p_expr_optr(p):
    'expr : expr OPTR expr'
    p[0] = [p[1], ['optr', p[2]], p[3]]
    print('expr_optr:', p[0])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

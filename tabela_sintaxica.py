TABELA_SINTAXICA = {
    'PROGRAM': {'def': ['FUNCLIST'], 'ident': ['STATEMENT'], '{': ['STATEMENT'], 'int': ['STATEMENT'], 'float': ['STATEMENT'], 'string': ['STATEMENT'], ';': ['STATEMENT'], 'break': ['STATEMENT'],'print': ['STATEMENT'], 'read': ['STATEMENT'], 'return': ['STATEMENT'], 'if': ['STATEMENT'], 'for': ['STATEMENT'], '$': []},
    'FUNCLIST': {'def': ['FUNCDEF', 'T6']},
    'FUNCDEF': {'def': ['def', 'ident', '(', 'PARAMLIST', ')', '{', 'STATELIST', '}']},
    'PARAMLIST': {')': [], 'int': ['int', 'ident', 'T7'], 'float': ['float', 'ident', 'T7'], 'string': ['string', 'ident', 'T7']},
    'STATEMENT': {'ident': ['ATRIBSTAT', ';'], '{': ['{', 'STATELIST', '}'], 'int': ['VARDECL', ';'], 'float': ['VARDECL', ';'], 'string': ['VARDECL', ';'], ';': [';'], 'break': ['break', ';'], 'print': ['PRINTSTAT', ';'], 'read': ['READSTAT', ';'], 'return': ['RETURNSTAT', ';'], 'if': ['IFSTAT'], 'for': ['FORSTAT']},
    'VARDECL': {'int': ['int', 'ident', 'T1'], 'float': ['float', 'ident', 'T1'], 'string': ['string', 'ident', 'T1']},
    'ATRIBSTAT': {'ident': ['LVALUE', '=', 'T8']},
    'FUNCCALL': {'exec': ['exec', 'ident', '(', 'PARAMLISTCALL', ')']},
    'PARAMLISTCALL': {'ident': ['ident', 'T9'], ')': []},
    'PRINTSTAT': {'print': ['print', 'EXPRESSION']},
    'READSTAT': {'read': ['read', 'LVALUE']},
    'RETURNSTAT': {'return': ['return']},
    'IFSTAT': {'if': ['if', '(', 'EXPRESSION', ')', '{', 'STATEMENT', '}', 'T10']},
    'FORSTAT': {'for': ['for', '(', 'ATRIBSTAT', ';', 'EXPRESSION', ';', 'ATRIBSTAT', ')', 'STATEMENT']},
    'STATELIST': {'ident': ['STATEMENT', 'T11'], '{': ['STATEMENT', 'T11'], 'int': ['STATEMENT', 'T11'], 'float': ['STATEMENT', 'T11'], 'string': ['STATEMENT', 'T11'], ';': ['STATEMENT', 'T11'], 'break': ['STATEMENT', 'T11'], 'print': ['STATEMENT', 'T11'], 'read': ['STATEMENT', 'T11'], 'return': ['STATEMENT', 'T11'], 'if': ['STATEMENT', 'T11'], 'for': ['STATEMENT', 'T11']},
    'ALLOCEXPRESSION': {'new': ['new', 'T12']},
    'NUMEXPRESSION': {'ident': ['TERM', 'T3'], '(': ['TERM', 'T3'], 'int_constant': ['TERM', 'T3'], '+': ['TERM', 'T3'], '-': ['TERM', 'T3'], 'float_constant': ['TERM', 'T3'], 'string_constant': ['TERM', 'T3'], 'null': ['TERM', 'T3']},
    'EXPRESSION': {'ident': ['NUMEXPRESSION', 'T14'], '(': ['NUMEXPRESSION', 'T14'], 'int_constant': ['NUMEXPRESSION', 'T14'], '+': ['NUMEXPRESSION', 'T14'], '-': ['NUMEXPRESSION', 'T14'], 'float_constant': ['NUMEXPRESSION', 'T14'], 'string_constant': ['NUMEXPRESSION', 'T14'], 'null': ['NUMEXPRESSION', 'T14']},
    'TERM': {'ident': ['UNARYEXPR', 'T4'], '(': ['UNARYEXPR', 'T4'], 'int_constant': ['UNARYEXPR', 'T4'], '+': ['UNARYEXPR', 'T4'], '-': ['UNARYEXPR', 'T4'], 'float_constant': ['UNARYEXPR', 'T4'], 'string_constant': ['UNARYEXPR', 'T4'], 'null': ['UNARYEXPR', 'T4']},
    'UNARYEXPR': {'ident': ['FACTOR'], '(': ['FACTOR'], 'int_constant': ['FACTOR'], '+': ['+', 'FACTOR'], '-': ['-', 'FACTOR'], 'float_constant': ['FACTOR'], 'string_constant': ['FACTOR'], 'null': ['FACTOR']},
    'FACTOR': {'ident': ['LVALUE'], '(': ['(', 'NUMEXPRESSION', ')'], 'int_constant': ['int_constant'], 'float_constant': ['float_constant'], 'string_constant': ['string_constant'], 'null': ['null']},
    'LVALUE': {'ident': ['ident', 'T5']},
    'T1': {';': [], '[': ['[', 'int_constant', ']', 'T1'], ')': []},
    'T2': {'[': ['[', 'NUMEXPRESSION', ']', 'T13']},
    'T3': {'ident': [], ',': [], ')': [], ';': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': ['+', 'TERM', 'T3'], '-': ['-', 'TERM', 'T3']},
    'T4': {'ident': [], ',': [], ')': [], ';': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': [], '-': [], '*': ['*', 'UNARYEXPR', 'T4'], '/': ['/', 'UNARYEXPR', 'T4'], '%': ['%', 'UNARYEXPR', 'T4']},
    'T5': {',': [], ')': [], ';': [], '[': ['[', 'NUMEXPRESSION', ']', 'T5'], '=': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': [], '-': [], '*': [], '/': [], '%': []},
    'T6': {'def': ['FUNCLIST'], '$': []},
    'T7': {',': [',', 'PARAMLIST'], ')': []},
    'T8': {'ident': ['EXPRESSION'], 'exec': ['FUNCCALL'], '(': ['EXPRESSION'], 'int_constant': ['EXPRESSION'], 'new': ['ALLOCEXPRESSION'], '+': ['EXPRESSION'], '-': ['EXPRESSION'], 'float_constant': ['EXPRESSION'], 'string_constant': ['EXPRESSION'], 'null': ['EXPRESSION']},
    'T9': {',': [',', 'PARAMLISTCALL'], ')': []},
    'T10': {'ident': [], '{': [], '}': [], 'int': [], 'float': [], 'string': [], ';': [], 'break': [], 'print': [], 'read': [], 'return': [], 'if': [], 'else': ['else', '{', 'STATEMENT', '}'], 'for': [], '$': []},
    'T11': {'ident': ['STATELIST'], '{': ['STATELIST'], '}': [], 'int': ['STATELIST'], 'float': ['STATELIST'], 'string': ['STATELIST'], ';': ['STATELIST'], 'break': ['STATELIST'], 'print': ['STATELIST'], 'read': ['STATELIST'], 'return': ['STATELIST'], 'if': ['STATELIST'], 'for': ['STATELIST']},
    'T12': {'int': ['int', 'T2'], 'float': ['float', 'T2'], 'string': ['string', 'T2']},
    'T13': {')': [], ';': [], '[': ['T2']},
    'T14': {'ident': [], ')': [], ';': [], '<': ['<', 'NUMEXPRESSION'], '>': ['>', 'NUMEXPRESSION'], '<=': ['<=', 'NUMEXPRESSION'], '>=': ['>=', 'NUMEXPRESSION'], '==': ['==', 'NUMEXPRESSION'], '!=': ['!=', 'NUMEXPRESSION']}
}
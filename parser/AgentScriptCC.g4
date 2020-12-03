grammar AgentScriptCC;

// agent script structure

program : ( initial_attitude | transformational_rule | active_rule )+ ;

// main components

initial_attitude : ( belief | procedural_goal | achievement_goal | maintenance_goal ) DOT ;

belief : neg_literal ;
test_goal : QUESTIONMARK neg_literal ;
procedural_goal : EXCLAMATIONMARK AT pos_literal ;
achievement_goal : EXCLAMATIONMARK neg_literal ;
maintenance_goal : DOUBLEEXCLAMATIONMARK neg_literal ;

// active rules: goal-plan and percept-plan rules

active_rule : trigger ( COLON list_conditions )? ACTIVERULEOPERATOR list_actions DOT ;
trigger : ( PLUS | MINUS ) ( belief | test_goal | procedural_goal | achievement_goal | maintenance_goal ) ;
list_actions : action ( SEMICOLON action )*  ;
action : primitive_action | belief_action | goal_action | SUCCESS | FAIL  ;
belief_action: ( PLUS | MINUS ) (belief | maintenance_goal) ;
goal_action: procedural_goal | achievement_goal | test_goal ; // we are not considering interventions on other threads

primitive_action : HASH primitive_invocation | PRIMITIVECODE ;
primitive_invocation : ( ( LOWERCASEATOM DOT )+ | UPPERCASEATOM DOT )? LOWERCASEATOM ( LEFTROUNDBRACKET RIGHTROUNDBRACKET | list_predicate_terms )  ; // for Python

// transformational rules, e.g. inferential

transformational_rule : ( belief )? TRANSFORMATIONALRULEOPERATOR list_conditions DOT ;

list_conditions : logical_expression ( COMMA logical_expression )* ;

arithmetic_expression
: l=arithmetic_expression binaryoperator=ARITHMETICBINARYOPERATOR1 r=arithmetic_expression
| l=arithmetic_expression binaryoperator=ARITHMETICBINARYOPERATOR2 r=arithmetic_expression
| l=arithmetic_expression binaryoperator=ARITHMETICBINARYOPERATOR3 r=arithmetic_expression
| arithmetic_expression_term
;

logical_arithmetic_expression
: l=arithmetic_expression binaryoperator=RELATIONALARITHMETICOPERATOR r=arithmetic_expression
;

logical_expression:
// l=logical_expression binaryoperator=LOGICALOPERATOR1 r=logical_expression
//| l=logical_expression binaryoperator=LOGICALOPERATOR2 r=logical_expression
//| l=logical_expression binaryoperator=LOGICALOPERATOR3 r=logical_expression
| l=logical_expression binaryoperator=RELATIONALLOGICALOPERATOR r=logical_expression
| logical_arithmetic_expression
| logical_expression_term
;

// --- term elements ---------------------------------------------------------------

neg_literal : ( STRONGNEGATION )? pos_literal ;
pos_literal : LOWERCASEATOM ( list_predicate_terms )? ;
naf_attitude : (DEFAULTNEGATION)? ( belief | procedural_goal | test_goal | achievement_goal | maintenance_goal );

variable : UPPERCASEATOM ;
constant : NUMBER | STRING ;

list_predicate_terms : LEFTROUNDBRACKET predicate_term ( COMMA predicate_term )* RIGHTROUNDBRACKET ;
predicate_term : LOWERCASEATOM | variable | constant ; // no predicate functions!

arithmetic_expression_term : variable | constant ;
logical_expression_term : naf_attitude | TRUE | FALSE ;

// keywords

NUMBER : MINUS? DIGITSEQUENCE ;
STRING : SINGLEQUOTESTRING | DOUBLEQUOTESTRING ;

PRIMITIVECODE : '#{' .*? '}' ;

PLUS : '+' ;
MINUS : '-' ;

// operators

STRONGNEGATION : '~' ;
DEFAULTNEGATION : 'not' ;

// LOGICALOPERATOR1 : AND ;
// LOGICALOPERATOR2 : XOR ;
// LOGICALOPERATOR3 : OR ;

ARITHMETICBINARYOPERATOR1 : POW ;
ARITHMETICBINARYOPERATOR2 : MULTIPLY | DIVIDE | MODULO ;
ARITHMETICBINARYOPERATOR3 : PLUS | MINUS ;

RELATIONALLOGICALOPERATOR : EQUAL | NOTEQUAL ;
RELATIONALARITHMETICOPERATOR : EQUAL | NOTEQUAL | LESS | LESSEQUAL | GREATER | GREATEREQUAL ;

// atoms

UPPERCASEATOM : ( UPPERCASELETTER | UNDERSCORE ) ( LOWERCASELETTER | UPPERCASELETTER | MINUS | UNDERSCORE )* ;
LOWERCASEATOM : LOWERCASELETTER ( LOWERCASELETTER | UPPERCASELETTER | DIGIT | MINUS | UNDERSCORE )* ;

// lexemes

DOUBLEEXCLAMATIONMARK : '!!' ;
EXCLAMATIONMARK : '!' ;
COMMA : ',' ;
QUESTIONMARK : '?' ;
DOLLAR : '$' ;
VLINE : '|' ;
HASH : '#' ;

ACTIVERULEOPERATOR : '=>' ;
TRANSFORMATIONALRULEOPERATOR : ':-' ;
AT : '@' ;
COLON : ':' ;
SEMICOLON : ';' ;
DOT : '.' ;
UNDERSCORE : '_' ;
LEFTSHIFT : '<<' ;
RIGHTSHIFT : '>>' ;

LEFTROUNDBRACKET : '(' ;
RIGHTROUNDBRACKET : ')' ;
LEFTANGULARBRACKET : '[' ;
RIGHTANGULARBRACKET : ']' ;
LEFTCURVEDBRACKET : '{' ;
RIGHTCURVEDBRACKET : '}' ;

// fragment AND : '&&' | 'and' | COMMA ;
// fragment OR : '||' | 'or' | COLON ;
// fragment XOR : '^' | 'xor' ;

TRUE : 'true' ;
FALSE : 'false' ;
SUCCESS : 'success' ;
FAIL : 'fail' ;

fragment LESS : '<' ;
fragment LESSEQUAL : '<=' ;
fragment GREATER : '>' ;
fragment GREATEREQUAL : '>=' ;
fragment EQUAL : '==' ;
fragment NOTEQUAL : '!=' ;
fragment POW : '**' ;
fragment MULTIPLY : '*' ;
fragment DIVIDE : '/' ;
fragment MODULO : '%' | 'mod' ;

fragment SINGLEQUOTESTRING : '\'' ~('\'')* '\'' ;
fragment DOUBLEQUOTESTRING : '"' ~('"')* '"' ;

fragment LOWERCASELETTER : [a-z] ;
fragment UPPERCASELETTER : [A-Z] ;
fragment DIGIT : [0-9] ;
fragment DIGITSEQUENCE : DIGIT+ ('.' DIGIT+)? ;

// skip items

WHITESPACE : (' ' | '\n' | '\t' | '\r')+ -> skip;
LINECOMMENT : '//' .*? '\r'? '\n' -> skip;
BLOCKCOMMENT : '/*' .*? '*/' -> skip;
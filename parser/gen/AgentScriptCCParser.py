# Generated from /home/giovanni/ownCloud/dev/pycosmos/mas/scriptcc/singlecc/parser/AgentScriptCC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u00fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\3\2\6\2@\n\2\r\2\16\2A\3\3\3\3\3\3\3\3\5\3H\n")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\5\t^\n\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\5\nj\n\n\3\13\3\13\3\13\7\13")
        buf.write("o\n\13\f\13\16\13r\13\13\3\f\3\f\3\f\3\f\3\f\5\fy\n\f")
        buf.write("\3\r\3\r\3\r\5\r~\n\r\3\16\3\16\3\16\5\16\u0083\n\16\3")
        buf.write("\17\3\17\3\17\5\17\u0088\n\17\3\20\3\20\6\20\u008c\n\20")
        buf.write("\r\20\16\20\u008d\3\20\3\20\5\20\u0092\n\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u0098\n\20\3\21\5\21\u009b\n\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\7\22\u00a4\n\22\f\22\16\22")
        buf.write("\u00a7\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u00b5\n\23\f\23\16\23\u00b8\13")
        buf.write("\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u00c1\n\25")
        buf.write("\3\25\3\25\3\25\7\25\u00c6\n\25\f\25\16\25\u00c9\13\25")
        buf.write("\3\26\5\26\u00cc\n\26\3\26\3\26\3\27\3\27\5\27\u00d2\n")
        buf.write("\27\3\30\5\30\u00d5\n\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00dc\n\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u00e6\n\33\f\33\16\33\u00e9\13\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\5\34\u00f0\n\34\3\35\3\35\5\35\u00f4\n\35\3\36")
        buf.write("\3\36\3\36\5\36\u00f9\n\36\3\36\2\4$(\37\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:\2\4\3")
        buf.write("\2\6\7\3\2\3\4\2\u010a\2?\3\2\2\2\4G\3\2\2\2\6K\3\2\2")
        buf.write("\2\bM\3\2\2\2\nP\3\2\2\2\fT\3\2\2\2\16W\3\2\2\2\20Z\3")
        buf.write("\2\2\2\22c\3\2\2\2\24k\3\2\2\2\26x\3\2\2\2\30z\3\2\2\2")
        buf.write("\32\u0082\3\2\2\2\34\u0087\3\2\2\2\36\u0091\3\2\2\2 \u009a")
        buf.write("\3\2\2\2\"\u00a0\3\2\2\2$\u00a8\3\2\2\2&\u00b9\3\2\2\2")
        buf.write("(\u00c0\3\2\2\2*\u00cb\3\2\2\2,\u00cf\3\2\2\2.\u00d4\3")
        buf.write("\2\2\2\60\u00dd\3\2\2\2\62\u00df\3\2\2\2\64\u00e1\3\2")
        buf.write("\2\2\66\u00ef\3\2\2\28\u00f3\3\2\2\2:\u00f8\3\2\2\2<@")
        buf.write("\5\4\3\2=@\5 \21\2>@\5\20\t\2?<\3\2\2\2?=\3\2\2\2?>\3")
        buf.write("\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\3\3\2\2\2CH\5\6")
        buf.write("\4\2DH\5\n\6\2EH\5\f\7\2FH\5\16\b\2GC\3\2\2\2GD\3\2\2")
        buf.write("\2GE\3\2\2\2GF\3\2\2\2HI\3\2\2\2IJ\7\35\2\2J\5\3\2\2\2")
        buf.write("KL\5*\26\2L\7\3\2\2\2MN\7\24\2\2NO\5*\26\2O\t\3\2\2\2")
        buf.write("PQ\7\22\2\2QR\7\32\2\2RS\5,\27\2S\13\3\2\2\2TU\7\22\2")
        buf.write("\2UV\5*\26\2V\r\3\2\2\2WX\7\21\2\2XY\5*\26\2Y\17\3\2\2")
        buf.write("\2Z]\5\22\n\2[\\\7\33\2\2\\^\5\"\22\2][\3\2\2\2]^\3\2")
        buf.write("\2\2^_\3\2\2\2_`\7\30\2\2`a\5\24\13\2ab\7\35\2\2b\21\3")
        buf.write("\2\2\2ci\t\2\2\2dj\5\6\4\2ej\5\b\5\2fj\5\n\6\2gj\5\f\7")
        buf.write("\2hj\5\16\b\2id\3\2\2\2ie\3\2\2\2if\3\2\2\2ig\3\2\2\2")
        buf.write("ih\3\2\2\2j\23\3\2\2\2kp\5\26\f\2lm\7\34\2\2mo\5\26\f")
        buf.write("\2nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\25\3\2\2\2")
        buf.write("rp\3\2\2\2sy\5\34\17\2ty\5\30\r\2uy\5\32\16\2vy\7)\2\2")
        buf.write("wy\7*\2\2xs\3\2\2\2xt\3\2\2\2xu\3\2\2\2xv\3\2\2\2xw\3")
        buf.write("\2\2\2y\27\3\2\2\2z}\t\2\2\2{~\5\6\4\2|~\5\16\b\2}{\3")
        buf.write("\2\2\2}|\3\2\2\2~\31\3\2\2\2\177\u0083\5\n\6\2\u0080\u0083")
        buf.write("\5\f\7\2\u0081\u0083\5\b\5\2\u0082\177\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0081\3\2\2\2\u0083\33\3\2\2\2\u0084\u0085")
        buf.write("\7\27\2\2\u0085\u0088\5\36\20\2\u0086\u0088\7\5\2\2\u0087")
        buf.write("\u0084\3\2\2\2\u0087\u0086\3\2\2\2\u0088\35\3\2\2\2\u0089")
        buf.write("\u008a\7\20\2\2\u008a\u008c\7\35\2\2\u008b\u0089\3\2\2")
        buf.write("\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u0092\3\2\2\2\u008f\u0090\7\17\2\2\u0090")
        buf.write("\u0092\7\35\2\2\u0091\u008b\3\2\2\2\u0091\u008f\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0097")
        buf.write("\7\20\2\2\u0094\u0095\7!\2\2\u0095\u0098\7\"\2\2\u0096")
        buf.write("\u0098\5\64\33\2\u0097\u0094\3\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\37\3\2\2\2\u0099\u009b\5\6\4\2\u009a\u0099\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d")
        buf.write("\7\31\2\2\u009d\u009e\5\"\22\2\u009e\u009f\7\35\2\2\u009f")
        buf.write("!\3\2\2\2\u00a0\u00a5\5(\25\2\u00a1\u00a2\7\23\2\2\u00a2")
        buf.write("\u00a4\5(\25\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2")
        buf.write("\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6#\3\2\2")
        buf.write("\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\b\23\1\2\u00a9\u00aa")
        buf.write("\58\35\2\u00aa\u00b6\3\2\2\2\u00ab\u00ac\f\6\2\2\u00ac")
        buf.write("\u00ad\7\n\2\2\u00ad\u00b5\5$\23\7\u00ae\u00af\f\5\2\2")
        buf.write("\u00af\u00b0\7\13\2\2\u00b0\u00b5\5$\23\6\u00b1\u00b2")
        buf.write("\f\4\2\2\u00b2\u00b3\7\f\2\2\u00b3\u00b5\5$\23\5\u00b4")
        buf.write("\u00ab\3\2\2\2\u00b4\u00ae\3\2\2\2\u00b4\u00b1\3\2\2\2")
        buf.write("\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3")
        buf.write("\2\2\2\u00b7%\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba")
        buf.write("\5$\23\2\u00ba\u00bb\7\16\2\2\u00bb\u00bc\5$\23\2\u00bc")
        buf.write("\'\3\2\2\2\u00bd\u00c1\b\25\1\2\u00be\u00c1\5&\24\2\u00bf")
        buf.write("\u00c1\5:\36\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c1\u00c7\3\2\2\2\u00c2\u00c3\f")
        buf.write("\5\2\2\u00c3\u00c4\7\r\2\2\u00c4\u00c6\5(\25\6\u00c5\u00c2")
        buf.write("\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8)\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cc\7\b\2\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\u00ce\5,\27\2\u00ce+\3\2\2")
        buf.write("\2\u00cf\u00d1\7\20\2\2\u00d0\u00d2\5\64\33\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2-\3\2\2\2\u00d3\u00d5")
        buf.write("\7\t\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00db\3\2\2\2\u00d6\u00dc\5\6\4\2\u00d7\u00dc\5\n\6\2")
        buf.write("\u00d8\u00dc\5\b\5\2\u00d9\u00dc\5\f\7\2\u00da\u00dc\5")
        buf.write("\16\b\2\u00db\u00d6\3\2\2\2\u00db\u00d7\3\2\2\2\u00db")
        buf.write("\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2")
        buf.write("\u00dc/\3\2\2\2\u00dd\u00de\7\17\2\2\u00de\61\3\2\2\2")
        buf.write("\u00df\u00e0\t\3\2\2\u00e0\63\3\2\2\2\u00e1\u00e2\7!\2")
        buf.write("\2\u00e2\u00e7\5\66\34\2\u00e3\u00e4\7\23\2\2\u00e4\u00e6")
        buf.write("\5\66\34\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7\"\2\2\u00eb\65\3\2")
        buf.write("\2\2\u00ec\u00f0\7\20\2\2\u00ed\u00f0\5\60\31\2\u00ee")
        buf.write("\u00f0\5\62\32\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2")
        buf.write("\2\u00ef\u00ee\3\2\2\2\u00f0\67\3\2\2\2\u00f1\u00f4\5")
        buf.write("\60\31\2\u00f2\u00f4\5\62\32\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f49\3\2\2\2\u00f5\u00f9\5.\30\2\u00f6")
        buf.write("\u00f9\7\'\2\2\u00f7\u00f9\7(\2\2\u00f8\u00f5\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9;\3\2\2")
        buf.write("\2\35?AG]ipx}\u0082\u0087\u008d\u0091\u0097\u009a\u00a5")
        buf.write("\u00b4\u00b6\u00c0\u00c7\u00cb\u00d1\u00d4\u00db\u00e7")
        buf.write("\u00ef\u00f3\u00f8")
        return buf.getvalue()


class AgentScriptCCParser ( Parser ):

    grammarFileName = "AgentScriptCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'~'", "'not'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'!!'", "'!'", "','", "'?'", "'$'", "'|'", 
                     "'#'", "'=>'", "':-'", "'@'", "':'", "';'", "'.'", 
                     "'_'", "'<<'", "'>>'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'true'", "'false'", "'success'", "'fail'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "STRING", "PRIMITIVECODE", 
                      "PLUS", "MINUS", "STRONGNEGATION", "DEFAULTNEGATION", 
                      "ARITHMETICBINARYOPERATOR1", "ARITHMETICBINARYOPERATOR2", 
                      "ARITHMETICBINARYOPERATOR3", "RELATIONALLOGICALOPERATOR", 
                      "RELATIONALARITHMETICOPERATOR", "UPPERCASEATOM", "LOWERCASEATOM", 
                      "DOUBLEEXCLAMATIONMARK", "EXCLAMATIONMARK", "COMMA", 
                      "QUESTIONMARK", "DOLLAR", "VLINE", "HASH", "ACTIVERULEOPERATOR", 
                      "TRANSFORMATIONALRULEOPERATOR", "AT", "COLON", "SEMICOLON", 
                      "DOT", "UNDERSCORE", "LEFTSHIFT", "RIGHTSHIFT", "LEFTROUNDBRACKET", 
                      "RIGHTROUNDBRACKET", "LEFTANGULARBRACKET", "RIGHTANGULARBRACKET", 
                      "LEFTCURVEDBRACKET", "RIGHTCURVEDBRACKET", "TRUE", 
                      "FALSE", "SUCCESS", "FAIL", "WHITESPACE", "LINECOMMENT", 
                      "BLOCKCOMMENT" ]

    RULE_program = 0
    RULE_initial_attitude = 1
    RULE_belief = 2
    RULE_test_goal = 3
    RULE_procedural_goal = 4
    RULE_achievement_goal = 5
    RULE_maintenance_goal = 6
    RULE_active_rule = 7
    RULE_trigger = 8
    RULE_list_actions = 9
    RULE_action = 10
    RULE_belief_action = 11
    RULE_goal_action = 12
    RULE_primitive_action = 13
    RULE_primitive_invocation = 14
    RULE_transformational_rule = 15
    RULE_list_conditions = 16
    RULE_arithmetic_expression = 17
    RULE_logical_arithmetic_expression = 18
    RULE_logical_expression = 19
    RULE_neg_literal = 20
    RULE_pos_literal = 21
    RULE_naf_attitude = 22
    RULE_variable = 23
    RULE_constant = 24
    RULE_list_predicate_terms = 25
    RULE_predicate_term = 26
    RULE_arithmetic_expression_term = 27
    RULE_logical_expression_term = 28

    ruleNames =  [ "program", "initial_attitude", "belief", "test_goal", 
                   "procedural_goal", "achievement_goal", "maintenance_goal", 
                   "active_rule", "trigger", "list_actions", "action", "belief_action", 
                   "goal_action", "primitive_action", "primitive_invocation", 
                   "transformational_rule", "list_conditions", "arithmetic_expression", 
                   "logical_arithmetic_expression", "logical_expression", 
                   "neg_literal", "pos_literal", "naf_attitude", "variable", 
                   "constant", "list_predicate_terms", "predicate_term", 
                   "arithmetic_expression_term", "logical_expression_term" ]

    EOF = Token.EOF
    NUMBER=1
    STRING=2
    PRIMITIVECODE=3
    PLUS=4
    MINUS=5
    STRONGNEGATION=6
    DEFAULTNEGATION=7
    ARITHMETICBINARYOPERATOR1=8
    ARITHMETICBINARYOPERATOR2=9
    ARITHMETICBINARYOPERATOR3=10
    RELATIONALLOGICALOPERATOR=11
    RELATIONALARITHMETICOPERATOR=12
    UPPERCASEATOM=13
    LOWERCASEATOM=14
    DOUBLEEXCLAMATIONMARK=15
    EXCLAMATIONMARK=16
    COMMA=17
    QUESTIONMARK=18
    DOLLAR=19
    VLINE=20
    HASH=21
    ACTIVERULEOPERATOR=22
    TRANSFORMATIONALRULEOPERATOR=23
    AT=24
    COLON=25
    SEMICOLON=26
    DOT=27
    UNDERSCORE=28
    LEFTSHIFT=29
    RIGHTSHIFT=30
    LEFTROUNDBRACKET=31
    RIGHTROUNDBRACKET=32
    LEFTANGULARBRACKET=33
    RIGHTANGULARBRACKET=34
    LEFTCURVEDBRACKET=35
    RIGHTCURVEDBRACKET=36
    TRUE=37
    FALSE=38
    SUCCESS=39
    FAIL=40
    WHITESPACE=41
    LINECOMMENT=42
    BLOCKCOMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initial_attitude(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Initial_attitudeContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Initial_attitudeContext,i)


        def transformational_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Transformational_ruleContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Transformational_ruleContext,i)


        def active_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Active_ruleContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Active_ruleContext,i)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AgentScriptCCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.initial_attitude()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.transformational_rule()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.active_rule()
                    pass


                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AgentScriptCCParser.PLUS) | (1 << AgentScriptCCParser.MINUS) | (1 << AgentScriptCCParser.STRONGNEGATION) | (1 << AgentScriptCCParser.LOWERCASEATOM) | (1 << AgentScriptCCParser.DOUBLEEXCLAMATIONMARK) | (1 << AgentScriptCCParser.EXCLAMATIONMARK) | (1 << AgentScriptCCParser.TRANSFORMATIONALRULEOPERATOR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initial_attitudeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(AgentScriptCCParser.DOT, 0)

        def belief(self):
            return self.getTypedRuleContext(AgentScriptCCParser.BeliefContext,0)


        def procedural_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Procedural_goalContext,0)


        def achievement_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Achievement_goalContext,0)


        def maintenance_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Maintenance_goalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_initial_attitude

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitial_attitude" ):
                listener.enterInitial_attitude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitial_attitude" ):
                listener.exitInitial_attitude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitial_attitude" ):
                return visitor.visitInitial_attitude(self)
            else:
                return visitor.visitChildren(self)




    def initial_attitude(self):

        localctx = AgentScriptCCParser.Initial_attitudeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_initial_attitude)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 65
                self.belief()
                pass

            elif la_ == 2:
                self.state = 66
                self.procedural_goal()
                pass

            elif la_ == 3:
                self.state = 67
                self.achievement_goal()
                pass

            elif la_ == 4:
                self.state = 68
                self.maintenance_goal()
                pass


            self.state = 71
            self.match(AgentScriptCCParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeliefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neg_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Neg_literalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_belief

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBelief" ):
                listener.enterBelief(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBelief" ):
                listener.exitBelief(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBelief" ):
                return visitor.visitBelief(self)
            else:
                return visitor.visitChildren(self)




    def belief(self):

        localctx = AgentScriptCCParser.BeliefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_belief)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.neg_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_goalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTIONMARK(self):
            return self.getToken(AgentScriptCCParser.QUESTIONMARK, 0)

        def neg_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Neg_literalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_test_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest_goal" ):
                listener.enterTest_goal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest_goal" ):
                listener.exitTest_goal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest_goal" ):
                return visitor.visitTest_goal(self)
            else:
                return visitor.visitChildren(self)




    def test_goal(self):

        localctx = AgentScriptCCParser.Test_goalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_test_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(AgentScriptCCParser.QUESTIONMARK)
            self.state = 76
            self.neg_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedural_goalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATIONMARK(self):
            return self.getToken(AgentScriptCCParser.EXCLAMATIONMARK, 0)

        def AT(self):
            return self.getToken(AgentScriptCCParser.AT, 0)

        def pos_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Pos_literalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_procedural_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedural_goal" ):
                listener.enterProcedural_goal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedural_goal" ):
                listener.exitProcedural_goal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedural_goal" ):
                return visitor.visitProcedural_goal(self)
            else:
                return visitor.visitChildren(self)




    def procedural_goal(self):

        localctx = AgentScriptCCParser.Procedural_goalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_procedural_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(AgentScriptCCParser.EXCLAMATIONMARK)
            self.state = 79
            self.match(AgentScriptCCParser.AT)
            self.state = 80
            self.pos_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Achievement_goalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATIONMARK(self):
            return self.getToken(AgentScriptCCParser.EXCLAMATIONMARK, 0)

        def neg_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Neg_literalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_achievement_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAchievement_goal" ):
                listener.enterAchievement_goal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAchievement_goal" ):
                listener.exitAchievement_goal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAchievement_goal" ):
                return visitor.visitAchievement_goal(self)
            else:
                return visitor.visitChildren(self)




    def achievement_goal(self):

        localctx = AgentScriptCCParser.Achievement_goalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_achievement_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(AgentScriptCCParser.EXCLAMATIONMARK)
            self.state = 83
            self.neg_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Maintenance_goalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLEEXCLAMATIONMARK(self):
            return self.getToken(AgentScriptCCParser.DOUBLEEXCLAMATIONMARK, 0)

        def neg_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Neg_literalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_maintenance_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaintenance_goal" ):
                listener.enterMaintenance_goal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaintenance_goal" ):
                listener.exitMaintenance_goal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaintenance_goal" ):
                return visitor.visitMaintenance_goal(self)
            else:
                return visitor.visitChildren(self)




    def maintenance_goal(self):

        localctx = AgentScriptCCParser.Maintenance_goalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_maintenance_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(AgentScriptCCParser.DOUBLEEXCLAMATIONMARK)
            self.state = 86
            self.neg_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Active_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trigger(self):
            return self.getTypedRuleContext(AgentScriptCCParser.TriggerContext,0)


        def ACTIVERULEOPERATOR(self):
            return self.getToken(AgentScriptCCParser.ACTIVERULEOPERATOR, 0)

        def list_actions(self):
            return self.getTypedRuleContext(AgentScriptCCParser.List_actionsContext,0)


        def DOT(self):
            return self.getToken(AgentScriptCCParser.DOT, 0)

        def COLON(self):
            return self.getToken(AgentScriptCCParser.COLON, 0)

        def list_conditions(self):
            return self.getTypedRuleContext(AgentScriptCCParser.List_conditionsContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_active_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActive_rule" ):
                listener.enterActive_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActive_rule" ):
                listener.exitActive_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActive_rule" ):
                return visitor.visitActive_rule(self)
            else:
                return visitor.visitChildren(self)




    def active_rule(self):

        localctx = AgentScriptCCParser.Active_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_active_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.trigger()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AgentScriptCCParser.COLON:
                self.state = 89
                self.match(AgentScriptCCParser.COLON)
                self.state = 90
                self.list_conditions()


            self.state = 93
            self.match(AgentScriptCCParser.ACTIVERULEOPERATOR)
            self.state = 94
            self.list_actions()
            self.state = 95
            self.match(AgentScriptCCParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TriggerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(AgentScriptCCParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AgentScriptCCParser.MINUS, 0)

        def belief(self):
            return self.getTypedRuleContext(AgentScriptCCParser.BeliefContext,0)


        def test_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Test_goalContext,0)


        def procedural_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Procedural_goalContext,0)


        def achievement_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Achievement_goalContext,0)


        def maintenance_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Maintenance_goalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_trigger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigger" ):
                listener.enterTrigger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigger" ):
                listener.exitTrigger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigger" ):
                return visitor.visitTrigger(self)
            else:
                return visitor.visitChildren(self)




    def trigger(self):

        localctx = AgentScriptCCParser.TriggerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_trigger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==AgentScriptCCParser.PLUS or _la==AgentScriptCCParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 98
                self.belief()
                pass

            elif la_ == 2:
                self.state = 99
                self.test_goal()
                pass

            elif la_ == 3:
                self.state = 100
                self.procedural_goal()
                pass

            elif la_ == 4:
                self.state = 101
                self.achievement_goal()
                pass

            elif la_ == 5:
                self.state = 102
                self.maintenance_goal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_actionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.ActionContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.ActionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AgentScriptCCParser.SEMICOLON)
            else:
                return self.getToken(AgentScriptCCParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_list_actions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_actions" ):
                listener.enterList_actions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_actions" ):
                listener.exitList_actions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_actions" ):
                return visitor.visitList_actions(self)
            else:
                return visitor.visitChildren(self)




    def list_actions(self):

        localctx = AgentScriptCCParser.List_actionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.action()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AgentScriptCCParser.SEMICOLON:
                self.state = 106
                self.match(AgentScriptCCParser.SEMICOLON)
                self.state = 107
                self.action()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_action(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Primitive_actionContext,0)


        def belief_action(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Belief_actionContext,0)


        def goal_action(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Goal_actionContext,0)


        def SUCCESS(self):
            return self.getToken(AgentScriptCCParser.SUCCESS, 0)

        def FAIL(self):
            return self.getToken(AgentScriptCCParser.FAIL, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = AgentScriptCCParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_action)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.PRIMITIVECODE, AgentScriptCCParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.primitive_action()
                pass
            elif token in [AgentScriptCCParser.PLUS, AgentScriptCCParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.belief_action()
                pass
            elif token in [AgentScriptCCParser.EXCLAMATIONMARK, AgentScriptCCParser.QUESTIONMARK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.goal_action()
                pass
            elif token in [AgentScriptCCParser.SUCCESS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.match(AgentScriptCCParser.SUCCESS)
                pass
            elif token in [AgentScriptCCParser.FAIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.match(AgentScriptCCParser.FAIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Belief_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(AgentScriptCCParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AgentScriptCCParser.MINUS, 0)

        def belief(self):
            return self.getTypedRuleContext(AgentScriptCCParser.BeliefContext,0)


        def maintenance_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Maintenance_goalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_belief_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBelief_action" ):
                listener.enterBelief_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBelief_action" ):
                listener.exitBelief_action(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBelief_action" ):
                return visitor.visitBelief_action(self)
            else:
                return visitor.visitChildren(self)




    def belief_action(self):

        localctx = AgentScriptCCParser.Belief_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_belief_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==AgentScriptCCParser.PLUS or _la==AgentScriptCCParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.STRONGNEGATION, AgentScriptCCParser.LOWERCASEATOM]:
                self.state = 121
                self.belief()
                pass
            elif token in [AgentScriptCCParser.DOUBLEEXCLAMATIONMARK]:
                self.state = 122
                self.maintenance_goal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goal_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedural_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Procedural_goalContext,0)


        def achievement_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Achievement_goalContext,0)


        def test_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Test_goalContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_goal_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal_action" ):
                listener.enterGoal_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal_action" ):
                listener.exitGoal_action(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoal_action" ):
                return visitor.visitGoal_action(self)
            else:
                return visitor.visitChildren(self)




    def goal_action(self):

        localctx = AgentScriptCCParser.Goal_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_goal_action)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.procedural_goal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.achievement_goal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.test_goal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(AgentScriptCCParser.HASH, 0)

        def primitive_invocation(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Primitive_invocationContext,0)


        def PRIMITIVECODE(self):
            return self.getToken(AgentScriptCCParser.PRIMITIVECODE, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_primitive_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_action" ):
                listener.enterPrimitive_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_action" ):
                listener.exitPrimitive_action(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_action" ):
                return visitor.visitPrimitive_action(self)
            else:
                return visitor.visitChildren(self)




    def primitive_action(self):

        localctx = AgentScriptCCParser.Primitive_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_action)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(AgentScriptCCParser.HASH)
                self.state = 131
                self.primitive_invocation()
                pass
            elif token in [AgentScriptCCParser.PRIMITIVECODE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(AgentScriptCCParser.PRIMITIVECODE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWERCASEATOM(self, i:int=None):
            if i is None:
                return self.getTokens(AgentScriptCCParser.LOWERCASEATOM)
            else:
                return self.getToken(AgentScriptCCParser.LOWERCASEATOM, i)

        def LEFTROUNDBRACKET(self):
            return self.getToken(AgentScriptCCParser.LEFTROUNDBRACKET, 0)

        def RIGHTROUNDBRACKET(self):
            return self.getToken(AgentScriptCCParser.RIGHTROUNDBRACKET, 0)

        def list_predicate_terms(self):
            return self.getTypedRuleContext(AgentScriptCCParser.List_predicate_termsContext,0)


        def UPPERCASEATOM(self):
            return self.getToken(AgentScriptCCParser.UPPERCASEATOM, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(AgentScriptCCParser.DOT)
            else:
                return self.getToken(AgentScriptCCParser.DOT, i)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_primitive_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_invocation" ):
                listener.enterPrimitive_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_invocation" ):
                listener.exitPrimitive_invocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_invocation" ):
                return visitor.visitPrimitive_invocation(self)
            else:
                return visitor.visitChildren(self)




    def primitive_invocation(self):

        localctx = AgentScriptCCParser.Primitive_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_invocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 137 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 135
                        self.match(AgentScriptCCParser.LOWERCASEATOM)
                        self.state = 136
                        self.match(AgentScriptCCParser.DOT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)


            elif la_ == 2:
                self.state = 141
                self.match(AgentScriptCCParser.UPPERCASEATOM)
                self.state = 142
                self.match(AgentScriptCCParser.DOT)


            self.state = 145
            self.match(AgentScriptCCParser.LOWERCASEATOM)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(AgentScriptCCParser.LEFTROUNDBRACKET)
                self.state = 147
                self.match(AgentScriptCCParser.RIGHTROUNDBRACKET)
                pass

            elif la_ == 2:
                self.state = 148
                self.list_predicate_terms()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Transformational_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSFORMATIONALRULEOPERATOR(self):
            return self.getToken(AgentScriptCCParser.TRANSFORMATIONALRULEOPERATOR, 0)

        def list_conditions(self):
            return self.getTypedRuleContext(AgentScriptCCParser.List_conditionsContext,0)


        def DOT(self):
            return self.getToken(AgentScriptCCParser.DOT, 0)

        def belief(self):
            return self.getTypedRuleContext(AgentScriptCCParser.BeliefContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_transformational_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransformational_rule" ):
                listener.enterTransformational_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransformational_rule" ):
                listener.exitTransformational_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransformational_rule" ):
                return visitor.visitTransformational_rule(self)
            else:
                return visitor.visitChildren(self)




    def transformational_rule(self):

        localctx = AgentScriptCCParser.Transformational_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_transformational_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AgentScriptCCParser.STRONGNEGATION or _la==AgentScriptCCParser.LOWERCASEATOM:
                self.state = 151
                self.belief()


            self.state = 154
            self.match(AgentScriptCCParser.TRANSFORMATIONALRULEOPERATOR)
            self.state = 155
            self.list_conditions()
            self.state = 156
            self.match(AgentScriptCCParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_conditionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Logical_expressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentScriptCCParser.COMMA)
            else:
                return self.getToken(AgentScriptCCParser.COMMA, i)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_list_conditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_conditions" ):
                listener.enterList_conditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_conditions" ):
                listener.exitList_conditions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_conditions" ):
                return visitor.visitList_conditions(self)
            else:
                return visitor.visitChildren(self)




    def list_conditions(self):

        localctx = AgentScriptCCParser.List_conditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.logical_expression(0)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AgentScriptCCParser.COMMA:
                self.state = 159
                self.match(AgentScriptCCParser.COMMA)
                self.state = 160
                self.logical_expression(0)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.l = None # Arithmetic_expressionContext
            self.binaryoperator = None # Token
            self.r = None # Arithmetic_expressionContext

        def arithmetic_expression_term(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Arithmetic_expression_termContext,0)


        def arithmetic_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Arithmetic_expressionContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Arithmetic_expressionContext,i)


        def ARITHMETICBINARYOPERATOR1(self):
            return self.getToken(AgentScriptCCParser.ARITHMETICBINARYOPERATOR1, 0)

        def ARITHMETICBINARYOPERATOR2(self):
            return self.getToken(AgentScriptCCParser.ARITHMETICBINARYOPERATOR2, 0)

        def ARITHMETICBINARYOPERATOR3(self):
            return self.getToken(AgentScriptCCParser.ARITHMETICBINARYOPERATOR3, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_arithmetic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expression" ):
                listener.enterArithmetic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expression" ):
                listener.exitArithmetic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression" ):
                return visitor.visitArithmetic_expression(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AgentScriptCCParser.Arithmetic_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_arithmetic_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.arithmetic_expression_term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 178
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = AgentScriptCCParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 170
                        localctx.binaryoperator = self.match(AgentScriptCCParser.ARITHMETICBINARYOPERATOR1)
                        self.state = 171
                        localctx.r = self.arithmetic_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = AgentScriptCCParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 173
                        localctx.binaryoperator = self.match(AgentScriptCCParser.ARITHMETICBINARYOPERATOR2)
                        self.state = 174
                        localctx.r = self.arithmetic_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = AgentScriptCCParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 176
                        localctx.binaryoperator = self.match(AgentScriptCCParser.ARITHMETICBINARYOPERATOR3)
                        self.state = 177
                        localctx.r = self.arithmetic_expression(3)
                        pass

             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_arithmetic_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.l = None # Arithmetic_expressionContext
            self.binaryoperator = None # Token
            self.r = None # Arithmetic_expressionContext

        def arithmetic_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Arithmetic_expressionContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Arithmetic_expressionContext,i)


        def RELATIONALARITHMETICOPERATOR(self):
            return self.getToken(AgentScriptCCParser.RELATIONALARITHMETICOPERATOR, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_logical_arithmetic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_arithmetic_expression" ):
                listener.enterLogical_arithmetic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_arithmetic_expression" ):
                listener.exitLogical_arithmetic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_arithmetic_expression" ):
                return visitor.visitLogical_arithmetic_expression(self)
            else:
                return visitor.visitChildren(self)




    def logical_arithmetic_expression(self):

        localctx = AgentScriptCCParser.Logical_arithmetic_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logical_arithmetic_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            localctx.l = self.arithmetic_expression(0)
            self.state = 184
            localctx.binaryoperator = self.match(AgentScriptCCParser.RELATIONALARITHMETICOPERATOR)
            self.state = 185
            localctx.r = self.arithmetic_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.l = None # Logical_expressionContext
            self.binaryoperator = None # Token
            self.r = None # Logical_expressionContext

        def logical_arithmetic_expression(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Logical_arithmetic_expressionContext,0)


        def logical_expression_term(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Logical_expression_termContext,0)


        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Logical_expressionContext,i)


        def RELATIONALLOGICALOPERATOR(self):
            return self.getToken(AgentScriptCCParser.RELATIONALLOGICALOPERATOR, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AgentScriptCCParser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 188
                self.logical_arithmetic_expression()
                pass

            elif la_ == 3:
                self.state = 189
                self.logical_expression_term()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AgentScriptCCParser.Logical_expressionContext(self, _parentctx, _parentState)
                    localctx.l = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 192
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 193
                    localctx.binaryoperator = self.match(AgentScriptCCParser.RELATIONALLOGICALOPERATOR)
                    self.state = 194
                    localctx.r = self.logical_expression(4) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Neg_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pos_literal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Pos_literalContext,0)


        def STRONGNEGATION(self):
            return self.getToken(AgentScriptCCParser.STRONGNEGATION, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_neg_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg_literal" ):
                listener.enterNeg_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg_literal" ):
                listener.exitNeg_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_literal" ):
                return visitor.visitNeg_literal(self)
            else:
                return visitor.visitChildren(self)




    def neg_literal(self):

        localctx = AgentScriptCCParser.Neg_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_neg_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AgentScriptCCParser.STRONGNEGATION:
                self.state = 200
                self.match(AgentScriptCCParser.STRONGNEGATION)


            self.state = 203
            self.pos_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pos_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWERCASEATOM(self):
            return self.getToken(AgentScriptCCParser.LOWERCASEATOM, 0)

        def list_predicate_terms(self):
            return self.getTypedRuleContext(AgentScriptCCParser.List_predicate_termsContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_pos_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPos_literal" ):
                listener.enterPos_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPos_literal" ):
                listener.exitPos_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos_literal" ):
                return visitor.visitPos_literal(self)
            else:
                return visitor.visitChildren(self)




    def pos_literal(self):

        localctx = AgentScriptCCParser.Pos_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_pos_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(AgentScriptCCParser.LOWERCASEATOM)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 206
                self.list_predicate_terms()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Naf_attitudeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def belief(self):
            return self.getTypedRuleContext(AgentScriptCCParser.BeliefContext,0)


        def procedural_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Procedural_goalContext,0)


        def test_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Test_goalContext,0)


        def achievement_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Achievement_goalContext,0)


        def maintenance_goal(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Maintenance_goalContext,0)


        def DEFAULTNEGATION(self):
            return self.getToken(AgentScriptCCParser.DEFAULTNEGATION, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_naf_attitude

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNaf_attitude" ):
                listener.enterNaf_attitude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNaf_attitude" ):
                listener.exitNaf_attitude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNaf_attitude" ):
                return visitor.visitNaf_attitude(self)
            else:
                return visitor.visitChildren(self)




    def naf_attitude(self):

        localctx = AgentScriptCCParser.Naf_attitudeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_naf_attitude)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AgentScriptCCParser.DEFAULTNEGATION:
                self.state = 209
                self.match(AgentScriptCCParser.DEFAULTNEGATION)


            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 212
                self.belief()
                pass

            elif la_ == 2:
                self.state = 213
                self.procedural_goal()
                pass

            elif la_ == 3:
                self.state = 214
                self.test_goal()
                pass

            elif la_ == 4:
                self.state = 215
                self.achievement_goal()
                pass

            elif la_ == 5:
                self.state = 216
                self.maintenance_goal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPPERCASEATOM(self):
            return self.getToken(AgentScriptCCParser.UPPERCASEATOM, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = AgentScriptCCParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(AgentScriptCCParser.UPPERCASEATOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AgentScriptCCParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(AgentScriptCCParser.STRING, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = AgentScriptCCParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not(_la==AgentScriptCCParser.NUMBER or _la==AgentScriptCCParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_predicate_termsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTROUNDBRACKET(self):
            return self.getToken(AgentScriptCCParser.LEFTROUNDBRACKET, 0)

        def predicate_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentScriptCCParser.Predicate_termContext)
            else:
                return self.getTypedRuleContext(AgentScriptCCParser.Predicate_termContext,i)


        def RIGHTROUNDBRACKET(self):
            return self.getToken(AgentScriptCCParser.RIGHTROUNDBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentScriptCCParser.COMMA)
            else:
                return self.getToken(AgentScriptCCParser.COMMA, i)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_list_predicate_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_predicate_terms" ):
                listener.enterList_predicate_terms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_predicate_terms" ):
                listener.exitList_predicate_terms(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_predicate_terms" ):
                return visitor.visitList_predicate_terms(self)
            else:
                return visitor.visitChildren(self)




    def list_predicate_terms(self):

        localctx = AgentScriptCCParser.List_predicate_termsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_predicate_terms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(AgentScriptCCParser.LEFTROUNDBRACKET)
            self.state = 224
            self.predicate_term()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AgentScriptCCParser.COMMA:
                self.state = 225
                self.match(AgentScriptCCParser.COMMA)
                self.state = 226
                self.predicate_term()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(AgentScriptCCParser.RIGHTROUNDBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWERCASEATOM(self):
            return self.getToken(AgentScriptCCParser.LOWERCASEATOM, 0)

        def variable(self):
            return self.getTypedRuleContext(AgentScriptCCParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(AgentScriptCCParser.ConstantContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_predicate_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_term" ):
                listener.enterPredicate_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_term" ):
                listener.exitPredicate_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_term" ):
                return visitor.visitPredicate_term(self)
            else:
                return visitor.visitChildren(self)




    def predicate_term(self):

        localctx = AgentScriptCCParser.Predicate_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_predicate_term)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.LOWERCASEATOM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(AgentScriptCCParser.LOWERCASEATOM)
                pass
            elif token in [AgentScriptCCParser.UPPERCASEATOM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.variable()
                pass
            elif token in [AgentScriptCCParser.NUMBER, AgentScriptCCParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expression_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(AgentScriptCCParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(AgentScriptCCParser.ConstantContext,0)


        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_arithmetic_expression_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expression_term" ):
                listener.enterArithmetic_expression_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expression_term" ):
                listener.exitArithmetic_expression_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression_term" ):
                return visitor.visitArithmetic_expression_term(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_expression_term(self):

        localctx = AgentScriptCCParser.Arithmetic_expression_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arithmetic_expression_term)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.UPPERCASEATOM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.variable()
                pass
            elif token in [AgentScriptCCParser.NUMBER, AgentScriptCCParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expression_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def naf_attitude(self):
            return self.getTypedRuleContext(AgentScriptCCParser.Naf_attitudeContext,0)


        def TRUE(self):
            return self.getToken(AgentScriptCCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AgentScriptCCParser.FALSE, 0)

        def getRuleIndex(self):
            return AgentScriptCCParser.RULE_logical_expression_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression_term" ):
                listener.enterLogical_expression_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression_term" ):
                listener.exitLogical_expression_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression_term" ):
                return visitor.visitLogical_expression_term(self)
            else:
                return visitor.visitChildren(self)




    def logical_expression_term(self):

        localctx = AgentScriptCCParser.Logical_expression_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_logical_expression_term)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AgentScriptCCParser.STRONGNEGATION, AgentScriptCCParser.DEFAULTNEGATION, AgentScriptCCParser.LOWERCASEATOM, AgentScriptCCParser.DOUBLEEXCLAMATIONMARK, AgentScriptCCParser.EXCLAMATIONMARK, AgentScriptCCParser.QUESTIONMARK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.naf_attitude()
                pass
            elif token in [AgentScriptCCParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(AgentScriptCCParser.TRUE)
                pass
            elif token in [AgentScriptCCParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(AgentScriptCCParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.arithmetic_expression_sempred
        self._predicates[19] = self.logical_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         





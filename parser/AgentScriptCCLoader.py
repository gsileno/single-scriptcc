import antlr4
import logging

import parser.AgentScriptCC as lp
from parser.gen.AgentScriptCCParser import AgentScriptCCParser
from parser.gen.AgentScriptCCLexer import AgentScriptCCLexer
from parser.gen.AgentScriptCCListener import AgentScriptCCListener
from parser.AgentScriptCCErrorListener import AgentScriptCCErrorListener

logging.basicConfig(filename='parser.log', filemode='w', level=logging.INFO)


class AgentScriptCCLoader(AgentScriptCCListener):

    def __init__(self):
        self.decorations = {}
        self.program = lp.Program()

    def exitPos_literal(self, ctx):
        if ctx.list_predicate_terms():
            terms = tuple(self.decorations[ctx.list_predicate_terms()])
        else:
            terms = ()
        pos_literal = lp.PosLiteral(ctx.LOWERCASEATOM().getText(), terms)

        self.decorations[ctx] = pos_literal
        logging.info("captured pos_literal: " + str(pos_literal))

    def exitNeg_literal(self, ctx):
        pos_literal = self.decorations[ctx.pos_literal()]
        neg = True if ctx.STRONGNEGATION() else False
        neg_literal = lp.NegLiteral(pos_literal, neg)
        self.decorations[ctx] = neg_literal
        logging.info("captured neg_literal: " + str(neg_literal))

    def exitBelief(self, ctx):
        neg_literal = self.decorations[ctx.neg_literal()]
        belief = lp.Belief(neg_literal)
        self.decorations[ctx] = belief
        logging.info("captured belief: " + str(belief))

    def exitTest_goal(self, ctx: AgentScriptCCParser.Test_goalContext):
        neg_literal = self.decorations[ctx.neg_literal()]
        goal = lp.TestGoal(neg_literal)
        self.decorations[ctx] = goal
        logging.info("captured test goal: " + str(goal))

    def exitProcedural_goal(self, ctx: AgentScriptCCParser.Procedural_goalContext):
        pos_literal = self.decorations[ctx.pos_literal()]
        goal = lp.ProceduralGoal(pos_literal)
        self.decorations[ctx] = goal
        logging.info("captured procedural goal: " + str(goal))

    def exitAchievement_goal(self, ctx: AgentScriptCCParser.Achievement_goalContext):
        neg_literal = self.decorations[ctx.neg_literal()]
        goal = lp.AchievementGoal(neg_literal)
        self.decorations[ctx] = goal
        logging.info("captured achievement goal: " + str(goal))

    def exitMaintenance_goal(self, ctx: AgentScriptCCParser.Maintenance_goalContext):
        neg_literal = self.decorations[ctx.neg_literal()]
        goal = lp.MaintenanceGoal(neg_literal)
        self.decorations[ctx] = goal
        logging.info("captured maintenance goal: " + str(goal))

    def exitNaf_attitude(self, ctx: AgentScriptCCParser.Naf_attitudeContext):

        if ctx.belief():
            attitude = self.decorations[ctx.belief()]
        elif ctx.test_goal():
            attitude = self.decorations[ctx.test_goal()]
        elif ctx.procedural_goal():
            attitude = self.decorations[ctx.procedural_goal()]
        elif ctx.achievement_goal():
            attitude = self.decorations[ctx.achievement_goal()]
        elif ctx.maintenance_goal():
            attitude = self.decorations[ctx.maintenance_goal()]
        else:
            raise RuntimeError("You should not be here.")

        naf = True if ctx.DEFAULTNEGATION() else False
        naf_attitude = lp.ExtMentalAttitude(attitude, naf)
        self.decorations[ctx] = naf_attitude
        logging.info("captured extended attitude: " + str(naf_attitude))

    def exitVariable(self, ctx: AgentScriptCCParser.VariableContext):
        identifier = ctx.UPPERCASEATOM().getText()
        variable = lp.Variable(identifier)
        self.decorations[ctx] = variable
        logging.info("captured variable: " + str(variable))

    def exitConstant(self, ctx: AgentScriptCCParser.ConstantContext):
        if ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
        elif ctx.STRING():
            value = ctx.NUMBER().getText()
        else:
            raise RuntimeError("You should not be here.")
        constant = lp.Constant(value)
        self.decorations[ctx] = constant
        logging.info("captured constant: " + str(constant))

    def exitPredicate_term(self, ctx: AgentScriptCCParser.Predicate_termContext):
        if ctx.LOWERCASEATOM():
            term = lp.PosLiteral(ctx.LOWERCASEATOM().getText())
        elif ctx.variable():
            term = self.decorations[ctx.variable()]
        elif ctx.constant():
            term = self.decorations[ctx.constant()]
        else:
            raise RuntimeError("You should not be here.")

        self.decorations[ctx] = term
        logging.info("captured predicate term: " + str(term))

    def exitList_predicate_terms(self, ctx: AgentScriptCCParser.List_predicate_termsContext):
        terms = []
        for node in ctx.predicate_term():
            terms.append(self.decorations[node])
        self.decorations[ctx] = terms
        logging.info("captured list terms: " + str(terms))

    def exitLogical_expression_term(self, ctx: AgentScriptCCParser.Logical_expression_termContext):
        if ctx.naf_attitude():
            term = self.decorations[ctx.naf_attitude()]
        elif ctx.TRUE():
            term = True
        elif ctx.FALSE():
            term = False
        else:
            raise RuntimeError("You should not be here.")
        self.decorations[ctx] = term
        logging.info("captured logical expression term: " + str(term))

    def exitArithmetic_expression_term(self, ctx: AgentScriptCCParser.Arithmetic_expression_termContext):
        if ctx.variable():
            term = self.decorations[ctx.variable()]
        elif ctx.constant():
            term = self.decorations[ctx.constant()]
        else:
            raise RuntimeError("You should not be here.")
        self.decorations[ctx] = term
        logging.info("captured arithmetic expression term: " + str(term))

    def exitLogical_expression(self, ctx: AgentScriptCCParser.Logical_expressionContext):
        if ctx.RELATIONALLOGICALOPERATOR():
            operator = lp.Operator[ctx.RELATIONALLOGICALOPERATOR().getText()]
            left_term = self.decorations[ctx.l]
            right_term = self.decorations[ctx.r]
            expression = lp.BinaryExpression(operator, left_term, right_term)
        elif ctx.logical_arithmetic_expression():
            expression = self.decorations[ctx.logical_arithmetic_expression()]
        elif ctx.logical_expression_term():
            expression = self.decorations[ctx.logical_expression_term()]
        else:
            raise RuntimeError("You should not be here.")
        self.decorations[ctx] = expression
        logging.info("captured logical expression: " + str(expression))

    def exitLogical_arithmetic_expression(self, ctx: AgentScriptCCParser.Logical_arithmetic_expressionContext):
        operator = lp.Operator.from_text(ctx.RELATIONALARITHMETICOPERATOR().getText())
        left_term = self.decorations[ctx.l]
        right_term = self.decorations[ctx.r]
        expression = lp.BinaryExpression(operator, left_term, right_term)
        self.decorations[ctx] = expression
        logging.info("captured logical arithmetic expression: " + str(expression))

    def exitArithmetic_expression(self, ctx: AgentScriptCCParser.Arithmetic_expressionContext):
        if ctx.arithmetic_expression_term():
            expression = self.decorations[ctx.arithmetic_expression_term()]
        else:
            if ctx.ARITHMETICBINARYOPERATOR1():
                operator = lp.Operator[ctx.ARITHMETICBINARYOPERATOR1().getText()]
            elif ctx.ARITHMETICBINARYOPERATOR2():
                operator = lp.Operator[ctx.ARITHMETICBINARYOPERATOR2().getText()]
            elif ctx.ARITHMETICBINARYOPERATOR3():
                operator = lp.Operator[ctx.ARITHMETICBINARYOPERATOR3().getText()]
            else:
                raise RuntimeError("You should not be here.")
            left_term = self.decorations[ctx.l]
            right_term = self.decorations[ctx.r]
            expression = lp.BinaryExpression(operator, left_term, right_term)

        self.decorations[ctx] = expression
        logging.info("captured arithmetic expression: " + str(expression))

    def exitList_conditions(self, ctx: AgentScriptCCParser.List_conditionsContext):
        conditions = []
        for node in ctx.logical_expression():
            conditions.append(self.decorations[node])
        self.decorations[ctx] = conditions
        logging.info("captured list conditions: " + str(conditions))

    def exitTransformational_rule(self, ctx: AgentScriptCCParser.Transformational_ruleContext):
        if ctx.belief():
            conclusion = self.decorations[ctx.belief()]
        else:
            conclusion = None
        conditions = self.decorations[ctx.list_conditions()]
        rule = lp.TransformationalRule(conclusion, conditions)
        self.decorations[ctx] = rule
        logging.info("captured transformational rule: " + str(rule))
        self.program.transformational_rules.append(rule)

    def exitPrimitive_invocation(self, ctx: AgentScriptCCParser.Primitive_invocationContext):
        if ctx.DOT():
            raise RuntimeError("Not yet implemented")
        elif ctx.UPPERCASEATOM():
            raise RuntimeError("Not yet implemented")

        primitive = lp.PrimitiveAction(ctx.LOWERCASEATOM(0).getText(), ())
        self.decorations[ctx] = primitive
        logging.info("captured primitive action: " + str(primitive))

    def exitPrimitive_action(self, ctx: AgentScriptCCParser.Primitive_actionContext):
        if ctx.primitive_invocation():
            action = self.decorations[ctx.primitive_invocation()]
        elif ctx.PRIMITIVECODE():
            action = lp.PrimitiveAction(ctx.PRIMITIVECODE().getText())
        else:
            raise RuntimeError("You should not be here.")
        self.decorations[ctx] = action
        logging.info("captured primitive action: " + str(action))

    def exitBelief_action(self, ctx: AgentScriptCCParser.Belief_actionContext):
        if ctx.PLUS():
            production = True
        elif ctx.MINUS():
            production = False
        else:
            raise RuntimeError("You should not be here.")

        if ctx.belief():
            attitude = self.decorations[ctx.belief()]
        elif ctx.maintenance_goal():
            attitude = self.decorations[ctx.maintenance_goal()]
        else:
            raise RuntimeError("You should not be here.")

        action = lp.InternalAction(attitude, production)
        self.decorations[ctx] = action
        logging.info("captured belief action: " + str(action))

    def exitGoal_action(self, ctx: AgentScriptCCParser.Goal_actionContext):
        if ctx.procedural_goal():
            attitude = self.decorations[ctx.procedural_goal()]
        elif ctx.achievement_goal():
            attitude = self.decorations[ctx.achievement_goal()]
        elif ctx.test_goal():
            attitude = self.decorations[ctx.test_goal()]
        else:
            raise RuntimeError("You should not be here.")
        action = lp.InternalAction(attitude)
        self.decorations[ctx] = action
        logging.info("captured goal action: " + str(action))

    def exitAction(self, ctx: AgentScriptCCParser.ActionContext):
        if ctx.SUCCESS():
            action = True
        elif ctx.FAIL():
            action = False
        elif ctx.primitive_action():
            action = self.decorations[ctx.primitive_action()]
        elif ctx.belief_action():
            action = self.decorations[ctx.belief_action()]
        elif ctx.goal_action():
            action = self.decorations[ctx.goal_action()]
        else:
            raise RuntimeError("You should not be here.")
        self.decorations[ctx] = action
        logging.info("captured action: " + str(action))

    def exitList_actions(self, ctx: AgentScriptCCParser.List_actionsContext):
        actions = []
        for node in ctx.action():
            actions.append(self.decorations[node])
        self.decorations[ctx] = actions
        logging.info("captured list conditions: " + str(actions))

    def exitTrigger(self, ctx: AgentScriptCCParser.TriggerContext):
        if ctx.PLUS():
            production = True
        elif ctx.MINUS():
            production = False
        else:
            raise RuntimeError("You should not be here.")

        if ctx.belief():
            attitude = self.decorations[ctx.belief()]
        elif ctx.test_goal():
            attitude = self.decorations[ctx.test_goal()]
        elif ctx.procedural_goal():
            attitude = self.decorations[ctx.procedural_goal()]
        elif ctx.achievement_goal():
            attitude = self.decorations[ctx.achievement_goal()]
        elif ctx.maintenance_goal():
            attitude = self.decorations[ctx.maintenance_goal()]
        else:
            raise RuntimeError("You should not be here.")

        event = lp.Event(attitude, production)
        self.decorations[ctx] = event
        logging.info("captured trigger event: " + str(event))

    def exitActive_rule(self, ctx: AgentScriptCCParser.Active_ruleContext):
        event = self.decorations[ctx.trigger()]
        conditions = self.decorations[ctx.list_conditions()] if ctx.COLON() else None
        actions = self.decorations[ctx.list_actions()]

        rule = lp.ActiveRule(event, conditions, actions)
        self.decorations[ctx] = rule
        logging.info("captured active rule: " + str(rule))
        self.program.active_rules.append(rule)

    def exitInitial_attitude(self, ctx: AgentScriptCCParser.Initial_attitudeContext):
        if ctx.belief():
            attitude = self.decorations[ctx.belief()]
        elif ctx.procedural_goal():
            attitude = self.decorations[ctx.procedural_goal()]
        elif ctx.achievement_goal():
            attitude = self.decorations[ctx.achievement_goal()]
        elif ctx.maintenance_goal():
            attitude = self.decorations[ctx.maintenance_goal()]
        else:
            raise RuntimeError("You should not be here.")

        self.decorations[ctx] = attitude
        logging.info("captured initial attitude " + str(attitude))
        self.program.initial_attitudes.append(attitude)


def parse_string(code):
    return parse(antlr4.InputStream(code))


def parse_file(filename):
    with open(filename, 'r') as my_file:
        code = my_file.read().replace('\n', '')
    return parse_string(code)


def parse(input_stream):
    lexer = AgentScriptCCLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = AgentScriptCCParser(stream)

    parser.removeErrorListeners()
    errorListener = AgentScriptCCErrorListener()
    parser.addErrorListener(errorListener)

    tree = parser.program()
    loader = AgentScriptCCLoader()
    walker = antlr4.ParseTreeWalker()
    walker.walk(loader, tree)

    program = loader.program
    program.parsing_errors = errorListener.errors

    return program

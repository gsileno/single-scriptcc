# Generated from /home/giovanni/ownCloud/dev/pycosmos/mas/scriptcc/singlecc/parser/AgentScriptCC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AgentScriptCCParser import AgentScriptCCParser
else:
    from AgentScriptCCParser import AgentScriptCCParser

# This class defines a complete generic visitor for a parse tree produced by AgentScriptCCParser.

class AgentScriptCCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AgentScriptCCParser#program.
    def visitProgram(self, ctx:AgentScriptCCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#initial_attitude.
    def visitInitial_attitude(self, ctx:AgentScriptCCParser.Initial_attitudeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#belief.
    def visitBelief(self, ctx:AgentScriptCCParser.BeliefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#test_goal.
    def visitTest_goal(self, ctx:AgentScriptCCParser.Test_goalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#procedural_goal.
    def visitProcedural_goal(self, ctx:AgentScriptCCParser.Procedural_goalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#achievement_goal.
    def visitAchievement_goal(self, ctx:AgentScriptCCParser.Achievement_goalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#maintenance_goal.
    def visitMaintenance_goal(self, ctx:AgentScriptCCParser.Maintenance_goalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#active_rule.
    def visitActive_rule(self, ctx:AgentScriptCCParser.Active_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#trigger.
    def visitTrigger(self, ctx:AgentScriptCCParser.TriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#list_actions.
    def visitList_actions(self, ctx:AgentScriptCCParser.List_actionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#action.
    def visitAction(self, ctx:AgentScriptCCParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#belief_action.
    def visitBelief_action(self, ctx:AgentScriptCCParser.Belief_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#goal_action.
    def visitGoal_action(self, ctx:AgentScriptCCParser.Goal_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#primitive_action.
    def visitPrimitive_action(self, ctx:AgentScriptCCParser.Primitive_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#primitive_invocation.
    def visitPrimitive_invocation(self, ctx:AgentScriptCCParser.Primitive_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#transformational_rule.
    def visitTransformational_rule(self, ctx:AgentScriptCCParser.Transformational_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#list_conditions.
    def visitList_conditions(self, ctx:AgentScriptCCParser.List_conditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:AgentScriptCCParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#logical_arithmetic_expression.
    def visitLogical_arithmetic_expression(self, ctx:AgentScriptCCParser.Logical_arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#logical_expression.
    def visitLogical_expression(self, ctx:AgentScriptCCParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#neg_literal.
    def visitNeg_literal(self, ctx:AgentScriptCCParser.Neg_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#pos_literal.
    def visitPos_literal(self, ctx:AgentScriptCCParser.Pos_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#naf_attitude.
    def visitNaf_attitude(self, ctx:AgentScriptCCParser.Naf_attitudeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#variable.
    def visitVariable(self, ctx:AgentScriptCCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#constant.
    def visitConstant(self, ctx:AgentScriptCCParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#list_predicate_terms.
    def visitList_predicate_terms(self, ctx:AgentScriptCCParser.List_predicate_termsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#predicate_term.
    def visitPredicate_term(self, ctx:AgentScriptCCParser.Predicate_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#arithmetic_expression_term.
    def visitArithmetic_expression_term(self, ctx:AgentScriptCCParser.Arithmetic_expression_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentScriptCCParser#logical_expression_term.
    def visitLogical_expression_term(self, ctx:AgentScriptCCParser.Logical_expression_termContext):
        return self.visitChildren(ctx)



del AgentScriptCCParser
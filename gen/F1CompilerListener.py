# Generated from C:/Users/berna/Documents/Dev/projects/F1Compiler/src/core/F1Compiler.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .F1CompilerParser import F1CompilerParser
else:
    from F1CompilerParser import F1CompilerParser

# This class defines a complete listener for a parse tree produced by F1CompilerParser.
class F1CompilerListener(ParseTreeListener):

    # Enter a parse tree produced by F1CompilerParser#program.
    def enterProgram(self, ctx:F1CompilerParser.ProgramContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#program.
    def exitProgram(self, ctx:F1CompilerParser.ProgramContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#statement.
    def enterStatement(self, ctx:F1CompilerParser.StatementContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#statement.
    def exitStatement(self, ctx:F1CompilerParser.StatementContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#declaracion.
    def enterDeclaracion(self, ctx:F1CompilerParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#declaracion.
    def exitDeclaracion(self, ctx:F1CompilerParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#asignacion.
    def enterAsignacion(self, ctx:F1CompilerParser.AsignacionContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#asignacion.
    def exitAsignacion(self, ctx:F1CompilerParser.AsignacionContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#impresion.
    def enterImpresion(self, ctx:F1CompilerParser.ImpresionContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#impresion.
    def exitImpresion(self, ctx:F1CompilerParser.ImpresionContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#condicional.
    def enterCondicional(self, ctx:F1CompilerParser.CondicionalContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#condicional.
    def exitCondicional(self, ctx:F1CompilerParser.CondicionalContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#ciclo.
    def enterCiclo(self, ctx:F1CompilerParser.CicloContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#ciclo.
    def exitCiclo(self, ctx:F1CompilerParser.CicloContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#tipo.
    def enterTipo(self, ctx:F1CompilerParser.TipoContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#tipo.
    def exitTipo(self, ctx:F1CompilerParser.TipoContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#NotExp.
    def enterNotExp(self, ctx:F1CompilerParser.NotExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#NotExp.
    def exitNotExp(self, ctx:F1CompilerParser.NotExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#AndExp.
    def enterAndExp(self, ctx:F1CompilerParser.AndExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#AndExp.
    def exitAndExp(self, ctx:F1CompilerParser.AndExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#RelacionalExp.
    def enterRelacionalExp(self, ctx:F1CompilerParser.RelacionalExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#RelacionalExp.
    def exitRelacionalExp(self, ctx:F1CompilerParser.RelacionalExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#IdLiteral.
    def enterIdLiteral(self, ctx:F1CompilerParser.IdLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#IdLiteral.
    def exitIdLiteral(self, ctx:F1CompilerParser.IdLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:F1CompilerParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:F1CompilerParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#ParentesisExp.
    def enterParentesisExp(self, ctx:F1CompilerParser.ParentesisExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#ParentesisExp.
    def exitParentesisExp(self, ctx:F1CompilerParser.ParentesisExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#FalseLiteral.
    def enterFalseLiteral(self, ctx:F1CompilerParser.FalseLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#FalseLiteral.
    def exitFalseLiteral(self, ctx:F1CompilerParser.FalseLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#StringLiteral.
    def enterStringLiteral(self, ctx:F1CompilerParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#StringLiteral.
    def exitStringLiteral(self, ctx:F1CompilerParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#TrueLiteral.
    def enterTrueLiteral(self, ctx:F1CompilerParser.TrueLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#TrueLiteral.
    def exitTrueLiteral(self, ctx:F1CompilerParser.TrueLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#OrExp.
    def enterOrExp(self, ctx:F1CompilerParser.OrExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#OrExp.
    def exitOrExp(self, ctx:F1CompilerParser.OrExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#FuncionExp.
    def enterFuncionExp(self, ctx:F1CompilerParser.FuncionExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#FuncionExp.
    def exitFuncionExp(self, ctx:F1CompilerParser.FuncionExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#IntLiteral.
    def enterIntLiteral(self, ctx:F1CompilerParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#IntLiteral.
    def exitIntLiteral(self, ctx:F1CompilerParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#MultiplicativaExp.
    def enterMultiplicativaExp(self, ctx:F1CompilerParser.MultiplicativaExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#MultiplicativaExp.
    def exitMultiplicativaExp(self, ctx:F1CompilerParser.MultiplicativaExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#AditivaExp.
    def enterAditivaExp(self, ctx:F1CompilerParser.AditivaExpContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#AditivaExp.
    def exitAditivaExp(self, ctx:F1CompilerParser.AditivaExpContext):
        pass


    # Enter a parse tree produced by F1CompilerParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:F1CompilerParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by F1CompilerParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:F1CompilerParser.Llamada_funcionContext):
        pass



del F1CompilerParser
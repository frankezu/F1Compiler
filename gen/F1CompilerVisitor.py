# Generated from C:/Users/berna/Documents/Dev/projects/F1Compiler/src/core/F1Compiler.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .F1CompilerParser import F1CompilerParser
else:
    from F1CompilerParser import F1CompilerParser

# This class defines a complete generic visitor for a parse tree produced by F1CompilerParser.

class F1CompilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by F1CompilerParser#program.
    def visitProgram(self, ctx:F1CompilerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#statement.
    def visitStatement(self, ctx:F1CompilerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#declaracion.
    def visitDeclaracion(self, ctx:F1CompilerParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#asignacion.
    def visitAsignacion(self, ctx:F1CompilerParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#impresion.
    def visitImpresion(self, ctx:F1CompilerParser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#condicional.
    def visitCondicional(self, ctx:F1CompilerParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#ciclo.
    def visitCiclo(self, ctx:F1CompilerParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#tipo.
    def visitTipo(self, ctx:F1CompilerParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#NotExp.
    def visitNotExp(self, ctx:F1CompilerParser.NotExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#AndExp.
    def visitAndExp(self, ctx:F1CompilerParser.AndExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#RelacionalExp.
    def visitRelacionalExp(self, ctx:F1CompilerParser.RelacionalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#IdLiteral.
    def visitIdLiteral(self, ctx:F1CompilerParser.IdLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:F1CompilerParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#ParentesisExp.
    def visitParentesisExp(self, ctx:F1CompilerParser.ParentesisExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#FalseLiteral.
    def visitFalseLiteral(self, ctx:F1CompilerParser.FalseLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#StringLiteral.
    def visitStringLiteral(self, ctx:F1CompilerParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#TrueLiteral.
    def visitTrueLiteral(self, ctx:F1CompilerParser.TrueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#OrExp.
    def visitOrExp(self, ctx:F1CompilerParser.OrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#FuncionExp.
    def visitFuncionExp(self, ctx:F1CompilerParser.FuncionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#IntLiteral.
    def visitIntLiteral(self, ctx:F1CompilerParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#MultiplicativaExp.
    def visitMultiplicativaExp(self, ctx:F1CompilerParser.MultiplicativaExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#AditivaExp.
    def visitAditivaExp(self, ctx:F1CompilerParser.AditivaExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by F1CompilerParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:F1CompilerParser.Llamada_funcionContext):
        return self.visitChildren(ctx)



del F1CompilerParser
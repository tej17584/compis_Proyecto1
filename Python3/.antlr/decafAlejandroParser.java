// Generated from c:\Users\josea\Desktop\Compiladores\compis_Proyecto1\Python3\decafAlejandro.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class decafAlejandroParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, PROGRAM=2, IF=3, ELSE=4, FOR=5, WHILE=6, RETURN=7, BREAK=8, CONTINUE=9, 
		BOOLEAN=10, CHAR=11, INT=12, STRING=13, TRUE=14, FALSE=15, VOID=16, STRUCT=17, 
		CALLOUT=18, SEMICOLON=19, LCURLY=20, RCURLY=21, LSQUARE=22, RSQUARE=23, 
		LROUND=24, RROUND=25, COMMA=26, QUOTES=27, APOSTROPHE=28, ADD=29, SUB=30, 
		MULTIPLY=31, DIVIDE=32, REMINDER=33, AND=34, OR=35, NOT=36, GREATER_OP=37, 
		LESS_OP=38, GREATER_eq_op=39, LESS_eq_op=40, EQUAL_OP=41, ADD_eq_op=42, 
		SUB_eq_op=43, EQUALITY_OP=44, UNEQUALITY_OP=45, POINT=46, ID=47, ALPHA=48, 
		CHAR_LITERAL=49, DECIMAL_LITERAL=50, DIGIT=51, HEX_LITERAL=52, BOOL_LITERAL=53, 
		STRING_LITERAL=54, ALPHA_NUM=55, HEX_DIGIT=56, LINE_COMMENT=57, COMMENT=58, 
		NEWLINE=59, WHITESPACE=60;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_vardeclr = 2, RULE_field_declr = 3, 
		RULE_array_id = 4, RULE_field_var = 5, RULE_var_id = 6, RULE_struct_declr = 7, 
		RULE_method_declr = 8, RULE_return_type = 9, RULE_block = 10, RULE_statement = 11, 
		RULE_method_call_inter = 12, RULE_method_call = 13, RULE_expr = 14, RULE_location = 15, 
		RULE_callout_arg = 16, RULE_int_literal = 17, RULE_rel_op = 18, RULE_eq_op = 19, 
		RULE_cond_op = 20, RULE_literal = 21, RULE_bin_op = 22, RULE_arith_op = 23, 
		RULE_var_type = 24, RULE_assign_op = 25, RULE_method_name = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "vardeclr", "field_declr", "array_id", "field_var", 
			"var_id", "struct_declr", "method_declr", "return_type", "block", "statement", 
			"method_call_inter", "method_call", "expr", "location", "callout_arg", 
			"int_literal", "rel_op", "eq_op", "cond_op", "literal", "bin_op", "arith_op", 
			"var_type", "assign_op", "method_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'if'", "'else'", "'for'", "'while'", "'return'", 
			"'break'", "'continue'", "'boolean'", "'char'", "'int'", "'string'", 
			"'True'", "'False'", "'void'", "'struct'", "'callout'", "';'", "'{'", 
			"'}'", "'['", "']'", "'('", "')'", "','", "'\"'", "'''", "'+'", "'-'", 
			"'*'", "'/'", "'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", 
			"'='", "'+='", "'-='", "'=='", "'!='", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "PROGRAM", "IF", "ELSE", "FOR", "WHILE", "RETURN", "BREAK", 
			"CONTINUE", "BOOLEAN", "CHAR", "INT", "STRING", "TRUE", "FALSE", "VOID", 
			"STRUCT", "CALLOUT", "SEMICOLON", "LCURLY", "RCURLY", "LSQUARE", "RSQUARE", 
			"LROUND", "RROUND", "COMMA", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", 
			"DIVIDE", "REMINDER", "AND", "OR", "NOT", "GREATER_OP", "LESS_OP", "GREATER_eq_op", 
			"LESS_eq_op", "EQUAL_OP", "ADD_eq_op", "SUB_eq_op", "EQUALITY_OP", "UNEQUALITY_OP", 
			"POINT", "ID", "ALPHA", "CHAR_LITERAL", "DECIMAL_LITERAL", "DIGIT", "HEX_LITERAL", 
			"BOOL_LITERAL", "STRING_LITERAL", "ALPHA_NUM", "HEX_DIGIT", "LINE_COMMENT", 
			"COMMENT", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "decafAlejandro.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public decafAlejandroParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(decafAlejandroParser.CLASS, 0); }
		public TerminalNode PROGRAM() { return getToken(decafAlejandroParser.PROGRAM, 0); }
		public TerminalNode LCURLY() { return getToken(decafAlejandroParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(decafAlejandroParser.RCURLY, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(CLASS);
			setState(55);
			match(PROGRAM);
			setState(56);
			match(LCURLY);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << STRING) | (1L << VOID) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(57);
				declaration();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public Struct_declrContext struct_declr() {
			return getRuleContext(Struct_declrContext.class,0);
		}
		public VardeclrContext vardeclr() {
			return getRuleContext(VardeclrContext.class,0);
		}
		public Method_declrContext method_declr() {
			return getRuleContext(Method_declrContext.class,0);
		}
		public Field_declrContext field_declr() {
			return getRuleContext(Field_declrContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				struct_declr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				vardeclr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(67);
				method_declr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(68);
				field_declr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclrContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(decafAlejandroParser.SEMICOLON, 0); }
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(decafAlejandroParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafAlejandroParser.COMMA, i);
		}
		public VardeclrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclr; }
	}

	public final VardeclrContext vardeclr() throws RecognitionException {
		VardeclrContext _localctx = new VardeclrContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vardeclr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(71);
			var_type();
			setState(72);
			field_var();
			}
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(74);
				match(COMMA);
				setState(75);
				var_type();
				setState(76);
				field_var();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_declrContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public List<Field_varContext> field_var() {
			return getRuleContexts(Field_varContext.class);
		}
		public Field_varContext field_var(int i) {
			return getRuleContext(Field_varContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(decafAlejandroParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(decafAlejandroParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafAlejandroParser.COMMA, i);
		}
		public Field_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_declr; }
	}

	public final Field_declrContext field_declr() throws RecognitionException {
		Field_declrContext _localctx = new Field_declrContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_field_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			var_type();
			setState(86);
			field_var();
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(87);
				match(COMMA);
				setState(88);
				field_var();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(94);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_idContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafAlejandroParser.ID, 0); }
		public TerminalNode LSQUARE() { return getToken(decafAlejandroParser.LSQUARE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RSQUARE() { return getToken(decafAlejandroParser.RSQUARE, 0); }
		public TerminalNode POINT() { return getToken(decafAlejandroParser.POINT, 0); }
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Array_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_id; }
	}

	public final Array_idContext array_id() throws RecognitionException {
		Array_idContext _localctx = new Array_idContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_array_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(ID);
			setState(97);
			match(LSQUARE);
			setState(98);
			expr(0);
			setState(99);
			match(RSQUARE);
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(100);
				match(POINT);
				setState(101);
				location();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_varContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public Field_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_var; }
	}

	public final Field_varContext field_var() throws RecognitionException {
		Field_varContext _localctx = new Field_varContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_field_var);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_idContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafAlejandroParser.ID, 0); }
		public TerminalNode POINT() { return getToken(decafAlejandroParser.POINT, 0); }
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Var_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_id; }
	}

	public final Var_idContext var_id() throws RecognitionException {
		Var_idContext _localctx = new Var_idContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_var_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(ID);
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(109);
				match(POINT);
				setState(110);
				location();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Struct_declrContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(decafAlejandroParser.STRUCT, 0); }
		public TerminalNode ID() { return getToken(decafAlejandroParser.ID, 0); }
		public TerminalNode LCURLY() { return getToken(decafAlejandroParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(decafAlejandroParser.RCURLY, 0); }
		public TerminalNode SEMICOLON() { return getToken(decafAlejandroParser.SEMICOLON, 0); }
		public List<VardeclrContext> vardeclr() {
			return getRuleContexts(VardeclrContext.class);
		}
		public VardeclrContext vardeclr(int i) {
			return getRuleContext(VardeclrContext.class,i);
		}
		public Struct_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_declr; }
	}

	public final Struct_declrContext struct_declr() throws RecognitionException {
		Struct_declrContext _localctx = new Struct_declrContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_struct_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(STRUCT);
			setState(114);
			match(ID);
			setState(115);
			match(LCURLY);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << STRING) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(116);
				vardeclr();
				}
				}
				setState(121);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(122);
			match(RCURLY);
			setState(123);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declrContext extends ParserRuleContext {
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(decafAlejandroParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafAlejandroParser.RROUND, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode VOID() { return getToken(decafAlejandroParser.VOID, 0); }
		public List<TerminalNode> COMMA() { return getTokens(decafAlejandroParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafAlejandroParser.COMMA, i);
		}
		public List<Var_typeContext> var_type() {
			return getRuleContexts(Var_typeContext.class);
		}
		public Var_typeContext var_type(int i) {
			return getRuleContext(Var_typeContext.class,i);
		}
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public Method_declrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declr; }
	}

	public final Method_declrContext method_declr() throws RecognitionException {
		Method_declrContext _localctx = new Method_declrContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_method_declr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			return_type();
			setState(126);
			method_name();
			setState(127);
			match(LROUND);
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << STRING) | (1L << VOID) | (1L << STRUCT))) != 0)) {
				{
				setState(132);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BOOLEAN:
				case INT:
				case STRING:
				case STRUCT:
					{
					{
					setState(128);
					var_type();
					setState(129);
					var_id();
					}
					}
					break;
				case VOID:
					{
					setState(131);
					match(VOID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(134);
					match(COMMA);
					setState(135);
					var_type();
					setState(136);
					var_id();
					}
					}
					setState(142);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(145);
			match(RROUND);
			setState(146);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_typeContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public TerminalNode VOID() { return getToken(decafAlejandroParser.VOID, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_return_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case STRING:
			case STRUCT:
				{
				setState(148);
				var_type();
				}
				break;
			case VOID:
				{
				setState(149);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(decafAlejandroParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(decafAlejandroParser.RCURLY, 0); }
		public List<VardeclrContext> vardeclr() {
			return getRuleContexts(VardeclrContext.class);
		}
		public VardeclrContext vardeclr(int i) {
			return getRuleContext(VardeclrContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(LCURLY);
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << STRING) | (1L << STRUCT))) != 0)) {
				{
				{
				setState(153);
				vardeclr();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << FOR) | (1L << WHILE) | (1L << RETURN) | (1L << BREAK) | (1L << CALLOUT) | (1L << ID))) != 0)) {
				{
				{
				setState(159);
				statement();
				}
				}
				setState(164);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(165);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(decafAlejandroParser.SEMICOLON, 0); }
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode IF() { return getToken(decafAlejandroParser.IF, 0); }
		public TerminalNode LROUND() { return getToken(decafAlejandroParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafAlejandroParser.RROUND, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(decafAlejandroParser.ELSE, 0); }
		public TerminalNode WHILE() { return getToken(decafAlejandroParser.WHILE, 0); }
		public List<TerminalNode> EQUAL_OP() { return getTokens(decafAlejandroParser.EQUAL_OP); }
		public TerminalNode EQUAL_OP(int i) {
			return getToken(decafAlejandroParser.EQUAL_OP, i);
		}
		public TerminalNode RETURN() { return getToken(decafAlejandroParser.RETURN, 0); }
		public TerminalNode FOR() { return getToken(decafAlejandroParser.FOR, 0); }
		public List<Var_idContext> var_id() {
			return getRuleContexts(Var_idContext.class);
		}
		public Var_idContext var_id(int i) {
			return getRuleContext(Var_idContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(decafAlejandroParser.COMMA, 0); }
		public List<Int_literalContext> int_literal() {
			return getRuleContexts(Int_literalContext.class);
		}
		public Int_literalContext int_literal(int i) {
			return getRuleContext(Int_literalContext.class,i);
		}
		public TerminalNode BREAK() { return getToken(decafAlejandroParser.BREAK, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_statement);
		int _la;
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				location();
				setState(168);
				assign_op();
				setState(169);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(171);
				location();
				setState(172);
				assign_op();
				setState(173);
				expr(0);
				setState(174);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(176);
				method_call();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(177);
				match(IF);
				setState(178);
				match(LROUND);
				setState(179);
				expr(0);
				setState(180);
				match(RROUND);
				setState(181);
				block();
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(182);
					match(ELSE);
					setState(183);
					block();
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(186);
				match(WHILE);
				setState(187);
				match(LROUND);
				setState(188);
				expr(0);
				setState(189);
				match(RROUND);
				setState(190);
				block();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(192);
				location();
				setState(193);
				match(EQUAL_OP);
				setState(194);
				expr(0);
				setState(195);
				match(SEMICOLON);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(197);
				match(RETURN);
				setState(198);
				expr(0);
				setState(199);
				match(SEMICOLON);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(201);
				match(FOR);
				setState(202);
				var_id();
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL_OP) {
					{
					setState(203);
					match(EQUAL_OP);
					setState(204);
					int_literal();
					}
				}

				setState(207);
				match(COMMA);
				setState(214);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					{
					setState(208);
					var_id();
					setState(211);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==EQUAL_OP) {
						{
						setState(209);
						match(EQUAL_OP);
						setState(210);
						int_literal();
						}
					}

					}
					}
					break;
				case DECIMAL_LITERAL:
				case HEX_LITERAL:
					{
					setState(213);
					int_literal();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(216);
				block();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(218);
				match(BREAK);
				setState(219);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_call_interContext extends ParserRuleContext {
		public Method_nameContext method_name() {
			return getRuleContext(Method_nameContext.class,0);
		}
		public TerminalNode LROUND() { return getToken(decafAlejandroParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafAlejandroParser.RROUND, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(decafAlejandroParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafAlejandroParser.COMMA, i);
		}
		public Method_call_interContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call_inter; }
	}

	public final Method_call_interContext method_call_inter() throws RecognitionException {
		Method_call_interContext _localctx = new Method_call_interContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_method_call_inter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			method_name();
			setState(223);
			match(LROUND);
			setState(232);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CALLOUT) | (1L << LROUND) | (1L << SUB) | (1L << NOT) | (1L << ID) | (1L << DECIMAL_LITERAL) | (1L << HEX_LITERAL) | (1L << BOOL_LITERAL) | (1L << STRING_LITERAL))) != 0)) {
				{
				setState(224);
				expr(0);
				setState(229);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(225);
					match(COMMA);
					setState(226);
					expr(0);
					}
					}
					setState(231);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(234);
			match(RROUND);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_callContext extends ParserRuleContext {
		public Method_call_interContext method_call_inter() {
			return getRuleContext(Method_call_interContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(decafAlejandroParser.SEMICOLON, 0); }
		public TerminalNode CALLOUT() { return getToken(decafAlejandroParser.CALLOUT, 0); }
		public TerminalNode LROUND() { return getToken(decafAlejandroParser.LROUND, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(decafAlejandroParser.STRING_LITERAL, 0); }
		public TerminalNode RROUND() { return getToken(decafAlejandroParser.RROUND, 0); }
		public List<TerminalNode> COMMA() { return getTokens(decafAlejandroParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(decafAlejandroParser.COMMA, i);
		}
		public List<Callout_argContext> callout_arg() {
			return getRuleContexts(Callout_argContext.class);
		}
		public Callout_argContext callout_arg(int i) {
			return getRuleContext(Callout_argContext.class,i);
		}
		public Method_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call; }
	}

	public final Method_callContext method_call() throws RecognitionException {
		Method_callContext _localctx = new Method_callContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_method_call);
		int _la;
		try {
			setState(256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				method_call_inter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(237);
				method_call_inter();
				setState(238);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(240);
				match(CALLOUT);
				setState(241);
				match(LROUND);
				setState(242);
				match(STRING_LITERAL);
				setState(252);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(243);
					match(COMMA);
					setState(244);
					callout_arg();
					setState(249);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(245);
						match(COMMA);
						setState(246);
						callout_arg();
						}
						}
						setState(251);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(254);
				match(RROUND);
				setState(255);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode SUB() { return getToken(decafAlejandroParser.SUB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode NOT() { return getToken(decafAlejandroParser.NOT, 0); }
		public TerminalNode LROUND() { return getToken(decafAlejandroParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(decafAlejandroParser.RROUND, 0); }
		public Bin_opContext bin_op() {
			return getRuleContext(Bin_opContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(259);
				location();
				}
				break;
			case 2:
				{
				setState(260);
				literal();
				}
				break;
			case 3:
				{
				setState(261);
				match(SUB);
				setState(262);
				expr(4);
				}
				break;
			case 4:
				{
				setState(263);
				method_call();
				}
				break;
			case 5:
				{
				setState(264);
				match(NOT);
				setState(265);
				expr(2);
				}
				break;
			case 6:
				{
				setState(266);
				match(LROUND);
				setState(267);
				expr(0);
				setState(268);
				match(RROUND);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(278);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(272);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(273);
					bin_op();
					setState(274);
					expr(6);
					}
					} 
				}
				setState(280);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LocationContext extends ParserRuleContext {
		public Var_idContext var_id() {
			return getRuleContext(Var_idContext.class,0);
		}
		public Array_idContext array_id() {
			return getRuleContext(Array_idContext.class,0);
		}
		public LocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location; }
	}

	public final LocationContext location() throws RecognitionException {
		LocationContext _localctx = new LocationContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_location);
		try {
			setState(283);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(281);
				var_id();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(282);
				array_id();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Callout_argContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode STRING_LITERAL() { return getToken(decafAlejandroParser.STRING_LITERAL, 0); }
		public Callout_argContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callout_arg; }
	}

	public final Callout_argContext callout_arg() throws RecognitionException {
		Callout_argContext _localctx = new Callout_argContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_callout_arg);
		try {
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(285);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(286);
				match(STRING_LITERAL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Int_literalContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LITERAL() { return getToken(decafAlejandroParser.DECIMAL_LITERAL, 0); }
		public TerminalNode HEX_LITERAL() { return getToken(decafAlejandroParser.HEX_LITERAL, 0); }
		public Int_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_literal; }
	}

	public final Int_literalContext int_literal() throws RecognitionException {
		Int_literalContext _localctx = new Int_literalContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_int_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			_la = _input.LA(1);
			if ( !(_la==DECIMAL_LITERAL || _la==HEX_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rel_opContext extends ParserRuleContext {
		public TerminalNode GREATER_OP() { return getToken(decafAlejandroParser.GREATER_OP, 0); }
		public TerminalNode LESS_OP() { return getToken(decafAlejandroParser.LESS_OP, 0); }
		public TerminalNode LESS_eq_op() { return getToken(decafAlejandroParser.LESS_eq_op, 0); }
		public TerminalNode GREATER_eq_op() { return getToken(decafAlejandroParser.GREATER_eq_op, 0); }
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GREATER_OP) | (1L << LESS_OP) | (1L << GREATER_eq_op) | (1L << LESS_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Eq_opContext extends ParserRuleContext {
		public TerminalNode EQUALITY_OP() { return getToken(decafAlejandroParser.EQUALITY_OP, 0); }
		public TerminalNode UNEQUALITY_OP() { return getToken(decafAlejandroParser.UNEQUALITY_OP, 0); }
		public Eq_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eq_op; }
	}

	public final Eq_opContext eq_op() throws RecognitionException {
		Eq_opContext _localctx = new Eq_opContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			_la = _input.LA(1);
			if ( !(_la==EQUALITY_OP || _la==UNEQUALITY_OP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Cond_opContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(decafAlejandroParser.AND, 0); }
		public TerminalNode OR() { return getToken(decafAlejandroParser.OR, 0); }
		public Cond_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond_op; }
	}

	public final Cond_opContext cond_op() throws RecognitionException {
		Cond_opContext _localctx = new Cond_opContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_cond_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public TerminalNode STRING_LITERAL() { return getToken(decafAlejandroParser.STRING_LITERAL, 0); }
		public TerminalNode BOOL_LITERAL() { return getToken(decafAlejandroParser.BOOL_LITERAL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal);
		try {
			setState(300);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_LITERAL:
			case HEX_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				int_literal();
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(298);
				match(STRING_LITERAL);
				}
				break;
			case BOOL_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(299);
				match(BOOL_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Bin_opContext extends ParserRuleContext {
		public Arith_opContext arith_op() {
			return getRuleContext(Arith_opContext.class,0);
		}
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public Eq_opContext eq_op() {
			return getRuleContext(Eq_opContext.class,0);
		}
		public Cond_opContext cond_op() {
			return getRuleContext(Cond_opContext.class,0);
		}
		public Bin_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bin_op; }
	}

	public final Bin_opContext bin_op() throws RecognitionException {
		Bin_opContext _localctx = new Bin_opContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_bin_op);
		try {
			setState(306);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
			case SUB:
			case MULTIPLY:
			case DIVIDE:
			case REMINDER:
				enterOuterAlt(_localctx, 1);
				{
				setState(302);
				arith_op();
				}
				break;
			case GREATER_OP:
			case LESS_OP:
			case GREATER_eq_op:
			case LESS_eq_op:
				enterOuterAlt(_localctx, 2);
				{
				setState(303);
				rel_op();
				}
				break;
			case EQUALITY_OP:
			case UNEQUALITY_OP:
				enterOuterAlt(_localctx, 3);
				{
				setState(304);
				eq_op();
				}
				break;
			case AND:
			case OR:
				enterOuterAlt(_localctx, 4);
				{
				setState(305);
				cond_op();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_opContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(decafAlejandroParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(decafAlejandroParser.SUB, 0); }
		public TerminalNode MULTIPLY() { return getToken(decafAlejandroParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(decafAlejandroParser.DIVIDE, 0); }
		public TerminalNode REMINDER() { return getToken(decafAlejandroParser.REMINDER, 0); }
		public Arith_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op; }
	}

	public final Arith_opContext arith_op() throws RecognitionException {
		Arith_opContext _localctx = new Arith_opContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_arith_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << SUB) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << REMINDER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(decafAlejandroParser.INT, 0); }
		public TerminalNode BOOLEAN() { return getToken(decafAlejandroParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(decafAlejandroParser.STRING, 0); }
		public TerminalNode STRUCT() { return getToken(decafAlejandroParser.STRUCT, 0); }
		public TerminalNode ID() { return getToken(decafAlejandroParser.ID, 0); }
		public Struct_declrContext struct_declr() {
			return getRuleContext(Struct_declrContext.class,0);
		}
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_var_type);
		try {
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(310);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(311);
				match(BOOLEAN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(312);
				match(STRING);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(313);
				match(STRUCT);
				setState(314);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(315);
				struct_declr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_opContext extends ParserRuleContext {
		public TerminalNode EQUAL_OP() { return getToken(decafAlejandroParser.EQUAL_OP, 0); }
		public TerminalNode ADD_eq_op() { return getToken(decafAlejandroParser.ADD_eq_op, 0); }
		public TerminalNode SUB_eq_op() { return getToken(decafAlejandroParser.SUB_eq_op, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_assign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL_OP) | (1L << ADD_eq_op) | (1L << SUB_eq_op))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_nameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(decafAlejandroParser.ID, 0); }
		public Method_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_name; }
	}

	public final Method_nameContext method_name() throws RecognitionException {
		Method_nameContext _localctx = new Method_nameContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_method_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 14:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>\u0145\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\7\2=\n\2\f\2\16\2@\13\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\5\3H\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4Q\n\4"+
		"\f\4\16\4T\13\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\\\n\5\f\5\16\5_\13\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6i\n\6\3\7\3\7\5\7m\n\7\3\b\3\b\3\b\5\br"+
		"\n\b\3\t\3\t\3\t\3\t\7\tx\n\t\f\t\16\t{\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\5\n\u0087\n\n\3\n\3\n\3\n\3\n\7\n\u008d\n\n\f\n\16\n\u0090"+
		"\13\n\5\n\u0092\n\n\3\n\3\n\3\n\3\13\3\13\5\13\u0099\n\13\3\f\3\f\7\f"+
		"\u009d\n\f\f\f\16\f\u00a0\13\f\3\f\7\f\u00a3\n\f\f\f\16\f\u00a6\13\f\3"+
		"\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\5\r\u00bb\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d0\n\r\3\r\3\r\3\r\3\r\5\r\u00d6\n\r\3"+
		"\r\5\r\u00d9\n\r\3\r\3\r\3\r\3\r\5\r\u00df\n\r\3\16\3\16\3\16\3\16\3\16"+
		"\7\16\u00e6\n\16\f\16\16\16\u00e9\13\16\5\16\u00eb\n\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00fa\n\17\f\17"+
		"\16\17\u00fd\13\17\5\17\u00ff\n\17\3\17\3\17\5\17\u0103\n\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0111\n\20\3\20"+
		"\3\20\3\20\3\20\7\20\u0117\n\20\f\20\16\20\u011a\13\20\3\21\3\21\5\21"+
		"\u011e\n\21\3\22\3\22\5\22\u0122\n\22\3\23\3\23\3\24\3\24\3\25\3\25\3"+
		"\26\3\26\3\27\3\27\3\27\5\27\u012f\n\27\3\30\3\30\3\30\3\30\5\30\u0135"+
		"\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u013f\n\32\3\33\3\33"+
		"\3\34\3\34\3\34\2\3\36\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&"+
		"(*,.\60\62\64\66\2\b\4\2\64\64\66\66\3\2\'*\3\2./\3\2$%\3\2\37#\3\2+-"+
		"\2\u015c\28\3\2\2\2\4G\3\2\2\2\6I\3\2\2\2\bW\3\2\2\2\nb\3\2\2\2\fl\3\2"+
		"\2\2\16n\3\2\2\2\20s\3\2\2\2\22\177\3\2\2\2\24\u0098\3\2\2\2\26\u009a"+
		"\3\2\2\2\30\u00de\3\2\2\2\32\u00e0\3\2\2\2\34\u0102\3\2\2\2\36\u0110\3"+
		"\2\2\2 \u011d\3\2\2\2\"\u0121\3\2\2\2$\u0123\3\2\2\2&\u0125\3\2\2\2(\u0127"+
		"\3\2\2\2*\u0129\3\2\2\2,\u012e\3\2\2\2.\u0134\3\2\2\2\60\u0136\3\2\2\2"+
		"\62\u013e\3\2\2\2\64\u0140\3\2\2\2\66\u0142\3\2\2\289\7\3\2\29:\7\4\2"+
		"\2:>\7\26\2\2;=\5\4\3\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2"+
		"\2\2@>\3\2\2\2AB\7\27\2\2B\3\3\2\2\2CH\5\20\t\2DH\5\6\4\2EH\5\22\n\2F"+
		"H\5\b\5\2GC\3\2\2\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H\5\3\2\2\2IJ\5\62\32"+
		"\2JK\5\f\7\2KR\3\2\2\2LM\7\34\2\2MN\5\62\32\2NO\5\f\7\2OQ\3\2\2\2PL\3"+
		"\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7\25\2\2V\7"+
		"\3\2\2\2WX\5\62\32\2X]\5\f\7\2YZ\7\34\2\2Z\\\5\f\7\2[Y\3\2\2\2\\_\3\2"+
		"\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\25\2\2a\t\3\2\2\2bc\7"+
		"\61\2\2cd\7\30\2\2de\5\36\20\2eh\7\31\2\2fg\7\60\2\2gi\5 \21\2hf\3\2\2"+
		"\2hi\3\2\2\2i\13\3\2\2\2jm\5\16\b\2km\5\n\6\2lj\3\2\2\2lk\3\2\2\2m\r\3"+
		"\2\2\2nq\7\61\2\2op\7\60\2\2pr\5 \21\2qo\3\2\2\2qr\3\2\2\2r\17\3\2\2\2"+
		"st\7\23\2\2tu\7\61\2\2uy\7\26\2\2vx\5\6\4\2wv\3\2\2\2x{\3\2\2\2yw\3\2"+
		"\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2\2\2|}\7\27\2\2}~\7\25\2\2~\21\3\2\2\2\177"+
		"\u0080\5\24\13\2\u0080\u0081\5\66\34\2\u0081\u0091\7\32\2\2\u0082\u0083"+
		"\5\62\32\2\u0083\u0084\5\16\b\2\u0084\u0087\3\2\2\2\u0085\u0087\7\22\2"+
		"\2\u0086\u0082\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u008e\3\2\2\2\u0088\u0089"+
		"\7\34\2\2\u0089\u008a\5\62\32\2\u008a\u008b\5\16\b\2\u008b\u008d\3\2\2"+
		"\2\u008c\u0088\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f"+
		"\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0086\3\2\2\2\u0091"+
		"\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7\33\2\2\u0094\u0095\5"+
		"\26\f\2\u0095\23\3\2\2\2\u0096\u0099\5\62\32\2\u0097\u0099\7\22\2\2\u0098"+
		"\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099\25\3\2\2\2\u009a\u009e\7\26\2"+
		"\2\u009b\u009d\5\6\4\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c"+
		"\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a4\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1"+
		"\u00a3\5\30\r\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3"+
		"\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7"+
		"\u00a8\7\27\2\2\u00a8\27\3\2\2\2\u00a9\u00aa\5 \21\2\u00aa\u00ab\5\64"+
		"\33\2\u00ab\u00ac\5\36\20\2\u00ac\u00df\3\2\2\2\u00ad\u00ae\5 \21\2\u00ae"+
		"\u00af\5\64\33\2\u00af\u00b0\5\36\20\2\u00b0\u00b1\7\25\2\2\u00b1\u00df"+
		"\3\2\2\2\u00b2\u00df\5\34\17\2\u00b3\u00b4\7\5\2\2\u00b4\u00b5\7\32\2"+
		"\2\u00b5\u00b6\5\36\20\2\u00b6\u00b7\7\33\2\2\u00b7\u00ba\5\26\f\2\u00b8"+
		"\u00b9\7\6\2\2\u00b9\u00bb\5\26\f\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3"+
		"\2\2\2\u00bb\u00df\3\2\2\2\u00bc\u00bd\7\b\2\2\u00bd\u00be\7\32\2\2\u00be"+
		"\u00bf\5\36\20\2\u00bf\u00c0\7\33\2\2\u00c0\u00c1\5\26\f\2\u00c1\u00df"+
		"\3\2\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\7+\2\2\u00c4\u00c5\5\36\20\2"+
		"\u00c5\u00c6\7\25\2\2\u00c6\u00df\3\2\2\2\u00c7\u00c8\7\t\2\2\u00c8\u00c9"+
		"\5\36\20\2\u00c9\u00ca\7\25\2\2\u00ca\u00df\3\2\2\2\u00cb\u00cc\7\7\2"+
		"\2\u00cc\u00cf\5\16\b\2\u00cd\u00ce\7+\2\2\u00ce\u00d0\5$\23\2\u00cf\u00cd"+
		"\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d8\7\34\2\2"+
		"\u00d2\u00d5\5\16\b\2\u00d3\u00d4\7+\2\2\u00d4\u00d6\5$\23\2\u00d5\u00d3"+
		"\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9\5$\23\2\u00d8"+
		"\u00d2\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\5\26"+
		"\f\2\u00db\u00df\3\2\2\2\u00dc\u00dd\7\n\2\2\u00dd\u00df\7\25\2\2\u00de"+
		"\u00a9\3\2\2\2\u00de\u00ad\3\2\2\2\u00de\u00b2\3\2\2\2\u00de\u00b3\3\2"+
		"\2\2\u00de\u00bc\3\2\2\2\u00de\u00c2\3\2\2\2\u00de\u00c7\3\2\2\2\u00de"+
		"\u00cb\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\31\3\2\2\2\u00e0\u00e1\5\66\34"+
		"\2\u00e1\u00ea\7\32\2\2\u00e2\u00e7\5\36\20\2\u00e3\u00e4\7\34\2\2\u00e4"+
		"\u00e6\5\36\20\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3"+
		"\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea"+
		"\u00e2\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7\33"+
		"\2\2\u00ed\33\3\2\2\2\u00ee\u0103\5\32\16\2\u00ef\u00f0\5\32\16\2\u00f0"+
		"\u00f1\7\25\2\2\u00f1\u0103\3\2\2\2\u00f2\u00f3\7\24\2\2\u00f3\u00f4\7"+
		"\32\2\2\u00f4\u00fe\78\2\2\u00f5\u00f6\7\34\2\2\u00f6\u00fb\5\"\22\2\u00f7"+
		"\u00f8\7\34\2\2\u00f8\u00fa\5\"\22\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3"+
		"\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd"+
		"\u00fb\3\2\2\2\u00fe\u00f5\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2"+
		"\2\2\u0100\u0101\7\33\2\2\u0101\u0103\7\25\2\2\u0102\u00ee\3\2\2\2\u0102"+
		"\u00ef\3\2\2\2\u0102\u00f2\3\2\2\2\u0103\35\3\2\2\2\u0104\u0105\b\20\1"+
		"\2\u0105\u0111\5 \21\2\u0106\u0111\5,\27\2\u0107\u0108\7 \2\2\u0108\u0111"+
		"\5\36\20\6\u0109\u0111\5\34\17\2\u010a\u010b\7&\2\2\u010b\u0111\5\36\20"+
		"\4\u010c\u010d\7\32\2\2\u010d\u010e\5\36\20\2\u010e\u010f\7\33\2\2\u010f"+
		"\u0111\3\2\2\2\u0110\u0104\3\2\2\2\u0110\u0106\3\2\2\2\u0110\u0107\3\2"+
		"\2\2\u0110\u0109\3\2\2\2\u0110\u010a\3\2\2\2\u0110\u010c\3\2\2\2\u0111"+
		"\u0118\3\2\2\2\u0112\u0113\f\7\2\2\u0113\u0114\5.\30\2\u0114\u0115\5\36"+
		"\20\b\u0115\u0117\3\2\2\2\u0116\u0112\3\2\2\2\u0117\u011a\3\2\2\2\u0118"+
		"\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\37\3\2\2\2\u011a\u0118\3\2\2"+
		"\2\u011b\u011e\5\16\b\2\u011c\u011e\5\n\6\2\u011d\u011b\3\2\2\2\u011d"+
		"\u011c\3\2\2\2\u011e!\3\2\2\2\u011f\u0122\5\36\20\2\u0120\u0122\78\2\2"+
		"\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122#\3\2\2\2\u0123\u0124\t"+
		"\2\2\2\u0124%\3\2\2\2\u0125\u0126\t\3\2\2\u0126\'\3\2\2\2\u0127\u0128"+
		"\t\4\2\2\u0128)\3\2\2\2\u0129\u012a\t\5\2\2\u012a+\3\2\2\2\u012b\u012f"+
		"\5$\23\2\u012c\u012f\78\2\2\u012d\u012f\7\67\2\2\u012e\u012b\3\2\2\2\u012e"+
		"\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012f-\3\2\2\2\u0130\u0135\5\60\31"+
		"\2\u0131\u0135\5&\24\2\u0132\u0135\5(\25\2\u0133\u0135\5*\26\2\u0134\u0130"+
		"\3\2\2\2\u0134\u0131\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135"+
		"/\3\2\2\2\u0136\u0137\t\6\2\2\u0137\61\3\2\2\2\u0138\u013f\7\16\2\2\u0139"+
		"\u013f\7\f\2\2\u013a\u013f\7\17\2\2\u013b\u013c\7\23\2\2\u013c\u013f\7"+
		"\61\2\2\u013d\u013f\5\20\t\2\u013e\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e"+
		"\u013a\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013d\3\2\2\2\u013f\63\3\2\2"+
		"\2\u0140\u0141\t\7\2\2\u0141\65\3\2\2\2\u0142\u0143\7\61\2\2\u0143\67"+
		"\3\2\2\2!>GR]hlqy\u0086\u008e\u0091\u0098\u009e\u00a4\u00ba\u00cf\u00d5"+
		"\u00d8\u00de\u00e7\u00ea\u00fb\u00fe\u0102\u0110\u0118\u011d\u0121\u012e"+
		"\u0134\u013e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
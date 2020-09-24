from jack_tokenizer import JackTokenizer


class CompilationEngine:
    CLASS_VAR_DEC_KEYWORDS = ['static', 'field']
    SUBROUTINE_DEC_KEYWORDS = ['constructor', 'function', 'method']
    BINARY_OPERATOR_SYMBOLS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
    UNARY_OPERATOR_SYMBOLS = ['-', '~']
    TYPE_TO_TAG = {'STRING_CONST': 'stringConstant', 'INT_CONST': 'integerConstant', 'KEYWORD': 'keyword',
                   'IDENTIFIER': 'identifier', 'SYMBOL': 'symbol'}

    SYMBOLS_TO_XML_CONVENTION = {'<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;'}

    def __init__(self, input_file_path, output_file_path):
        self.output_file = open(output_file_path, 'w')
        self.jack_tokenizer = JackTokenizer(input_file_path)
        if self.jack_tokenizer.has_more_tokens():
            self.compile_class()

    def compile_class(self):
        self.output_file.write('<class>\n')  # get first token
        self.jack_tokenizer.advance()
        self.write_token(self.jack_tokenizer.key_word())
        self.write_token(self.jack_tokenizer.identifier())
        self.write_token(self.jack_tokenizer.symbol())

        if self.jack_tokenizer.key_word() in CompilationEngine.CLASS_VAR_DEC_KEYWORDS:
            self.compile_class_var_dec()
        if self.jack_tokenizer.key_word() in CompilationEngine.SUBROUTINE_DEC_KEYWORDS:
            self.compile_subroutine()

        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</class>')
        self.output_file.close()

    def write_token(self, token_name):
        type_tag = CompilationEngine.TYPE_TO_TAG[self.jack_tokenizer.token_type()]
        self.output_file.write('<{0}> {1} </{0}>\n'.format(
            type_tag, token_name))
        self.jack_tokenizer.advance()

    def compile_class_var_dec(self):
        while self.jack_tokenizer.key_word() in CompilationEngine.CLASS_VAR_DEC_KEYWORDS:
            self.output_file.write('<classVarDec>\n')

            self.write_token(self.jack_tokenizer.key_word())
            self.write_type()
            self.write_token(self.jack_tokenizer.identifier())

            while self.jack_tokenizer.symbol() != ';':
                self.write_token(self.jack_tokenizer.symbol())
                self.write_token(self.jack_tokenizer.identifier())
            self.write_token(self.jack_tokenizer.symbol())

            self.output_file.write('</classVarDec>\n')

    def write_type(self):
        if self.jack_tokenizer.token_type() == 'KEYWORD':
            self.write_token(self.jack_tokenizer.key_word())
        elif self.jack_tokenizer.token_type() == 'IDENTIFIER':
            self.write_token(self.jack_tokenizer.identifier())

    def compile_subroutine(self):
        while self.jack_tokenizer.key_word() in CompilationEngine.SUBROUTINE_DEC_KEYWORDS:
            self.output_file.write('<subroutineDec>\n')
            self.write_token(self.jack_tokenizer.key_word())
            self.write_type()
            self.write_token(self.jack_tokenizer.identifier())
            self.write_token(self.jack_tokenizer.symbol())
            self.compile_parameter_list()
            self.write_token(self.jack_tokenizer.symbol())


            self.output_file.write('<subroutineBody>\n')
            self.write_token(self.jack_tokenizer.symbol())
            while self.jack_tokenizer.key_word() == 'var':
                self.compile_var_dec()
            self.compile_statements()
            self.write_token(self.jack_tokenizer.symbol())
            self.output_file.write('</subroutineBody>\n')

            self.output_file.write('</subroutineDec>\n')

    def compile_parameter_list(self):
        self.output_file.write('<parameterList>\n')
        if self.jack_tokenizer.symbol() != ')':
            self.write_type()
            self.write_token(self.jack_tokenizer.identifier())
            while self.jack_tokenizer.symbol() == ",":
                self.write_token(self.jack_tokenizer.symbol())
                self.write_type()
                self.write_token(self.jack_tokenizer.identifier())
        self.output_file.write('</parameterList>\n')


    def compile_var_dec(self):
        self.output_file.write('<varDec>\n')
        self.write_token(self.jack_tokenizer.key_word())
        self.write_type()
        self.write_token(self.jack_tokenizer.identifier())
        while self.jack_tokenizer.symbol() == ",":
            self.write_token(self.jack_tokenizer.symbol())
            self.write_token(self.jack_tokenizer.identifier())
        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</varDec>\n')


    def compile_statements(self):
        self.output_file.write('<statements>\n')

        while self.jack_tokenizer.token_type() == 'KEYWORD':
            if self.jack_tokenizer.key_word() == 'let':
                self.compile_let()
            elif self.jack_tokenizer.key_word() == 'if':
                self.compile_if()
            elif self.jack_tokenizer.key_word() == 'while':
                self.compile_while()
            elif self.jack_tokenizer.key_word() == 'do':
                self.compile_do()
            elif self.jack_tokenizer.key_word() == 'return':
                self.compile_return()

        self.output_file.write('</statements>\n')

    def compile_do(self):
        self.output_file.write('<doStatement>\n')
        self.write_token(self.jack_tokenizer.key_word())

        self.write_token(self.jack_tokenizer.identifier())
        self.compile_subroutine_call()

        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</doStatement>\n')

    def compile_subroutine_call(self):
        if self.jack_tokenizer.symbol() == '(':
            self.write_token(self.jack_tokenizer.symbol())
            self.compile_expression_list()
            self.write_token(self.jack_tokenizer.symbol())
        elif self.jack_tokenizer.symbol() == '.':
            self.write_token(self.jack_tokenizer.symbol())
            self.write_token(self.jack_tokenizer.identifier())
            self.write_token(self.jack_tokenizer.symbol())
            self.compile_expression_list()
            self.write_token(self.jack_tokenizer.symbol())

    def compile_let(self):
        self.output_file.write('<letStatement>\n')
        self.write_token(self.jack_tokenizer.key_word())
        self.write_token(self.jack_tokenizer.identifier())
        if self.jack_tokenizer.symbol() == '[':
            self.write_token(self.jack_tokenizer.symbol())
            self.compile_expression()
            self.write_token(self.jack_tokenizer.symbol())
        self.write_token(self.jack_tokenizer.symbol())
        self.compile_expression()
        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</letStatement>\n')

    def compile_while(self):
        self.output_file.write('<whileStatement>\n')
        self.write_token(self.jack_tokenizer.identifier())
        self.write_token(self.jack_tokenizer.symbol())
        self.compile_expression()
        self.write_token(self.jack_tokenizer.symbol())
        self.write_token(self.jack_tokenizer.symbol())
        self.compile_statements()
        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</whileStatement>\n')


    def compile_return(self):
        self.output_file.write('<returnStatement>\n')
        self.write_token(self.jack_tokenizer.key_word())
        if self.jack_tokenizer.symbol() != ';':
            self.compile_expression()
        self.write_token(self.jack_tokenizer.symbol())
        self.output_file.write('</returnStatement>\n')


    def compile_if(self):
        self.output_file.write('<ifStatement>\n')
        self.write_token(self.jack_tokenizer.key_word())
        self.write_token(self.jack_tokenizer.symbol())
        self.compile_expression()
        self.write_token(self.jack_tokenizer.symbol())

        self.write_token(self.jack_tokenizer.symbol())
        self.compile_statements()
        self.write_token(self.jack_tokenizer.symbol())
        if self.jack_tokenizer.key_word() == 'else':
            self.write_token(self.jack_tokenizer.key_word())
            self.write_token(self.jack_tokenizer.symbol())
            self.compile_statements()
            self.write_token(self.jack_tokenizer.symbol())

        self.output_file.write('</ifStatement>\n')


    def compile_expression(self):
        self.output_file.write('<expression>\n')
        self.compile_term()
        while self.jack_tokenizer.symbol() in CompilationEngine.BINARY_OPERATOR_SYMBOLS:
            symbol = self.jack_tokenizer.symbol()
            if symbol in CompilationEngine.SYMBOLS_TO_XML_CONVENTION:
                symbol = CompilationEngine.SYMBOLS_TO_XML_CONVENTION[symbol]
            self.write_token(symbol)
            self.compile_term()
        self.output_file.write('</expression>\n')


    def compile_term(self):
        self.output_file.write('<term>\n')
        token_type = self.jack_tokenizer.token_type()
        if token_type == 'IDENTIFIER':
            self.write_token(self.jack_tokenizer.identifier())
            if self.jack_tokenizer.symbol() == '[':
                self.write_token(self.jack_tokenizer.symbol())
                self.compile_expression()
                self.write_token(self.jack_tokenizer.symbol())
            elif self.jack_tokenizer.symbol() == '(' or self.jack_tokenizer.symbol() == '.':
                self.compile_subroutine_call()
        elif token_type == 'STRING_CONST':
            self.write_token(self.jack_tokenizer.string_val())
        elif token_type == 'INT_CONST':
            self.write_token(self.jack_tokenizer.int_val())
        elif token_type == 'KEYWORD':
            self.write_token(self.jack_tokenizer.key_word())
        elif token_type == 'INT_CONST':
            self.write_token(self.jack_tokenizer.int_val())
        elif token_type == 'SYMBOL':
            if self.jack_tokenizer.symbol() == '(':
                self.write_token(self.jack_tokenizer.symbol())
                self.compile_expression()
                self.write_token(self.jack_tokenizer.symbol())
            elif self.jack_tokenizer.symbol() in CompilationEngine.UNARY_OPERATOR_SYMBOLS:
                self.write_token(self.jack_tokenizer.symbol())
                self.compile_term()
        self.output_file.write('</term>\n')

    def compile_expression_list(self):
        self.output_file.write('<expressionList>\n')
        if self.jack_tokenizer.symbol() != ')':
            self.compile_expression()
            while self.jack_tokenizer.symbol() == ',':
                self.write_token(self.jack_tokenizer.symbol())
                self.compile_expression()
        self.output_file.write('</expressionList>\n')

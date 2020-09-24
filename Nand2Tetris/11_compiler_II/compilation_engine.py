from jack_tokenizer import JackTokenizer
from symbol_table import SymbolTable
from vm_writer import VMWriter


class CompilationEngine:
    CLASS_VAR_DEC_KEYWORDS = ['static', 'field']
    SUBROUTINE_DEC_KEYWORDS = ['constructor', 'function', 'method']
    BINARY_OPERATOR_SYMBOLS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
    UNARY_OPERATOR_SYMBOLS = ['-', '~']
    BINARY_OPERATORS_TO_COMMAND = {'+': 'add', '-': 'sub', '=': 'eq', '>': 'gt', '<': 'lt', '&': 'and', '|': 'or'}
    UNARY_OPERATORS_TO_COMMAND = {'-': 'neg', '~': 'not'}
    TYPE_TO_TAG = {'STRING_CONST': 'stringConstant', 'INT_CONST': 'integerConstant', 'KEYWORD': 'keyword',
                   'IDENTIFIER': 'identifier', 'SYMBOL': 'symbol'}

    SYMBOLS_TO_XML_CONVENTION = {'<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;'}

    def __init__(self, input_file_path, vm_writer: VMWriter):
        self.jack_tokenizer = JackTokenizer(input_file_path)
        self.symbol_table = SymbolTable()
        self.vm_writer = vm_writer
        if self.jack_tokenizer.has_more_tokens():
            self.compile_class()

    def compile_class(self):
        self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()
        self.symbol_table.define(self.jack_tokenizer.identifier(), 'NONE', 'CLASS')
        self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()

        if self.jack_tokenizer.key_word() in CompilationEngine.CLASS_VAR_DEC_KEYWORDS:
            self.compile_class_var_dec()
        if self.jack_tokenizer.key_word() in CompilationEngine.SUBROUTINE_DEC_KEYWORDS:
            self.compile_subroutine()

        self.jack_tokenizer.advance()
        self.vm_writer.close()

    def write_token(self, token_name):
        type_tag = CompilationEngine.TYPE_TO_TAG[self.jack_tokenizer.token_type()]
        self.output_file.write('<{0}> {1} </{0}>\n'.format(
            type_tag, token_name))
        self.jack_tokenizer.advance()

    def compile_class_var_dec(self):
        while self.jack_tokenizer.key_word() in CompilationEngine.CLASS_VAR_DEC_KEYWORDS:
            kind = ''
            if self.jack_tokenizer.key_word() == 'field':
                kind = 'FIELD'
            elif self.jack_tokenizer.key_word() == 'static':
                kind = 'STATIC'
            self.jack_tokenizer.advance()
            field_type = self.get_type()
            self.jack_tokenizer.advance()
            self.symbol_table.define(self.jack_tokenizer.identifier(), field_type, kind)

            self.jack_tokenizer.advance()

            while self.jack_tokenizer.symbol() != ';':
                self.jack_tokenizer.advance()
                self.symbol_table.define(self.jack_tokenizer.identifier(), field_type, kind)
                self.jack_tokenizer.advance()

            self.jack_tokenizer.advance()

    def write_type(self):
        if self.jack_tokenizer.token_type() == 'KEYWORD':
            self.write_token(self.jack_tokenizer.key_word())
        elif self.jack_tokenizer.token_type() == 'IDENTIFIER':
            self.write_token(self.jack_tokenizer.identifier())

    def compile_subroutine(self):
        self.vm_writer.zero_branching_indexes()
        while self.jack_tokenizer.key_word() in CompilationEngine.SUBROUTINE_DEC_KEYWORDS:
            self.symbol_table.start_subroutine()
            constructor = True if self.jack_tokenizer.key_word() == 'constructor' else False

            method = False
            if self.jack_tokenizer.key_word() == 'method':
                method = True
                self.symbol_table.define('this', self.symbol_table.get_class_name(), 'ARG')

            self.jack_tokenizer.advance()
            self.jack_tokenizer.advance()
            self.symbol_table.define(self.jack_tokenizer.identifier(), 'NONE', 'SUBROUTINE')
            name = self.symbol_table.get_class_name() + '.' + self.jack_tokenizer.identifier()
            self.jack_tokenizer.advance()
            self.jack_tokenizer.advance()
            self.compile_parameter_list()
            self.jack_tokenizer.advance()

            self.jack_tokenizer.advance()
            var_num = 0
            while self.jack_tokenizer.key_word() == 'var':
                var_num += self.compile_var_dec()
            self.vm_writer.write_function(name, var_num)
            if method:
                self.vm_writer.write_push('ARG', 0)
                self.vm_writer.write_pop('POINTER', 0)
            elif constructor:
                field_count = self.symbol_table.var_count('FIELD')
                self.vm_writer.write_push('CONST', field_count)
                self.vm_writer.write_call('Memory.alloc', 1)
                self.vm_writer.write_pop('POINTER', 0)
            self.compile_statements()
            self.jack_tokenizer.advance()

    def compile_parameter_list(self):
        if self.jack_tokenizer.symbol() != ')':
            parameter_type = self.get_type()
            self.jack_tokenizer.advance()
            self.symbol_table.define(self.jack_tokenizer.identifier(), parameter_type, 'ARG')
            self.jack_tokenizer.advance()
            while self.jack_tokenizer.symbol() == ",":
                self.jack_tokenizer.advance()
                parameter_type = self.get_type()
                self.jack_tokenizer.advance()
                self.symbol_table.define(self.jack_tokenizer.identifier(), parameter_type, 'ARG')
                self.jack_tokenizer.advance()

    def get_type(self):
        if self.jack_tokenizer.token_type() == 'KEYWORD':
            parameter_type = self.jack_tokenizer.key_word()
        elif self.jack_tokenizer.token_type() == 'IDENTIFIER':
            parameter_type = self.jack_tokenizer.identifier()
        return parameter_type

    def compile_var_dec(self):
        var_num = 1
        self.jack_tokenizer.advance()
        var_type = self.get_type()
        self.jack_tokenizer.advance()
        self.symbol_table.define(self.jack_tokenizer.identifier(), var_type, 'VAR')
        self.jack_tokenizer.advance()

        while self.jack_tokenizer.symbol() == ",":
            var_num += 1
            self.jack_tokenizer.advance()
            self.symbol_table.define(self.jack_tokenizer.identifier(), var_type, 'VAR')
            self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()
        return var_num

    def compile_statements(self):
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

    def compile_do(self):
        self.jack_tokenizer.advance()

        name = self.jack_tokenizer.identifier()
        self.jack_tokenizer.advance()
        self.compile_subroutine_call(name)

        # must dispose of void function return value
        self.vm_writer.write_pop('TEMP', 0)
        self.jack_tokenizer.advance()

    def compile_subroutine_call(self, prefix_call=''):
        if self.jack_tokenizer.symbol() == '(':
            subroutine = False
            # If not in symbol table - then subroutine
            if not self.symbol_table.kind_of(prefix_call) or self.symbol_table.kind_of(prefix_call) == 'SUBROUTINE':
                subroutine = True
            self.jack_tokenizer.advance()

            args_count = 0
            if subroutine:
                self.vm_writer.write_push('POINTER', 0)
                args_count += 1
            args_count += self.compile_expression_list()

            if subroutine:
                self.vm_writer.write_call(self.symbol_table.get_class_name() + '.' + prefix_call, args_count)
            else:
                self.vm_writer.write_call(prefix_call, args_count)
            self.jack_tokenizer.advance()
        elif self.jack_tokenizer.symbol() == '.':
            variable = False
            self.jack_tokenizer.advance()
            if self.symbol_table.kind_of(prefix_call) in ['VAR', 'FIELD']:
                variable = True
                variable_name = prefix_call
                prefix_call = self.symbol_table.type_of(prefix_call)
            prefix_call += '.{0}'.format(self.jack_tokenizer.identifier())
            self.jack_tokenizer.advance()
            self.jack_tokenizer.advance()

            args_count = 0
            if variable:
                self.vm_writer.write_push(self.symbol_table.kind_of(variable_name),
                                          self.symbol_table.index_of(variable_name))
                args_count += 1
            args_count += self.compile_expression_list()

            self.vm_writer.write_call(prefix_call, args_count)
            self.jack_tokenizer.advance()

    def compile_let(self):
        self.jack_tokenizer.advance()
        var_name = self.jack_tokenizer.identifier()
        self.jack_tokenizer.advance()
        if self.jack_tokenizer.symbol() == '[':
            self.vm_writer.write_push(self.symbol_table.kind_of(var_name), self.symbol_table.index_of(var_name))
            self.jack_tokenizer.advance()
            self.compile_expression()
            self.vm_writer.write_arithmetic("add")
            self.jack_tokenizer.advance()
            self.jack_tokenizer.advance()
            self.compile_expression()
            self.vm_writer.write_pop('TEMP', 0)
            self.vm_writer.write_pop('POINTER', 1)
            self.vm_writer.write_push('TEMP', 0)
            self.vm_writer.write_pop('THAT', 0)
        else:
            self.jack_tokenizer.advance()
            self.compile_expression()
            self.vm_writer.write_pop(self.symbol_table.kind_of(var_name), self.symbol_table.index_of(var_name))

        self.jack_tokenizer.advance()

    def compile_while(self):
        while_idx = self.vm_writer.get_next_label_index('while')
        if_label = 'WHILE_IF_{0}'.format(while_idx)
        end_label = 'WHILE_END_{0}'.format(while_idx)

        self.vm_writer.write_label(if_label)
        self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()
        self.compile_expression()
        self.vm_writer.write_arithmetic('not')
        self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()
        self.vm_writer.write_if(end_label)
        self.compile_statements()
        self.vm_writer.write_goto(if_label)
        self.jack_tokenizer.advance()
        self.vm_writer.write_label(end_label)

    def compile_return(self):
        self.jack_tokenizer.advance()
        if self.jack_tokenizer.symbol() != ';':
            self.compile_expression()
        else:
            self.vm_writer.write_push('CONST', 0)
        self.vm_writer.write_return()
        self.jack_tokenizer.advance()

    def compile_if(self):
        if_idx = self.vm_writer.get_next_label_index('if')
        else_label = 'IF_ELSE_{0}'.format(if_idx)
        end_label = 'IF_END_{0}'.format(if_idx)

        self.jack_tokenizer.advance()
        self.jack_tokenizer.advance()
        self.compile_expression()
        self.vm_writer.write_arithmetic('not')
        self.jack_tokenizer.advance()

        self.jack_tokenizer.advance()
        self.vm_writer.write_if(else_label)
        self.compile_statements()
        self.jack_tokenizer.advance()
        self.vm_writer.write_goto(end_label)

        self.vm_writer.write_label(else_label)
        if self.jack_tokenizer.key_word() == 'else':
            self.jack_tokenizer.advance()
            self.jack_tokenizer.advance()
            self.compile_statements()
            self.jack_tokenizer.advance()

        self.vm_writer.write_label(end_label)

    def compile_expression(self):
        self.compile_term()

        while self.jack_tokenizer.symbol() in CompilationEngine.BINARY_OPERATOR_SYMBOLS:
            symbol = self.jack_tokenizer.symbol()
            self.jack_tokenizer.advance()

            self.compile_term()

            if symbol in self.BINARY_OPERATORS_TO_COMMAND:
                self.vm_writer.write_arithmetic(self.BINARY_OPERATORS_TO_COMMAND[symbol])
            elif symbol == '*':
                self.vm_writer.write_call('Math.multiply', 2)
            elif symbol == '/':
                self.vm_writer.write_call('Math.divide', 2)

    def compile_term(self):
        token_type = self.jack_tokenizer.token_type()

        if token_type == 'IDENTIFIER':
            name = self.jack_tokenizer.identifier()
            self.jack_tokenizer.advance()
            if self.jack_tokenizer.symbol() == '(' or self.jack_tokenizer.symbol() == '.':
                self.compile_subroutine_call(name)
            elif self.jack_tokenizer.symbol() == '[':
                self.vm_writer.write_push(self.symbol_table.kind_of(name), self.symbol_table.index_of(name))
                self.jack_tokenizer.advance()
                self.compile_expression()
                self.jack_tokenizer.advance()
                self.vm_writer.write_arithmetic('add')
                self.vm_writer.write_pop('POINTER', 1)
                self.vm_writer.write_push('THAT', 0)
            else:
                kind = self.symbol_table.kind_of(name)
                idx = self.symbol_table.index_of(name)
                self.vm_writer.write_push(kind, idx)
        elif token_type == 'STRING_CONST':
            string_const = self.jack_tokenizer.string_val()

            self.vm_writer.write_push("CONST", len(string_const))
            self.vm_writer.write_call("String.new", 1)
            for char in string_const:
                self.vm_writer.write_push('CONST', ord(char))
                self.vm_writer.write_call("String.appendChar", 2)
            self.jack_tokenizer.advance()
        elif token_type == 'KEYWORD':
            keyword = self.jack_tokenizer.key_word()
            if keyword == 'true':
                self.vm_writer.write_push('CONST', 1)
                self.vm_writer.write_arithmetic('neg')
            elif keyword == 'false' or keyword == 'null':
                self.vm_writer.write_push('CONST', 0)
            elif keyword == 'this':
                self.vm_writer.write_push('POINTER', 0)
            self.jack_tokenizer.advance()
        elif token_type == 'SYMBOL':
            if self.jack_tokenizer.symbol() == '(':
                self.jack_tokenizer.advance()
                self.compile_expression()
                self.jack_tokenizer.advance()
            elif self.jack_tokenizer.symbol() in CompilationEngine.UNARY_OPERATOR_SYMBOLS:
                command = CompilationEngine.UNARY_OPERATORS_TO_COMMAND[self.jack_tokenizer.symbol()]
                self.jack_tokenizer.advance()
                self.compile_term()
                self.vm_writer.write_arithmetic(command)
        elif token_type == 'INT_CONST':
            self.vm_writer.write_push('CONST', self.jack_tokenizer.int_val())
            self.jack_tokenizer.advance()

    def compile_expression_list(self):
        expression_count = 0
        if self.jack_tokenizer.symbol() != ')':
            self.compile_expression()
            expression_count += 1
            while self.jack_tokenizer.symbol() == ',':
                self.jack_tokenizer.advance()
                self.compile_expression()
                expression_count += 1
        return expression_count

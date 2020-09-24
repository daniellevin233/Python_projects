import re


class JackTokenizer:
    KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean',
                'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
    SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    IGNORED_SIGNS = ['\t', ' ', '\n']
    COMMENTS = [('//', '\n'), ('^/\*\*', '\*/'), ('^/\*', '\*/')]

    KEYWORD_REGEX = re.compile('[a-z][a-z]*\\b')
    IDENTIFIER_REGEX = re.compile('[a-zA-Z_][a-zA-Z0-9_]*\\b')
    CONST_INT_REGEX = re.compile('\\d{1,5}')
    STRING_REGEX = re.compile('"(.*?)"')
    TOKEN_REGEX = re.compile('[^\t \n]')

    def __init__(self, jack_code_file_path):
        file = open(jack_code_file_path)
        self.__file_text = file.read()
        file.close()
        self.remove_comments()
        self.char_counter = 0

        self.current_token = ''
        self.__token_type = ''

    def remove_comments(self):
        for item in JackTokenizer.COMMENTS:
            sub = re.sub('({0}.*?{1})'.format(item[0], item[1]),
                               '', self.__file_text, flags=re.DOTALL)
            self.__file_text = sub

    def has_more_tokens(self):
        rest_of_file = self.__file_text[self.char_counter:]
        token = re.search(JackTokenizer.TOKEN_REGEX, rest_of_file)

        if token:
            return True
        return False

    def advance(self):
        while True:
            if self.char_counter == len(self.__file_text):
                return False

            current_char = self.__file_text[self.char_counter]
            if current_char not in JackTokenizer.IGNORED_SIGNS:
                self.parse_token(current_char)
                return True
            else:
                self.char_counter += 1

    def parse_token(self, current_char):
        rest_of_file = self.__file_text[self.char_counter:]

        keyword_pattern_match = re.match(JackTokenizer.KEYWORD_REGEX, rest_of_file)
        identifier_match = re.match(JackTokenizer.IDENTIFIER_REGEX, rest_of_file)
        const_int_match = re.match(JackTokenizer.CONST_INT_REGEX, rest_of_file)
        const_string_match = re.match(JackTokenizer.STRING_REGEX, rest_of_file)

        char_offset = 0
        if current_char in JackTokenizer.SYMBOLS:
            self.current_token = current_char
            self.__token_type = 'SYMBOL'
            char_offset = 1

        elif keyword_pattern_match and keyword_pattern_match.group(0) in JackTokenizer.KEYWORDS:
            self.current_token = keyword_pattern_match.group(0)
            self.__token_type = 'KEYWORD'
            char_offset = len(self.current_token)

        elif identifier_match:
            self.current_token = identifier_match.group(0)
            self.__token_type = 'IDENTIFIER'
            char_offset = len(self.current_token)

        elif const_int_match:
            self.current_token = const_int_match.group(0)
            char_offset = len(self.current_token)
            self.__token_type = 'INT_CONST'

        elif const_string_match:
            self.current_token = const_string_match.group(1)
            char_offset = len(const_string_match.group(0))
            self.__token_type = 'STRING_CONST'

        self.char_counter += char_offset

    def token_type(self):
        return self.__token_type

    def key_word(self):
        return self.current_token

    def symbol(self):
        return self.current_token

    def identifier(self):
        return self.current_token

    def int_val(self):
        return self.current_token

    def string_val(self):
        return self.current_token

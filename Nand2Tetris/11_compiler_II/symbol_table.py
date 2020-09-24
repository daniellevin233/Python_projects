class SymbolTable:
    def __init__(self):
        self.class_symbol_table = {}
        self.subroutine_symbol_table = {}

    def start_subroutine(self):
        self.subroutine_symbol_table = {}

    def get_class_name(self):
        for key in self.class_symbol_table:
            if self.kind_of(key) == 'CLASS':
                return key

    def define(self, name, type, kind):
        relevant_dict = self.get_relevant_dict(kind)

        if kind == 'CLASS' or kind == 'SUBROUTINE':
            relevant_dict[name] = (kind, type)
        else:
            kind_count = self.var_count(kind)
            relevant_dict[name] = (kind, type, kind_count)

    def var_count(self, kind):
        count = 0

        relevant_dict = self.get_relevant_dict(kind)
        for key in relevant_dict:
            if self.kind_of(key) == kind:
                count += 1

        return count

    def get_relevant_dict(self, kind):
        if kind == 'CLASS' or kind == 'SUBROUTINE' or kind == 'STATIC' or kind == 'FIELD':
            return self.class_symbol_table
        elif kind == 'ARG' or kind == 'VAR':
            return self.subroutine_symbol_table

    def kind_of(self, name):
        if name in self.subroutine_symbol_table:
            return self.subroutine_symbol_table[name][0]
        elif name in self.class_symbol_table:
            return self.class_symbol_table[name][0]
        return None

    def type_of(self, name):
        if name in self.subroutine_symbol_table:
            return self.subroutine_symbol_table[name][1]
        elif name in self.class_symbol_table:
            return self.class_symbol_table[name][1]
        return None

    def index_of(self, name):
        if name in self.subroutine_symbol_table:
            return self.subroutine_symbol_table[name][2]
        elif name in self.class_symbol_table:
            return self.class_symbol_table[name][2]
        return None

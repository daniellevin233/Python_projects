"""
Class that's responsible to populate and maintain the symbol table for translation
"""


class SymbolTable:
    def __init__(self):
        self.__symbol_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }
        self.__mem_address = 16

    def add_entry(self, symbol, address):
        if not self.contains(symbol):
            self.__symbol_table[symbol] = address

    """
    Wrapper that assigns the new variable a memory address, then adds it to the table
    """
    def add_variable(self, var):
        self.add_entry(var, self.__mem_address)
        self.__mem_address += 1

    def contains(self, symbol):
        return symbol in self.__symbol_table

    def get_address(self, symbol):
        return self.__symbol_table[symbol]

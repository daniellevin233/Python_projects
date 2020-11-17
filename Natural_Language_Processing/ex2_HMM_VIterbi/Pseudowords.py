import re
from enum import Enum


class Pseudoword(Enum):
    TwoDigitNum = 'twoDigitNum'
    FourDigitNum = 'fourDigitNum'
    ContainsDigitAndAlpha = 'containsDigitAndAlpha'
    ContainsDigitAndDash = 'containsDigitAndDash'
    ContainsDigitAndSlash = 'containsDigitAndSlash'
    ContainsDigitAndComma = 'containsDigitAndComma'
    ContainsDigitAndPeriod = 'containsDigitAndPeriod'
    Othernum = 'othernum'
    AllCaps = 'allCaps'
    CapPeriod = 'capPeriod'
    DollarMoney = 'dollarMoney'
    InitCap = 'initCap'
    LowerCase = 'lowerCase'
    Other = 'other'


class Pseudowords:
    def __init__(self, lst_of_samples):
        self.__words_to_pseudowords_dict = \
            {sample[0]: Pseudowords.classify_pseudoword(sample[0]) for sample in lst_of_samples}

    def get_words_to_pseudowords_dict(self):
        return self.__words_to_pseudowords_dict

    @staticmethod
    def classify_pseudoword(word):
        if re.fullmatch('\\d{2}', word):  # 90
            return Pseudoword.TwoDigitNum
        if re.fullmatch('\\d{4}', word):  # 1990
            return Pseudoword.FourDigitNum
        if re.fullmatch('[A-Za-z][0-9_-]+', word):  # A8956-67
            return Pseudoword.ContainsDigitAndAlpha
        if '-' in word and re.fullmatch('[0-9-]+', word):  # 09-96
            return Pseudoword.ContainsDigitAndDash
        if '/' in word and re.fullmatch('[0-9/]+', word):  # 11/9/89
            return Pseudoword.ContainsDigitAndSlash
        if ',' in word and '.' in word and re.fullmatch('[0-9,.]+', word):  # 23,000.00
            return Pseudoword.ContainsDigitAndComma
        if '.' in word and re.fullmatch('[0-9.]+', word):  # 1.00
            return Pseudoword.ContainsDigitAndPeriod
        if re.fullmatch('\\d+', word):  # 456789
            return Pseudoword.Othernum
        if re.fullmatch('[A-Z]+', word):  # BBN
            return Pseudoword.AllCaps
        if re.fullmatch('[A-Z].', word):  # M.
            return Pseudoword.CapPeriod
        if re.fullmatch('\\$\\d+', word):  # $12
            return Pseudoword.DollarMoney
        if re.fullmatch('[A-Z][a-z]+', word):  # Sally
            return Pseudoword.InitCap
        if re.fullmatch('[a-z]+', word):  # can
            return Pseudoword.LowerCase
        else:  # ,
            return Pseudoword.Other

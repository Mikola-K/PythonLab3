from abc import ABC
from modules.bank_type import BankType

class BankService(ABC):
    def __init__ (self, bank_name = ' ', bank_type = BankType.COMERCIAL, is_available = False, interest_rate = 0.0):
        self.bank_name = bank_name
        self.bank_type = bank_type
        self.is_available = is_available
        self.interest_rate = interest_rate
    
    def __str__(self):
        return f"Name of bank: {self.bank_name}\n"\
               f"Type of Bank: {self.bank_type.name}\n"\
               f"Available: {self.is_available}\n" \
               f"Interest rate: {self.interest_rate}\n"                                                                              
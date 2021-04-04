from modules.bank_service import BankService
from modules.credit_type import CretidType
from modules.credit_term import CretidTerm
from modules.bank_type import BankType
from modules.lending import Lending

class Credit(BankService):
    def __init__(self, bank_name=' ', bank_type=BankType.COMERCIAL, is_available=False, interest_rate=0.0,
                 credit_type=CretidType.BANKING, credit_term=CretidTerm.LONG_TERM, method_of_lending=Lending.COMERCIAL,
                 collateral_loans="", consumer_loans='', credit_interest=""):
        super().__init__(bank_name, bank_type, is_available, interest_rate)
        self.credit_type = credit_type
        self.credit_term = credit_term
        self.method_of_landing = method_of_lending
        self.collateral_loans = collateral_loans
        self.consumer_loans = consumer_loans
        self.credit_interest = credit_interest

    def __str__(self):
        return  f"{super().__str__()}\n"\
                f"Cretid type: {self.credit_type.name}\n"\
                f"Credit term: {self.credit_term.name}\n"\
                f"Method of landing: {self.method_of_landing.name}\n" \
                f"Collateral loans: {self.collateral_loans}\n"\
                f"Consumer loans: {self.consumer_loans}\n"\
                f"Credit interest: {self.credit_interest}\n"

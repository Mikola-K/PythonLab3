from manager import *
from modules import *
from modules.deposit import Deposit
from modules.credit import Credit
import unittest

class TestBankManager(unittest.TestCase):

    def setUp(self): 
        self.First_bank = Credit("Tikva", BankType.NATIONAL, True, 15, CretidType.PUBLIC,
                                 CretidTerm.SHORT_TERM , Lending.COMERCIAL, "Mortgage real estate", "Commodity", 22)
        self.Second_bank = Deposit("Popular Bank", BankType.COMERCIAL, False, 10, 44 , DepositType.SAVINGS)
        self.Third_bank = Credit("Money for you", BankType.NATIONAL, True, 33, CretidType.BANKING,
                                 CretidTerm.LONG_TERM, Lending.COMMODITY, "Tesla shares", 'Cash', 10)
        self.Fourth_bank = Credit("Free Money", BankType.COMERCIAL, False, 3, CretidType.BANKING,
                                  CretidTerm.LONG_TERM, Lending.COMMODITY, "Apple shares", 'Cash', 100)
        self.Fifth_bank = Deposit("BankA", BankType.NATIONAL, True, 11, 1, DepositType.SAVINGS)
        self.Sixth_bank = Deposit("Ukraine", BankType.COMERCIAL, False, 44, 20, DepositType.UNIVERSAL)

        self.bank_interest_asc_order = [self.Fourth_bank, self.Second_bank, self.Fifth_bank, self.First_bank, self.Third_bank, self.Sixth_bank]
        self.bank_interest_desc_order = list(reversed(self.bank_interest_asc_order))

        self.credit_by_rate_asc_order = [self.Fourth_bank, self.First_bank, self.Third_bank]
        self.credit_by_rate_desc_order = list(reversed(self.credit_by_rate_asc_order))

        self.bank_manager = BankManager()
        self.bank_manager.add_bank_services(self.First_bank, self.Second_bank, self.Third_bank, self.Fourth_bank, self.Fifth_bank, self.Sixth_bank)
             
    def test_search_by_avaliability(self):
        self.assertEqual(self.bank_manager.search_by_avaliability(is_available = False),
                        [self.Second_bank, self.Fourth_bank, self.Sixth_bank])
        self.assertEqual(self.bank_manager.search_by_avaliability(is_available = True),
                        [self.First_bank, self.Third_bank, self.Fifth_bank])            

    def test_sort_by_interest_rate(self):
        self.assertEqual(self.bank_manager.sort_by_interest_rate(self.bank_manager.bank_services, SortOrder.ASC),
                                                                 self.bank_interest_asc_order)
        self.assertEqual(self.bank_manager.sort_by_interest_rate(self.bank_manager.bank_services, SortOrder.DESC),
                                                                 self.bank_interest_desc_order)

if __name__ == "__main__":
    unittest.main()

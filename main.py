from manager import *
from modules import *
from modules.deposit import Deposit

def main():
    First_bank = Credit(bank_name = "Tikva", bank_type = BankType.NATIONAL, is_available = True, interest_rate = 15, credit_type = CretidType.PUBLIC,
                credit_term = CretidTerm.SHORT_TERM, method_of_lending = Lending.COMERCIAL , collateral_loans = "Mortgage real estate", consumer_loans = 'Commodity', credit_interest= 22)

    Second_bank = Deposit(bank_name = "Popular Bank", bank_type = BankType.COMERCIAL, is_available = False, interest_rate = 10, deposit_term = 44 , deposit_type = DepositType.SAVINGS)

    Third_bank = Credit(bank_name = "Money for you", bank_type = BankType.NATIONAL , is_available = True, interest_rate = 33, credit_type = CretidType.BANKING ,
                credit_term = CretidTerm.LONG_TERM , method_of_lending = Lending.COMMODITY , collateral_loans = "Tesla shares", consumer_loans = 'Cash', credit_interest= 10)

    Fourth_bank = Credit(bank_name = "Free Money", bank_type = BankType.COMERCIAL , is_available = False, interest_rate = 3, credit_type = CretidType.BANKING ,
                credit_term = CretidTerm.LONG_TERM , method_of_lending = Lending.COMMODITY , collateral_loans = "Apple shares", consumer_loans = 'Cash', credit_interest= 100)

    Fifth_bank = Deposit(bank_name = "BankA", bank_type = BankType.NATIONAL, is_available = True, interest_rate = 11, deposit_term = 1 , deposit_type = DepositType.SAVINGS)

    Sixth_bank = Deposit(bank_name = "Ukraine", bank_type = BankType.COMERCIAL, is_available = False, interest_rate = 44, deposit_term = 20 , deposit_type = DepositType.UNIVERSAL)

    list_of_credits = []
    list_of_credits.append(First_bank)
    list_of_credits.append(Third_bank)
    list_of_credits.append(Fourth_bank)

    list_of_deposits = []
    list_of_deposits.append(Second_bank)
    list_of_deposits.append(Fifth_bank)
    list_of_deposits.append(Sixth_bank)

    list_of_credits_and_deposits = []
    list_of_credits_and_deposits.append(First_bank)
    list_of_credits_and_deposits.append(Second_bank)
    list_of_credits_and_deposits.append(Third_bank)
    list_of_credits_and_deposits.append(Fourth_bank)
    list_of_credits_and_deposits.append(Fifth_bank)
    list_of_credits_and_deposits.append(Sixth_bank)

    Serega = BankManager()

    Serega.add_bank_services(First_bank, Second_bank, Third_bank, Fourth_bank, Fifth_bank, Sixth_bank)
    print ("Search by avaliability: \n" )
    print (*Serega.search_by_avaliability(is_available = False))
    print ("####################################################################")

    Serega.sort_by_interest_rate(list_of_credits_and_deposits, sort_order=SortOrder.DESC)
    print ("Sorted by interest rate: \n", *list_of_credits_and_deposits) 
    
    print ("Credits sorted by interest rate: #########################################")
    Serega.print_credit_by_interest_rate(list_of_credits, sort_order=SortOrder.ASC)

    print ("Deposits sotred by term: #########################################")
    Serega.print_deposit_by_term(list_of_deposits, sort_order= SortOrder.DESC)

if __name__ == "__main__":
    main()
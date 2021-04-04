from manager import *
from modules import *
from modules.deposit import Deposit

if __name__ == "__main__":
    First_bank = Credit( "Tikva", BankType.NATIONAL, True, 15, CretidType.PUBLIC, 
                        CretidTerm.SHORT_TERM , Lending.COMERCIAL, "Mortgage real estate", "Commodity", 22)

    Second_bank = Deposit("Popular Bank", BankType.COMERCIAL, False, 10, 44 , DepositType.SAVINGS)

    Third_bank = Credit("Money for you", BankType.NATIONAL, True, 33, CretidType.BANKING,
                        CretidTerm.LONG_TERM, Lending.COMMODITY, "Tesla shares", 'Cash', 10)

    Fourth_bank = Credit("Free Money", BankType.COMERCIAL, False, 3, CretidType.BANKING,
                        CretidTerm.LONG_TERM, Lending.COMMODITY, "Apple shares", 'Cash', 100)

    Fifth_bank = Deposit("BankA", BankType.NATIONAL, True, 11, 1, DepositType.SAVINGS)

    Sixth_bank = Deposit("Ukraine", BankType.COMERCIAL, False, 44, 20, DepositType.UNIVERSAL)

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
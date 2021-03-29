from manager.sort_order import SortOrder
from copy import deepcopy
from modules.bank_service import BankService

class BankManager:
    def __init__(self):
        self.bank_services = []
        self.credits = []
        self.deposits = []

    def add_bank_services(self, *bank_services):
        for bank_service in bank_services:
            self.bank_services.append(bank_service)

    def search_by_avaliability (self, is_available: bool):
        found_bank_services = [bank_service for bank_service in self.bank_services if bank_service.is_available == is_available]
        return found_bank_services
       
    def sort_by_interest_rate (self, items: list, sort_order: SortOrder):
        items.sort(key=lambda x: x.interest_rate, reverse= sort_order.value)

    def print_credit_by_interest_rate (self, credits = [], sort_order = SortOrder.ASC):
        sorted_credits = deepcopy(credits)
        sorted_credits.sort(key=lambda x: x.credit_interest, reverse= sort_order.value)
        for credit in sorted_credits:
            print(credit)

    def print_deposit_by_term (self, deposits = [], sort_order = SortOrder.ASC):
        sorted_deposits = deepcopy(deposits)
        sorted_deposits.sort(key=lambda x: x.deposit_term, reverse= sort_order.value)
        for deposit in sorted_deposits:
            print(deposit)
  

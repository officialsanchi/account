import  unittest
import account
from account import Account

class AccountTest(unittest.TestCase):

    def test_check_If_Account_Exists(self):
        self.assertTrue(Account)

    def test_to_check_If_Account_Can_return_first_Name(self):
        account1 = account.Account("chidinma","esther")
        self.assertEquals(account1.account_firstName,"chidinma")
    def test_to_check_If_Account_Can_return_last_name(self):
        account1 = account.Accoount("chidinma","esther")
        self.assertEquals(account1.account_lastName,"chidinma")

    def test_to_check_if_Account_Can_


################
#### OOP #####
################

class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    error.py:12
    """
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def format(self):
        return self.file + ':' + str(self.line)

    def write(self):
        print(self.format())

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "lab10.py")
    >>> err1.write()
    lab10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "lab10.py", 4)
    >>> err2.write()
    lab10.py:18 SyntaxError : EOL while scanning string literal
    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        self.line = line
        self.file = file
        self.code = code

    def format(self):
        assert(self.code >= 0)
        if self.code != 0:
            return self.file + ':' + str(self.line) + ' ' + self.type + ' : ' + self.msgs[self.code]
        else:
            return super().format() + ' ' + self.type + ' : ' + self.msgs[0]
            
    def add_code(self, code, msg):
        self.msgs[code] = msg

class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "lab10.py")
    >>> err1.write()
    lab10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        self.line = line
        self.file = file
        self.message = message

    def format(self):
        end = self.type + ' : ' + self.message
        return self.file + ':' + str(self.line) + ' ' + end


class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
    def deposit_check(self, check):
        if check.payable_to != self.holder:
            print('The police have been notified.')
        else:
            check_amount = check.value
            if check.deposited:
                print('The police have been notified.')
            check,value = 0
            if check.value == 0 and not check.deposited:
                super().deposit(check_amount)
                check.deposited = True
                return check_amount


class Check(object):
    deposited = False
    def __init__(self, payable_to, value):
        self.payable_to = payable_to
        self.value = value


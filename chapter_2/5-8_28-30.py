class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def _set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('amount must be numeric')
        elif amount < 0:
            raise ValueError('amount must be postive')
        self._balance -= amount

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, mmp, add_fine, balance):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._mon_charge = 0
        self._mon_pay = 0
        self._mmp = mmp # mmp = monthly min pay
        self._add_fine = add_fine
        self._mmpm = self._balance*self._mmpm
        super()._set_balance(balance)

    def make_payment(self, amount):
        super().make_payment(amount)
        self._mon_pay += amount

    def charge(self, price):
        self._mon_charge += 1
        success = super().charge(price)
        if not success:
            self._balance+=5
            return False
        else:
            return True

    def process_month(self):
        if self._mmpm > self._mon_pay:
            self._balance += self._add_fine

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

        if self._mon_charge > 10:
            self._balance += self._mon_charge-10

        self._mon_charge = 0
        self._mon_pay = 0
        self._mmpm = self._balance * self._mmp

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings',
                             '5391 0375 9387 5309', 2500) )
    wallet.append(CreditCard('John Bowman', 'California Federal',
                             '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Bowman', 'California Finance',
                             '5391 0375 9387 5309', 5000) )

    for val in range(1, 59):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
    print()

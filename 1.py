def mk_wd(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


rem = mk_wd(100)
print(rem(10))
print(rem(20))
print(rem(100))

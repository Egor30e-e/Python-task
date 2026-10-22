class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма должна быть положительной")
    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств")
    return balance - amount


try:
    print(withdraw(100, 50))
    print(withdraw(100, -10))
except BankError as e:
    print(type(e).__name__, ":", e)

try:
    print(withdraw(30, 50))
except BankError as e:
    print(type(e).__name__, ":", e)

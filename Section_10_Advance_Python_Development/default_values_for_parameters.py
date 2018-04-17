accounts = {
    'checking': 1956.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balnce."""
    accounts[name] += amount
    return accounts[name]


if __name__ == '__main__':
    add_balance(500.00, 'savings')
    print(accounts['savings'])

    add_balance(100.00)
    print(accounts['checking'])





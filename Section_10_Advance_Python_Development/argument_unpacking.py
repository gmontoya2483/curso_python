accounts = {
    'checking': 1956.00,
    'savings': 3695.50
}


users = [
    {'username': 'Rolf', 'password': '123'},
    {'username': 'blabla', 'password': '1234'}
]


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balnce."""
    accounts[name] += amount
    return accounts[name]


if __name__ == '__main__':
    transactions = [
        (-180.67, 'checking'),
        (-220.00, 'checking'),
        (220.00, 'savings'),
        (-15.70, 'checking'),
        (-23.90, 'checking'),
        (-13.00, 'checking'),
        (1579.50, 'checking'),
        (-600.50, 'checking'),
        (600.50, 'savings'),
    ]

    # Normal
    for t in transactions:
        add_balance(t[0], t[1])

    # Unpacking arguments *
    for t in transactions:
        add_balance(*t)

    # naming the arguments
    for t in transactions:
        add_balance(amount=t[0], name=t[1])

    # Deconstruction
    for t in transactions:
        amount, name = t
        add_balance(amount, name)

    # Name argument unpacking **
    user_objects = [User(**data) for data in users]
    # Es lo mismo que: [User(username = data['username', password= data['password']) for data in users]


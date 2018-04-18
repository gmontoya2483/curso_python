
def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)
    print(id(account_holders))
    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


if __name__ == '__main__':
    a1 = create_account('checking', 'Rolf')
    a2 = create_account('savings', 'Jen')

    print(a2)

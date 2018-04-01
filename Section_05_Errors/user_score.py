class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__(self):
        return f'<User {self.name}>'


def email_engaged_user (user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        # raise este raise haria un re raise de la exception para obtener el trace, pero interrumpe la ejecucion
    else:  # El else dentro del try, se ejecuta si no hubo ningun error. A diferencia del finally que se ejecuta siempre
        send_engagement_notification(user)
    finally:
        print('Print finally.')


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to { user }.')


if __name__ == '__main__':
    my_user = User('Rolf', {'clicks': 61, 'hits': 100})
    email_engaged_user(my_user)

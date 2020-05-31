class Value:
    def __get__(self, obj, obj_type):  # определяет поведение при доступе к атрибуту.
        # print('get')
        return self.total

    def __set__(self, obj, value):  # срабатывает при присовении значения атрибуту
        # print('value in class Value = ', value)
        # print('obj.commission = ', obj.commission)
        # print('надо вернуть = ', value - obj.commission * value)
        self.total = value - obj.commission * value
        return self.total

    def __delete__(self, obj):
        print('delete')


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission




if __name__ == "__main__":
    # execute only if run as a script
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

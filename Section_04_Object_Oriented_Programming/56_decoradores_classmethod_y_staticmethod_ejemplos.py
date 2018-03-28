class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @staticmethod
    def from_sum_static(value1, value2):
        return FixedFloat(value1 + value2)
    
    @classmethod
    def from_sum_class(cls,value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

number = FixedFloat(18.5768)
print(number)

new_number = FixedFloat.from_sum_static(19.568, 0.789)
print(new_number)


money = Euro(45.456)
print(money)

money2 = Euro.from_sum_static(18.89, 9.9999)
print(money2)

money3 = Euro.from_sum_class(154.5666, 14.456)
print(money3)

    
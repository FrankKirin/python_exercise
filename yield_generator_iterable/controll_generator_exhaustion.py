class Bank(object):
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'


hsbc = Bank()
corner_street_atm = hsbc.create_atm()

print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for cash in range(5)])
hsbc.crisis = True  # crisis is coming, no more money
print(corner_street_atm.__next__())
wall_street_atm = hsbc.create_atm()
print(wall_street_atm.__next__())
brand_new_atm = hsbc.create_atm()
for cash in brand_new_atm:
    print(cash)
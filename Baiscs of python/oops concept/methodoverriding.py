# When the parent class method is defined in the child class with some specific implementation,
# then the concept is called method overriding


class Bank:
    def roi(self):
        return "10% return"

class IcIcBank(Bank):
    def roi(self):
        return "7% return"

class UnionBank(Bank):
    def roi(self):
        return "9% return"

bankb1 = Bank()
bankb2 = IcIcBank()
bankb3 = UnionBank()

print("Bank Rate of interest:",bankb1.roi())
print("Bank Rate of interest:",bankb2.roi())
print("Bank Rate of interest:",bankb3.roi())

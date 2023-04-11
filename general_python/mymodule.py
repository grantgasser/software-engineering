def hello(name):
    print(f"hello {name}")

car = {
    'model': 'camry',
    'make': 'toyota',
    'year': '2016'
}

class Motorcyle:
    def __init__(self, make, model, year, cc) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.cc = cc

    def __str__(self) -> str:
        return f"Motorcyle Object: {self.year} {self.make} {self.model}, {self.cc}cc"
class Car:
    def __init__(self, model, year, milage):
        self.model = model
        self.year = year
        self.milage = milage

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return "This is my car!"


    def shape(self, n):
        # n = int(input("Enter number of rows:"))

        m = 1
        while m < n:
            d = "*"
            print(m*d, end=" ")
            m += 2
            print("\r")


# audi = Car("BRAND AUDI_202", 1965, 173)
# print(audi.year)
# print(audi.model)
# print(audi.milage)
# print(audi.age(2022))
# print(audi.shape(10))

mylist = [3,4,5,6,7]
new = iter(mylist)
# print(next(new))
# print(next(new))
# print(next(new))
# print(next(new))
# print(next(new))


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
class Dessert():
    def __init__(self, name = None, calories = None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    @property
    def is_healthy(self):
        if self._calories == None:
            return None
        return self._calories < 200

    @property
    def is_delicious(self):
        return True


a = Dessert()
print(a.name)
print(a.calories)
print(a.is_healthy)
print(a.is_delicious)
a.name = "smth"
a.calories = 4356
print("_____")
print(a.name)
print(a.calories)
print(a.is_healthy)
print(a.is_delicious)
print("_____")
a = Dessert("chocolate", 123)
print(a.name)
print(a.calories)
print(a.is_healthy)
print(a.is_delicious)

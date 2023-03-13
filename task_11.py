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

    def is_healthy(self):
        if type(self._calories) != int:
            return None
        return self._calories < 200

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

dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
dessert.calories = "test_calories2"
print(dessert.calories)
if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
print(dessert.is_healthy())

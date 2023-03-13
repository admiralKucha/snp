class JellyBean():
    def __init__(self, name = None, calories = None, flavor = None):
        self.name = name
        self.calories = calories
        self.flavor = flavor

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
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_healthy(self):
        if type(self._calories) != int or type(self._calories) != float:
            return None
        return self._calories < 200

    def is_delicious(self):
        if self.flavor != "black licorice":
            return True
        return False

dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
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
dessert.flavor = 23
print(dessert.flavor)
print(dessert.is_delicious())


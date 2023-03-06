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

    @property
    def is_healthy(self):
        if self._calories == None:
            return None
        return self._calories < 200

    @property
    def is_delicious(self):
        if self.flavor != "black licorice":
            return True
        return False

a = JellyBean()
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
a = JellyBean("chocolate", 123)
print(a.name)
print(a.calories)
print(a.is_healthy)
print(a.is_delicious)
print("_____")
a = JellyBean(flavor="black licorice")
print(a.name)
print(a.calories)
print(a.is_healthy)
print(a.is_delicious)
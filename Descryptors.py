from abc import ABC, abstractmethod

class Storage(object):
    _count = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._count
        self.storage_name = f"_{prefix}#{index}"
        cls._count += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validator(ABC, Storage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abstractmethod
    def validate(self, instance, value):
        pass

class SideV(Validator):

    def validate(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Błędna wartość.")
        else:
            if value > 0.0:
                return value
            else:
                raise ValueError("Długość boku musi być wieksza od 0.")

class AngleV(Validator):

    def validate(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Błędna wartość.")
        else:
            if value <=120.0:
                return value
            else:
                raise ValueError("Szerokość kąta musi być poniżej 120 stopni")

class ColorV(Validator):

    def validate(self, instance, value):
        colours = ['black', 'red', 'blue', 'yellow', 'green']

        if len(value) > 0 and value.isalpha():
            for i in colours:
                if i == value:
                    return value
            else:
                raise ValueError("Brak koloru. Dostępne kolory: black, red, blue, yellow, green")
        else:
            raise ValueError("Brak koloru. Dostępne kolory: black, red, blue, yellow, green")
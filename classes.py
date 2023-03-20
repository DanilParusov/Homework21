from abc import abstractmethod


class Storage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print(f"Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как не достаточно места")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_space(self):
        return self.capacity - sum(self.items.values())

    def get_item(self):
        return self.items

    def get_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 30
        self._limit = limit
        self.items = {}

    @property
    def get_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_count() < self._limit:
            super().add(name, count)
        else:
            print(f"Товар не может быть добавлен")

    def get_count(self):
        return len(self.items.keys())


class Request:
    def __init__(self, user_string):
        user_string = self.get_info(user_string)

        self.from_ = user_string[4]
        self.amount = int(user_string[1])
        self.product = user_string[2]
        self.to = user_string[6]

    def get_info(self, user_string):
        return user_string.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'

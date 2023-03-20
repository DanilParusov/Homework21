from classes import Shop, Store, Request

shop = Shop()
store = Store()
shop.add("печеньки", 5)
shop.add("собачки", 5)
store.add("печеньки", 5)
user_string = input()
user_list = user_string.split(" ")
r = Request(user_string)

if user_list[0] == "Доставить":
    print(r)
    if "магазин" in r.from_:
        print("Доставить можно только со склада")
    elif "склад" in r.from_:
        if r.product in store.get_item():
            if r.amount <= store.get_item()[r.product]:
                print(f"Курьер забирает {r.amount} {r.product} из {r.from_}")
                print(f"Курьер везет {r.amount} {r.product} со {r.from_} в {r.to}")
                if sum(shop.get_item().values()) + int(r.amount) < shop.capacity:
                    print(f"Курьер доставил {r.amount} {r.product} в {r.to}")
                    store.remove(r.product, r.amount)
                    shop.add(r.product, r.amount)
                else:
                    print("В магазин недостаточно места, попобуйте что-то другое")
            else:
                print(f"На складе не хватает {r.product}, всего на складе {store.get_item()[r.product]}")
        else:
            print("Такого товара нет на складе")
        print("В магазине хранится:")
        for key, value in shop.items.items():
            print(key, value)
        print("На складе хранится:")
        for key, value in store.items.items():
            print(key, value)

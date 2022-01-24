# shopping_list = {
#     "bread": 1,
#     "milk": 2,
#     "Chocolate": 1,
#     "butter": 1,
#     "coffee": 1
# }

shopping_list = {}


def add_item(item_name, quantity):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity


add_item("Bread", 1)
add_item("Bread", 1)
print(shopping_list)


def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{quantity} X {item_name}")


# show_list()


# del[shopping_list["bread"]]
# print(shopping_list)
# print(shopping_list.items())

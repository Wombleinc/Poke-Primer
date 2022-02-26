import items_list
from Item import Item


def main():
    item1 = Item('https://pokeapi.co/api/v2/item/1/')
    print(str(item1) + '\n')

    items_list.print_all_items()

    # items_list.print_all_item_objects()
    # This takes a very long time to execute,
    # as it's first creating a list of all the Item objects,
    # then looping through and printing each object individually.
    # Use test.py to print all 1607 Item objects.


if __name__ == '__main__':
    main()

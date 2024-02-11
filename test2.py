def main():

    while True:
        choice = input("type letter a to e to choose the action. type q to quit. TYPE: ").lower()
        if choice == "a":
            first_letter_fish()
        elif choice == "b":
            three_letters_fish()
        elif choice == "c":
            longest_fish_name()
        elif choice == "d":
            more_than_one_word_fish()
        elif choice == "e":
            contains_cod()
        elif choice == "q":
            break


fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]


def first_letter_fish():
    for item in fish:
        print(item[0])


def three_letters_fish():
    for item in fish:
        print(item[0:3])


def longest_fish_name():
    longest = ""
    for item in fish:
        if len(item) > len(longest):
            longest = item
    print(longest)


def more_than_one_word_fish():
    for item in fish:
        if " " in item:
            print(item)


def contains_cod():
    contains_cod = [item for item in fish if 'cod' in item.lower()]
    if contains_cod:
        print(contains_cod)
    else:
        print("No fish contain cod")


main()

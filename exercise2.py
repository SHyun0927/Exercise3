fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

# print the first letter of each fish name on new lines
def first_letter_fish():
    for item in fish:
        print(fish[0])

# print the first 3 letters of each fish name on new lines
def three_leters_fish():    
    for item in fish:
        print(fish[0:3])

# print the longest fish name
def longest_fish_name():    
    longest = ""
    for item in fish:
        if len(fish) > len(longest):
            longest = fish
    print(longest)

# print out any fish name which is more than one word
def more_than_one_word_fish():   
    more_than_one_word_fish = []     
    for item in fish:
        if " " in fish:
            more_than_one_word_fish.append(item)
    print(more_than_one_word_fish)

# print out any fish name which contains the word cod

def contains_cod():
    contains_cod = []
    for item in fish:
        if 'cod' in item.lower():
            contains_cod.append(item)
    if contains_cod:
        print(contains_cod)
    else:
        print("No fish contain cod")

def main():
    input("type letter a to e to choose the action." 
          "type q to quit." 
            "TYPE: ")
    while True:
        choice = input().lower()
        if choice == "a":
            first_letter_fish()
        elif choice == "b":
            three_leters_fish()
        elif choice == "c":
            longest_fish_name()
        elif choice == "d":
            more_than_one_word_fish()
        elif choice == "e":
            contains_cod()
        elif choice == "q":
            break

main()
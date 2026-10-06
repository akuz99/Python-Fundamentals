deck_of_cards = input().split()
count_of_shuffles = int(input())



for current_shuffle in range(count_of_shuffles):
    middle = len(deck_of_cards) // 2
    left = deck_of_cards[:middle]
    right = deck_of_cards[middle:]
    deck_of_cards_shuffled = []
    for index in range (len(left)):
        deck_of_cards_shuffled.append(left[index])
        deck_of_cards_shuffled.append(right[index])

    deck_of_cards = deck_of_cards_shuffled

print(deck_of_cards)







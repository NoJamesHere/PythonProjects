import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 11 represents Ace

def calculate_hand_value(hand):
    total = sum(hand)
    # If total > 21 and there's an Ace counted as 11, count it as 1 instead
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10  # Count Ace as 1 instead of 11
        aces -= 1
    return total

def deal_card():
    return random.choice(cards)

def main():
    hand = []
    # Deal two cards initially
    hand.append(deal_card())
    hand.append(deal_card())
    
    while True:
        print(f"Your hand: {hand} (Total: {calculate_hand_value(hand)})")
        total = calculate_hand_value(hand)
        if total > 21:
            print("Busted! You went over 21.")
            break
        if total == 21:
            print("Blackjack! You win!")
            break
        choice = input("Do you want to hit (get another card) or stand? (hit/stand): ").strip().lower()
        if choice == 'hit':
            card = deal_card()
            hand.append(card)
            print(f"You got a {card}.")
        elif choice == 'stand':
            print(f"Final hand: {hand} (Total: {total})")
            break
        else:
            print("Please enter 'hit' or 'stand'.")
            
main()
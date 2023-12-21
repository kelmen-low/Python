import random

def drawCard():
    card = random.randint(1,11)
    return card

def dealerPlays(firstCard):
    cards = [firstCard, drawCard()]

    print(f"The dealer's cards are {cards[0]} & {cards[1]}")

    while sum(cards) < 21:

        if sum(cards) <= 16:
            input("The dealer draws (PRESS ENTER TO CONTINUE)")
            cards.append(drawCard())

            print(f"The dealer drew a {cards[-1]}")
            print(f"The dealer's total is {sum(cards)}\n")

            if sum(cards) > 21:
                print("The dealer busted!")
                break
            else:
                continue
        else:
            break

    print(f"The dealer's final score is {sum(cards)}\n")

    return sum(cards)


def playerPlays(cards, dealerCard):

    while sum(cards) < 21:

        print(f"The dealer's cards are: {dealerCard} & *")
        print(f"Your cards are {cards}")

        print(f"Your current total is: {sum(cards)}\n")
        hit = input("Would you like another? (y/n)") == "y"
        if hit:
            cards.append(drawCard())
        else:
            break

        if sum(cards) > 21:
            print("You busted!")
            break
        else:
            continue

    print(f"Your final score is {sum(cards)}\n")
    return sum(cards)


def calculateScore(playerTotal, dealerTotal):
    if playerTotal > 21 and dealerTotal > 21:
        print("It's a tie. You both busted.")
    elif playerTotal > 21:
        print("Dealer won. You busted.")
    elif dealerTotal > 21:
        print("You won. Dealer busted.")
    elif playerTotal > dealerTotal:
        print("You won. Your score is higher.")
    else:
        print("Dealer won. Their score is higher.")

def play():
    print("Welcome to the game of blackjack!")
    dealerCard1 = drawCard()

    playerCards = [drawCard(), drawCard()]

    playerTotal = playerPlays(playerCards, dealerCard1)

    input("The dealer will now play (PRESS ENTER TO CONTINUE)")

    dealerTotal = dealerPlays(dealerCard1)

    calculateScore(playerTotal, dealerTotal)


play()
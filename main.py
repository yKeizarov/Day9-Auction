# Auction
from data import auction_participants


def search_winner(participants: dict) -> str:
    """Search winner in auction"""
    names = list(participants.keys())
    participants_bet = list(participants.values())
    winner_bet = max(participants_bet)
    winner_name = names[participants_bet.index(winner_bet)]
    return f"WINNER ---> {winner_name} <--- WITH BET ---> ${winner_bet} <---"


def auction():
    pre_string = "### WELCOME TO AUCTION ###"
    print(f'{pre_string:>35}')
    trigger = True
    count = 1
    while trigger:
        name = input(f"PLEASE INTER {count} PARTICIPANTS:  ").lower()
        bit = float(input(f"PLEASE ENTER BIT {count} PARTICIPANTS:  "))
        new_participants = {name: bit}
        auction_participants.update(new_participants)

        # IN CASE SOMEONE WANTS TO RAISE THE RATE
        count += 1
        control_answer = input("WILL THERE BE MORE PARTICIPANTS? 1-YES, 2-NO, 3-IF SOMEONE WANTS TO RAISE THE RATE ")
        trigger_ca = True
        while trigger_ca:
            if control_answer == "1":
                trigger_ca = False
            elif control_answer == "2":
                trigger = False
                trigger_ca = False
            elif control_answer == "3":
                user_name = input("PLEASE INTER THE NAME WHO RAISE: ").lower()
                user_bit = float(input("PLEASE INTER NEW BIT: "))
                update_user_bit = {user_name: user_bit}
                auction_participants.update(update_user_bit)
                control_answer = input("WILL THERE BE MORE PARTICIPANTS? 1-YES, 2-NO, "
                                       "3-IF SOMEONE WANTS TO RAISE THE RATE ")
                continue
            else:
                print("INCORRECT ANSWER ")
                control_answer = input("WILL THERE BE MORE PARTICIPANTS? \n"
                                       "1-YES, 2-NO, 3-IF SOMEONE WANTS TO RAISE THE RATE ")

                continue
    return auction_participants


if __name__ == "__main__":
    auction_participants = auction()
    print(search_winner(auction_participants).upper())

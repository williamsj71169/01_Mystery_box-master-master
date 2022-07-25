from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # Main Panel GUI
        self.start_frame = Frame(parent)
        self.start_frame.grid()

        self.intro_label = Label(self.start_frame, text="Mystery Box Game",
                                 font="Arial 19 bold", padx=10, pady=10)
        self.intro_label.grid(row=0)

        self.push_me_button = Button(self.start_frame, text="Push Me",
                                     command=self.to_game)
        self.push_me_button.grid(row=1, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        # self.start_frame.destroy()

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialize variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, font="Arial 10",
                                        text="Please <enter> of click 'Open "
                                             "Boxes' button to revel the "
                                             "contents of the mystery boxes",
                                        wrap=300, justify=LEFT, padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"   # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Balance label (row 4)

        start_text = "Game Cost: ${} \n""\nHow much " \
                     "will you win?".format(stakes * 5)

        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", text=start_text,
                                   fg="green", wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=5, pady=10)

        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

    def reveal_boxes(self):
        # get the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier

            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier

            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += stakes_multiplier

            else:
                prize = "lead\n($0)"

            # make sure can't spend more money than you have
            if round_winnings >= current_balance:
                self.play_button.config(state=DISABLED)
                prize = "Noo"

            prizes.append(prize)

        # display prizes...

        self.prize1_label.config(text=prizes[0])
        self.prize2_label.config(text=prizes[1])
        self.prize3_label.config(text=prizes[2])

        # deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${} \nPayback: ${} \n" \
                            "Current Balance: ${}".format(5*stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)
        if current_balance + round_winnings <= 0:
            self.play_button.config(state=DISABLED)
            current_balance = 0
            balance_statement = "You have run out of money.\n" \
                                "Current Balance: ${}".format(current_balance)

        # Edit Label so user can see their balance
        self.balance_label.configure(text=balance_statement)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()

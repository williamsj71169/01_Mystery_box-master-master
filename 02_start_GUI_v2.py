# stuff

from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # giu to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # set initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                               "(between $5 and $50) in the box below. "
                                               "Then choose the stakes. The higher the "
                                               "stakes the more you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box, button and error label (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.entry_error_frame,
                                       font="Arial 14 bold",
                                       text="Add Funds",
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame ()row 3
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here  ***************
        button_font = "Arial 12 bold"

        # yellow low stakes button
        self.lowstakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="yellow")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # orange med stakes button
        self.medstakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="orange")
        self.medstakes_button.grid(row=0, column=1, padx=5, pady=10)

        # red high stakes button
        self.highstakes_button = Button(self.stakes_frame, text="High ($15)",
                                        command=lambda: self.to_game(3),
                                        font=button_font, bg="red")
        self.highstakes_button.grid(row=0, column=2, pady=10)

        # disable all stakes buttons at start
        self.lowstakes_button.config(state=DISABLED)
        self.medstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        # Help button
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=4, pady=10)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        self.lowstakes_button.config(state=DISABLED)
        self.medstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too High! The most you can risk in this game is $50"

            elif starting_balance >= 15:
                # enable all buttons
                self.lowstakes_button.config(state=NORMAL)
                self.medstakes_button.config(state=NORMAL)
                self.highstakes_button.config(state=NORMAL)

            elif starting_balance >= 10:
                # enable low and medium stakes buttons
                self.lowstakes_button.config(state=NORMAL)
                self.medstakes_button.config(state=NORMAL)

            else:
                self.lowstakes_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        # retrieve starting balance
        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialize variables
        self.balance = IntVar()

        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Balance label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="Gain",
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

    def reveal_boxes(self):
        # get the balance from the initial function...
        current_balance = self.balance.get()

        # Adjust the balance (subtract game cost and add pay out)
        # for testing purposes, just add 2
        current_balance += 2

        # Set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit Label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()

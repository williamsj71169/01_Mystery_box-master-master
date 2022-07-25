from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, partner):

        # Main Panel GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # heading
        self.intro_label = Label(self.start_frame, text="Mystery Box Game",
                                 font="Arial 19 bold", )
        self.intro_label.grid(row=1)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help",
                                  command=self.to_help)
        self.help_button.grid(row=2, pady=10)

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window
        self.help_box = Toplevel()

        # if user press cross at top closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # set up heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Choose and amount to play with and then choose the stakes." \
                    "Higher stakes cost more per round but you can win more as well.\n\n" \
                    "When you enter the play area, you will see three mystery boxes. To reveal" \
                    "the contents of the boxes, click the 'Open Boxes' button. If you don't have " \
                    "enough money to play, the button will turn red and you need to quit the game.\n\n" \
                    "The contents of the boxes will be added to your balance. The boxes could contain...\n\n" \
                    "Low: Lead($0) | Copper ($1) | Silver($2) | Gold ($10)\n" \
                    "Medium: Lead($0) | Copper ($2) | Silver($4) | Gold ($25)\n" \
                    "High: Lead($0) | Copper ($5) | Silver($10) | Gold ($50)\n\n" \

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold")
        self.dismiss_btn.grid(row=3, pady=10)

    def close_help(self, partner):
        # put calc history button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()

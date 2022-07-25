from tkinter import *
from functools import partial  # to prevent unwanted windows
import random

# heading, date/time?


if __name__ == '__main__':
    class Mystery:
        def __init__(self):

            # formatting variables
            background_colour = "light grey"

            # initialise list to hold game stats
            self.all_calc_list = []

            # mystery Frame
            self.mystery_frame = Frame(bg=background_colour, pady=10)
            self.mystery_frame.grid()

            # temperature mystery heading (row 0)
            self.temp_heading_label = Label(self.mystery_frame, text="Mystery Box Game", font="Arial 19 bold",
                                            bg=background_colour, padx=10, pady=10)
            self.temp_heading_label.grid(row=0)

            # user instructions (row 1)
            self.temp_instructions_label = Label(self.mystery_frame,
                                                 text="enter money amount",
                                                 font="Arial 10 italic", wrap=290, justify=LEFT,
                                                 bg=background_colour, padx=10, pady=10)
            self.temp_instructions_label.grid(row=1)

            # temperature entry box (row 2)
            self.to_convert_entry = Entry(self.mystery_frame, width=20, font="Arial 14 bold")
            self.to_convert_entry.grid(row=2)

            # stakes buttons frame (row 3)
            self.stakes_buttons_frame = Frame(self.mystery_frame)
            self.stakes_buttons_frame.grid(row=3, pady=10)

            self.low_button = Button(self.stakes_buttons_frame,
                                     text="Low($5)", font="Arial 10 bold",
                                     bg="yellow", padx=10, pady=10, command=self.low)
            self.low_button.grid(row=0, column=0)

            self.medium_button = Button(self.stakes_buttons_frame,
                                        text="Medium($10)", font="Arial 10 bold",
                                        bg="orange", padx=10, pady=10)
            self.medium_button.grid(row=0, column=1)

            self.high_button = Button(self.stakes_buttons_frame,
                                      text="High($15)", font="Arial 10 bold",
                                      bg="red", padx=10, pady=10)
            self.high_button.grid(row=0, column=2)

            # stats / help button frame (row 5)
            self.hist_help_frame = Frame(self.mystery_frame)
            self.hist_help_frame.grid(row=4, pady=10)

            self.calc_stats_button = Button(self.hist_help_frame, text="Game Stats",
                                            font=("Arial", "14"), width=10,
                                            command=lambda: self.stats(self.all_calc_list))
            self.calc_stats_button.grid(row=0, column=0)

            if len(self.all_calc_list) == 0:
                self.calc_stats_button.config(state=DISABLED)

            self.help_button = Button(self.hist_help_frame, text="Help / Rules",
                                      font=("Arial 12 bold"), width=10, pady=4,
                                      command=self.help)
            self.help_button.grid(row=0, column=1)

        def round_it(self, to_round):
            if to_round % 1 == 0:
                rounded = int(to_round)
            else:
                rounded = round(to_round, 1)

            return rounded

        def stats(self, calc_stats):
            Stats(self, calc_stats)

        def help(self):
            print("You asked for help")
            get_help = Help(self)
            get_help.help_text.configure(text="Please enter a number into the box and then push one of the buttons"
                                              " to convert the number to either degrees C or degrees F.\n\n"
                                              "The Game Stats area shows up to seven past games"
                                              " (most recent at the top). \n\nYou can also export your full game"
                                              "stats to a text file if you want to.")

        def low(self):
            print("You clicked low")
            in_low_button = Low(self)
            in_low_button.low_text.configure(text="info")


class Low:
    def __init__(self, partner):

        background = "yellow"  # pale green/orange?

        # disable calc stats button
        partner.calc_stats_button.config(state=DISABLED)

        # sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # if users pres cross at top, closes stats and 'releases' calc stats button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up GUI frame
        self.stats_frame = Frame(self.stats_box, width=300, bg=background)
        self.stats_frame.grid()

        # set ip Stats heading (row 0)
        self.how_heading = Label(self.stats_frame, text="Play: Low($5)",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # stats text (label, row 1)
        # help text (label, row 1)
        self.low_text = Label(self.stats_frame, text="",
                              justify=LEFT, width=40, bg=background, wrap=250)
        self.low_text.grid(row=1)

        # stats output goes here (row 2)

        # Generate string from list of games
        stats_string = ""

        # label to display game stats to user
        self.calc_label = Label(self.stats_frame, text=stats_string, bg=background,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export / dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_stats(self, partner):
        # put calc stats button back to normal
        partner.calc_stats_button.config(state=NORMAL)
        self.stats_box.destroy()


class Stats:
    def __init__(self, partner, calc_stats):

        background = "#a9ef99"  # pale green/orange?

        # disable calc stats button
        partner.calc_stats_button.config(state=DISABLED)

        # sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # if users pres cross at top, closes stats and 'releases' calc stats button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up GUI frame
        self.stats_frame = Frame(self.stats_box, width=300, bg=background)
        self.stats_frame.grid()

        # set ip Stats heading (row 0)
        self.how_heading = Label(self.stats_frame, text="Game Stats",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # stats text (label, row 1)
        self.stats_text = Label(self.stats_frame,
                                text="Here are your most recent games, "
                                     "Please ues the export button to create "
                                     "a text file of all your games for "
                                     "this session", wrap=250,
                                font="arial 10 italic", fg="maroon",
                                justify=LEFT, width=40, bg=background,
                                padx=10, pady=10)
        self.stats_text.grid(row=1)

        # stats output goes here (row 2)

        # Generate string from list of games
        stats_string = ""

        if len(calc_stats) >= 7:
            for item in range(0, 7):
                stats_string += calc_stats[len(calc_stats)
                                           - item - 1] + "\n"

        else:
            for item in calc_stats:
                stats_string += calc_stats[len(calc_stats) -
                                           calc_stats.index(item) - 1] + "\n"
                self.stats_text.config(text="Here is your game stats."
                                            "You can use the export button to save "
                                            "this data to a text file if you want.")

        # label to display game stats to user
        self.calc_label = Label(self.stats_frame, text=stats_string, bg=background,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export / dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_stats))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_stats(self, partner):
        # put calc stats button back to normal
        partner.calc_stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, calc_stats):
        Export(self, calc_stats)


class Export:
    def __init__(self, partner, calc_stats):

        print(calc_stats)

        background = "#a9ef99"  # pale green

        # disabled export button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # if user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # export instructions
        self.export_text = Label(self.export_frame, justify=LEFT, width=40, bg=background,
                                 wrap=250, text="Enter a filename in the box below and press"
                                                "the Save button to save your game"
                                                "stats to a text file.")
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, "
                                                         "its content will be replaced with your game stats",
                                 justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / cancel frame (row4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_stats(partner, calc_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_stats(self, partner, calc_stats):

        # Regular expressions to check filename is valid
        valid_char = '[A-Za-z0-9_]'
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # if there ar eno errors, generate text file and then close
            # dialogue and add .txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_stats:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if users pres cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set ip Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Mystery()
    root.mainloop()

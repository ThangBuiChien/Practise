import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog
import random
from PIL import Image, ImageTk

import main

### Global Variables to store the solution analytics ###
algorithm = "BFS"
initialState = "012345678"
statepointer = cost = counter = depth = 0
runtime = 0.0
path = []
input_image = Image.open("Pokemon.jpg")
num_to_pieces = None
pieces_to_num = None


class ConnectDotsGame:
    # Rest of your code remains unchanged, you just need to modify the following methods:

    def enterInitialState(self, event=None):
        """
        Invoked at pressing enter initial state button. Randomly places dots on the grid.
        """
        global initialState, statepointer

        # Create a list of numbers from 0 to 8
        numbers = list(range(9))

        # Shuffle the list to randomize the order
        random.shuffle(numbers)

        # Convert the shuffled list to a string
        initial_state = "".join(map(str, numbers))

        # Set the initial state
        initialState = initial_state

        # Reset and display the generated initial state
        self.reset()
        app.displayStateOnGrid(initialState)

    def solve(self, event=None):
        """
        Function is invoked at pressing the solve button. Solves the puzzle with the given initialState and algorithm
        then gives a suitable response to the user
        """
        global algorithm, initialState
        app.gif_loading.place(x=600, y=125, anchor="s")
        if self.readyToSolve():
            msg = (
                "Algorithm: "
                + str(algorithm)
                + "\nInitial State = "
                + str(initialState)
            )
            messagebox.showinfo("Confirm", msg)
            self.resetGrid()
            self.solveState()
            if len(path) == 0:
                messagebox.showinfo(
                    "Unsolvable!", "The state you entered is unsolvable"
                )
                self.displaySearchAnalysis(True)
            else:
                self.refreshFrame()
        else:
            solvingerror = (
                "Cannot solve.\n"
                "Algorithm in use: " + str(algorithm) + "\n"
                "Initial State   : " + str(initialState)
            )
            messagebox.showerror("Cannot Solve", solvingerror)
        app.gif_loading.place_forget()

    def fromPiecestoNum(pieces):
        # This method converts the pieces to a string of numbers
        result = ""
        for piece in pieces:
            if piece in pieces_to_num:
                result += str(pieces_to_num[piece])
            else:
                result += " "
        return result

    def fromNumtoPieces(self, number):
        # This method converts a string of numbers to a list of images
        result = []
        number_str = str(number)

        # Split the string into individual digits
        individual_digits = [int(digit) for digit in number_str]
        for numbers in individual_digits:
            if numbers in num_to_pieces:
                result.append(num_to_pieces[numbers])
            else:
                result.append(None)
        return result


if __name__ == "__main__":
    global app
    root = tk.Tk()
    root.title("Connect the Dots Game")
    app = ConnectDotsGame(root)
    app.run()

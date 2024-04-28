import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    # Add letters if use_letters is True
    if use_letters:
        characters += string.ascii_letters
    # Add numbers if use_numbers is True
    if use_numbers:
        characters += string.digits
    # Add symbols if use_symbols is True
    if use_symbols:
        characters += string.punctuation

    # Show an error message if no character type is selected
    if not characters:
        messagebox.showerror("Error", "Please choose at least one character type.")
        return None

    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Function to get a password when the button is clicked
    def get_password():
        # Get the input values
        length = length_entry.get()
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        # Show an error message if the length is not a valid number
        if not length.isdigit():
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
            return

        # Generate a password
        password = generate_password(int(length), use_letters, use_numbers, use_symbols)
        # Update the password entry with the generated password
        if password:
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)

    # Create a new window
    root = tk.Tk()
    # Set the window size and position
    root.geometry("500x500+100+100")
    root.title("Password Generator by Mubashar Ghazi")

    # Create and pack the widgets
    length_label = tk.Label(root, text="Enter the length of the password: ", font=("Helvetica", 14))
    length_label.pack()

    length_entry = tk.Entry(root, font=("Helvetica", 14))
    length_entry.pack()

    letters_var = tk.BooleanVar(value=True)
    letters_check = tk.Checkbutton(root, text="Include letters?", variable=letters_var, font=("Helvetica", 14))
    letters_check.pack()

    numbers_var = tk.BooleanVar(value=True)
    numbers_check = tk.Checkbutton(root, text="Include numbers?", variable=numbers_var, font=("Helvetica", 14))
    numbers_check.pack()

    symbols_var = tk.BooleanVar(value=True)
    symbols_check = tk.Checkbutton(root, text="Include symbols?", variable=symbols_var, font=("Helvetica", 14))
    symbols_check.pack()

    generate_button = tk.Button(root, text="Generate Password", command=get_password, font=("Helvetica", 14))
    generate_button.pack()

    password_entry = tk.Entry(root, font=("Helvetica", 14))
    password_entry.pack()

    # Start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()
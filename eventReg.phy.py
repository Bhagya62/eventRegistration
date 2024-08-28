import tkinter as tk
from tkinter import messagebox


def save_registration():
    # Get input values from entry fields
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    event = entry_event.get()

    # Check if all fields are filled
    if name and email and phone and event:
        with open("registrations.txt", "a") as file:
            file.write(f"{name},{email},{phone},{event}\n")
        messagebox.showinfo("Success", "Registration details saved successfully!")
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")


def clear_fields():
    # Clear all entry fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_event.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Event Registration Form")

# Create labels and entry widgets
tk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email Address").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=2, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Event").grid(row=3, column=0, padx=10, pady=5)
entry_event = tk.Entry(root, width=30)
entry_event.grid(row=3, column=1, padx=10, pady=5)

# Create Register button
register_button = tk.Button(root, text="Register", command=save_registration)
register_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()

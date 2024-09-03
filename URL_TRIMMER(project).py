import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    long_url = url_entry.get()
    if long_url:
        s = pyshorteners.Shortener()
        try:
            short_url = s.tinyurl.short(long_url)
            result_label.config(text="Shortened URL: " + short_url)
            copy_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL")

def copy_to_clipboard():
    short_url = result_label.cget("text").replace("Shortened URL: ", "")
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)


# Set up the main application window
root = tk.Tk()
root.title("URL Shortener")

# URL entry label and field
url_label = tk.Label(root, text="Enter long URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Shorten button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Result label to display the shortened URL
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

# Run the application
root.mainloop()

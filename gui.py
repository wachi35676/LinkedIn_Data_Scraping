import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from main import main


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LinkedIn Data Scraper")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Select a CSV file containing LinkedIn usernames:")
        self.label.pack(pady=10)

        self.file_path = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.file_path, width=40)
        self.entry.pack()

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Scraping", command=self.start_scraping)
        self.start_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.file_path.set(file_path)

    def start_scraping(self):
        file_path = self.file_path.get()
        if file_path:
            scrape_window = ScrapeWindow(self)
            scraping_thread = threading.Thread(target=scrape_window.scrape_data,
                                               args=(file_path, scrape_window.update_username, scrape_window.duplicate_username_warning))
            scraping_thread.start()
        else:
            self.label.config(text="Please select a CSV file first.")


class ScrapeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Scraping in Progress")
        self.geometry("400x250")
        self.resizable(False, False)

        self.progress_bar = ttk.Progressbar(self, mode='indeterminate')
        self.progress_bar.pack(pady=10)

        self.status_text = tk.Text(self, height=10, width=40)  # Create a Text widget
        self.status_text.pack(pady=10)

        self.progress_bar.start()

    def scrape_data(self, file_path, update_username_callback, duplicate_username_warning_callback):
        try:
            main(file_path, update_username_callback, duplicate_username_warning_callback)
            messagebox.showinfo("Success", "Data added to CSV file")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", str(e))
        finally:
            self.progress_bar.stop()
            self.destroy()

    def update_username(self, username):
        self.status_text.insert(tk.END, f"Scraping data for: {username}\n")  # Insert message to status_text
        self.status_text.see(tk.END)

    def duplicate_username_warning(self, username):
        self.status_text.insert(tk.END, f"Duplicate username found: {username}\n")  # Insert message to status_text
        self.status_text.see(tk.END)
        self.update()


if __name__ == "__main__":
    app = App()
    app.mainloop()

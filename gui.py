import tkinter as tk
from tkinter import filedialog
import threading
from main import main


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LinkedIn Data Scraper")
        self.geometry("400x200")

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
            scraping_thread = threading.Thread(target=self.scrape_data, args=(file_path,))
            scraping_thread.start()
        else:
            self.label.config(text="Please select a CSV file first.")

    def scrape_data(self, file_path):
        main(file_path)
        self.label.config(text="Data scraping completed successfully.")


if __name__ == "__main__":
    app = App()
    app.mainloop()

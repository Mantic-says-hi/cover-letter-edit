import tkinter as tk
import subprocess

class AutoResumeGUI:
    def __init__(self, master):
        self.master = master
        master.title("AutoResume")

        self.position_label = tk.Label(master, text="Position:")
        self.position_label.grid(row=0, column=0, sticky="w")
        self.position_entry = tk.Entry(master)
        self.position_entry.grid(row=0, column=1)

        self.company_label = tk.Label(master, text="Company:")
        self.company_label.grid(row=1, column=0, sticky="w")
        self.company_entry = tk.Entry(master)
        self.company_entry.grid(row=1, column=1)

        self.applicant_label = tk.Label(master, text="Applicant:")
        self.applicant_label.grid(row=2, column=0, sticky="w")
        self.applicant_entry = tk.Entry(master)
        self.applicant_entry.grid(row=2, column=1)

        self.street_label = tk.Label(master, text="Street:")
        self.street_label.grid(row=3, column=0, sticky="w")
        self.street_entry = tk.Entry(master)
        self.street_entry.grid(row=3, column=1)

        self.suburb_label = tk.Label(master, text="Suburb:")
        self.suburb_label.grid(row=4, column=0, sticky="w")
        self.suburb_entry = tk.Entry(master)
        self.suburb_entry.grid(row=4, column=1)

        self.submit_button = tk.Button(master, text="Generate Cover Letter", command=self.generate_cover_letter)
        self.submit_button.grid(row=5, columnspan=2)

    def generate_cover_letter(self):
        position = self.position_entry.get()
        company = self.company_entry.get()
        applicant = self.applicant_entry.get()
        street = self.street_entry.get()
        suburb = self.suburb_entry.get()

        command = f'python Code/auto_cover_letter.py "{position}" "{company}" "{applicant}" "{street}" "{suburb}"'
        subprocess.run(command, shell=True)

        self.position_entry.delete(0, 'end')
        self.company_entry.delete(0, 'end')
        self.applicant_entry.delete(0, 'end')
        self.street_entry.delete(0, 'end')
        self.suburb_entry.delete(0, 'end')

        

root = tk.Tk()
gui = AutoResumeGUI(root)
root.mainloop()
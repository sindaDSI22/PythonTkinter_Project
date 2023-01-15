import tkinter as tk
from tkinter import messagebox
from db import Database
from tkinter import *
from PIL import ImageTk, Image

db = Database('Employee.db')

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Employee')

        master.geometry("900x350")



        image1 = Image.open("bg.png")
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test


        label1.place(x=620, y= 90)

        self.create_widgets()

        self.selected_item = 0

        self.populate_list()



    def create_widgets(self):

        self.nom_text = tk.StringVar()
        self.nom_label = tk.Label(
            self.master, text='Nom et Prénom', font=('bold', 14), pady=20)
        self.nom_label.grid(row=0, column=0, sticky=tk.W)
        self.nom_entry = tk.Entry(self.master, textvariable=self.nom_text)
        self.nom_entry.grid(row=0, column=1)

        self.age_text = tk.StringVar()
        self.age_label = tk.Label(
            self.master, text='Age', font=('bold', 14))
        self.age_label.grid(row=0, column=2, sticky=tk.W)
        self.age_entry = tk.Entry(
            self.master, textvariable=self.age_text)
        self.age_entry.grid(row=0, column=3)

        self.post_text = tk.StringVar()
        self.post_label = tk.Label(
            self.master, text='Post', font=('bold', 14))
        self.post_label.grid(row=1, column=0, sticky=tk.W)
        self.post_entry = tk.Entry(
            self.master, textvariable=self.post_text)
        self.post_entry.grid(row=1, column=1)

        self.salaire_text = tk.StringVar()
        self.salaire_label = tk.Label(
            self.master, text='Salaire', font=('bold', 14))
        self.salaire_label.grid(row=1, column=2, sticky=tk.W)
        self.salaire_entry = tk.Entry(self.master, textvariable=self.salaire_text)
        self.salaire_entry.grid(row=1, column=3)


        self.employee_list = tk.Listbox(self.master, height=8, width=80, border=0,bg="pink",)
        self.employee_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6,  padx=25)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3,padx=5)

        self.employee_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_list.yview)


        self.employee_list.bind('<<ListboxSelect>>', self.select_item)


        self.add_btn = tk.Button(
            self.master, text="Ajouter Employee", width=17,bg="pink", command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=10,padx=10)

        self.remove_btn = tk.Button(
            self.master, text="Supprimer Employee", width=17,bg="pink", command=self.remove_item)
        self.remove_btn.grid(row=2, column=1,padx=10,pady=10)

        self.update_btn = tk.Button(
            self.master, text="Modifier Employee", width=17,bg="pink", command=self.update_item)
        self.update_btn.grid(row=2, pady=10,column=2, padx=10)

        self.exit_btn = tk.Button(
            self.master, text="Vider champs", width=17,bg="pink", command=self.clear_text)
        self.exit_btn.grid(row=2, pady=10,column=3,padx=10)







    def populate_list(self):
        self.employee_list.delete(0, tk.END)

        for row in db.fetch():
            # Insert into list
            self.employee_list.insert(tk.END, row)


    def add_item(self):
        if self.nom_text.get() == '' or self.age_text.get() == '' or self.post_text.get() == '' or self.salaire_text.get() == '':
            messagebox.showerror(
                "champ obligatoire")
            return
        print(self.nom_text.get())

        db.insert(self.nom_text.get(), self.age_text.get(),
                  self.post_text.get(), self.salaire_text.get())

        self.employee_list.delete(0, tk.END)

        self.employee_list.insert(tk.END, (self.nom_text.get(), self.age_text.get(
        ), self.post_text.get(), self.salaire_text.get()))
        self.clear_text()
        self.populate_list()


    def select_item(self, event):

        try:

            index = self.employee_list.curselection()[0]

            self.selected_item = self.employee_list.get(index)

            self.nom_entry.delete(0, tk.END)
            self.nom_entry.insert(tk.END, self.selected_item[1])
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(tk.END, self.selected_item[2])
            self.post_entry.delete(0, tk.END)
            self.post_entry.insert(tk.END, self.selected_item[3])
            self.salaire_entry.delete(0, tk.END)
            self.salaire_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass


    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()


    def update_item(self):
        db.update(self.selected_item[0], self.nom_text.get(
        ), self.age_text.get(), self.post_text.get(), self.salaire_text.get())
        self.populate_list()


    def clear_text(self):
        self.nom_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.post_entry.delete(0, tk.END)
        self.salaire_entry.delete(0, tk.END)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

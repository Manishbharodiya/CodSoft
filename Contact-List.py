import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")

        self.contacts = []

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.add_contact_frame = tk.Frame(self.notebook)
        self.view_contact_frame = tk.Frame(self.notebook)
        self.search_contact_frame = tk.Frame(self.notebook)
        self.update_contact_frame = tk.Frame(self.notebook)
        self.delete_contact_frame = tk.Frame(self.notebook)

        self.notebook.add(self.add_contact_frame, text="Add Contact")
        self.notebook.add(self.view_contact_frame, text="View Contacts")
        self.notebook.add(self.search_contact_frame, text="Search Contact")
        self.notebook.add(self.update_contact_frame, text="Update Contact")
        self.notebook.add(self.delete_contact_frame, text="Delete Contact")


        self.initialize_add_contact_frame()
        self.initialize_view_contact_frame()
        self.initialize_search_contact_frame()
        self.initialize_update_contact_frame()
        self.initialize_delete_contact_frame()

    def initialize_add_contact_frame(self):
        tk.Label(self.add_contact_frame, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.add_contact_frame, text="Phone:").grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self.add_contact_frame)
        self.phone_entry = tk.Entry(self.add_contact_frame)

        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        add_button = tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_contact)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def initialize_view_contact_frame(self):
        self.view_contact_text = tk.Text(self.view_contact_frame, height=10, width=40)
        self.view_contact_text.grid(row=0, column=0, padx=10, pady=10)

        refresh_button = tk.Button(self.view_contact_frame, text="Refresh", command=self.refresh_view_contacts)
        refresh_button.grid(row=1, column=0, pady=10)

    def initialize_search_contact_frame(self):
        tk.Label(self.search_contact_frame, text="Search Name:").grid(row=0, column=0, padx=10, pady=10)

        self.search_name_entry = tk.Entry(self.search_contact_frame)
        self.search_name_entry.grid(row=0, column=1, padx=10, pady=10)

        search_button = tk.Button(self.search_contact_frame, text="Search", command=self.search_contact)
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.search_result_label = tk.Label(self.search_contact_frame, text="")
        self.search_result_label.grid(row=2, column=0, columnspan=2)

    def initialize_update_contact_frame(self):
        tk.Label(self.update_contact_frame, text="Search Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.update_contact_frame, text="New Phone:").grid(row=1, column=0, padx=10, pady=10)

        self.update_search_name_entry = tk.Entry(self.update_contact_frame)
        self.update_new_phone_entry = tk.Entry(self.update_contact_frame)

        self.update_search_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.update_new_phone_entry.grid(row=1, column=1, padx=10, pady=10)

        update_button = tk.Button(self.update_contact_frame, text="Update Contact", command=self.update_contact)
        update_button.grid(row=2, column=0, columnspan=2, pady=10)

    def initialize_delete_contact_frame(self):
        tk.Label(self.delete_contact_frame, text="Delete Name:").grid(row=0, column=0, padx=10, pady=10)

        self.delete_name_entry = tk.Entry(self.delete_contact_frame)
        self.delete_name_entry.grid(row=0, column=1, padx=10, pady=10)

        delete_button = tk.Button(self.delete_contact_frame, text="Delete Contact", command=self.delete_contact)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = {"name": name, "phone": phone}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone.")

    def refresh_view_contacts(self):
        self.view_contact_text.delete(1.0, tk.END)
        for contact in self.contacts:
            self.view_contact_text.insert(tk.END, f"Name: {contact['name']}\nPhone: {contact['phone']}\n\n")

    def search_contact(self):
        search_name = self.search_name_entry.get()

        if search_name:
            found_contacts = [contact for contact in self.contacts if contact['name'].lower() == search_name.lower()]

            if found_contacts:
                self.search_result_label.config(text=f"Contact(s) found for '{search_name}':")
                self.view_contact_text.delete(1.0, tk.END)
                for contact in found_contacts:
                    self.view_contact_text.insert(tk.END, f"Name: {contact['name']}\nPhone: {contact['phone']}\n\n")
            else:
                self.search_result_label.config(text=f"No contact found for '{search_name}'.")
                self.view_contact_text.delete(1.0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a name for the search.")

    def update_contact(self):
        search_name = self.update_search_name_entry.get()
        new_phone = self.update_new_phone_entry.get()

        if search_name and new_phone:
            for contact in self.contacts:
                if contact['name'].lower() == search_name.lower():
                    contact['phone'] = new_phone
                    messagebox.showinfo("Success", "Contact updated successfully.")
                    break
            else:
                messagebox.showwarning("Warning", f"No contact found for '{search_name}'.")
        else:
            messagebox.showwarning("Warning", "Please enter both search name and new phone.")

    def delete_contact(self):
        delete_name = self.delete_name_entry.get()

        if delete_name:
            for contact in self.contacts:
                if contact['name'].lower() == delete_name.lower():
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                    break
            else:
                messagebox.showwarning("Warning", f"No contact found")
        else:
            messagebox.showwarning("Warning", "Please enter a name for deletion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from chat import responding
from database import add_entry , delete_data , update_data , get_data , alldata
from proccessing import is_convertible_to_string


# Create the main window
app = tb.Window(themename="superhero")
app.title("Dynamic Tree Manager")
app.geometry("800x600")

# --- Input Frame (Top) ---
input_frame = tb.Frame(app)
input_frame.pack(pady=10)

# Text Input Field
text_label = tb.Label(input_frame, text="what did you eat:")
text_label.pack(side=LEFT, padx=5)

text_entry = tb.Entry(input_frame, width=15)
text_entry.pack(side=LEFT, padx=5)

# Date Input Field
date_label = tb.Label(input_frame, text="Date:")
date_label.pack(side=LEFT, padx=5)

date_entry = tb.Entry(input_frame, width=15)
date_entry.pack(side=LEFT, padx=5)

# Function to add new data

# --- Tree View ---
tree = tb.Treeview(app, columns=("Size", "Modified"), show="headings")
tree.heading("Size", text="Date")
tree.heading("Modified", text="Chalories")
tree.pack(padx=20, pady=10, fill=BOTH, expand=True)




#functions to add data
def refresh_tree(tree):
    # Clear existing tree data
    for row in tree.get_children():
        tree.delete(row)

    # Fetch data from database
    data_list = alldata()

    # Insert data into Treeview
    for row in data_list:
        tree.insert("", "end", values=row)

#to database
def add_data_to_database(date, data):
    if is_convertible_to_string(data):
        x = float(responding(data))
        return add_entry(date, x)  # <- directly return the success status
    else:
        return False

    
#adding
def add_item(tree):
    text = text_entry.get()
    date = date_entry.get()

    if text and date:
        result = add_data_to_database(date, text)
        if result:
            refresh_tree(tree)
            text_entry.delete(0, END)
            date_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Invalid input or failed to insert data.")
    else:
        messagebox.showwarning("Warning", "Please fill both fields!")


# Add Button
add_btn = tb.Button(input_frame, text="➕ Add", bootstyle="success", command= lambda: add_item(tree))
add_btn.pack(side=LEFT, padx=5)


#delete records
def delete_selected_record(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("⚠️ No item selected for deletion.")
        return

    # Get values from selected item
    values = tree.item(selected_item)['values']
    if not values:
        messagebox.showwarning("⚠️ Selected item has no data.")
        return

    date_to_delete = values[0]  # Assuming 'entry_date' is the second column

    # Delete from database
    if delete_data(date_to_delete):
        # If successful, remove from Treeview too
        tree.delete(selected_item)
        messagebox.showwarning(f"🗑️ Deleted record with date: {date_to_delete} from both DB and Treeview.")
    else:
        messagebox.showwarning("⚠️ Failed to delete from database. Check if the date exists.")



# Delete Button (Below Tree)
delete_btn = tb.Button(app, text="❌ Delete Selected", bootstyle="danger", command= lambda: delete_selected_record(tree))
delete_btn.pack(pady=10)


refresh_tree(tree)




# Run the app
app.mainloop()




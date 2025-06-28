import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:8000/api/appointments/"

def open_add_appointment_window():
    add_window = tk.Toplevel()
    add_window.title("Add appointment")
    add_window.geometry("400x350")

    tk.Label(add_window, text="Pet owner").pack()
    pet_owner_entry = tk.Entry(add_window)
    pet_owner_entry.pack()

    tk.Label(add_window, text="Pet type").pack()
    pet_type_entry = tk.Entry(add_window)
    pet_type_entry.pack()

    tk.Label(add_window, text="Date and time").pack()
    date_time_entry = tk.Entry(add_window)
    date_time_entry.pack()

    tk.Label(add_window, text="Location").pack()
    location_entry = tk.Entry(add_window)
    location_entry.pack()

    tk.Label(add_window, text="Van ID (optional)").pack()
    van_entry = tk.Entry(add_window)
    van_entry.pack()

    def save_appointment():
        data = {
            "pet_owner": pet_owner_entry.get(),
            "pet_type": pet_type_entry.get(),
            "appointment_time": date_time_entry.get(),
            "location": location_entry.get(),
            "van": van_entry.get(),
        }
        if not all([data["pet_owner"], data["pet_type"], data["appointment_time"], data["location"]]):
            messagebox.showwarning("Incomplete Form", "Please fill all required fields before saving.")
            return
        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Appointment Saved!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", f"Failed to save appointment.\n{response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server:\n{e}")

    tk.Button(add_window, text="Save", command=save_appointment).pack(pady=10)

def open_view_schedule_window():
    view_window = tk.Toplevel()
    view_window.title("View Schedule")
    view_window.geometry("600x400")

    listbox = tk.Listbox(view_window, width=80)
    listbox.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            appointments = response.json()
            for app in appointments:
                display = f"{app['appointment_time']} | {app['pet_owner']} | {app['pet_type']} | {app['location']} | {app.get('van', '')}"
                listbox.insert(tk.END, display)
        else:
            messagebox.showerror("Error", "Failed to fetch appointments.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to server:\n{e}")

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Main Dashboard")
    dashboard.geometry("300x200")

    tk.Button(dashboard, text="Add appointment", command=open_add_appointment_window).pack(pady=10)
    tk.Button(dashboard, text="View schedule", command=open_view_schedule_window).pack(pady=10)

    dashboard.mainloop()

def handle_login():
    if username_entry.get() == "Pethugs@10" and password_entry.get() == "Brute@2020":
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Pet Grooming Login")
root.geometry("300x150")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=handle_login).pack(pady=10)

root.mainloop()
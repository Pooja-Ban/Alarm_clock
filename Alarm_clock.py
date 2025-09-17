import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound  # For beep sound (Windows only)

# List to store triggered alarms
triggered_alarms = []

# Function to check if it's time to trigger the alarm
def check_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current system time (HH:MM:SS)
    alarm_time = time_entry.get()  # Get the time entered by the user
    alarm_caption = caption_entry.get()  # Get the custom caption entered by the user
    
    if alarm_time == current_time:
        # Play beep sound three times
        for _ in range(3):
            winsound.Beep(1000, 500)  # frequency, duration in ms
            time.sleep(0.2)  # Short delay between beeps
            
        # Show popup with custom caption that stays open until user closes it
        messagebox.showinfo("⏰ Alarm Triggered", f"{alarm_caption}\nTime: {alarm_time}")
        
        # Add alarm to list and clear info after it triggers
        triggered_alarms.append(f"Alarm Set at {alarm_time} - {alarm_caption}")
        clear_alarm_info()

    # Schedule the function to check the alarm again after 1 second
    root.after(1000, check_alarm)

# Function to start checking alarm
def start_alarm_check():
    alarm_time = time_entry.get()
    if not is_valid_time(alarm_time):
        messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM:SS format.")
        return

    # Check if the entered time is in the future
    if is_past_time(alarm_time):
        messagebox.showerror("Invalid Time", "You cannot set an alarm for a past time.")
        return
    
    # Start the alarm check (it will run periodically every second)
    check_alarm()

# Function to clear alarm input fields
def clear_alarm_info():
    time_entry.delete(0, tk.END)
    caption_entry.delete(0, tk.END)

# Function to validate time format (HH:MM:SS)
def is_valid_time(time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        return True
    except ValueError:
        return False

# Function to check if the entered time is in the past
def is_past_time(alarm_time):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return alarm_time < current_time

# GUI setup
root = tk.Tk()
root.title("⏰ Alarm Clock")

# Set the window size and background color
root.geometry("400x350")
root.configure(bg='#f7f7f7')

# Add an attractive title label
title_label = tk.Label(root, text="Alarm Clock", font=("Arial", 24, "bold"), bg='#f7f7f7', fg='#5c5c5c')
title_label.pack(pady=20)

# Instructions label for time entry
label = tk.Label(root, text="Enter alarm time (HH:MM:SS):", font=("Arial", 12), bg='#f7f7f7', fg='#333')
label.pack()

# Time entry field (HH:MM:SS format)
time_entry = tk.Entry(root, font=("Arial", 14), width=15, justify="center")
time_entry.pack(pady=10)

# Instructions label for caption entry
caption_label = tk.Label(root, text="Enter custom caption for alarm:", font=("Arial", 12), bg='#f7f7f7', fg='#333')
caption_label.pack()

# Caption entry field
caption_entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
caption_entry.pack(pady=10)

# Set alarm button with an attractive style
set_button = tk.Button(root, text="Set Alarm", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=start_alarm_check)
set_button.pack(pady=20)

# Run the mainloop for the GUI
root.mainloop() 



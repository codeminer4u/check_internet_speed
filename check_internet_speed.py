import speedtest
from tkinter import Tk, Button, Label, messagebox, DISABLED, NORMAL
from threading import Thread  
# Add import statement for Thread class
# Create the main window
root = Tk()
# Set window properties
root.geometry("320x350")
root.resizable(True, True)
root.title("Internet Speed Test")
root.config(bg="#E6E6FA")
# Define btn as a global variable
btn = None

# Function to check internet speed
def check():
    global btn 
    btn.config(text="Please wait...", state=DISABLED)
    root.update()
    def run_speed_test():
        try:
            speedtester = speedtest.Speedtest()
            speedtester.get_servers()
            download_speed = round(speedtester.download() / (10 ** 6), 3)
            upload_speed = round(speedtester.upload() / (10 ** 6), 3)  
        except Exception as e:
            messagebox.showerror("Error", f"Error checking internet speed: {e}")
            btn.config(text="Start Test", state=NORMAL) 
            return

        # Update speed labels on the main thread
        root.after(0, lambda: update_speed_labels(download_speed, upload_speed))

    thread = Thread(target=run_speed_test)
    thread.start()

# Function to update speed labels
def update_speed_labels(download_speed, upload_speed):
    download_speed_label.config(text=f"{download_speed} Mbps")
    upload_speed_label.config(text=f"{upload_speed} Mbps")
    btn.config(text="Start Test", state=NORMAL)  # Enable button and restore text

# Display program title
title_label = Label(
    root,
    text="Internet Speed Test",
    font=("Arial black, bold", 22),
    bg="#8B8386",
    fg="White",
    width=30,
)
title_label.pack(pady=10)

# Design and display labels for download and upload speeds
download_label = Label(root, text="Download Speed:", font=("Arial, bold", 15), bg="#E6E6FA")
download_label.place(x=10, y=80)

download_speed_label = Label(root, text="", font=("Arial, bold", 15), bg="#E6E6FA", fg="#089927")
download_speed_label.place(x=180, y=80)

upload_label = Label(root, text="Upload Speed:", font=("Arial, bold", 15), bg="#E6E6FA")
upload_label.place(x=10, y=130)

upload_speed_label = Label(root, text="", font=("Arial, bold", 15), bg="#E6E6FA", fg="#089927")
upload_speed_label.place(x=180, y=130)

# Create and configure the start test button
btn = Button(
    root,
    text="Start Test",
    font=("Arial, bold", 15),
    bd=5,
    bg="#8B8386",
    fg="White",
    activebackground="#8B8386",
    activeforeground="White",
    command=check,
    cursor="hand2",
)
btn.place(x=125, y=190)

# Run the Tkinter event loop
root.mainloop()

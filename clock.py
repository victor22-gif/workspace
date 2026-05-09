import sys
import tkinter as tk
import time 

def update_time():
    # get current time in 12 hours format AM/PM 
    current_time = time.strftime("%I:%M:%S:%p")
    
    # update the label text
    clock_label.config(text=current_time)
    
      # get current date
    current_date = time.strftime("%A, %B %d, %Y")
    
    # update the label text
    date_label.config(text=current_date)
    
    
    # call this function again after 1000 milliseconds (1 second)
    clock_label.after(1000, update_time)
    
    
# create the main wimdow
root = tk.Tk()
root.title("Python digital clock")
root.configure(bg="#1e1e1e") # dark background

# fetch mobile screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# force window to match fullscreen
root.geometry(f"{screen_width}x{screen_height}")

# remove window border
root.overrideredirect(True)

# set main container to keep elements well centered
main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(expand=True)


# create a label to display the time
clock_label = tk.Label(main_frame, font=("Arial", 40, "bold"), bg="#1e1e1e", fg="#00ffcc")

# center the label inside the window
clock_label.pack(pady=10)

# date content (adds context below the time)
date_label = tk.Label(main_frame, font=("Arial", 20, "normal"), bg="#1e1e1e", fg="#888888")

date_label.pack(pady=5)

# exit button
exit_button = tk.Button(root,text="exit clock",font=("Arial", 12), bg="#333333",fg="#ffffff", command=root.destroy, bd=0,padx=10,pady=5)

exit_button.pack(side="bottom", pady=40)

# start live update loop
update_time()

# run the application
root.mainloop()
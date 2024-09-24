import tkinter as tk
import os

def open_file(x):
    file_path = "test.json"
    if os.name == 'nt':
        os.startfile(file_path)
    # Method 2: For macOS and Linux
    else:
        subprocess.call(('open' if os.name == 'posix' else 'xdg-open', file_path))


# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Visualization of 3D Model of Biofilm")

# Define colors and font styles
bg_color = "#f0f0f0"
button_color = "#4CAF50"
button_text_color = "white"
label_color = "#333333"
font_style = ("Arial", 12)
heading_font_style = ("Arial", 14, "bold")

# Set the background color of the main window
root.configure(bg=bg_color)

# Create a frame for the radio buttons to group them together
options_frame = tk.Frame(root, bg=bg_color)
options_frame.pack(pady=10)

# Create a heading label for the radio buttons
heading_label = tk.Label(options_frame, text="Select Bacteria Type:", font=heading_font_style, bg=bg_color, fg=label_color)
heading_label.pack(anchor="w", padx=20)

# Options for radio buttons
options = ["Staphylococcus aureus", "Viridans streptococcus", "Klebsiella pneumoniae", "Escherichia coli"]
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set default option

# Create radio buttons
for option in options:
    radio_button = tk.Radiobutton(
        options_frame,
        text=option,
        variable=selected_option,
        value=option,
        font=font_style,
        bg=bg_color,
        fg=label_color,
        activebackground=bg_color,
        activeforeground=label_color,
        highlightthickness=0
    )
    radio_button.pack(anchor="w", padx=20, pady=5)

# Function to update label based on slider value
def update_label(value):
    od_label.config(text=f"Selected: {value}")

# Create a frame for the scale widget
scale_frame = tk.Frame(root, bg=bg_color)
scale_frame.pack(pady=10)

# Create a heading label for the scale
scale_heading_label = tk.Label(scale_frame, text="Adjust Optical Density:", font=heading_font_style, bg=bg_color, fg=label_color)
scale_heading_label.pack(anchor="w", padx=20)

# Create the scale widget
scale = tk.Scale(
    scale_frame,
    from_=0.5,
    to=2,
    orient="horizontal",
    length=200,
    tickinterval=0.5,
    resolution=0.01,
    command=update_label,
    bg=bg_color,
    fg=label_color,
    font=font_style
)
scale.pack(pady=10)

# Create a label to display the selected scale value
od_label = tk.Label(root, text="Selected: 0.5", font=font_style, bg=bg_color, fg=label_color)
od_label.pack()

# Function to show the text label with the link
def show_text_label():
    text_label.pack(pady = 10)
    link_label.pack(pady = 20)
    

# Create a submit button
submit_button = tk.Button(
    root,
    text="Submit",
    command=show_text_label,
    font=font_style,
    activebackground="#45a049",
    activeforeground=button_text_color
)
submit_button.pack(pady=20)

# Create a label for the link to the 3D model (hidden by default)
text_label = tk.Label(root, text = "Link to see the 3D model:", font = font_style, bg = bg_color, fg = label_color)
link_label = tk.Label(root, text = "Click here", fg = "blue", cursor = "hand2", font = font_style,)
link_label.bind("<Button-1>", open_file)


# Run the application
root.mainloop()

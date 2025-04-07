import tkinter as tk
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speaknow():
    text = textv.get()
    if text.strip():  # Check if the input is not empty
        engine.say(text)
        engine.runAndWait()

# Create the main window
root = tk.Tk()

textv = tk.StringVar()

obj = tk.LabelFrame(root, text="Text to Speech", font=("Arial", 14), bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lb1 = tk.Label(obj, text="Text", font=("Arial", 12))
lb1.pack(side=tk.LEFT, padx=5)

text = tk.Entry(obj, textvariable=textv, font=("Arial", 12), width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

btn = tk.Button(obj, text="Speak", font=("Arial", 12), bg="green", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry("480x200")
root.resizable(False, False)
root.mainloop()
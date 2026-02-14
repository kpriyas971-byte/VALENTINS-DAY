import tkinter as tk
import random

MAX_MOVES = 7
move_count = 0

# Main window
root = tk.Tk()
root.title("For Someone Special 🤍")
root.geometry("520x520")
root.config(bg="white")

# Title
question = tk.Label(root,
                    text="Will You Be My Valentine?",
                    font=("Georgia", 22, "bold"),
                    bg="white",
                    fg="#8B0000")
question.pack(pady=60)

subtext = tk.Label(root,
                   text="Choose wisely 🤍",
                   font=("Georgia", 12),
                   bg="white",
                   fg="gray")
subtext.pack()

# Frame
frame = tk.Frame(root, bg="white", width=400, height=300)
frame.pack(expand=True)
frame.pack_propagate(False)

# YES button
yes_button = tk.Button(frame,
                       text="Yes",
                       font=("Georgia", 14),
                       bg="#8B0000",
                       fg="white",
                       relief="flat",
                       padx=25, pady=8)

yes_button.place(x=100, y=150)

# NO button
no_button = tk.Button(frame,
                      text="No",
                      font=("Georgia", 14),
                      bg="gray",
                      fg="white",
                      relief="flat",
                      padx=25, pady=8)

no_button.place(x=240, y=150)

# Move YES button
def move_yes(event):
    global move_count
    if move_count < MAX_MOVES:
        move_count += 1
        x = random.randint(20, 300)
        y = random.randint(20, 200)
        yes_button.place(x=x, y=y)

        if move_count == MAX_MOVES:
            subtext.config(text="Alright… I’ll stop running now 🤍")

yes_button.bind("<Enter>", move_yes)

# Heart Confetti
def start_confetti():
    hearts = []  # reset hearts list

    canvas = tk.Canvas(root, width=520, height=520, bg="white", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    colors = ["#ff69b4", "#ff1493", "#8B0000", "#ffc0cb"]

    for _ in range(60):
        x = random.randint(0, 520)
        y = random.randint(-500, 0)
        size = random.randint(12, 18)
        color = random.choice(colors)

        heart = canvas.create_text(x, y, text="❤", font=("Arial", size), fill=color)
        speed = random.randint(2, 5)
        hearts.append((heart, speed))

    # Romantic Message (Wrapped properly)
    canvas.create_text(
        260, 260,
        text="You chose beautifully 🤍\n\n"
             "Happy Valentine's Day, my darling.\n\n"
             "You make my life brighter with your smile,\n"
             "your kindness, and the way you care for me.\n"
             "I'm so grateful to share these memories with you.\n\n"
             "I LOVEEEEEEE YOUUUU. 💕",
        font=("Georgia", 14),
        fill="#8B0000",
        width=420,      # ensures clean wrapping
        justify="center"
    )

    def animate():
        for heart, speed in hearts:
            canvas.move(heart, 0, speed)
            pos = canvas.coords(heart)
            if pos[1] > 520:
                canvas.move(heart, 0, -600)
        root.after(50, animate)

    animate()

# YES clicked
def accepted():
    for widget in root.winfo_children():
        widget.destroy()
    start_confetti()

# NO clicked
def rejected():
    subtext.config(text="Hmm… are you sure? 😌")

yes_button.config(command=accepted)
no_button.config(command=rejected)

root.mainloop()

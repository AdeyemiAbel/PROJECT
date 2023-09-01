import tkinter as tk

# Function to handle votes
def vote(feature):
    votes[feature] += 1
    update_display()

# Function to update the display with current vote counts
def update_display():
    for feature, count in votes.items():
        label_var[feature].set(f"{feature}: {count} votes")

# Create the main window
root = tk.Tk()
root.title("Featured Voting System")

# Initialize the votes dictionary
features = ["Feature A", "Feature B", "Feature C"]
votes = {feature: 0 for feature in features}

# Create labels and buttons for each feature
label_var = {}
for feature in features:
    label_var[feature] = tk.StringVar()
    label_var[feature].set(f"{feature}: 0 votes")

    label = tk.Label(root, textvariable=label_var[feature])
    label.pack()

    vote_button = tk.Button(root, text=f"Vote for {feature}", command=lambda f=feature: vote(f))
    vote_button.pack()

# Start the Tkinter main loop
root.mainloop()

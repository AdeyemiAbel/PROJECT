# import tkinter as tk
# from tkinter import messagebox

# # Initialize the feature list (you can use a database for a real application)
# features = []

# # Function to add a feature
# def add_feature():
#     feature_name = feature_entry.get()
#     if feature_name:
#         features.append({"name": feature_name, "votes": 0})
#         update_listbox()
#         feature_entry.delete(0, tk.END)
#     else:
#         messagebox.showerror("Error", "Please enter a feature name.")

# # Function to upvote a feature
# def upvote_feature():
#     selected_index = feature_listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         features[index]["votes"] += 1
#         update_listbox()

# # Function to update the listbox with current feature data
# def update_listbox():
#     feature_listbox.delete(0, tk.END)
#     for feature in features:
#         feature_listbox.insert(tk.END, f"{feature['name']} - Votes: {feature['votes']}")

# # Create the main window
# root = tk.Tk()
# root.title("Feature Voting System")

# # Entry widget for adding a new feature
# feature_label = tk.Label(root, text="Enter a new feature:")
# feature_label.pack()
# feature_entry = tk.Entry(root)
# feature_entry.pack()

# # Button to add a feature
# add_button = tk.Button(root, text="Add Feature", command=add_feature)
# add_button.pack()

# # Listbox to display features
# feature_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
# feature_listbox.pack()

# # Button to upvote a feature
# upvote_button = tk.Button(root, text="Upvote Feature", command=upvote_feature)
# upvote_button.pack()

# # Update the listbox initially
# update_listbox()

# # Start the Tkinter main loop
# root.mainloop()

# import tkinter as tk

# class VotingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Featured Voting System")
        
#         self.options = ["Option 1", "Option 2", "Option 3"]
#         self.votes = {option: 0 for option in self.options}
        
#         self.create_widgets()

#     def create_widgets(self):
#         self.title_label = tk.Label(self.root, text="Vote for Your Favorite Option:")
#         self.title_label.pack()

#         self.option_labels = []
#         for option in self.options:
#             label = tk.Label(self.root, text=option)
#             label.pack()
#             self.option_labels.append(label)

#         self.vote_button = tk.Button(self.root, text="Vote", command=self.vote)
#         self.vote_button.pack()

#     def vote(self):
#         selected_option = self.options[0]  # Default to the first option
        
#         for i, option in enumerate(self.options):
#             if self.option_labels[i].cget("bg") == "green":
#                 selected_option = option
#                 break
        
#         self.votes[selected_option] += 1
#         self.update_labels()

#     def update_labels(self):
#         for i, option in enumerate(self.options):
#             self.option_labels[i].config(text=f"{option}: {self.votes[option]} votes")
#             self.option_labels[i].config(bg="white")  # Reset background color

#         selected_option = self.options[0]  # Default to the first option
#         max_votes = 0

#         for option, votes in self.votes.items():
#             if votes > max_votes:
#                 max_votes = votes
#                 selected_option = option

#         self.option_labels[self.options.index(selected_option)].config(bg="green")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VotingApp(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# # Sample list of features to vote for
# features = ["Feature 1", "Feature 2", "Feature 3", "Feature 4"]

# # Initialize votes dictionary with zero votes for each feature
# votes = {feature: 0 for feature in features}

# def vote(feature):
#     votes[feature] += 1
#     update_labels()

# def update_labels():
#     for i, feature in enumerate(features):
#         label_texts[i].set(f"{feature}: {votes[feature]} votes")

# # Create the main window
# root = tk.Tk()
# root.title("Feature Voting System")

# # Create labels and buttons for each feature
# label_texts = [tk.StringVar() for _ in features]
# for i, feature in enumerate(features):
#     label = tk.Label(root, textvariable=label_texts[i])
#     label.pack()
#     vote_button = tk.Button(root, text=f"Vote for {feature}", command=lambda f=feature: vote(f))
#     vote_button.pack()

# # Update the labels initially
# update_labels()

# # Start the Tkinter main loop
# root.mainloop()


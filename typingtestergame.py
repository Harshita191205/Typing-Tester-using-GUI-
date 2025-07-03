import time
import random
import datetime
import tkinter as tk
from tkinter import messagebox

# List of quotes to choose from
quotes = [
    {"text": "The quick brown fox jumps over the lazy dog The cat is sleeping on the couch. It is very lazy. The dog is barking outside. I need to take it for a walk.", "difficulty": "easy"},
    {"text": "Pack my box with five dozen liquor jugs The city is very crowded during rush hour. I hate driving in traffic. It takes me forever to get to work. I wish I could take the train instead. The weather is supposed to be nice this weekend.", "difficulty": "medium"},
    {"text": "How vexingly quick waltzing zebras jump The new policy has been met with widespread criticism from experts in the field. They argue that it will have devastating consequences for the economy. The government is refusing to back down, despite mounting pressure from opposition parties. The situation is becoming increasingly volatile. I'm not sure what the future holds, but I'm worried about the impact on my family.", "difficulty": "hard"},
    {"text": "Bright vixens jump; dozy fowl quack The new policy has been met with widespread criticism from experts in the field. They argue that it will have devastating consequences for the economy. The government is refusing to back down, despite mounting pressure from opposition parties. The situation is becoming increasingly volatile. I'm not sure what the future holds, but I'm worried about the impact on my family.", "difficulty": "hard"},
    {"text": "Quick wafting zephyrs vex bold Jim The new policy has been met with widespread criticism from experts in the field. They argue that it will have devastating consequences for the economy. The government is refusing to back down, despite mounting pressure from opposition parties. The situation is becoming increasingly volatile. I'm not sure what the future holds, but I'm worried about the impact on my family.", "difficulty": "hard"},
    {"text": "I'll be back The cat is sleeping on the couch. It is very lazy. The dog is barking outside. I need to take it for a walk.", "difficulty": "easy"},
    {"text": "May the force be with you. The cat is sleeping on the couch. It is very lazy. The dog is barking outside. I need to take it for a walk.","difficulty": "easy"},
    {"text": "I am your father. The city is very crowded during rush hour. I hate driving in traffic. It takes me forever to get to work. I wish I could take the train instead. The weather is supposed to be nice this weekend.","difficulty": "medium"},
    # Add more quotes here
]



# User profiles
users = {}

def create_profile(username):
    users[username] = {"quotes": {}, "favorite_quotes": []}

def get_profile(username):
    return users.get(username)

def save_profile(username, quote, elapsed_time, accuracy):
    profile = get_profile(username)
    if profile:
        if quote not in profile["quotes"]:
            profile["quotes"][quote] = {"best_time": elapsed_time, "best_accuracy": accuracy}
        else:
            if elapsed_time < profile["quotes"][quote]["best_time"] or accuracy > profile["quotes"][quote]["best_accuracy"]:
                profile["quotes"][quote]["best_time"] = elapsed_time
                profile["quotes"][quote]["best_accuracy"] = accuracy

def get_quote_of_the_day():
    today = datetime.date.today()
    quote_of_the_day = random.choice(quotes)
    return quote_of_the_day

def calculate_accuracy(quote, typed_quote):
    correct_chars = sum(1 for i, j in zip(quote, typed_quote) if i == j)
    accuracy = (correct_chars / len(quote)) * 100
    return accuracy

# GUI Functions
def create_profile_gui():
    username = profile_entry.get()
    if username:
        create_profile(username)
        messagebox.showinfo("Profile Created", f"Profile created for {username}!")
        profile_window.destroy()
    else:
        messagebox.showwarning("Input Error", "Please enter a username.")

def show_typing_test():
    global selected_quote, start_time, user_input, typing_window
    
    selected_quote = random.choice(quotes)
    start_time = time.time()
    
    typing_window = tk.Toplevel(root)
    typing_window.title("Typing Test")

    tk.Label(typing_window, text="Type this text:").pack(pady=10)
    tk.Label(typing_window, text=selected_quote["text"], wraplength=400, justify="center").pack(pady=10)
    
    user_input = tk.Text(typing_window, height=5, width=50)
    user_input.pack(pady=10)
    
    submit_button = tk.Button(typing_window, text="Submit", command=submit_typing_test)
    submit_button.pack(pady=10)

def submit_typing_test():
    end_time = time.time()
    elapsed_time = end_time - start_time
    typed_quote = user_input.get("1.0", "end-1c")
    accuracy = calculate_accuracy(selected_quote["text"], typed_quote)
    
    messagebox.showinfo("Results", f"Elapsed time: {elapsed_time:.2f} seconds\nAccuracy: {accuracy:.2f}%")
    
    typing_window.destroy()

def show_quote_of_the_day():
    quote = get_quote_of_the_day()
    messagebox.showinfo("Quote of the Day", f"{quote['text']} ({quote['difficulty']})")

def main_menu():
    global root, profile_entry, profile_window

    root = tk.Tk()
    root.title("Typing Tester")

    tk.Label(root, text="Typing Tester", font=("Arial", 16)).pack(pady=20)
    
    tk.Button(root, text="Create Profile", width=20, command=lambda: create_profile_screen()).pack(pady=5)
    tk.Button(root, text="Start Typing Test", width=20, command=show_typing_test).pack(pady=5)
    tk.Button(root, text="Quote of the Day", width=20, command=show_quote_of_the_day).pack(pady=5)
    tk.Button(root, text="Quit", width=20, command=root.quit).pack(pady=20)
    
    root.mainloop()

def create_profile_screen():
    global profile_entry, profile_window
    profile_window = tk.Toplevel(root)
    profile_window.title("Create Profile")
    
    tk.Label(profile_window, text="Enter Username:").pack(pady=10)
    profile_entry = tk.Entry(profile_window, width=30)
    profile_entry.pack(pady=10)
    tk.Button(profile_window, text="Create", command=create_profile_gui).pack(pady=10)

if __name__ == "__main__":
    main_menu()

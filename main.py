import tkinter as tk
import random
import time
from threading import Thread

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Positive Reinforcement Slot Machine")
        self.root.geometry("400x320")
        self.root.configure(bg="#FCE4EC")  # Vibrant background color

        # Track consecutive losses to avoid more than 5 in a row
        self.consecutive_losses = 0

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="#FCE4EC")
        self.main_frame.pack(pady=20)

        # Title Label
        self.title_label = tk.Label(
            self.main_frame,
            text="Positive Reinforcement\nSlot Machine",
            font=("Helvetica", 16, "bold"),
            fg="#880E4F",
            bg="#FCE4EC"
        )
        self.title_label.pack(pady=10)

        # Reel Frame
        self.reel_frame = tk.Frame(self.main_frame, bg="#FCE4EC")
        self.reel_frame.pack()

        # Create three labels for reels
        self.reel_labels = []
        for _ in range(3):
            label = tk.Label(
                self.reel_frame,
                text="?",
                font=("Helvetica", 24, "bold"),
                width=4,
                fg="#AD1457",
                bg="#F8BBD0",
                borderwidth=2,
                relief="groove"
            )
            label.pack(side="left", padx=5)
            self.reel_labels.append(label)

        # Spin Button - Visible and colorful by default
        self.spin_button = tk.Button(
            self.main_frame,
            text="SPIN",
            font=("Helvetica", 14, "bold"),
            fg="blue",
            bg="#D81B60",         # Default color
            activebackground="#EC407A"
        )
        # Instead of command=..., we bind a custom function that first animates, then spins
        self.spin_button.config(command=self.on_spin_button_click)
        self.spin_button.pack(pady=10)  # Ensures the button is visible

        # Message Label
        self.message_label = tk.Label(
            self.main_frame,
            text="",
            font=("Helvetica", 12, "italic"),
            fg="#880E4F",
            bg="#FCE4EC"
        )
        self.message_label.pack(pady=10)

    def on_spin_button_click(self):
        """Handle what happens when user clicks 'SPIN':
           1) Disable the button
           2) Animate the button text
           3) Start the spin in another thread
        """
        self.spin_button.config(state="disabled")
        self.animate_spin_button()

    def animate_spin_button(self):
        """
        A simple text/ color animation for the spin button using `after()`.
        We cycle through frames to simulate a short 'light show'.
        After the animation, we call `spin()`.
        """
        # Frames = (Text, Background Color)
        frames = [
            ("S",    "#EF5350"),  # red
            ("P",    "#AB47BC"),  # purple
            ("I",    "#5C6BC0"),  # indigo
            ("N",    "#26A69A"),  # teal
            ("SPIN", "#FFA726"),  # orange
            ("SPIN!", "#EC407A")  # pinkish
        ]

        def run_animation(index=0):
            if index < len(frames):
                text, color = frames[index]
                self.spin_button.config(text=text, bg=color)
                # Schedule next frame in 100 ms
                self.root.after(100, run_animation, index + 1)
            else:
                # Animation complete -> Start the actual spin logic in a thread
                spin_thread = Thread(target=self.spin)
                spin_thread.start()

        run_animation(0)

    def spin(self):
        """
        Perform the slot machine spin with short reel animation.
        Win/loss is random, BUT if the player has lost 5 times in a row,
        the next spin must be a forced win (so they never lose more than 5 times in a row).
        """
        self.message_label.config(text="")  # Clear previous message

        # Symbols that can appear on the reels
        symbols = ["❤", "★", "♣", "♦", "☀", "❀"]

        # Animate the reels briefly
        for _ in range(15):  # 15 iterations to simulate spinning
            for i in range(3):
                self.reel_labels[i].config(text=random.choice(symbols))
            time.sleep(0.1)
            self.root.update_idletasks()

        # If user has lost 5 times in a row, force a win
        force_win = (self.consecutive_losses >= 5)

        if force_win:
            # All reels match with the same random symbol
            winning_symbol = random.choice(symbols)
            results = [winning_symbol, winning_symbol, winning_symbol]
        else:
            # Otherwise, purely random results
            results = [random.choice(symbols) for _ in range(3)]

        # Show final results
        for i in range(3):
            self.reel_labels[i].config(text=results[i])

        # Check if it's a win (all reels match)
        if len(set(results)) == 1:
            self.display_positive_message()
            self.consecutive_losses = 0
        else:
            self.message_label.config(
                text="No match this time. Remember to take breaks!"
            )
            self.consecutive_losses += 1

        # Re-enable the spin button after a short delay
        self.root.after(150, self.reset_spin_button)

    def reset_spin_button(self):
        # Restore button text, color, and enable it again
        self.spin_button.config(
            text="SPIN",
            bg="#D81B60",
            state="normal"
        )

    def display_positive_message(self):
        """Display a supportive message to help curb gambling impulses."""
        # Sample messages (you can paste your 50+ if you like)
        positive_messages = [
            "Great job! Life has many rewards – keep your balance in everything you do!",
    "You’ve won, but remember: the best wins happen outside the casino!",
    "Fantastic spin! Taking breaks keeps gambling fun and healthy.",
    "You’re a winner today! Celebrate responsibly and treasure other parts of life!",
    "Awesome match! Tomorrow is another day full of fresh possibilities!",
    "Keep in mind: controlling gambling is your superpower – use it wisely!",
    "Amazing! You nailed it. Take a moment to savor healthy achievements, too!",
    "Victory! But also find happiness beyond the reels—your life is rich!",
    "Way to go! Every win is a reminder that fun comes in moderation.",
    "Congratulations! Let this success inspire you in the real world as well.",
    "Fantastic spin! Don’t forget to enjoy non-gambling adventures, too!",
    "Wow, you’re on a roll! Keep a healthy mindset as you play.",
    "Well done! Pursue your dreams both inside and outside the game!",
    "Great spin! Keep your spirit bright, and your gambling in check.",
    "Hooray! Life beyond the slot machine is calling—answer with enthusiasm!",
    "You did it! Reward yourself responsibly—there’s more to life than spinning.",
    "Triple match! Remember you’re in control—play wisely and stay happy.",
    "Jackpot! Let your success shine on other parts of your life, too!",
    "Brilliant! Keep your focus on balance for even greater achievements.",
    "High-five! Embrace the fun, then take a breather to enjoy other hobbies.",
    "You got it! Acknowledge this moment, but remember to pause and reflect.",
    "Incredible! Celebrate the win, but don’t forget tomorrow’s adventures!",
    "Amazing result! Consider this a cue to explore new joys in your day.",
    "Lucky you! Always pair your luck with good judgment and self-care.",
    "Boom! You’ve proven you can win—now relax and enjoy something else.",
    "Magnificent! Make sure to savor real-life moments just as much!",
    "You’re a winner! Remember, the real prize is a balanced approach to fun.",
    "Fantastic job! Keep that bright energy for your next healthy pursuit.",
    "Yes! The reels align, and so should your perspective on responsible play.",
    "Great work! Celebrate in moderation—there’s a world of fun out there.",
    "A perfect spin! Channel your winning energy into something meaningful.",
    "Brilliant match! Let this be a reminder to protect your well-being first.",
    "Way to spin! Enjoy this victory, then reconnect with life’s other joys.",
    "You’re shining today! It’s a beautiful day to step away and smile.",
    "Look at you go! Stay mindful and keep life’s priorities in check.",
    "Marvelous! Time to stretch, breathe, and remember what matters most.",
    "So lucky! But true fortune lies in how you value yourself beyond gambling.",
    "Stellar result! Let your gratitude shine brighter than the slot lights.",
    "Impressive! Keep aiming for goals that bring lasting happiness.",
    "You’ve won big! Stay grounded and share the joy with loved ones.",
    "Excellent spin! Treat yourself to a well-deserved break or new hobby.",
    "Hurrah! Use this success to remind yourself of healthy boundaries.",
    "You got this! A short pause can make the next win feel even sweeter.",
    "Gorgeous match! Remember the real jackpot: your mental well-being.",
    "You’re a champ! Never forget that balance is key in all games of life.",
    "Dazzling outcome! Keep the excitement in check and enjoy responsibly.",
    "Triumph! Rest, recharge, and be proud of all you do outside gambling.",
    "Sparkling win! Let this motivate you to embrace life’s other adventures.",
    "Congrats! Make time for the things that truly matter beyond the reels.",
    "Glorious spin! Let your spirit thrive without overindulging in gambling.",
    "Bravo! A little luck goes a long way—especially when kept in perspective.",
    "Top-notch match! Sometimes, the best reward is enjoying your free time."
        ]
        self.message_label.config(text=random.choice(positive_messages))

def main():
    root = tk.Tk()
    app = SlotMachine(root)
    root.mainloop()

if __name__ == "__main__":
    main()

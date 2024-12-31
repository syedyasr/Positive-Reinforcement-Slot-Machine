Positive Reinforcement Slot Machine

A fun, colorful slot machine game built in Python with Tkinter. When the player wins, they are rewarded with uplifting messages that encourage responsible behavior and help them maintain a healthy perspective on gambling. The game also ensures the player does not lose more than 5 consecutive times.

Features

Tkinter-Based GUI
A simple yet vibrant interface created with Python’s built-in GUI toolkit.
Randomized Slot Machine Results
Each spin is random, except for a forced win when the user has lost 5 times in a row to prevent long losing streaks.
Positive Reinforcement Messages
A set of 50 (or more) uplifting messages is displayed whenever the user wins, reminding them to stay balanced, take breaks, and enjoy life beyond gambling.
Animated Spin Button
The “SPIN” button includes a brief color/text animation before the reels start spinning, adding a fun effect to each spin.
Smooth Reel Animation
The reels simulate a “spinning” motion before settling on their final symbols.
Demo

Installation

Clone or Download the repository:
git clone https://github.com/<syedyasr>/positiveslotmachine.git
cd positiveslotmachine
Or download the ZIP from GitHub and extract it.
python3 -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
Install Dependencies
This project primarily uses Python’s standard libraries (Tkinter, time, threading, random). If you want to bundle it or run tests, you might install additional tools (e.g., PyInstaller). By default, though, no extra pip install steps are required.
Usage

Run the Application:
python3 main.py
Click “SPIN”:
The spin button will animate briefly.
The reels will spin (randomly) and then stop.
If you win, an uplifting message will appear.
If you lose 5 times consecutively, the 6th spin guarantees a win to avoid frustration.
Close the Window:
Exit anytime by closing the Tkinter window.
Customization

Symbols
Modify the list of symbols in the spin method (e.g., ["❤", "★", "♣", "♦", "☀", "❀"]) to use your own icons, emojis, or short words.
Positive Messages
Add or replace the messages in display_positive_message() to suit your style or to include hotlines, counseling information, or additional resources for gambling addiction.
Forced Win Frequency
Currently, the game forces a win if you lose 5 times in a row. If you want a different threshold, adjust self.consecutive_losses >= 5 inside the spin method.
Spin Button Animation
The animation sequence can be found in animate_spin_button(). Change the colors, timing, or text to create your own unique effect.
Contributing

Fork the repository on GitHub.
Create a new branch for your feature or fix:
git checkout -b feature/some-awesome-improvement
Commit your changes:
git commit -m "Describe your changes here"
Push to your branch:
git push origin feature/some-awesome-improvement
Open a Pull Request on GitHub.
License


This project is released under the MIT License.

Contact

Author: Yaser Syed
Feel free to reach out if you have any questions or suggestions for improving the game.

Enjoy responsibly and always remember that real life has countless joys beyond the reels!

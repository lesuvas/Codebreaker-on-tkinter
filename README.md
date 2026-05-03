# Code Breaker – Beginner Edition

A beginner-friendly desktop adaptation of the classic Mastermind/Code Breaker game, built with Python and Tkinter.

## How to Play

The computer generates a secret code made of 4 colored hearts (red, green, yellow, blue). Your goal is to guess the correct sequence in 6 tries or fewer.

After each guess you receive hints:
- **Black circle** – correct color in the correct position
- **White circle** – correct color but in the wrong position
- **Grey circle** – color not in the code at all

## Features

- 🎮 Simple point-and-click interface — click hearts to cycle through colors
- 📜 Previous guesses screen to review your attempts
- 🏆 Top 5 leaderboard with score tracking
- ℹ️ About and Rules screens
- 💾 Scores saved locally to `players.json`

## Installation

### Option 1 – Run the executable
Download and run `mix.exe` — no Python required.

### Option 2 – Run from source
1. Make sure Python 3 is installed
2. Install dependencies:
pip install pillow
3. Run the game:
python mix.py

## Scoring

Score is calculated as `7 - number of tries`. The fewer guesses you use, the higher your score.

## Made By

lesuvas — built in two weeks as a learning project.  
Main sources: skolo.lv, tkdocs.com, YouTube tutorials.

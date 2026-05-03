import tkinter as tk
from PIL import Image, ImageTk
import random
import json

# GLOBAL VARIABLES
mode = "spele"
prev = []
prev_hints = []
hearts = ["static/red_heart.png", "static/green_heart.png", "static/yellow_heart.png", "static/blue_heart.png"]
hints = ["static/black_c.png", "static/white_c.png", "static/grey_c.png"]
rule_labels = []
hint_labels = []
prev_labels = []
heart_labels = []
prev_frame_labels = []
top_labels = []
displayed_prev_labels = []
top5_labels = []
about_labels = []
tries = 0
hint = []

font = "Arial"

def start_clicked():
    global cmp, tries, mode
    mode = "spele"
    for lbl in displayed_prev_labels:
        lbl.destroy()
        displayed_prev_labels.clear()
    hearts_frame.grid(row=1, column=0)
    hints_frame.grid(row=2, column=0)
    states[:] = [0, 0, 0, 0]
    prev.clear()
    prev_hints.clear()
    heart_labels.clear()
    hint_labels.clear()
    start_hint = ["static/grey_c.png"] * 4
    start_button.grid_forget()
    rule_button.grid_forget()
    start_label.grid_forget()
    hdln_bgnr_lbl.grid_forget()
    empty_lbl.grid_forget()
    top5_btn.grid_forget()
    about_btn.grid_forget()
    cmp = comp_code()
    tries = 0
    for lbl in labels:
        lbl.destroy()
    labels.clear()
    spele_label.config(text="YOUR GUESS:")
    spele_label.grid(row=0, column=0, pady=15, columnspan=2, sticky="n")
    remain_label.config(text=f"Tries left: {6 - tries}")
    remain_label.grid(row=4, column=0, columnspan=2)
    submit_button.grid(row=1, column=4, sticky="e", pady=10)
    prev_button.grid(row=5, column=0, pady=10, columnspan=2)
    for i, hint_img in enumerate(start_hint):
        img = Image.open(hint_img).resize((30,30))
        tk_img = ImageTk.PhotoImage(img)
        hint_label = tk.Label(hints_frame, image=tk_img)
        hint_label.image = tk_img
        hint_labels.append(hint_label)
        hint_label.grid(row=3, column=i, padx=5)
    for i in range(4):
        img = heart_image(i)
        lbl = tk.Label(hearts_frame, image=img)
        lbl.image = img
        lbl.grid(row=1, column=i, padx=5)
        heart_labels.append(lbl)
        lbl.bind("<Button-1>", lambda e, i=i: click(i))
        labels.append(lbl)

def back_to_game():
    for lbl in displayed_prev_labels:
        lbl.destroy()
    displayed_prev_labels.clear()
    hearts_frame.grid(row=1, column=0)
    hints_frame.grid(row=2, column=0)
    spele_label.grid(row=0, column=0, pady=10, columnspan=2, sticky="n")
    remain_label.grid(row=4, column=0, pady=10, columnspan=2)
    if mode == "spele":
        submit_button.grid(row=1, column=4, pady=10)
    prev_button.grid(row=5, column=0, pady=10, columnspan=2)
    for lbl in hint_labels:
        lbl.grid()
    for lbl in heart_labels:
        lbl.grid()

def rule_clicked():
    start_button.grid_forget()
    rule_button.grid_forget()
    start_label.grid_forget()
    hdln_bgnr_lbl.grid_forget()
    empty_lbl.grid_forget()
    top5_btn.grid_forget()
    about_btn.grid_forget()
    rule_hdln.grid(row=0, column=0, pady=10, columnspan=2)
    rules = [
        "1. Click on the hearts to change their colors.",
        "2. White hint - colour is correct, but not in its place.",
        "3. Black hint - colour correct and in its place.",
        "4. Your goal is to break the code in 6 tries, good luck!"
    ]
    for i, rule in enumerate(rules):
        rule_text = tk.Label(frame, text=rule, font=(font, 12))
        rule_text.grid(row=2+i, column=0, pady=10, columnspan=2, sticky="w")
        rule_labels.append(rule_text)
    rule_return_button.grid(row=0, column=0, padx=15, pady=10, columnspan=2, sticky="w")

def about():
    start_button.grid_forget()
    rule_button.grid_forget()
    start_label.grid_forget()
    hdln_bgnr_lbl.grid_forget()
    empty_lbl.grid_forget()
    top5_btn.grid_forget()
    about_btn.grid_forget()
    rule_return_button.grid(row=0, column=0, padx=15, pady=10, columnspan=2, sticky="w")
    about = [
        "This is the light version of classic codebreaker.",
        "Unlike the original, here hint refers to a specific field.",
        "Made by Alesia Vasilevich in two weeks.",
        "Main sources: skolo.lv, tkdocs.com, youtube tutorials."
    ]
    abt_hdln_lbl.grid(row=0, column=0, pady=10, columnspan=2)
    for i, about in enumerate(about):
        about_text = tk.Label(frame, text=about, font=(font, 12))
        about_text.grid(row=2+i, column=0, pady=10, columnspan=2, sticky="w")
        about_labels.append(about_text)
    rule_return_button.grid(row=0, column=0, padx=15, pady=10, columnspan=2, sticky="w")

def top5():
    start_button.grid_forget()
    rule_button.grid_forget()
    start_label.grid_forget()
    hdln_bgnr_lbl.grid_forget()
    empty_lbl.grid_forget()
    top5_btn.grid_forget()
    about_btn.grid_forget()
    leaderboard_menu()

def heart_image(index):
    img = Image.open(hearts[states[index]]).resize((40,40))
    tk_img = ImageTk.PhotoImage(img)
    return tk_img

def click(index):
    states[index] = (states[index] + 1) % len(hearts)
    img = heart_image(index)
    labels[index].config(image=img)
    labels[index].image = img

states = [0, 0, 0, 0]
labels = []
root = tk.Tk()
root.title("Code Breaker")
root.geometry("420x320")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame = tk.Frame(root)
frame.grid(row=0, column=0)
hearts_frame = tk.Frame(frame)
hearts_frame.grid(row=1, column=0)
bottom_frame = tk.Frame(frame)
bottom_frame.grid(row=3, column=0)
hints_frame = tk.Frame(frame)
hints_frame.grid(row=2, column=0)

def first_screen():
    for label in rule_labels:
        label.grid_forget()
    for label in about_labels:
        label.grid_forget()
    top_pl_lbl.grid_forget()
    top_sc_lbl.grid_forget()
    menu_button.grid_forget()
    spele_label.grid_forget()
    remain_label.grid_forget()
    submit_button.grid_forget()
    abt_hdln_lbl.grid_forget()
    top_frame.grid_forget()
    bottom_frame.grid_forget()
    leaderboard_lbl.grid_forget()
    for lbl in top_labels:
        lbl[0].destroy()
        lbl[1].destroy()
    top_labels.clear()
    for lbl in hint_labels:
        lbl.destroy()
    hint_labels.clear()
    for lbl in labels:
        lbl.destroy()
    labels.clear()
    for lbl in heart_labels:
        lbl.destroy()
    heart_labels.clear()
    for lbl in displayed_prev_labels:
        lbl.destroy()
    displayed_prev_labels.clear()
    rule_labels.clear()
    about_labels.clear()
    hint_labels.clear()
    rule_hdln.grid_forget()
    rule_return_button.grid_forget()
    top10_return_button.grid_forget()
    bottom_frame.grid_forget()
    for i in range(10):
        frame.columnconfigure(i, minsize=0, weight=0)
    empty_lbl.grid(row=0, column=0)
    start_label.grid(row=1, column=0, pady=0, columnspan=2)
    hdln_bgnr_lbl.grid(row=2, column=0, pady=20, columnspan=2)
    rule_button.grid(row=3, column=1, pady=10)
    start_button.grid(row=3, column=0, pady=10)
    about_btn.grid(row=4, column=0, pady=10)
    top5_btn.grid(row=4, column=1, pady=10)

def player_code(states):
    playerlist = []
    for elem in states:
        if elem == 0:
            playerlist.append("rd")
        elif elem == 1:
            playerlist.append("gn")
        elif elem == 2:
            playerlist.append("ye")
        elif elem == 3:
            playerlist.append("bu")
    return playerlist

def on_submit():
    global tries, cmp, mode
    if mode != "spele":
        return
    tries += 1
    hint.clear()
    for lbl in hint_labels:
        lbl.grid_forget()
    hint_labels.clear()
    pl = player_code(states)
    mode = checkinput(pl, cmp)
    for i, obj in enumerate(hint):
        if obj == "bk":
            hint[i] = "static/black_c.png"
        elif obj == "wh":
            hint[i] = "static/white_c.png"
        elif obj == "gr":
            hint[i] = "static/grey_c.png"
    for i, hint_img in enumerate(hint):
        img = Image.open(hint_img).resize((30,30))
        tk_img = ImageTk.PhotoImage(img)
        hint_label = tk.Label(hints_frame, image=tk_img)
        hint_label.image = tk_img
        hint_labels.append(hint_label)
        hint_label.grid(row=3, column=i, padx=5)
    if mode == "uzvara":
        prev_button.grid_forget()
        end_hint = ["static/black_c.png"] * 4
        for i, hint_img in enumerate(end_hint):
            img = Image.open(hint_img).resize((30,30))
            tk_img = ImageTk.PhotoImage(img)
            hint_label = tk.Label(hints_frame, image=tk_img)
            hint_label.image = tk_img
            hint_labels.append(hint_label)
            hint_label.grid(row=3, column=i, padx=5)
        remain_label.config(text=f"You broke the code in {tries} tries :)")
        spele_label.config(text="CONGRATS!!")
        cont_button.grid(row=5, column=0, pady=10, columnspan=2)
    elif tries >= 6:
        mode = "lose"
        remain_label.config(text=f"Tries left: {6 - tries}")
        spele_label.config(text="GAME OVER :(")
        prev_button.grid_forget()
        menu_button.grid(row=5, column=0, pady=10, columnspan=2)
    else:
        remain_label.config(text=f"Tries left: {6 - tries}")
        remain_label.grid(row=4, column=0, pady=10, columnspan=2)

def comp_code():
    colouroptions = ["gn", "ye", "rd", "bu"]
    return [random.choice(colouroptions) for _ in range(4)]

def checkinput(playerlist, complist):
    global hint
    if playerlist == complist:
        return "uzvara"
    copyplayer = playerlist.copy()
    copycomp = complist.copy()
    for i in range(4):
        if copyplayer[i] == copycomp[i]:
            copyplayer[i] = None
            copycomp[i] = None
            hint.append("bk")
        else:
            hint.append("gr")
    for i in range(4):
        if copyplayer[i] is not None and copyplayer[i] in copycomp:
            hint[i] = "wh"
            copycomp[copycomp.index(copyplayer[i])] = None
            copyplayer[i] = None
    prev.append(playerlist)
    # hint_priority = {"bk": 0, "wh": 1, "gr": 2}
    # hint = sorted(hint, key=lambda x: hint_priority[x])
    prev_hints.append(hint.copy())
    print("Hint:", hint)
    return "spele"

def get_top5():
    with open("players.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
        top5_sorted = sorted(data, key=lambda x: x["score"], reverse=True)[:5]
    return top5_sorted

def previous(prev):
    spele_label.grid_forget()
    remain_label.grid_forget()
    prev_button.grid_forget()
    submit_button.grid_forget()
    hearts_frame.grid_forget()
    hints_frame.grid_forget()

    prev_screen_frame = tk.Frame(frame)
    prev_screen_frame.grid(row=0, column=0, columnspan=10, sticky="nw")
    displayed_prev_labels.append(prev_screen_frame)

    for row_idx in range(len(prev)):
        guess_imgs = make_image(prev[row_idx], prev_screen_frame)
        for col_idx, img_label in enumerate(guess_imgs):
            img_label.grid(row=row_idx, column=col_idx, padx=4, pady=4)

        spacer = tk.Label(prev_screen_frame, text="   ")
        spacer.grid(row=row_idx, column=4)

        hint_imgs = make_image(prev_hints[row_idx], prev_screen_frame)
        for col_idx, img_label in enumerate(hint_imgs):
            img_label.grid(row=row_idx, column=col_idx + 5, padx=4, pady=4)

    back_btn = tk.Button(prev_screen_frame, text="BACK", command=back_to_game)
    back_btn.grid(row=len(prev), column=2, pady=10, columnspan=4)

def make_image(listt, parent=None):
    if parent is None:
        parent = frame
    created_labels = []
    for i in listt:
        if i == "gn":
            img = Image.open("static/green_heart.png").resize((30, 30))
        elif i == "ye":
            img = Image.open("static/yellow_heart.png").resize((30, 30))
        elif i == "rd":
            img = Image.open("static/red_heart.png").resize((30, 30))
        elif i == "bu":
            img = Image.open("static/blue_heart.png").resize((30, 30))
        elif i == "bk":
            img = Image.open("static/black_c.png").resize((20, 20))
        elif i == "wh":
            img = Image.open("static/white_c.png").resize((20, 20))
        elif i == "gr":
            img = Image.open("static/grey_c.png").resize((20, 20))
        else:
            continue
        tk_img = ImageTk.PhotoImage(img)
        lbl = tk.Label(parent, image=tk_img)
        lbl.image = tk_img
        created_labels.append(lbl)
    return created_labels

def enter_name():
    for label in rule_labels:
        label.grid_forget()
    menu_button.grid_forget()
    spele_label.grid_forget()
    remain_label.grid_forget()
    submit_button.grid_forget()
    for lbl in hint_labels:
        lbl.destroy()
    hint_labels.clear()
    for lbl in labels:
        lbl.destroy()
    labels.clear()
    for lbl in displayed_prev_labels:
        lbl.destroy()
    displayed_prev_labels.clear()
    rule_labels.clear()
    hint_labels.clear()
    rule_hdln.grid_forget()
    rule_return_button.grid_forget()
    displayed_prev_labels.clear()
    cont_button.grid_forget()
    name_label.grid(row=0, column=0, pady=10, columnspan=2)
    name_entry.grid(row=1, column=0, pady=10, columnspan=2)
    submit_name_btn.grid(row=2, column=0, pady=10, columnspan=2)

def send_score(username):
    score_info = {"name": username, "score": 7 - tries}
    try:
        with open("players.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(score_info)
    with open("players.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    name_entry.grid_forget()
    name_label.grid_forget()
    submit_name_btn.grid_forget()

    leaderboard()

def leaderboard():
    top5 = get_top5()
    top_pl_lbl.grid(row=1, column=0, pady=5, sticky="w")
    top_sc_lbl.grid(row=1, column=1, pady=5, sticky="e")
    for num, info in enumerate(top5, start=1):
        top5line = tk.Label(frame, text=f"{num}. {info['name']}", font=(font, 12))
        top5_scoreline = tk.Label(frame, text=info['score'], font=(font, 12))
        top5line.grid(row=num+1, column=0, pady=5, sticky="w")
        top5_scoreline.grid(row=num+1, column=1, pady=5, sticky="e")
        top_labels.append((top5line, top5_scoreline))
    menu_button.grid(row=num+2, column=0, columnspan=2, pady=10)

def leaderboard_menu():
    bottom_frame.grid(row=2, column=0, columnspan=4, sticky="nw")
    top5 = get_top5()
    top10_return_button.grid(row=0, column=0, pady=10, padx=20, sticky="w")
    leaderboard_lbl.grid(row=0, column=1, pady=10, columnspan=2)
    pl_hdr = tk.Label(bottom_frame, text="Player", font=(font, 15))
    sc_hdr = tk.Label(bottom_frame, text="Score", font=(font, 15))
    pl_hdr.grid(row=1, column=0, pady=5, padx=20, sticky="w")
    sc_hdr.grid(row=1, column=1, pady=5, padx=20, sticky="e")
    top_labels.append((pl_hdr, sc_hdr))

    for num, info in enumerate(top5, start=1):
        top5line = tk.Label(bottom_frame, text=f"{num}. {info['name']}", font=(font, 12))
        top5_scoreline = tk.Label(bottom_frame, text=info['score'], font=(font, 12))
        top5line.grid(row=num+1, column=0, pady=5, sticky="w", padx=20)  # row num+1
        top5_scoreline.grid(row=num+1, column=1, pady=5, sticky="e", padx=20)
        top_labels.append((top5line, top5_scoreline))
top_frame = tk.Frame(frame)
bottom_frame = tk.Frame(frame)
top_frame.grid(row=0, column=0, columnspan=2, sticky="nw")
bottom_frame.grid(row=2, column=1, columnspan=2, sticky="nw")
rule_button = tk.Button(frame, text="RULES", command=rule_clicked)
start_label = tk.Label(frame, text="CODE BREAKER", font=(font, 20))
start_button = tk.Button(frame, text="START", command=start_clicked)
rule_return_button = tk.Button(frame, text="BACK", command=first_screen)
rule_hdln = tk.Label(frame, text="RULES", font=(font, 20))
submit_button = tk.Button(frame, text="GO!", command=on_submit)
remain_label = tk.Label(frame, text=f"Tries left: {6 - tries}", font=(font, 12))
spele_label = tk.Label(frame, text="YOUR GUESS:", font=(font, 20))
prev_button = tk.Button(frame, text="PREVIOUS GUESSES", command=lambda: previous(prev))
cont_button = tk.Button(frame, text="CONTINUE", command=enter_name)
menu_button = tk.Button(frame, text="MENU", command=first_screen)
name_label = tk.Label(frame, text="ENTER YOUR NAME:", font=(font, 12))
name_entry = tk.Entry(frame)
submit_name_btn = tk.Button(frame, text="SUBMIT", command=lambda:send_score(name_entry.get()))
top_pl_lbl = tk.Label(frame, text="Player", font=(font, 15))
top_sc_lbl = tk.Label(frame, text="Score", font=(font, 15))
hdln_bgnr_lbl = tk.Label(frame, text="BEGINNER EDITION!", font=(font, 12))
empty_lbl = tk.Label(frame, text="  ", font=(font, 15))
about_btn = tk.Button(frame, text="ABOUT", command=about)
abt_hdln_lbl = tk.Label(frame, text="ABOUT", font=(font, 20))
top5_btn = tk.Button(frame, text="TOP 5", command=top5)
top10_return_button = tk.Button(frame, text="BACK", command=first_screen)
leaderboard_lbl = tk.Label(frame, text="TOP 5", font=(font, 15))
first_screen()
root.mainloop()
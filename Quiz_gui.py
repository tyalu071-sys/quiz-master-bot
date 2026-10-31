"""
Quiz Master Bot - GUI version (Month 2, upgraded)

Screens:  Home (language, name, level)  ->  Quiz (10 questions)
          ->  Final result  ->  History (saved in scores.txt)

Run:  python quiz.py        (tkinter comes built in with Python on Windows)
"""

import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

SCORES_FILE = "scores.txt"
QUESTIONS_PER_QUIZ = 10

# ---------------------------------------------------------------------------
# QUESTION BANK
# QUIZ_BANK[language][level] = list of (question, [4 options], index_of_correct)
# To add a question, just add another tuple. To add a language, copy a block.
# ---------------------------------------------------------------------------
QUIZ_BANK = {
    "English": {
        "easy": [
            ("What is 2 + 2?", ["3", "4", "5", "6"], 1),
            ("What is the capital of Japan?", ["Seoul", "Beijing", "Tokyo", "Bangkok"], 2),
            ("How many days are in a week?", ["5", "6", "7", "8"], 2),
            ("What colour is the sky on a clear day?", ["Green", "Blue", "Red", "Yellow"], 1),
            ("How many legs does a spider have?", ["6", "8", "10", "4"], 1),
            ("Which planet do we live on?", ["Mars", "Venus", "Earth", "Jupiter"], 2),
            ("What is 10 - 3?", ["6", "7", "8", "9"], 1),
            ("Which animal is called the king of the jungle?", ["Tiger", "Lion", "Elephant", "Bear"], 1),
            ("How many months are in a year?", ["10", "11", "12", "13"], 2),
            ("What is the national animal of India?", ["Lion", "Tiger", "Elephant", "Peacock"], 1),
        ],
        "medium": [
            ("What is 12 x 12?", ["124", "144", "164", "132"], 1),
            ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], 2),
            ("What is the chemical formula of water?", ["H2O", "CO2", "O2", "NaCl"], 0),
            ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Saturn", "Mercury"], 1),
            ("Who wrote 'Romeo and Juliet'?", ["Dickens", "Shakespeare", "Austen", "Tolstoy"], 1),
            ("What is the square root of 81?", ["7", "8", "9", "10"], 2),
            ("How many continents are there?", ["5", "6", "7", "8"], 2),
            ("Which gas do plants take in from the air?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 1),
            ("What is the capital of Karnataka?", ["Mysuru", "Bengaluru", "Hubballi", "Mangaluru"], 1),
            ("What is 15% of 200?", ["20", "25", "30", "35"], 2),
        ],
        "difficult": [
            ("What is the chemical symbol for gold?", ["Go", "Gd", "Au", "Ag"], 2),
            ("In which year did India gain independence?", ["1945", "1947", "1950", "1952"], 1),
            ("What is 2 to the power 10?", ["512", "1024", "2048", "1000"], 1),
            ("Who developed the theory of general relativity?", ["Newton", "Einstein", "Bohr", "Galileo"], 1),
            ("What is the hardest natural substance?", ["Gold", "Iron", "Diamond", "Quartz"], 2),
            ("What is the capital of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], 1),
            ("Who painted the Mona Lisa?", ["Van Gogh", "Picasso", "Leonardo da Vinci", "Michelangelo"], 2),
            ("Approximately how fast does light travel?",
             ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^5 m/s", "3 x 10^10 m/s"], 0),
            ("Which is the largest ocean on Earth?", ["Atlantic", "Indian", "Pacific", "Arctic"], 2),
            ("How many bones are in an adult human body?", ["196", "206", "216", "226"], 1),
        ],
    },
    "हिन्दी": {
        "easy": [
            ("2 + 2 कितना होता है?", ["3", "4", "5", "6"], 1),
            ("जापान की राजधानी क्या है?", ["सियोल", "बीजिंग", "टोक्यो", "बैंकॉक"], 2),
            ("एक सप्ताह में कितने दिन होते हैं?", ["5", "6", "7", "8"], 2),
            ("साफ़ दिन में आसमान का रंग कैसा होता है?", ["हरा", "नीला", "लाल", "पीला"], 1),
            ("मकड़ी के कितने पैर होते हैं?", ["6", "8", "10", "4"], 1),
            ("हम किस ग्रह पर रहते हैं?", ["मंगल", "शुक्र", "पृथ्वी", "बृहस्पति"], 2),
            ("10 - 3 कितना होता है?", ["6", "7", "8", "9"], 1),
            ("जंगल का राजा किसे कहा जाता है?", ["बाघ", "शेर", "हाथी", "भालू"], 1),
            ("एक साल में कितने महीने होते हैं?", ["10", "11", "12", "13"], 2),
            ("भारत का राष्ट्रीय पशु कौन सा है?", ["शेर", "बाघ", "हाथी", "मोर"], 1),
        ],
        "medium": [
            ("12 × 12 कितना होता है?", ["124", "144", "164", "132"], 1),
            ("ऑस्ट्रेलिया की राजधानी क्या है?", ["सिडनी", "मेलबर्न", "कैनबरा", "पर्थ"], 2),
            ("पानी का रासायनिक सूत्र क्या है?", ["H2O", "CO2", "O2", "NaCl"], 0),
            ("किस ग्रह को लाल ग्रह कहते हैं?", ["शुक्र", "मंगल", "शनि", "बुध"], 1),
            ("'रोमियो और जूलियट' किसने लिखा?", ["डिकेंस", "शेक्सपियर", "ऑस्टिन", "टॉल्स्टॉय"], 1),
            ("81 का वर्गमूल क्या है?", ["7", "8", "9", "10"], 2),
            ("दुनिया में कुल कितने महाद्वीप हैं?", ["5", "6", "7", "8"], 2),
            ("पौधे हवा से कौन सी गैस लेते हैं?",
             ["ऑक्सीजन", "कार्बन डाइऑक्साइड", "नाइट्रोजन", "हाइड्रोजन"], 1),
            ("कर्नाटक की राजधानी क्या है?", ["मैसूरु", "बेंगलुरु", "हुबली", "मंगलुरु"], 1),
            ("200 का 15% कितना होता है?", ["20", "25", "30", "35"], 2),
        ],
        "difficult": [
            ("सोने का रासायनिक प्रतीक क्या है?", ["Go", "Gd", "Au", "Ag"], 2),
            ("भारत को आज़ादी किस वर्ष मिली?", ["1945", "1947", "1950", "1952"], 1),
            ("2 की घात 10 का मान क्या है?", ["512", "1024", "2048", "1000"], 1),
            ("सापेक्षता का सामान्य सिद्धांत किसने दिया?", ["न्यूटन", "आइंस्टीन", "बोर", "गैलीलियो"], 1),
            ("सबसे कठोर प्राकृतिक पदार्थ कौन सा है?", ["सोना", "लोहा", "हीरा", "क्वार्ट्ज़"], 2),
            ("कनाडा की राजधानी क्या है?", ["टोरंटो", "ओटावा", "वैंकूवर", "मॉन्ट्रियल"], 1),
            ("मोना लिसा किसने बनाई?", ["वैन गॉग", "पिकासो", "लियोनार्डो दा विंची", "माइकल एंजेलो"], 2),
            ("प्रकाश की चाल लगभग कितनी है?",
             ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^5 m/s", "3 x 10^10 m/s"], 0),
            ("सबसे बड़ा महासागर कौन सा है?", ["अटलांटिक", "हिंद", "प्रशांत", "आर्कटिक"], 2),
            ("वयस्क मानव शरीर में कितनी हड्डियाँ होती हैं?", ["196", "206", "216", "226"], 1),
        ],
    },
}

LEVELS = ["easy", "medium", "difficult"]

# ---------------------------------------------------------------------------
# SCREEN TEXT (one block per language)
# ---------------------------------------------------------------------------
UI = {
    "English": {
        "title": "Quiz Master Bot", "language": "Choose language", "name": "Your name",
        "level": "Difficulty level", "easy": "Easy", "medium": "Medium", "difficult": "Difficult",
        "start": "Start Quiz", "history": "View History",
        "name_req": "Please enter your name first.",
        "question_of": "Question {} of {}", "next": "Next", "see_result": "See Result",
        "correct": "Correct!", "wrong": "Wrong. The answer was: {}",
        "final": "Final Result", "score_line": "{name}, you scored {s} out of {t}",
        "perfect": "Perfect score! Amazing!", "good": "Good job!",
        "keep": "Keep practising - you will get there!",
        "review": "Your answers", "your_answer": "Your answer", "correct_answer": "Correct answer",
        "play_again": "Play Again", "back": "Back", "hist_title": "Quiz History",
        "no_scores": "No scores yet!", "cols": ("Date", "Player", "Language", "Level", "Score"),
        "clear": "Clear History", "clear_confirm": "Delete all saved history?",
        "saved": "Your score was saved!",
    },
    "हिन्दी": {
        "title": "क्विज़ मास्टर बॉट", "language": "भाषा चुनें", "name": "आपका नाम",
        "level": "कठिनाई स्तर", "easy": "आसान", "medium": "मध्यम", "difficult": "कठिन",
        "start": "क्विज़ शुरू करें", "history": "इतिहास देखें",
        "name_req": "कृपया पहले अपना नाम दर्ज करें।",
        "question_of": "प्रश्न {} / {}", "next": "अगला", "see_result": "परिणाम देखें",
        "correct": "सही!", "wrong": "गलत। सही उत्तर था: {}",
        "final": "अंतिम परिणाम", "score_line": "{name}, आपने {t} में से {s} अंक पाए",
        "perfect": "शानदार! पूरे अंक!", "good": "बहुत बढ़िया!",
        "keep": "अभ्यास करते रहिए, आप ज़रूर सफल होंगे!",
        "review": "आपके उत्तर", "your_answer": "आपका उत्तर", "correct_answer": "सही उत्तर",
        "play_again": "फिर से खेलें", "back": "वापस", "hist_title": "क्विज़ इतिहास",
        "no_scores": "अभी कोई स्कोर नहीं!", "cols": ("तारीख", "खिलाड़ी", "भाषा", "स्तर", "स्कोर"),
        "clear": "इतिहास मिटाएँ", "clear_confirm": "क्या आप सारा इतिहास मिटाना चाहते हैं?",
        "saved": "आपका स्कोर सेव हो गया!",
    },
}

# Colours and fonts
BG = "#f4f6fb"
PRIMARY = "#3b5bdb"
GOOD = "#2f9e44"
BAD = "#e03131"
FONT = "Segoe UI"


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Master Bot")
        self.geometry("680x640")
        self.minsize(560, 560)
        self.configure(bg=BG)

        # Choices made on the home page (they survive between screens)
        self.lang_var = tk.StringVar(value="English")
        self.name_var = tk.StringVar()
        self.level_var = tk.StringVar(value="easy")

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True, padx=30, pady=24)
        self.show_home()

    # ----- helpers --------------------------------------------------------
    def t(self, key):
        """Text for the currently chosen language."""
        return UI[self.lang_var.get()][key]

    def clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def label(self, text, size=12, bold=False, color="#212529", **kw):
        return tk.Label(self.container, text=text, bg=BG, fg=color,
                        font=(FONT, size, "bold" if bold else "normal"), **kw)

    def button(self, text, command, bg=PRIMARY, width=22):
        return tk.Button(self.container, text=text, command=command, bg=bg, fg="white",
                         activebackground=bg, activeforeground="white", relief="flat",
                         font=(FONT, 12, "bold"), width=width, pady=8, cursor="hand2")

    # ----- HOME PAGE ------------------------------------------------------
    def show_home(self):
        self.clear()
        self.label(self.t("title"), 26, True, PRIMARY).pack(pady=(10, 24))

        # Language
        self.label(self.t("language"), 12, True).pack(anchor="w")
        combo = ttk.Combobox(self.container, textvariable=self.lang_var,
                             values=list(QUIZ_BANK.keys()), state="readonly",
                             font=(FONT, 12))
        combo.pack(fill="x", pady=(4, 16))
        combo.bind("<<ComboboxSelected>>", lambda e: self.show_home())  # re-draw in new language

        # Name
        self.label(self.t("name"), 12, True).pack(anchor="w")
        entry = tk.Entry(self.container, textvariable=self.name_var, font=(FONT, 13),
                         relief="solid", bd=1)
        entry.pack(fill="x", pady=(4, 16), ipady=5)
        entry.bind("<Return>", lambda e: self.start_quiz())

        # Level
        self.label(self.t("level"), 12, True).pack(anchor="w")
        row = tk.Frame(self.container, bg=BG)
        row.pack(anchor="w", pady=(4, 24))
        for lv in LEVELS:
            tk.Radiobutton(row, text=self.t(lv), value=lv, variable=self.level_var,
                           bg=BG, activebackground=BG, font=(FONT, 12)).pack(side="left", padx=(0, 18))

        self.button(self.t("start"), self.start_quiz).pack(pady=6)
        self.button(self.t("history"), self.show_history, bg="#495057").pack(pady=6)

    # ----- QUIZ -----------------------------------------------------------
    def start_quiz(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning(self.t("title"), self.t("name_req"))
            return

        pool = QUIZ_BANK[self.lang_var.get()][self.level_var.get()]
        picked = random.sample(pool, min(QUESTIONS_PER_QUIZ, len(pool)))

        # Shuffle the answer options of every question
        self.questions = []
        for text, options, correct_index in picked:
            correct_text = options[correct_index]
            shuffled = options[:]
            random.shuffle(shuffled)
            self.questions.append({"q": text, "options": shuffled, "answer": correct_text})

        self.index = 0
        self.score = 0
        self.review = []        # (question, your answer, correct answer, was_right)
        self.show_question()

    def show_question(self):
        self.clear()
        self.answered = False
        item = self.questions[self.index]
        total = len(self.questions)

        self.label(self.t("question_of").format(self.index + 1, total), 12, True, "#868e96").pack(anchor="w")
        bar = ttk.Progressbar(self.container, maximum=total, value=self.index)
        bar.pack(fill="x", pady=(6, 20))

        self.label(item["q"], 18, True, wraplength=580, justify="left").pack(anchor="w", pady=(0, 20))

        self.option_buttons = []
        for option in item["options"]:
            b = tk.Button(self.container, text=option, font=(FONT, 13), bg="white", relief="solid",
                          bd=1, anchor="w", padx=14, pady=8, cursor="hand2",
                          command=lambda o=option: self.choose(o))
            b.pack(fill="x", pady=4)
            self.option_buttons.append(b)

        self.feedback = self.label("", 13, True, wraplength=580, justify="left")
        self.feedback.pack(anchor="w", pady=(14, 8))

        last = self.index == total - 1
        self.next_btn = self.button(self.t("see_result") if last else self.t("next"), self.next_question)
        self.next_btn.pack_forget()   # appears only after the player answers

    def choose(self, chosen):
        if self.answered:
            return
        self.answered = True
        item = self.questions[self.index]
        right = chosen == item["answer"]

        for b in self.option_buttons:
            if b["text"] == item["answer"]:
                b.configure(bg="#d3f9d8")                 # always show the right answer in green
            elif b["text"] == chosen:
                b.configure(bg="#ffe3e3")                 # wrong pick in red

        if right:
            self.score += 1
            self.feedback.configure(text=self.t("correct"), fg=GOOD)
        else:
            self.feedback.configure(text=self.t("wrong").format(item["answer"]), fg=BAD)

        self.review.append((item["q"], chosen, item["answer"], right))
        self.next_btn.pack(pady=6)

    def next_question(self):
        self.index += 1
        if self.index < len(self.questions):
            self.show_question()
        else:
            self.save_score()
            self.show_result()

    # ----- FINAL RESULT ---------------------------------------------------
    def show_result(self):
        self.clear()
        total = len(self.questions)
        self.label(self.t("final"), 24, True, PRIMARY).pack(pady=(0, 6))
        self.label(self.t("score_line").format(name=self.name_var.get().strip(), s=self.score, t=total),
                   15, True).pack()

        if self.score == total:
            msg = self.t("perfect")
        elif self.score >= total / 2:
            msg = self.t("good")
        else:
            msg = self.t("keep")
        self.label(msg, 13, color=GOOD if self.score >= total / 2 else BAD).pack(pady=(4, 12))

        # Review of every answer
        self.label(self.t("review"), 12, True).pack(anchor="w")
        frame = tk.Frame(self.container, bg=BG)
        frame.pack(fill="both", expand=True, pady=(4, 10))
        box = tk.Text(frame, wrap="word", font=(FONT, 11), relief="solid", bd=1, height=10)
        scroll = ttk.Scrollbar(frame, command=box.yview)
        box.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        box.pack(side="left", fill="both", expand=True)
        box.tag_configure("ok", foreground=GOOD)
        box.tag_configure("no", foreground=BAD)
        box.tag_configure("q", font=(FONT, 11, "bold"))

        for n, (q, mine, correct, right) in enumerate(self.review, start=1):
            box.insert("end", f"{n}. {q}\n", "q")
            mark = "✔" if right else "✘"
            box.insert("end", f"   {mark} {self.t('your_answer')}: {mine}\n", "ok" if right else "no")
            if not right:
                box.insert("end", f"   {self.t('correct_answer')}: {correct}\n", "ok")
            box.insert("end", "\n")
        box.configure(state="disabled")

        self.button(self.t("play_again"), self.show_home).pack(pady=4)
        self.button(self.t("history"), self.show_history, bg="#495057").pack(pady=4)

    # ----- SAVING & READING HISTORY (Week 3: files) -----------------------
    def save_score(self):
        name = self.name_var.get().strip().replace("|", " ")
        line = "|".join([
            datetime.now().strftime("%d-%m-%Y %H:%M"),
            name,
            self.lang_var.get(),
            self.level_var.get(),
            f"{self.score}/{len(self.questions)}",
        ])
        with open(SCORES_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def read_scores(self):
        rows = []
        try:                                              # first run: file may not exist yet
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 5:
                        rows.append(parts)
        except FileNotFoundError:
            pass
        return rows[::-1]                                 # newest first

    # ----- HISTORY PAGE ---------------------------------------------------
    def show_history(self):
        self.clear()
        self.label(self.t("hist_title"), 24, True, PRIMARY).pack(pady=(0, 14))

        rows = self.read_scores()
        if not rows:
            self.label(self.t("no_scores"), 14, color="#868e96").pack(pady=40)
        else:
            frame = tk.Frame(self.container, bg=BG)
            frame.pack(fill="both", expand=True)
            cols = self.t("cols")
            tree = ttk.Treeview(frame, columns=cols, show="headings")
            widths = (130, 120, 90, 90, 70)
            for col, w in zip(cols, widths):
                tree.heading(col, text=col)
                tree.column(col, width=w, anchor="center")
            for date, name, lang, level, score in rows:
                level_label = UI[self.lang_var.get()].get(level, level)
                tree.insert("", "end", values=(date, name, lang, level_label, score))
            scroll = ttk.Scrollbar(frame, command=tree.yview)
            tree.configure(yscrollcommand=scroll.set)
            scroll.pack(side="right", fill="y")
            tree.pack(side="left", fill="both", expand=True)

        self.button(self.t("back"), self.show_home).pack(pady=(14, 4))
        if rows:
            self.button(self.t("clear"), self.clear_history, bg=BAD).pack(pady=4)

    def clear_history(self):
        if messagebox.askyesno(self.t("title"), self.t("clear_confirm")):
            open(SCORES_FILE, "w", encoding="utf-8").close()
            self.show_history()


if __name__ == "__main__":
    QuizApp().mainloop()
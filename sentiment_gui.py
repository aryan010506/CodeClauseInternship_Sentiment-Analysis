import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

def analyze_sentiment():
    text = entry.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        result = "Positive 😊"
        color = "#4CAF50"
    elif polarity < 0:
        result = "Negative 😠"
        color = "#f44336"
    else:
        result = "Neutral 😐"
        color = "#777777"

    output_label.config(text=f"Sentiment: {result}\nPolarity Score: {polarity:.2f}", fg=color)

# ---------- GUI Setup ----------
app = tk.Tk()
app.title("Sentiment Analyzer")
app.geometry("500x400")
app.configure(bg="#2e2e2e")  # Dark background

# ---------- Styling ----------
style = {
    "font": ("Segoe UI", 12),
    "bg": "#3a3a3a",
    "fg": "white",
    "insertbackground": "white",  # Cursor color
    "relief": "solid",
    "bd": 1
}

title_label = tk.Label(app, text="🧠 Sentiment Analysis Tool", font=("Segoe UI", 18, "bold"), bg="#2e2e2e", fg="white")
title_label.pack(pady=20)

entry = tk.Text(app, height=6, width=50, **style, wrap=tk.WORD)
entry.pack(pady=10)

# Hover Effects
def on_enter(e): analyze_btn['bg'] = '#45a049'
def on_leave(e): analyze_btn['bg'] = '#4CAF50'

analyze_btn = tk.Button(app, text="Analyze Sentiment", command=analyze_sentiment, bg="#4CAF50", fg="white",
                        font=("Segoe UI", 12, "bold"), relief="flat", padx=10, pady=5)
analyze_btn.pack(pady=10)
analyze_btn.bind("<Enter>", on_enter)
analyze_btn.bind("<Leave>", on_leave)

output_label = tk.Label(app, text="", font=("Segoe UI", 14), bg="#2e2e2e", fg="white", justify="center")
output_label.pack(pady=20)

footer = tk.Label(app, text="Created by Aryan | Codeclause", font=("Segoe UI", 9), bg="#2e2e2e", fg="#aaaaaa")
footer.pack(side="bottom", pady=10)

app.mainloop()

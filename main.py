import tkinter as tk
from tkinter import messagebox
import random
import time

txts = [
    "India is the seventh-largest country by land area.",
    "The capital of India is New Delhi.",
    "India is the second-most populous country in the world.",
    "The official languages of India are Hindi and English.",
    "India gained independence from British rule on August 15, 1947.",
    "Chandragupta Maurya overthrew the Nanda Empire.",
    "The Taj Mahal is a symbol of love and beauty.",
    "The British Indian Empire was partitioned in August 1947 into the Dominion of India.",
    "The Indian independence movement was a series of historic events.",
    "Mahatma Gandhi led the Salt March in 1930 to protest against British salt laws.",
    "India is known for its diverse culture and rich history.",
    "The Indian Constitution was adopted on January 26, 1950.",
    "India's first Prime Minister was Jawaharlal Nehru.",
    "The Indian flag has three colors: saffron, white, and green.",
    "The Indian national anthem is 'Jana Gana Mana'.",
    "The Indian national song is 'Vande Mataram'.",
    "India is the world's largest democracy.",
    "The Indian film industry is one of the largest in the world.",
    "Cricket is a popular sport in India, with millions of fans.",
    "The Indian economy is one of the fastest-growing in the world.",
    "India is home to many languages, cultures, and traditions.",
    "The Himalayas are the highest mountain range in the world.",
    "The Indian Ocean is the third-largest ocean in the world.",
    "The Ganges River is considered sacred in Hinduism.",
    "The Indian Space Research Organisation (ISRO) is known for its space missions.",
    "The Indian Railways is one of the largest railway networks in the world.",
    "The Indian festival of Diwali is celebrated with lights and fireworks.",
    "Yoga originated in ancient India and is practiced worldwide.",
    "The Indian cuisine is known for its diverse flavors and spices.",
    "The Indian Independence Act was passed by the British Parliament in 1947.",
    "The Indian subcontinent has a rich history of art and architecture.",
    "The Indus Valley Civilization was one of the world's earliest urban cultures.",
    "The Maurya Empire was one of the largest empires in ancient India.",
    "The Gupta Empire is known as the Golden Age of India.",
    "The Mughal Empire was known for its cultural achievements and architectural wonders.",
    "The Indian Ocean trade routes were crucial for ancient commerce.",
    "The Indian subcontinent has been influenced by various cultures and religions.",
    "The Indian independence movement was marked by non-violent protests.",
    "The Indian Constitution guarantees fundamental rights to its citizens.",
    "The Indian Parliament is the supreme legislative body in India.",
    "The Indian judiciary is independent and upholds the rule of law.",
    "The Indian economy is diverse, with agriculture, industry, and services sectors.",
    "The Indian education system has evolved over the years to meet modern needs.",
    "The Indian healthcare system is a mix of public and private services.",
    "The Indian art scene includes traditional and contemporary forms.",
    "The Indian music industry is vibrant, with various genres and styles.",
    "The Indian dance forms are rich in tradition and cultural significance.",
    "The Indian textile industry is known for its craftsmanship and variety.",
    "The Indian automobile industry is one of the largest in the world.",
    "The Indian IT industry is a major contributor to the global tech landscape.",
    "The Indian startup ecosystem is thriving with innovation and entrepreneurship."
]

class Typing:
    def __init__(self, root):
        self.r = root
        self.r.title("Typing Speed Test")
        self.r.geometry("700x400")
        self.r.resizable(False, False)
        
        self.txt = random.choice(txts)
        self.st = None

        self.hd = tk.Label(self.r, text="Typing Speed Test", font=("Helvetica", 24))
        self.hd.pack(pady=10)

        self.lbl = tk.Label(self.r, text=self.txt, wraplength=650, font=("Helvetica", 16))
        self.lbl.pack(pady=20)

        self.ent = tk.Text(self.r, height=5, width=80, font=("Helvetica", 14))
        self.ent.pack()
        self.ent.bind("<KeyPress>", self.start)

        self.btn = tk.Button(self.r, text="Submit", command=self.calc)
        self.btn.pack(pady=10)

        self.rst = tk.Button(self.r, text="Restart", command=self.restart)
        self.rst.pack()

    def start(self, event):
        if not self.st:
            self.st = time.time()

    def calc(self):
        et = time.time()
        typed = self.ent.get("1.0", tk.END).strip()
        t = et - self.st if self.st else 1
        wpm = (len(typed.split()) / t) * 60
        correct = sum(1 for i, c in enumerate(typed) if i < len(self.txt) and c == self.txt[i])
        acc = (correct / len(self.txt)) * 100
        messagebox.showinfo("Result", f"WPM: {wpm:.2f}\nAccuracy: {acc:.2f}%")

    def restart(self):
        self.txt = random.choice(txts)
        self.lbl.config(text=self.txt)
        self.ent.delete("1.0", tk.END)
        self.st = None

root = tk.Tk()
app = Typing(root)
root.mainloop()
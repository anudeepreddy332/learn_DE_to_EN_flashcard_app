# 🇩🇪 Learn DE to EN Flashcard App

A simple and elegant **German–English flashcard app** to help you build vocabulary daily.

Created with the **100 most commonly used words** in German (Deutsch), this tool helps reinforce your language learning through an interactive flashcard interface.

---

## ✨ Features
  - 🔁 Flip cards to reveal the English meaning
  - ✅ Mark words as “known” to track your progress
  - 📂 Saves your progress automatically (`words_to_learn.csv`)
  - 🧠 Great for daily microlearning

---

## 🛠 Built With
  - Python 3.12.6
  - Tkinter GUI 🖼️
  - pandas for CSV handling 📊

---

## 📁 Project Structure
learn_DE_to_EN_flashcard_app/
├── data/
│   ├── german_words_100.csv
│   └── words_to_learn.csv (auto-generated)
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
├── main.py
└── README.md

✅ How Progress Is Tracked
  •	Your known words are removed from the learning list and saved to words_to_learn.csv
  •	Restarting the app will continue from where you left off

📌 Note
  •	If words_to_learn.csv is missing, the app will default back to the original german_words_100.csv
  •	All data is stored locally; no external dependencies beyond pandas and tkinter

📚 Ideal For
  •	Beginners learning German
  •	Anyone looking for a low-effort, high-reward vocabulary booster
  •	Daily language practice

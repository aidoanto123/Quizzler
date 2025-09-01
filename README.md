# 🧠 Quizzler – Interactive Quiz Game

Quizzler is a Python-based quiz application that fetches random True/False questions from the Open Trivia Database API.  
It features a modern Tkinter GUI with real-time score tracking, instant feedback, and smooth question transitions.

---

## ✨ Features

- 🎯 **10 Random True/False Questions** pulled from the Open Trivia DB API
- 🖥 **Interactive Tkinter GUI** with clickable True/False buttons
- 📊 **Live score tracking** displayed at the top
- 🎨 **Color feedback system** (Green for correct, Red for incorrect)
- 📡 **Automatic question fetching** using `requests` and `json`
- 🔄 **Question decoding** to handle HTML entities (e.g., `&quot;`, `&#039;`)

---

## 📂 Project Structure

│── main.py               # Entry point, initializes the quiz  
│── data.py               # Fetches question data from the API  
│── question_model.py     # Question class to store question/answer  
│── quiz_brain.py         # Logic for question handling and scoring  
│── ui.py                 # Tkinter GUI implementation  
│── images/               # True/False button images  
│── README.md             # Project documentation  

---

## 🛠 Requirements

Make sure you have **Python 3.x** installed.  
Install dependencies using:

```bash
pip install requests

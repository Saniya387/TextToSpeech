# TextToSpeech
# 🗣️ Text-to-Speech (TTS) App using Tkinter and pyttsx3

This is a simple **Text-to-Speech** desktop application built with **Python**, using **Tkinter** for the GUI and **pyttsx3** for offline speech synthesis.

---

## 🚀 Features

- Convert text input into spoken voice
- Clean and minimal interface
- Works completely offline
- Easy to extend with voice, speed, and volume settings

---

## 🛠️ Requirements

- Python 3.x
- `pyttsx3`
- `tkinter` (comes built-in with Python)

Install `pyttsx3` using pip:

```bash
pip install pyttsx3
 Code Overview
pyttsx3.init() — Initializes the speech engine

tk.Entry — Input box to type text

tk.Button — Triggers speech

engine.say() — Queues the text to be spoken

engine.runAndWait() — Processes the voice output

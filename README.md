# 📚 Word-Search-Application-Utilizing-Brute-Force-and-KMP-Algorithms

A flexible word search application that supports both **desktop (Tkinter)** and **web-based (Flask)** interfaces. It utilizes **Brute Force** and **Knuth-Morris-Pratt (KMP)** string-searching algorithms to locate words across multiple text files. Advanced matching options and performance comparison are built-in.

---

## 🚀 Features

### ✅ Search Functionality
- Search a keyword across multiple `.txt` files
- Displays:
  - File name
  - Row number
  - Column index (starting position in line)

### ⚙️ Advanced Matching Options
- **Whole Word Match**
  - ✔️ Checked: Match exact whole words (e.g., "pak" → only "pak")
  - ❌ Unchecked: Match substrings too (e.g., "pak" → "Pakistan", "adampak")
- **Case Sensitivity**
  - ✔️ Checked: Case-sensitive search
  - ❌ Unchecked: Case-insensitive (e.g., "Bilal", "bilaL", "BILAL")

### ⏱️ Performance Evaluation
- Implements both **Brute Force** and **KMP** algorithms
- Displays time taken by each algorithm after each search:
  - `Time (Brute Force):`
  - `Time (KMP):`

---

## 🖥️ User Interfaces

This project supports two modes:

### 🧩 Tkinter Desktop App
- Native desktop GUI
- Real-time input and result display

### 🌐 Flask Web App
- Accessible in browser
- Lightweight local server

---

## 🧪 Technology Stack

- **Language:** Python
- **GUI:** Tkinter
- **Web Framework:** Flask
- **Algorithms:** Brute Force & Knuth-Morris-Pratt (KMP)

---

## 📷 Screenshots

_Add screenshots showing both the Tkinter and Flask versions here._

---

## 📄 Documentation

- 📌 Dual implementation of string-search algorithms
- ⚖️ Algorithm timing comparison included
- 🧭 Step-by-step user instructions for both interfaces
- 🛠️ Error handling for empty input, invalid formats, and no matches

---

## 📚 References

- [KMP Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)

---

> Built for exploration, comparison, and hands-on learning 🎯

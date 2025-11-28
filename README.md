# 📚 DSA Library CLI Tool

A lightweight Python-based command-line tool to organize and store Data Structures &
Algorithms practice solutions efficiently.

This tool helps you:

- Categorize solutions by difficulty and tags
- Search problems quickly
- Maintain a personal offline DSA archive

---

## 🚀 Features

✔ Add solution with details (title, difficulty, tags, code file path)  
✔ Search stored solutions  
✔ List all saved entries  
✔ JSON-based persistent storage  
✔ Input validation and modular OOP design

---

## 🧠 Usage

### 1️⃣ Add a new problem

python dsa_cli.py add --title "Binary Search" --difficulty medium --tags array search --file solutions/binary_search.py

shell
Copy code

### 2️⃣ List all stored problems

python dsa_cli.py list

shell
Copy code

### 3️⃣ Search by keyword

python dsa_cli.py search --keyword binary

yaml
Copy code

### 3️⃣ Delete by keyword

python dsa_cli.py delete --keyword binary

yaml
Copy code

---

## 🗂 Folder Structure

dsa_library/
│
├── dsa_cli.py
├── models/
│ └── problem.py
├── services/
│ └── manager.py
├── storage/
│ └── database.json
└── README.md

yaml
Copy code

---

## 🛠 Tech Stack

| Component | Usage              |
| --------- | ------------------ |
| Python    | Core Language      |
| argparse  | CLI commands       |
| OOP       | Code architecture  |
| JSON      | Local data storage |

---

## 📌 Future Enhancements

- GitHub auto-sync
- PDF/Markdown export
- Run and test solutions
- AI-based tagging

---

## 👤 Author

**Viresh Panchal**  
Python Developer | Passionate about Automation, DSA & Clean Code

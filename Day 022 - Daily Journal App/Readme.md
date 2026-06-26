# Daily Journal App 📖

A beginner-friendly Python project created while learning file handling, dictionaries, nested data structures, and persistent data storage.

This application allows users to create daily journal entries, store them using text files, view all saved entries, and search previous journal entries by date.

This project was built to practice working with real-world data storage while improving debugging and program logic skills.

---

## Features

* Add new journal entries with title and content
* Automatically saves entries using the current date
* Store multiple journal entries using nested dictionaries
* View all saved journal entries
* Search previous journal entries by date
* Data persistence using text file storage
* Input validation for menu selection
* Handles missing journal file by creating a new one automatically

---

## Concepts Practiced

* Dictionaries and nested dictionaries
* Functions and modular code structure
* File handling (`open()`, read, write)
* Data persistence between program runs
* Working with `datetime` module
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`) for menu-driven program flow
* Exception handling using `try-except`
* Program state management and dictionary updates

---

## How It Works

The user is presented with a menu:

1. Add a new journal entry
2. View all journal entries
3. Search old journal entries by date
4. Exit application

When a new journal entry is added:

* Current date is automatically generated
* Entry title and content are stored inside a nested dictionary
* Data is saved to a text file for future use

Users can later search journal entries by entering a specific date.

---

## Example Data Structure

```python
journal = {
    "25-Jun": {
        "Python": "Solved one OOP exercise",
        "DSA": "Practiced array questions"
    }
}
```

---

## Skills Improved During This Project

* Managing nested dictionaries
* Understanding dictionary overwrite vs update behavior
* Debugging logical errors in data storage
* Handling persistent file-based data
* Thinking through program execution flow step by step

---

## Future Improvements

* Allow multiple entries with timestamps on the same day
* Store data using JSON instead of plain text
* Improve search functionality
* Add edit and delete journal entries
* Better formatting for displaying saved journals

---

## Project Goal

This project was built as part of a long-term Python learning roadmap focused on strengthening programming fundamentals through hands-on practice and real coding challenges.

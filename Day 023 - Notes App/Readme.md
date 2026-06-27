# Notes App

A simple command-line Notes Application built using Python.

This project allows users to create, view, search, edit, and delete notes using a menu-driven interface. The application stores notes in a dictionary where the note title acts as the key and the note content acts as the value.

## Features

* Add new notes
* View all saved notes
* Search notes by title
* Edit existing notes
* Delete notes
* Menu-driven interface for easy interaction

## Concepts Used

* Python Functions
* Dictionaries
* Loops (`while`)
* Conditional Statements (`if-elif-else`)
* User Input Handling
* Dictionary Methods (`update()`, `pop()`)
* Basic CRUD Operations

## Project Structure

```text
notes-app/
│
├── main.py
└── README.md
```

## How It Works

### Add Note

Users can create a note by providing:

* Title
* Content

Example:

```text
Enter title of note: study
Enter content for the note: Practice Python dictionaries
study successfully saved
```

### View Notes

Displays all saved notes.

Example:

```text
{
  'study': 'Practice Python dictionaries',
  'shopping': 'Buy groceries'
}
```

### Search Note

Search for a note using its title.

Example:

```text
Enter title of the note you want to search: study
{'study': 'Practice Python dictionaries'}
```

### Edit Note

Modify the content of an existing note.

Example:

```text
Enter title of the note you want to change: study
Enter new content: Revise functions
successfully edited the contents of study
```

### Delete Note

Remove a note by entering its title.

Example:

```text
Enter title of the note you want to remove: shopping
shopping successfully deleted
```

## Learning Outcome

Through this project, I practiced:

* Organizing code using functions
* Implementing CRUD operations
* Managing data using dictionaries
* Designing a menu-based terminal application
* Breaking a project into smaller reusable functions

## Future Improvements

Planned upgrades for the next version:

* Add file handling for permanent storage
* Add error handling for missing note titles
* Improve note display formatting
* Prevent accidental overwriting while editing
* Save notes automatically after every change

## How to Run

Run the following command in terminal:

```bash
python main.py
```

## Author

Pratik Kumar

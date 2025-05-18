
This Python-based CLI tool allows users to quickly jot down notes, review them, delete specific entries, and clear the terminal screen. It’s designed for simplicity and local use, without any cloud dependencies or accounts.



Add notes with confirmation prompt

Read all saved notes, numbered for clarity

Delete notes by selecting the corresponding number

Clear the terminal screen (clear command)

Help menu listing all commands

Handles edge cases like empty notes, invalid inputs, and missing files gracefully

Easter egg with a special response to “secret” note input

Requirements

Python 3.x installed on your system

Runs on Windows, Linux, and macOS terminals

Usage

Run the script in your terminal or command prompt:

python notebook.py

Then use these commands:

Command	Description
note	Add a new note
read	Display all saved notes
delete	Delete a selected note by number
clear	Clear the terminal screen
help	Show the list of available commands
exit or quit	Exit the program

Notes on Interaction


Adding a note requires confirmation (y or n).

When deleting, you must enter the note number and confirm deletion.

Invalid inputs prompt a retry without crashing.

If no notes are present, the program informs the user accordingly.

Example Flow

User types note and inputs a note.

Confirmation prompt appears before saving.

User types read to see all notes.

User types delete and inputs the note number to remove it.

User types exit to close the program.

License

You can use it if it helps you

# Student Management System

A simple Python console application for managing student records.

## Features

- Add a student
- View all students
- Update student details
- Remove a student
- Sort students by grade
- Show top students by grade threshold
- Save data to `Studentlist.json`

## Requirements

- Python 3.10 or later

## How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python cli.py
```

## Project Structure

- `cli.py` handles user interaction
- `service.py` contains the application logic
- `repository.py` handles JSON persistence
- `models.py` defines the domain objects

## Data File

Student records are stored in `Studentlist.json` in the same folder as the script.

## Notes

- If `Studentlist.json` is empty or missing, the program starts with an empty roster.
- Make sure student IDs are unique.

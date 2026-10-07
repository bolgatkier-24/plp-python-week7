# PLP Python Week 7 Assignment: Collections & Lists

This repository contains solutions for the Week 7 Python assignment focusing on list manipulation, interactive loops, input validation, and data summarization.

## File Descriptions
* **list_warmup.py**: Demonstrates index access, `.append()`, `.remove()`, and `len()` with a fruit list.
* **shopping_list.py**: An interactive command-line shopping list manager supporting add, remove, show, and exit actions with robust membership validation.
* **list_report.py**: Processes a predefined shopping items list to print numbered entries, count items longer than 4 characters, and find the longest item name manually using loops.

## Reflection
Checking if an item exists in a list using the `in` keyword before calling `.remove()` is essential because Python's `.remove()` method raises a `ValueError` if the item is not present, which would immediately crash the application. Validating membership first allows the program to handle missing items gracefully and present a user-friendly error message.

## Screenshots
Screenshots of each program running successfully are stored in the `screenshots/` directory.

# Task Tracker CLI

A simple command-line tool for tracking daily tasks. Logs are stored in a JSON file for easy persistence.

## Features

- Add daily task entries
- View full task log by date
- Simple, no dependencies

## How to Use

```bash
python main.py
```

Then follow the prompts.

## Example

```
1. Log a task
2. View log
3. Exit
Choose an option: 1
What task did you complete today? Studied Python
Task logged for 2025-07-04.
```

## File Output

Task are stored in `tasks.txt` like this:

```json
{
  "2025-07-04": ["Studied Python", "Worked out"]
}
```

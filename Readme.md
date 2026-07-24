# Lab 1: Grade Evaluator & Archiver

Calculates a student's final academic standing from a CSV of course grades, and archives grade files with a Bash script.

## Requirements

- Python 3
- Bash (Git Bash on Windows, or any Linux/macOS terminal)

## Input File Format

The evaluator reads a CSV with these exact columns: 
You can create your own csv file with the values below
and use it to run the program if you do not have one 
already

```
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

The group value should be `Formative` or `Summative`. The abbreviations FA and SA are also accepted, and matching is case-insensitive.

## Running the Grade Evaluator

Place your `grades.csv` in the same folder as the script, then run:

```bash
python grade-evaluator.py
```

Enter the CSV filename when prompted (e.g. `grades.csv` for correct run).

The program validates all scores (0–100) and weights (Total = 100, Formative = 60, Summative = 40),and then prints the category percentages, total grade, GPA out of 5.0, the final PASSED/FAILED status, and which failed formative assignments are eligible for resubmission.

A student passes only when they score at least 50% in both the Formative and Summative categories. Resubmission eligibility lists every failed formative assignment tied at the highest weight. Eligible resubmissions are shown regardless of overall pass/fail status, since a passing student can still resubmit a failed formative.

## Running the Organizer

Make the script executable once:

```bash
chmod +x organizer.sh
```

Then run it:

```
./organizer.sh
```

(or `bash organizer.sh` without making it executable if you like to do it like that)

Each run:
1. Creates an `archive/` directory if it doesn't exist
2. Moves `grades.csv` into `archive/` renamed with a timestamp (e.g. `grades_20260723-213641.csv`)
3. It then creates a fresh empty `grades.csv`
4. Appends the operation details to `organizer.log`

If `grades.csv` is not present, the script reports this and exits without writing a log entry.

## Error Handling

- Missing CSV file: reports the filename and exits
- Empty CSV (as produced by the organizer): reports that no records were found
- Invalid score values or non-numeric data: reports the error and exits without crashing
- Scores outside 0–100, or weights not matching the 100 / 60 / 40 split: reports which check failed


## Testing

Verified against the transcript structure provided with the assignment:

PROGRAM OUTPUT

--- Processing Grades ----
Formative: 44.4/60.0 (74.00%)
Summative: 32.5/40.0 (81.25%)
Total Grade: 76.90/100
GPA: 3.845 / 5.0
Final Status: PASSED
Eligible for resubmission (highest-weight failed formative):
  - Discussion Forum (score: 45.0, weight: 15.0)

J Paul@EileenBlessing MINGW64 ~/documents/lab1_Kabi-J-Paul (main)
$ 
This matches the transcript exactly, formatives 44.4, summatives 32.5, GPA 3.845, status PASSED, and the discussion forum as the resubmission. Discussion forum is selected over the heavier Group Coding Lab becuase only failed formatives i.e. below 50$ are considered, and general quiz is at 51% and is a pass
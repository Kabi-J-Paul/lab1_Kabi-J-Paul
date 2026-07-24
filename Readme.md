# Lab 1: Grade Evaluator & Archiver

Calculates a student's final academic standing from a CSV of course grades, and archives grade files with a Bash script.

## Requirements

- Python 3
- Bash (Git Bash on Windows, or any Linux/macOS terminal)

## Input File Format

This evaluator reads a CSV with these exact columns: 
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

Note: Run both scripts from inside the project folder:

```bash
cd lab1_Kabi-J-Paul
```

Place your `grades.csv` in the same folder as the script, then run:

```bash
python grade-evaluator.py
```

Enter the CSV filename when prompted (for example `grades.csv` for correct run).

The program validates all scores (0–100) and weights (Total = 100, Formative = 60, Summative = 40), and then prints the category percentages, total grade, GPA out of 5.0, the final PASSED/FAILED status, and which failed formative assignments are eligible for resubmission.

A student passes only when they score at least 50% in both the Formative and Summative categories. Resubmission eligibility lists every failed formative assignment tied at the highest weight. Eligible resubmissions are shown regardless of overall pass/fail status, since a passing student can still resubmit a failed formative.

## Running the Organizer

Make the script executable once:

```bash
chmod +x organizer.sh
```

Then you can run it:

```
./organizer.sh
```

(or `bash organizer.sh` without making it executable if you like to do it like that)

Each run:
1. Creates an `archive/` directory if it doesn't exist already
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

Verified against the transcript structure provided with the assignment, using a CSV containing the transcript's five assignments:

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): transcript-test.csv

--- Processing Grades ----
Formative: 44.4/60.0 (74.00%)
Summative: 32.5/40.0 (81.25%)
Total Grade: 76.90/100
GPA: 3.845 / 5.0
Final Status: PASSED
Eligible for resubmission (highest-weight failed formative):
  - Discussion Forum (score: 45.0, weight: 15.0)
```

This matches the transcript exactly: Formatives 44.4, Summatives 32.5, GPA 3.845, status PASSED, and Discussion Forum as the resubmission. Discussion Forum is selected over the heavier Group Coding Lab because only *failed* formatives (below 50%) are considered, and General Quiz at 51% is a pass.

### Edge cases tested

| # | Input | Result |
|---|---|---|
| 1 | Filename that does not exist | `Error: The file 'nofile.csv' was not found.` |
| 2 | Completely empty CSV | `No grade records found. The CSV file is empty.` |
| 3 | CSV with header row but no data | `No grade records found. The CSV file is empty.` |
| 4 | Non-numeric score value (`abc`) | `An error occurred while reading the file: could not convert string to float: 'abc'` |
| 5 | Score above 100 | `Error: 'Quiz' has an invalid score: 150.0` |
| 6 | Weights not summing to 100 | `Error: Total weights must equal 100, but got 105.0` |
| 7 | Weights summing to 100 with an incorrect 60/40 split | `Error: Formative weights must equal 60, but got 65.0` |
| 8 | CSV containing blank rows between records | Blank rows skipped; output identical to a clean file |

### Sample runs of edge cases

**1. Filename that does not exist**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): nofile.csv
Error: The file 'nofile.csv' was not found.
```

**2. Completely empty CSV** (as left behind by `organizer.sh`)

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv

--- Processing Grades ----
No grade records found. The CSV file is empty.
```

**3. CSV with a header row but no data**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): test-header.csv

--- Processing Grades ----
No grade records found. The CSV file is empty.
```

**4. Non-numeric score value**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
An error occurred while reading the file: could not convert string to float: 'abc'
```

**5. Score above 100**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): test-badscore.csv

--- Processing Grades ----
Error: 'Quiz' has an invalid score: 150.0
```

**6. Weights not summing to 100**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): test-badscore.csv

--- Processing Grades ----
Error: Total weights must equal 100, but got 105.0
```

**7. Weights summing to 100 with an incorrect 60/40 split**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): test-badscore.csv

--- Processing Grades ----
Error: Formative weights must equal 60, but got 65.0
```

**8. CSV containing blank rows between records**

```
$ python grade-evaluator.py
Enter the name of the CSV file to process (e.g., grades.csv): test-blankrows.csv

--- Processing Grades ----
Formative: 34.0/60.0 (56.67%)
Summative: 26.0/40.0 (65.00%)
Total Grade: 60.00/100
GPA: 3.000 / 5.0
Final Status: PASSED
Eligible for resubmission (highest-weight failed formative):
  - Group Exercise (score: 40.0, weight: 20.0)
  - Functions and Debugging Lab (score: 45.0, weight: 20.0)
```
Blank rows are skipped and the output matches a run on the equivalent file without them.

Tests 5 to 7 reuse the same test file, edited between runs to produce each condition.
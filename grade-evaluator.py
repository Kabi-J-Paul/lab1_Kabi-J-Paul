import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options


    if len(data) == 0:
        print("No grade records found. The CSV file is empty.")
        return

    for record in data:
        if record['score'] < 0 or record['score'] > 100:
            print(f"Error: '{record['assignment']}' has an invalid score: {record['score']}")
            sys.exit(1)
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for record in data:
        total_weight = total_weight + record['weight']
        if record['group'] == 'Formative':
            formative_weight = formative_weight + record['weight']
        elif record['group'] == 'Summative':
            summative_weight = summative_weight + record['weight']

    if total_weight != 100:
        print(f"Error: Total weights must equal 100, but got {total_weight}")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weights must equal 60, but got {formative_weight}")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weights must equal 40, but got {summative_weight}")
        sys.exit(1)

    formative_points = 0
    summative_points = 0

    for record in data:
        points = record['score'] * record['weight'] / 100
        if record['group'] == 'Formative':
            formative_points = formative_points + points
        else:
            summative_points = summative_points + points

    total_grade = formative_points + summative_points
    gpa = (total_grade / 100) * 5.0

    print(f"Formative: {formative_points}/{formative_weight} ({formative_points / formative_weight * 100:.2f}%)")
    print(f"Summative: {summative_points}/{summative_weight} ({summative_points / summative_weight * 100:.2f}%)")
    print(f"Total Grade: {total_grade:.2f}/100")
    print(f"GPA: {gpa:.2f} / 5.0")

    formative_percent = formative_points / formative_weight * 100
    summative_percent = summative_points / summative_weight * 100

    if formative_percent >= 50 and summative_percent >= 50:
        print("Final Status: PASSED")
    else:
        print("Final Status: FAILED")

    failed_formatives = []
    for record in data:
        if record['group'] == 'Formative' and record['score'] < 50:
            failed_formatives.append(record)

    if len(failed_formatives) == 0:
        print("No formative assignments eligible for resubmission.")
    else:
        highest_weight = failed_formatives[0]['weight']
        for record in failed_formatives:
            if record['weight'] > highest_weight:
                highest_weight = record['weight']

        print("Eligible for resubmission (highest-weight failed formative):")
        for record in failed_formatives:
            if record['weight'] == highest_weight:
                print(f"  - {record['assignment']} (score: {record['score']}, weight: {record['weight']})")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
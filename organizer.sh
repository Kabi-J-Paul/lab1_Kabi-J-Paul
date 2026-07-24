#!/bin/bash

# Exit early if there is no grades.csv to archive
if [ ! -f grades.csv ]; then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

# Create archive directory if it doesn't exist
mkdir -p archive

# Generate timestamp (e.g., 20260723-204512) as required
timestamp=$(date +%Y%m%d-%H%M%S)

# Build the timestamped filename
newname="grades_${timestamp}.csv"

# Move our grades.csv into archive under its new name
mv grades.csv "archive/${newname}" || exit 1

# Resets the workspace with a fresh empty grades.csv
touch grades.csv

# Append this operation to the log (>> accumulates across multiple runs)
echo "${timestamp} | original: grades.csv | archived as: archive/${newname}" >> organizer.log
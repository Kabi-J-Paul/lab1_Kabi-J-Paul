#!/bin/bash


mkdir -p archive

# Generate timestamp (e.g., 20260723-204512)
timestamp=$(date +%Y%m%d-%H%M%S)


newname="grades_${timestamp}.csv"


mv grades.csv "archive/${newname}"

touch grades.csv


echo "${timestamp} | original: grades.csv | archived as: archive/${newname}" >> organizer.log
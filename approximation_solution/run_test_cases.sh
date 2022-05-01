#!/bin/bash
touch test_case_output.txt
{
echo "Running test cases for Longest Path" 
echo "Running Test Case 1"
echo "Test Case 1 Input:"
echo
cat ../exact_solution/test_cases/input1.txt
echo "Test Case 1 Output:"
{ time python3 approximation.py < ../exact_solution/test_cases/input1.txt > test_output.txt; } 2>&1
cat test_output.txt
echo

echo "Running Test Case 2"
echo "Test Case 2 Input:"
echo
cat ../exact_solution/test_cases/input2.txt
echo
echo "Test Case 2 Output:"
{ time python3 approximation.py < ../exact_solution/test_cases/input2.txt > test_output.txt; } 2>&1
cat test_output.txt
echo

echo "Running Test Case 3"
echo "Test Case 3 Input:"
echo
cat ../exact_solution/test_cases/input3.txt
echo
echo "Test Case 3 Output:"
{ time python3 approximation.py < ../exact_solution/test_cases/input3.txt > test_output.txt; } 2>&1
cat test_output.txt
echo

echo "Running Test Case 4"
echo "Test Case 4 Input:"
cat ../exact_solution/test_cases/input5.txt
echo
echo "Test Case 4 Output:"
{ time python3 approximation.py < ../exact_solution/test_cases/input5.txt > test_output.txt; } 2>&1
cat test_output.txt
echo

echo "Running Test Case 5"
echo "Test Case 5 Input:"
cat ../exact_solution/test_cases/input4.txt
echo
echo "Test Case 5 Output:"
{ time python3 approximation.py < ../exact_solution/test_cases/input4.txt > test_output.txt; } 2>&1
cat test_output.txt
echo

} > test_case_output.txt

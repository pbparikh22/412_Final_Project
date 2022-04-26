#!/bin/bash
echo "Running test cases for Longest Path"
echo
echo "Running Test Case 1"
echo
echo "Test Case 1 Input:"
echo
cat input1.txt
echo
echo "Test Case 1 Output:"
python3 ../exact_solution.py < input1.txt
echo
echo "Running Test Case 2"
echo
echo "Test Case 2 Input:"
echo
cat input2.txt
echo
echo "Test Case 2 Output:"
python3 ../exact_solution.py < input2.txt
echo
echo "Generating medium test case"
echo "Number of nodes = 100 Number of edges = 99"
touch generatedInput.txt
python3 test_gen.py > generatedInput.txt
echo "Generated random test case input:"
cat generatedInput.txt
echo
python3 ../exact_solution.py < generatedInput.txt
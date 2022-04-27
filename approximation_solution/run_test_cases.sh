#!/bin/bash
echo "Running test cases for Longest Path Approximation"
echo
echo "Test case 1 input:"
cat ../exact_solution/test_cases/input1.txt
echo
echo "Test case 1 output"
python3 approximation.py < ../exact_solution/test_cases/input1.txt > output1.txt
cat output1.txt
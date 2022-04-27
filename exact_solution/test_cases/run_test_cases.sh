#!/bin/bash
touch test_case_output.txt
{
echo "Running test cases for Longest Path" 
echo "Running Test Case 1"
echo "Test Case 1 Input:"
echo
cat input1.txt
echo "Test Case 1 Output:"
python3 ../exact_solution.py < input1.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output1.txt || echo "TEST 1 FAILED"
echo

echo "Running Test Case 2"
echo "Test Case 2 Input:"
echo
cat input2.txt
echo
echo "Test Case 2 Output:"
python3 ../exact_solution.py < input2.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output2.txt || echo "TEST 2 FAILED"
echo

echo "Running Test Case 3"
echo "Test Case 3 Input:"
echo
cat input3.txt
echo
echo "Test Case 3 Output:"
python3 ../exact_solution.py < input3.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output3.txt || echo "TEST 3 FAILED"
echo

} > test_case_output.txt


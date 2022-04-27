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
python3 ../exact_solution.py < input1.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output1.txt || echo "TEST 1 FAILED"
echo

echo "Running Test Case 2"
echo
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
echo
echo "Test Case 3 Input:"
echo
cat input3.txt
echo
echo "Test Case 3 Output:"
python3 ../exact_solution.py < input3.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output3.txt || echo "TEST 3 FAILED"
echo

echo "Running Test Case 4"
echo
echo "Test Case 4 Input:"
echo
cat input4.txt
echo
echo "Test Case 4 Output:"
python3 ../exact_solution.py < input4.txt > test_output.txt
cat test_output.txt
cmp test_output.txt output4.txt || echo "TEST 4 FAILED"
echo

echo "Generating medium test case"
echo "Number of nodes = 100 Number of edges = 99"
touch generatedInput.txt
python3 test_gen.py > generatedInput.txt
echo "Generated random test case input:"
cat generatedInput.txt
echo
python3 ../exact_solution.py < generatedInput.txt
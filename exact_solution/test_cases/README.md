<h1>Test Case Folder</h1>

<h2>How to run all test cases:</h2>
<p> 
    On the command line this directory run:<br> $./run_test_cases.sh <br> This will run the exact solution on all the input files provided.<br>
    The output of the program will be sent to the file test_case_output.txt for viewing.
</p>

<h3>Types of input files</h3>
<ul>
    <li>input1.txt basic input</li>
    <li>input2.txt medium input</li>
    <li>input3.txt basic directed graph with a cycle</li>
    <li>input4.txt largest input</li>
    <li>input5.txt large input</li>
</ul>

<h3>Types of output files</h3>
<ul>
    <li>output1.txt basic (test case 1)</li>
    <li>output2.txt medium (test case 2)</li>
    <li>output3.txt cycle output (test case 3)</li>
    <li>output4.txt largest output (test case 5)</li>
    <li>output5.txt large output (test case 4)</li>
</ul>

<h4>Misc</h4>
<p>The file test_gen.py was made to create the large input files and will output to STDOUT a graph in the correct input format.</p>
<p>The test_output.txt file is used by run_test_cases.py to compare the output to the expected output.</p>
<p>The generatedInput.txt file is a test file to save generated test inputs created by test_gen.py and is not used as input in run_test_cases.sh.</p>


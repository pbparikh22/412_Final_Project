<h1>Exact Solution</h1>
<h2>Input</h2>

<p>Program exact_solution.py finds the longest path from a single source by all of the paths in the graph<br>
and adding the total lenght of all of the found paths to find a maximum (longest) path in the graph</p>
<p>exact_solution.py takes in a directed graph as input formatted as follows:</p>
<p>Line one contains two ints representing the number of nodes and number of edges in the graph</p>
<p>Remainder of input is formatted as u v w where u is the out node, v is the in node, and w is the weight of that edge.</p>

<h3>Example Input</h3>
<p>
3 3<br>
0 1 3<br>
1 2 3<br>
2 0 3
</p>
<h3>Example Output</h3>
<p>The output of exact_solution.py is the longest path represented as a list populated with the nodes that make up the path.<br></p>
<p>Along with the lenght of that longest path.</p>
<p>
Longest path: [0, 1, 2]<br>
Longest Path Length: 6
</p>
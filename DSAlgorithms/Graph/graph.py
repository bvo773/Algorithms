graph = {
  'A': ['B', 'C'],
  'B': ['D'], 
  'C': ['E'],
  'D': ['F'],
  'E': [],
  'F': [],
}

# param: graph - the graph of nodes | source - starting node to begin traversal
# iteratively, we have to explicitly create a stack to traverse
# if we use push(adding) and pop(removing), it always manipulate the end of the array, since top is the 'top' element
def depthFirstPrintIterative(graph, source):
  stack = [source] #initialize stack with starting node, in this case, some character

  while stack: #while stack is not empty, keep running the algo
    current = stack.pop()
    print(current)
    neighbors = graph[current] # get the neighbors from graph object
    # iterate through the array associate with current node, push its neighbors into the stack
    for neighbor in neighbors: 
      stack.append(neighbor)


# param: graph - the graph of nodes | source - starting node to begin traversal
# recursively - don't need to explicit create a stack since recursion uses the "underlying call stack"! 
depthFirstPrintIterative(graph, 'A')
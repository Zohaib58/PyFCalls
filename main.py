from analyzer.parser import parse_code
#from analyzer.call_graph import generate_call_graph
#from analyzer.visualizer import visualize_call_graph

def main():
    file_path = "tests/test1.py"  # Input Python file
    tree = parse_code(file_path)    # Step 1: Parse the file
    print(tree.dump(tree, indent=4))

    call_graph = generate_call_graph(tree)  # Step 2: Generate call graph
    visualize_call_graph(call_graph)        # Step 3: Visualize the graph

if __name__ == "__main__":
    main()

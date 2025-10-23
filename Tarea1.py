import sys

def minimize_dfa(num_states, alphabet, final_states, transitions):
    """
    Minimizes a DFA using the algorithm from Kozen's Lecture 14.

    Args:
        num_states (int): The number of states in the DFA.
        alphabet (list): The list of symbols in the alphabet.
        final_states (list): The list of final states.
        transitions (list): A 2D list representing the transition table.

    Returns:
        list: A list of tuples, where each tuple represents a pair of
              equivalent states.
    """
    
    # Step 1: Initialize the table of all pairs.
    marked_pairs = set()

    # Step 2: Mark pairs with one final and one non-final state.
    for i in range(num_states):
        for j in range(i + 1, num_states):
            is_i_final = i in final_states
            is_j_final = j in final_states
            if is_i_final != is_j_final:
                marked_pairs.add(tuple(sorted((i, j))))
    
    # Step 3: Iterate until no new pairs are marked.
    while True:
        new_mark_made = False
        for i in range(num_states):
            for j in range(i + 1, num_states):
                pair = tuple(sorted((i, j)))
                if pair not in marked_pairs:
                    for k in range(len(alphabet)):
                        next_state_i = transitions[i][k]
                        next_state_j = transitions[j][k]
                        
                        next_pair = tuple(sorted((next_state_i, next_state_j)))
                        
                        if next_pair in marked_pairs:
                            marked_pairs.add(pair)
                            new_mark_made = True
                            break
        if not new_mark_made:
            break

    # Step 4: Identify unmarked pairs as equivalent.
    equivalent_pairs = []
    for i in range(num_states):
        for j in range(i + 1, num_states):
            if tuple(sorted((i, j))) not in marked_pairs:
                equivalent_pairs.append((i, j))
    
    equivalent_pairs.sort()
    return equivalent_pairs

def main():
    try:
        num_cases = int(sys.stdin.readline().strip())
        for _ in range(num_cases):
            num_states = int(sys.stdin.readline().strip())
            
            alphabet = sys.stdin.readline().strip().split()
            
            final_states_str = sys.stdin.readline().strip().split()
            final_states = [int(s) for s in final_states_str]

            transitions = []
            for _ in range(num_states):
                row = [int(x) for x in sys.stdin.readline().strip().split()]
                transitions.append(row)
            
            equivalent_pairs = minimize_dfa(num_states, alphabet, final_states, transitions)
            
            output_pairs = []
            for p1, p2 in equivalent_pairs:
                output_pairs.append(f"({p1}, {p2})")
            
            print(" ".join(output_pairs))

    except Exception as e:
        # For local testing, can print error, but for submission, it should be silent
        pass

if __name__ == "__main__":
    main()
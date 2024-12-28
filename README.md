# dfa-minimization
![Python Version](https://img.shields.io/badge/python-3.9-blue)

# DFA Minimization Project

This repository contains a Python implementation of Deterministic Finite Automaton (DFA) minimization. The goal of this project is to optimize DFA states by removing unreachable states and merging equivalent states.

## Overview
Finite automata are crucial in computer science for representing and solving problems related to regular languages. DFA minimization ensures that the automaton is in its simplest form, improving efficiency without altering its language recognition capability.

## Features
- **Unreachable State Removal**: Detects and removes states that cannot be reached from the start state.
- **State Equivalence Merging**: Merges states that are equivalent, reducing the overall state count.
- **User Input Support**: Allows users to define their own DFA.
- **Predefined Example**: Includes a default DFA example for demonstration purposes.

## Input Format
The program requires the following inputs:
1. **States**: Comma-separated list of states (e.g., `q0,q1,q2,q3`).
2. **Alphabet**: Comma-separated list of input symbols (e.g., `0,1`).
3. **Transition Function**: Defined as `state,symbol -> target_state` (e.g., `q0,0 -> q1`).
4. **Start State**: A single state (e.g., `q0`).
5. **Accept States**: Comma-separated list of accepting states (e.g., `q3`).

## Example Input
```
States: q0,q1,q2,q3
Alphabet: 0,1
Transition Function:
q0,0 -> q1
q0,1 -> q2
q1,0 -> q0
q1,1 -> q3
q2,0 -> q3
q2,1 -> q0
q3,0 -> q3
q3,1 -> q3
Start State: q0
Accept States: q3
```

## Output Format
The program produces the following outputs:
1. **Original DFA**: Displays the DFA before any transformations.
2. **DFA After Removing Unreachable States**: Shows the DFA with unreachable states removed.
3. **Minimized DFA**: Displays the DFA after state minimization.

### Example Output
```
Original DFA:
States: ['q0', 'q1', 'q2', 'q3']
Alphabet: ['0', '1']
Transition Function:
(q0, 0) -> q1
(q0, 1) -> q2
(q1, 0) -> q0
(q1, 1) -> q3
(q2, 0) -> q3
(q2, 1) -> q0
(q3, 0) -> q3
(q3, 1) -> q3
Start State: q0
Accept States: ['q3']

Minimized DFA:
States: ['State_0', 'State_1', 'State_2', 'State_3']
Alphabet: ['0', '1']
Transition Function:
(State_2, 0) -> State_3
(State_2, 1) -> State_0
(State_3, 0) -> State_3
(State_3, 1) -> State_3
(State_1, 0) -> State_0
(State_1, 1) -> State_3
(State_0, 0) -> State_1
(State_0, 1) -> State_2
Start State: State_2
Accept States: {'State_3'}
```

## Files in the Repository
- **dfa_minimization.py**: Python implementation of the DFA minimization algorithm.
- **README.md**: This file, providing an overview of the project.
- **output_samples.txt**: Contains example inputs and outputs for testing and reference.

## How to Run
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dfa-minimization.git
   ```
2. Navigate to the project directory:
   ```
   cd dfa-minimization
   ```
3. Run the Python script:
   ```
   python dfa_minimization.py
   ```

## Future Enhancements
- **Visualization**: Add graphical representation of the DFA before and after minimization.
- **Performance Analysis**: Include metrics to evaluate optimization improvements.
- **Extended Input Validation**: Enhance error handling for user inputs.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---
Feel free to use, modify, and distribute this code as per the license terms.


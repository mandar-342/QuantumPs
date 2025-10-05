# QuantumPs
This has the problem statement 1 of Fallinduction of QC club.
The code shows how to:

Create a register of qubits

Apply single-qubit gates (H, X, S)

Apply two-qubit gates (CX, CY)

View the statevector and measure all qubits and view simulation results.It also prints the circuit design and displays the statevector of the system before measurement.


1. Importing Required Libraries

from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister

from qiskit.quantum_info import Statevector


This particular part includes all the import work.

QuantumRegister → creates the qubits.

ClassicalRegister → stores the measurement results.

QuantumCircuit → builds the actual circuit.

Statevector → helps simulate the complete quantum state (amplitudes of all possible outcomes).


2. Creating Registers and Circuit

qreg = QuantumRegister(2, 'q')

creg = ClassicalRegister(2, 'c')

qc = QuantumCircuit(qreg, creg)

Here, we create 2 -bit Classical Register and 2- quibt Quantum Register



3. Applying Single-Qubit Gates

qc.h(qreg[0]) 

qc.x(qreg[1])  

qc.s(qreg[0])

H gate puts q0 into superposition (both |0⟩ and |1⟩).

X gate flips q1 (|0⟩ → |1⟩).

S gate adds a 90° phase shift to q0.



4. Applying Two-Qubit Gates

qc.cx(qreg[0], qreg[1]) 

qc.cy(qreg[1], qreg[0])  


CNOT gate flips q1 if q0 is |1⟩.

CY gate applies a Y rotation on q0 if q1 is |1⟩.

These gates create entanglement between the qubits.

5.Displaying the Circuit

qc.draw()

This statement helps us to display the circuit i.e draw it in terminal.


6. Generating the Statevector

state = Statevector.from_instruction(qc)

Converts the entire circuit (before measurement) into a statevector.

The statevector represents all possible outcomes of the system as complex amplitudes.


7. Printing the Statevector

print("StateVector")

for i, amp in enumerate(state):

    print(f"|{i:02b}> : {amp.real:.4f} + {amp.imag:.4f}j, Prob = {abs(amp)**2:.4f}")

Loops through each basis state (|00⟩, |01⟩, |10⟩, |11⟩).

Displays:
1.The real and imaginary parts of each amplitude.

2.The probability of measuring that state


8. Adding Measurement
9. 
qc.measure(qreg, creg)

Measures both qubits and stores their results in classical bits.
Measurement collapses the quantum state to one definite outcome.


9. Simulating Measurement Outcomes

counts = state.sample_counts(shots=1024)

print("\nMeasurement results")
counts = {str(k): int(v) for k, v in counts.items()}

print(counts)

Simulates 1024 shots (measurements) of the circuit.

counts shows how many times each outcome appeared (like {'00': 512, '11': 512}).

Example Output

     ┌───┐┌───┐┌───┐
q_0: ┤ H ├┤ S ├┤ Y ├
     └───┘└───┘└─┬─┘
q_1: ┤ X ├───────■─
     └───┘        

StateVector

|00>: 0.0000+0.7071j, Prob=0.5000

|01>: 0.0000+0.0000j, Prob=0.0000

|10>: 0.0000+0.0000j, Prob=0.0000

|11>: 0.0000+0.7071j, Prob=0.5000

Measurement results:

{'00': 520, '11': 504}



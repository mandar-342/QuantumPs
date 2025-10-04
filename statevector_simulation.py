from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qreg=QuantumRegister(2,'q')
creg=ClassicalRegister(2,'c')
qc=QuantumCircuit(qreg,creg)

qc.h(qreg[0])
qc.x(qreg[1])
qc.s(qreg[0])

qc.cx(qreg[0],qreg[1])
qc.cy(qreg[1],qreg[0])

print(qc.draw())

state=Statevector.from_instruction(qc)
print("StateVector")
for i,amp in enumerate(state):
    print(f"|{i:02b}>:{amp.real:.4f}+{amp.imag:4f}j,Prob={abs}(amp)**2:.4f")

qc.measure(qreg,creg)


counts = state.sample_counts(shots=1024)
print("\nMeasurement results")
print(counts)


"""
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit


def initialize_program():
    qubit = QuantumRegister(2)
    A = qubit[0]
    B = qubit[1]
    
    bit = ClassicalRegister(2)
    a = bit[0]
    b = bit[1]
    
    qc = QuantumCircuit(qubit, bit)
    
    return A, B, a, b, qc

"""
from math import pi
from time import time
from qiskit import QuantumCircuit, transpile, providers
from qiskit_aer import AerSimulator

nu = time()

#from qiskit.providers import aer as ae
sim = AerSimulator()  # make new simulator object

# Create quantum circuit with 3 qubits and 3 classical bits
# (we'll explain why we need the classical bits later)
"""
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.tdg(1)
qc.cx(0,1)
qc.tdg(1)
qc.cx(0,1)
qc.s(1)
qc.t(0)
"""
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.t(1)
qc.cx(0,1)
qc.tdg(1)
qc.t(0)
qc.cx(0,1)



# measure qubits 0, 1 & 2 to classical bits 0, 1 & 2 respectively
qc.measure([0,1], [0,1])

job = sim.run(qc)      # run the experiment
result = job.result()  # get the results
#result.get_counts()    # interpret the results as a "counts" dictionary

x = time() - nu

print("Result: ", result.get_counts())
print(x)
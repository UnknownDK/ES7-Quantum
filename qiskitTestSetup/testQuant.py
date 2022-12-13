from math import pi
from time import time
from qiskit import QuantumCircuit, transpile, providers
from qiskit_aer import AerSimulator

nu = time()

#from qiskit.providers import aer as ae
sim = AerSimulator()  # make new simulator object

# Create quantum circuit with 3 qubits and 3 classical bits
# (we'll explain why we need the classical bits later)
qc = QuantumCircuit(4, 4)
qc.x([1,2])
qc.ry(pi/4, [0, 3])
qc.ry(pi/3, 2)
qc.h([0,2,3])
qc.z(3)
qc.cx(2,0)
qc.cz(0,1)



# measure qubits 0, 1 & 2 to classical bits 0, 1 & 2 respectively
qc.measure([0,1,2,3], [0,1,2,3])

job = sim.run(qc)      # run the experiment
result = job.result()  # get the results
#result.get_counts()    # interpret the results as a "counts" dictionary

x = time() - nu

print("Result: ", result.get_counts())
print(x)
print(qc.__class__)

#from qiskit.algorithms.optimizers import SPSA
#from qiskit_machine_learning.algorithms.classifiers import VQC
#log = OptimizerLog()
#vqc = VQC(feature_map=encodedCircuit,
#          ansatz=ansatz,
#          loss='cross_entropy',
#          optimizer=SPSA(callback=log.update),
#          initial_point=optiPara,
#          )
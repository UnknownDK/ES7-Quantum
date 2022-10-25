from time import time
from qiskit import QuantumCircuit, transpile, IBMQ, providers
#from qiskit.providers import *
from qiskit.visualization import plot_histogram

provider = IBMQ.load_account()


serverList = ['ibm_nairobi', 'ibm_oslo', 'ibmq_manila', 'ibmq_quito', 'ibmq_belem', 'ibmq_lima'] 
#serverList = ['ibmq_nairobi','ibmq_oslo'] #if we need 7 qubits
backendList = []
for i in serverList:
    try:
        backendList.append(provider.get_backend(i))
    except Exception:
        pass


try:
    backend = providers.ibmq.least_busy(backendList)
    print(backend.name)

except providers.ibmq.IBMQError as tnt:
    print("No server: {}".format(tnt))
    exit()




nu = time()


qc = QuantumCircuit(5, 5)
qc.h([0,2])
qc.cx(0,1)
qc.x(3)
qc.cz(2,3)
qc.h(2)
qc.ccx(2,3,4)



qc.measure([0,1,2,3,4], [0,1,2,3,4])


#backend = provider.get_backend('ibmq_quito')

for kk in range(4):
    transQC = transpile(qc, backend, optimization_level=kk)
    print('Optimization Level {}'.format(kk))
    print('Depth:', transQC.depth())
    print('Gate counts:', transQC.count_ops())
    print()

x = time() - nu
print(x)
exit()

job = backend.run(transQC, shots=100)
try:
    job_result = job.result()  # It will block until the job finishes.
    print("The job finished with result {}".format(job_result))
except providers.JobError as ex:
    print("Something wrong happened!: {}".format(ex))
    exit()


resultater = job_result.get_counts()

print("Result: ", resultater)

print(resultater['1111'])


#How to plot

#counts1 = {'00': 499, '11': 501}
#counts2 = {'00': 511, '11': 489}

#data = [counts1, counts2]
test = plot_histogram(resultater)
test.show() #prøv evemtuelt uden det her
input() #Input for at sikre det ikke lukker med det samme

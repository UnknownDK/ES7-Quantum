from qiskit import QuantumCircuit, transpile, IBMQ, providers

#choice of backend
provider = IBMQ.load_account()
backend = IBMQ.get_backend('ibmq_quito')

#Circuit generation
qc = QuantumCircuit(5, 5)
qc.measure([0,1,2,3,4], [0,1,2,3,4])


#Run on quantum computer
job = backend.run(qc, shots=8192)
try:
    job_result = job.result()  # It will block until the job finishes.
    print("The job finished with result {}".format(job_result))
except providers.JobError as ex:
    print("Something wrong happened!: {}".format(ex))
    exit()

#Results 
resultater = job_result.get_counts()
print("Result: ", resultater)
from SimulaQron.general.hostConfig import *
from SimulaQron.cqc.backend.cqcHeader import *
from SimulaQron.cqc.pythonLib.cqc import *
import numpy as np
import random
#from SimulaQron.virtnode.crudeSimulator.simpleEngine import *

from flow import circuit_file_to_flow, count_qubits_in_sequence


seq_out = circuit_file_to_flow("./circuits/circuit1.json")
nQubits= count_qubits_in_sequence(seq_out)
print("qubits needed: {}".format(nQubits))
print("----- out -----")
for s in seq_out:
	s.printinfo()

print("Qubit number=", nQubits)

# Initialize the connection
with CQCConnection("client") as client:
angles=[]
	for i in range(0,nQubits):
		rand_angle=int(256*random.random())rn
		angles.append(rand_angle)
		q = qubit(client)
		q.rot_Y(64) #|+> state
		q.rot_Z(rand_angle)
		client.sendQubit(q,"server")
		#m=q.measure()
	print(m)
		
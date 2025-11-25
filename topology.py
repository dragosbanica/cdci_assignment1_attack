#!/usr/bin/env python3
from mininet.net import Containernet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def run():

    net = Containernet(controller=Controller)
    net.addController("c0")

    print("*** Adding switch")
    s1 = net.addSwitch("s1")

    # -----------------------------
    # Attacker initially isolated
    # -----------------------------
    attacker = net.addDocker(
        "attacker",
        ip="10.0.0.10/24",
        dimage="cloudhopper-host",
        privileged=True,
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/attacker:/data"],
        dcmd="/usr/sbin/sshd -D"
    )
    # NOT ATTACHED to switch

    # -----------------------------
    # MSP
    # -----------------------------
    msp = net.addDocker(
        "msp",
        ip="10.0.0.2/24",
        dimage="cloudhopper-host",
        privileged=True,
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/msp:/data"],
        dcmd="/usr/sbin/sshd -D"
    )
    net.addLink(msp, s1)

    # -----------------------------
    # Clients
    # -----------------------------
    client1 = net.addDocker(
        "client1",
        ip="10.0.0.3/24",
        dimage="cloudhopper-host",
        privileged=True,
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/client1:/data"],
        dcmd="/usr/sbin/sshd -D"
    )
    net.addLink(client1, s1)

    client2 = net.addDocker(
        "client2",
        ip="10.0.0.4/24",
        dimage="cloudhopper-host",
        privileged=True,
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/client2:/data"],
        dcmd="/usr/sbin/sshd -D"
    )
    net.addLink(client2, s1)

    print("*** Starting network")
    net.start()

    # ------------------------------------------------
    # MANUAL NAT fix (safe, works on modern kernels)
    # ------------------------------------------------
    print("*** Applying manual NAT rules")

    # enable forwarding
    nat = msp  # choose any host that has Internet access
    nat.cmd("sysctl -w net.ipv4.ip_forward=1")

    # masquerading (internet access)
    nat.cmd("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")

    print("Attacker is isolated (no link).")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel("info")
    run()

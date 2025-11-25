#!/usr/bin/python3

from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def run():
    setLogLevel("info")
    net = Containernet(controller=Controller)

    net.addController("c0")

    attacker = net.addDocker(
        "attacker",
        dimage="cloudhopper-host",
        ip="10.0.0.1/24",
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/attacker:/data"]
    )

    msp = net.addDocker(
        "msp",
        dimage="cloudhopper-host",
        ip="10.0.0.2/24",
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/msp:/data"]
    )

    client1 = net.addDocker(
        "client1",
        dimage="cloudhopper-host",
        ip="10.0.0.3/24",
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/client1:/data"]
    )

    client2 = net.addDocker(
        "client2",
        dimage="cloudhopper-host",
        ip="10.0.0.4/24",
        cap_add=["NET_ADMIN"],
        volumes=["/home/dragosbanica/CDCI/assignment1/attack/hosts/client2:/data"]
    )

    s1 = net.addSwitch("s1")

    net.addLink(attacker, s1)
    net.addLink(msp, s1)
    net.addLink(client1, s1)
    net.addLink(client2, s1)

    net.start()
    CLI(net)
    net.stop()

if __name__ == "__main__":
    run()

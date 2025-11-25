FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# basic tools and ssh server
RUN apt update && apt install -y \
    iproute2 \
    net-tools \
    netcat-openbsd \
    iputils-ping \
    curl \
    wget \
    nano \
    python3 \
    python3-pip \
    openssh-server

# ssh directory
RUN mkdir /var/run/sshd

# user for ssh pivoting
RUN useradd -m -s /bin/bash user1 && \
    echo "user1:pass123" | chpasswd

# password login for ssh
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# avoid 'Connection closed' on minimal containers
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

# dir for mounted data
RUN mkdir -p /data && chown user1:user1 /data

#disable host key checking 
RUN mkdir -p /root/.ssh && \
    printf "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile /dev/null" > /root/.ssh/config

# ssh server runs in the foreground
CMD ["/usr/sbin/sshd", "-D"]

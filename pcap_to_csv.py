import subprocess
pcaps = ["16-09-27"]
for pcap in pcaps:
    print(pcap+".pcap")
    subprocess.run(['./script.sh',pcap])
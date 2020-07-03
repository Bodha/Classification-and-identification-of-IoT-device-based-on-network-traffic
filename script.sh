#! /bin/bash

tshark -r $1.pcap -T fields -e frame.number -e frame.time_relative -e frame.len -e ip.proto -e frame.protocols -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport  -e ip.dsfield.dscp -e eth.src -e eth.dst -E header=y -E separator=/t > $1.csv
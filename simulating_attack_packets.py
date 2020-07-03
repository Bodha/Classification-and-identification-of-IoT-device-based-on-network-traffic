import numpy as np 
import pandas as pd 
import csv

df = pd.read_csv("16-09-27.csv", sep='\t', dtype={'frame.number':np.int64})
print(df.head(5))

#Selecting 1 of packets randomly of amazon Echo: 44:65:0d:56:cc:d3
echo = df[df['eth.src']=='44:65:0d:56:cc:d3'].sample(n=1,random_state=1)['frame.number']
echo_start = echo.iloc[0]-1

echo_total = len(df[df['eth.src']=='44:65:0d:56:cc:d3'])
echo_10 = int(round(echo_total*.1))

echo_10p = df[(echo_start):][df['eth.src']=='44:65:0d:56:cc:d3']

echo
echo_10pc = pd.DataFrame()
length = len(echo_10p.index)
while(length>echo_10):
    echo_10p = echo_10p.drop(echo_10p.index[length-1])
    length = len(echo_10p.index)
echo_10p


#SIMULATION
import random

i = 0      # DNS ip = 192.168.1.1, des port 53, src port 44239, dscp 0, len 75
while(i<echo_10):
    while(i<2):
        echo_10p.loc[echo_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 75, 17, 'eth:ethertype:ip:udp:dns','192.168.1.240', '192.168.1.1', np.NaN, np.NaN, 23456, 53, 0
        i+=1
    while(i<6):
        echo_10p.loc[echo_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 75, 17, 'eth:ethertype:ip:udp:dns','192.168.1.240', '8.8.8.8', np.NaN, np.NaN, 23456, 53, 0
        i+=1
    rn = random.randint(1,5)           #random integer
    if (rn==1):
        echo_10p.loc[echo_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = random.choice([66,97,74,341,554,1472,148,296,774,2344]), 6, 'eth:ethertype:ip:tcp:tls','192.168.1.240', '62.210.205.141', random.choice([23323,23325,23326]), 443, np.NaN, np.NaN, 0
    else:
        echo_10p.loc[echo_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = random.choice([66,97,74,148,296]), 6, 'eth:ethertype:ip:tcp','192.168.1.240', '62.210.205.141', random.choice([23323,23325,23326]), 443, np.NaN, np.NaN, 0
    i+=1
    
echo_10p

after_echo = echo_10p

# inserting changed row back to overall dataframe

test = df
i = 0
while (i<echo_10):
    test.loc[after_echo.iloc[i].name] = after_echo.iloc[i]
    i+=1
test.head(32045)



#Selecting 1 of packets randomly of amazon Dropcam: 30:8c:fb:2f:e4:b2

dropcam = df[df['eth.src']=='30:8c:fb:2f:e4:b2'].sample(n=1,random_state=1)['frame.number']
dropcam
dropcam_start = echo.iloc[0]-1
dropcam_start
dropcam_total = len(df[df['eth.src']=='30:8c:fb:2f:e4:b2'])
dropcam_10 = int(round(dropcam_total*.1))
print(dropcam_10)
# dropcam_total
dropcam_10p = df[(dropcam_start):][df['eth.src']=='30:8c:fb:2f:e4:b2']
dropcam_10p

dropcam_10pc = pd.DataFrame()
length = len(dropcam_10p.index)
while(length>dropcam_10):
    dropcam_10p = dropcam_10p.drop(dropcam_10p.index[length-1])
    length = len(dropcam_10p.index)
dropcam_10p

#SIMULATION
import random

i = 0      # DNS ip = 192.168.1.1, des port 53, src port 33486, dscp 0, len 79, 
while(i<dropcam_10):
    while(i<2):
        dropcam_10p.loc[dropcam_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 79, 17, 'eth:ethertype:ip:udp:dns','192.168.1.106', '192.168.1.1', np.NaN, np.NaN, 33486, 53, 0
        i+=1
    while(i<6):
        dropcam_10p.loc[dropcam_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 79, 17, 'eth:ethertype:ip:udp:dns','192.168.1.106', '8.8.8.8', np.NaN, np.NaN, 33486, 53, 0
        i+=1
    rn = random.randint(1,5)           #random integer
    if (rn!=1):
        dropcam_10p.loc[dropcam_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 66, 6, 'eth:ethertype:ip:tcp:tls','192.168.1.106', '158.69.38.240', random.choice([45546,45547,45548]), 443, np.NaN, np.NaN, 0
    else:
        dropcam_10p.loc[dropcam_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = random.choice([156, 248, 172, 312]), 6, 'eth:ethertype:ip:tcp','192.168.1.106', '158.69.38.240', random.choice([45546,45547,45548]), 443, np.NaN, np.NaN, 0
    i+=1
    
dropcam_10p

after_dropcam = dropcam_10p

# inserting changed row back to overall dataframe

# test = df
i = 0
while (i<dropcam_10):
    test.loc[after_dropcam.iloc[i].name] = after_dropcam.iloc[i]
    i+=1
test.head(32065)



#Selecting 1 of packets randomly of amazon HP Printer: 70:5a:0f:e4:9b:c0
printer = df[df['eth.src']=='70:5a:0f:e4:9b:c0'].sample(n=1,random_state=1)['frame.number']
printer_start = echo.iloc[0]-1

printer_total = len(df[df['eth.src']=='70:5a:0f:e4:9b:c0'])
printer_10 = int(round(printer_total*.1))
print(printer_10)

printer_10p = df[(printer_start):][df['eth.src']=='70:5a:0f:e4:9b:c0']

# printer
printer_10pc = pd.DataFrame()
length = len(printer_10p.index)
while(length>printer_10):
    printer_10p = printer_10p.drop(printer_10p.index[length-1])
    length = len(printer_10p.index)
print(printer_10p)


#SIMULATION
import random

i = 0      # DNS ip = 192.168.1.1, des port 53, src port 58776, dscp 0, len 98
while(i<printer_10):
    while(i<2):
        printer_10p.loc[printer_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 84, 17, 'eth:ethertype:ip:udp:dns','192.168.1.236', '192.168.1.1', np.NaN, np.NaN, 44675, 53, 0
        i+=1
    while(i<6):
        printer_10p.loc[printer_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = 84, 17, 'eth:ethertype:ip:udp:dns','192.168.1.236', '8.8.8.8', np.NaN, np.NaN, 44675, 53, 0
        i+=1
    rn = random.randint(1,5)           #random integer
    if (rn==1):
        printer_10p.loc[printer_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = random.choice([140,280,356]), 6, 'eth:ethertype:ip:tcp:tls','192.168.1.236', '62.210.177.42', random.choice([44765,44766,44767]), 443, np.NaN, np.NaN, 0
    else:
        printer_10p.loc[printer_10p.iloc[i].name,['frame.len','ip.proto','frame.protocols','ip.src','ip.dst','tcp.srcport','tcp.dstport','udp.srcport','udp.dstport','ip.dsfield.dscp']] = random.choice([66,97,140,280,356,246]), 6, 'eth:ethertype:ip:tcp','192.168.1.236', '62.210.177.42', random.choice([44765,44766,44767]), 443, np.NaN, np.NaN, 0
    i+=1
    
print(printer_10p)

after_printer = printer_10p

# inserting changed row back to overall dataframe

# test = df
i = 0
while (i<printer_10):
    test.loc[after_printer.iloc[i].name] = after_printer.iloc[i]
    i+=1
test.head(79055)


# write to CSV
test.to_csv('simulated_csv.csv',index=None)



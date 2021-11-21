target_ip = '172.21.192.151'
lines = []
target_logs = []
new_target = []
with open("/home/wei/CTF/nsa_codebreaker/OOPS/logins.json") as file:
    for line in file:
        lines.append(line)
for line in lines:
    if target_ip in line:
        target_logs.append(line)

for line in target_logs:
    #print(line[line.find('TimeCreated')+15:-27]) #entire time line
    #print(line[line.find('TimeCreated')+26:-44]) # hour min
    if int(line[line.find('TimeCreated')+26:-47]) < 12:
        new_target.append(line)

for line in new_target:
    if line[line.find('"LogonId:')+10:line.find('"LogonId:')+12] == '0X' and line[line.find('"RemoteHost": "- ('):line.find('"RemoteHost": "- (')+14]:
        print(line[line.find('"LogonId:'):line.find('"LogonId:')+20],line[line.find('TimeCreated')+26:-38])


import socket, hashlib

username = "katant"
blocks = 1000  # Сколько блоков за раз, максимально 1000

soc = socket.socket()
soc.connect(('172.104.243.180', 9999))
ver = soc.recv(3).decode()
print('Server version ->', ver)
while True:
    soc.send(bytes("MJOB,{},{}".format(username, str(blocks)), encoding="utf8"))
    job = ''
    while not ';' in job:
        job += soc.recv(1024).decode()
    s_job = job[:-1].split(",")
    difficulty = s_job[0]
    s_job.pop(0)
    print('Got jobs count ->', len(s_job))
    to_send = ''
    for block in s_job:
        to_hash = block.split(":")[0]
        valid_hash = block.split(":")[1]
        for result in range(100 * int(difficulty) + 1):
            hashed = hashlib.sha1(str(to_hash + str(result)).encode("utf-8")).hexdigest()
            if hashed == valid_hash:
                to_send += str(result) + ","
    soc.send(bytes(to_send[:-1] + ";", encoding="utf8"))
    feedback = ''
    while not ';' in feedback:
        feedback += soc.recv(1024).decode()
    print('Reward ->', feedback.split(',')[1][:-1])

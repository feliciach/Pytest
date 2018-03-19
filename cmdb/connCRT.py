import paramiko


def exec_command(comm,hostname):
 #   hostname = '192.168.8.210'
    username = 'root'
    password = 'jiong1226##'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=22, username=username, password=password)
#    ssh.upload('manage.py','/')
    stdin, stdout, stderr = ssh.exec_command(comm)
    result = stdout.read()
    ssh.close()
    return result
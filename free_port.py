import subprocess

def localhost_free_port():
	netstat_an = subprocess.Popen('netstat -an', shell=True, stdout=subprocess.PIPE)

	output = netstat_an.stdout.read().splitlines()
	output = [str(i) for i in output if '127.0.0.1' in str(i)]

	ports = []
	for i in output:
		port = i[i.find('127.0.0.1')+10:]
		port = port[:port.find(' ')]
		ports.append(port)

	port = 1000
	while port < 2000:
		if str(port) not in ports:
			#print('Puerto Disponible: %s'%port)
			return int(port)
		port += 1

	#print('No se ha encontrado puerto disponible')
	return None
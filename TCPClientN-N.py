import socket
import time

# Endereco IP do servidor e porta que o servidor esta
HOST = '10.0.0.2'
PORT = 5000

# Cria o socket e conecta ao servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

# Recebe o tamanho do buffer de leitura do servidor
sBufferSize = tcp.recv(10)
bufferSize = int(sBufferSize)

# Numero de bytes que a mensagem contem e quantas mensagens serao necessarias enviar
numBytes = 102400
numMensagens = int(numBytes/bufferSize)

# Caso nao seja um numero inteiro "redondo", envia mais uma mensagem
restoMensagem = numBytes%bufferSize
ultimaMensagem = ''
if restoMensagem == 0:
	ultimaMensagem = 'b'
else:
	ultimaMensagem = ('a' * restoMensagem)  + 'b'

# Variaveis medicao de tempo
antes = 0.0
depois = 0.0
total = 0.0

# Envia as mensagens ao servidor
for i in range (0, numMensagens):
	# Strings com 'a' numBytes/numMensagens vezes
	msg = 'a' * bufferSize
	# Tempo de inicio de envio de mensagem
	antes = time.time()
	# Envio e espera de mensagem
	tcp.send(msg)
	response = tcp.recv(1)
	# Tempo apos envio de mensagem e resposta
	depois = time.time()
	total = total + (depois - antes)
# Envia sinal de fim de transmissao
antes = time.time()
tcp.send(ultimaMensagem)
response = tcp.recv(1)
depois = time.time()
total = total + (depois - antes)

# Tempo total gasto para enviar a mensagem e obter resposta do servidor
print 'Tempo de envio', total
tcp.close()

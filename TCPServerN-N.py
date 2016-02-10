import socket
import time

# Endereco IP do servidor e porta que o servidor esta
HOST = '10.0.0.2'
PORT = 5000

# Cria o socket e "escuta" a rede
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

# Define o tamanho do buffer de leitura - Converte para string para mandar como mensagem para o cliente
bufferSize = 1024
sBufferSize = str(bufferSize)

# Escuta a rede e espera conexoes por clientes
while True:
	# Aceita conexao do cliente e informa o tamanho do buffer de leitura
	con, cliente = tcp.accept()
	con.sendto(sBufferSize, cliente)

	while True:
		msg = con.recv(bufferSize)
		# Caractere de fim de mensagem - Encerra o envio de mensagem		
		if 'b' in msg:
			con.sendto('n', cliente)
			break
		# Envia resposta 'y' ao cliente, confirmando o recebimento da mensagem
		con.sendto('y', cliente)
	print 'Envio concluido'
	# Fecha a conexao do cliente para poder atender outro cliente	
	con.close()

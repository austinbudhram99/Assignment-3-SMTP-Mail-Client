from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    mailserver = ('127.0.1.1', 1025)
    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    # Fill in end
    clientSocket.connect(mailserver)
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'ab10067@nyu.edu\r\n'
    # Fill in end
    clientSocket.send(mailfromCommand.encode())
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'test@gmail.com\r\n'
    # Fill in end
    clientSocket.send(rcpttoCommand.encode())
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    # Fill in end
    clientSocket.send(dataCommand.encode())
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send message data.
    # Fill in start
    messageCommand = raw_input('Please enter your message in the following field: \r\n')
    # Fill in end
    clientSocket.send(messageCommand.encode())

    # Message ends with a single period.
    # Fill in start
    messageEndCommand = 'r\n.r\n'
    # Fill in end
    clientSocket.send(messageCommand+messageEndCommand)
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send('QUIT\r\n'.encode())
    # Fill in end
    messageCommand = clientSocket.recv(1024)
    print (messageCommand)
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = '127.0.0.1'
    port = 1025
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket = socket(AF_INET,SOCK_STREAM)
    # Fill in start
    # Fill in end
    clientSocket.connect((mailserver,port))
    # recv = clientSocket.recv(1024)
    # print(recv)
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'.encode()
    clientSocket.send(heloCommand)
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    # clientSocket.send = 'Mail FROM: <ab10067@nyu.edu>\r\n'
    # Fill in end
    # recv1 = clientSocket.recv(1024)
    mailfromCommand = 'MAIL FROM: ab10067@nyu.edu\r\n'
    # Fill in end
    clientSocket.send(mailfromCommand.encode())
    # print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    # Fill in start
    # clientSocket.send('RCPT TO: <smtp.gmail.com>\r\n')
    # Fill in end
    # recv1 = clientSocket.recv(1024)
    # print(recv1)
    rcpttoCommand = 'RCPT TO: <127.0.0.1>\r\n'
    # Fill in end
    clientSocket.send(rcpttoCommand.encode())
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send DATA command and print server response.
    # Fill in start
    
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    # Fill in end
    # clientSocket.send(data.encode())
    # print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send message data.
    # Fill in start
    # clientSocket.send('\r\n')
    # clientSocket.send('TESTING\r\n')
    # clientSocket.send(endmsg)
    # Fill in end
    clientSocket.send('\r\n')
    clientSocket.send('testing\r\n')
    # clientSocket.send(endmsg)

    # Message ends with a single period.
    # Fill in start
    clientSocket.send('.\r\n')
    # Fill in end
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send QUIT command and get server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    # Fill in end
    # recv1 = clientSocket.recv(1024)
    # print(recv1)
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

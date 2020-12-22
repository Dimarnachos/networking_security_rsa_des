from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
from RSA import decrypt
import des

PORT_NUMBER = 5000
SIZE = 8192

# hostName = gethostbyname( '192.168.1.3' )
hostName = gethostbyname('DE1_SoC')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ''
des_key = ''
while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    data = data.decode()
    if data.find('public_key') != -1:  # client has sent their public key\
        # retrieve public key and private key from the received message (message is a string!)
        x = data.split()
        public_key_e = int(x[1])
        public_key_n = int(x[2])
        public = (public_key_e, public_key_n)
        print('public key is : %d, %d' % (public_key_e, public_key_n))
    elif data.find('des_key') != -1:  # client has sent their DES key
        # read the next 8 bytes for the DES key by running (data,addr) = mySocket.recvfrom(SIZE) 8 times and then decrypting with RSA
        i = 0
        public = (public_key_e, public_key_n)
        while i < 8:
            (data, addr) = mySocket.recvfrom(SIZE)
            i = i + 1
        des_key = decrypt(public, data)
        print('DES key is :' + des_key)
        # now we will receive the image from the client
        (data, addr) = mySocket.recvfrom(SIZE)
        # decrypt the image
        ###################################your code goes here####################
        # the received encoded image is in data
        # perform des decryption using des.py
        coder = des.des()
        newdata = coder.decrypt(public, data)
        # the final output should be saved in a byte array called rr_byte
        rr_byte = bytearray()
        # write to file to make sure it is okay
        file2 = open(r'penguin_decrypted.jpg', "wb")
        file2.write(bytes(rr_byte))
        file2.close()
        print('decypting image completed')
        break
    else:
        continue
        # python2: print data ,

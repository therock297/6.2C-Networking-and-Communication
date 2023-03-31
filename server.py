# Import the socket module for networking functionality
import socket

# DNS table with domain name as key and IP address as value
dns_table = {
    "www.google.com": "192.168.1.1",
    "www.facebook.com": "192.168.1.5",
    "www.twitter.com": "192.168.1.6",
    "www.amazon.com": "192.168.1.7",
    "www.netflix.com": "192.168.1.8",
    "www.youtube.com": "192.168.1.9",
    "www.spotify.com": "192.168.1.10"
}

# CNAME record with domain name as key and canonical name as value
cname_record = {
    "www.google.com": "host.google.com",
    "www.facebook.com": "host.facebook.com",
    "www.twitter.com": "host.twitter.com",
    "www.amazon.com": "host.amazon.com",
    "www.netflix.com": "host.netflix.com",
    "www.youtube.com": "host.youtube.com",
    "www.spotify.com": "host.spotify.com"
}

# create UDP socket for server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a local address and port
print("Server is running")
clientSocket.bind(("127.0.0.1", 9990))

# start listening for incoming requests
while True:
    # receive data and address from client
    data, address = clientSocket.recvfrom(1024)

    # print request message
    message = format(address) + " request to fetch data "
    print(message)

    # decode the data received from client
    data = data.decode()

    # look up the IP address for the requested domain name in the DNS table
    ip = dns_table.get(data, "Data not found").encode()

    # look up the CNAME for the requested domain name in the CNAME record
    cname = cname_record.get(data, "name entered").encode()

    # send the IP address and CNAME back to the client
    send = clientSocket.sendto(ip, address)
    send1 = clientSocket.sendto(cname, address)

# Import the socket module for networking functionality
import socket

# Define the server address
serverAddr = "127.0.0.1"
serverPort = 9990

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server address and port
addr = (serverAddr, serverPort)

# Initialize userDecision variable to "Y"
userDecision = "Y"

# Loop until user decides to quit
while userDecision.upper() == "Y":
    # Get user input for domain name
    domain_input = input("Enter domain name for which the IP is needed:")

    # Send the user input to the server
    send = clientSocket.sendto(domain_input.encode(), addr)

    # Receive the IP and CNAME from the server
    data, address = clientSocket.recvfrom(1024)
    cname, address = clientSocket.recvfrom(1024)

    # Decode and format the server reply
    server_reply = data.decode().strip()
    cname_reply = cname.decode().strip()
    message = "The IP for the " + format(cname_reply) + " server is " + format(server_reply)
    print(message)

    # Ask user if they want to continue
    userDecision = (input("Do you want to continue further?(Y/N)"))

# Close the socket
clientSocket.close()

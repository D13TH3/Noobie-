import socket  # Import the socket module for networking

# Define a class to handle the client's operations for the guessing game
class GuessingGameClient:
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host  # Server's IP address to connect to (default is localhost)
        self.port = port  # Server's port number to connect to

    # Method to initiate the game and communicate with the server
    def play(self):
        # Create a TCP socket with IPv4 addressing
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))  # Connect to the server
            print("Connected to the server. Start guessing!")  # Inform the user about connection establishment
            
            while True:  # Infinite loop to keep the game running
                guess = input("Enter your guess (1-100): ")  # Prompt the user to enter a guess
                client_socket.sendall(guess.encode())  # Send the user's guess to the server
                response = client_socket.recv(1024).decode()  # Receive the server's feedback
                print(response)  # Display the server's response to the user
                
                # If the server responds with a win message, exit the game loop
                if response == "Correct! You win!":
                    break

# Define the main function that initializes the client and starts the game
def main():
    client = GuessingGameClient()  # Instantiate the client
    try:
        client.play()  # Start the game and communicate with the server
    except KeyboardInterrupt:
        # Handle clean shutdown when the user interrupts the process (e.g., Ctrl+C)
        print("Stopping client")
    finally:
        pass  # Placeholder for any cleanup operations

# Entry point for the script to start execution
if __name__ == "__main__":
    main()
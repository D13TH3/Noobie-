import random
import socket

# Define the GuessingGameServer class to handle the game server's operations
class GuessingGameServer:
    def __init__(self, host="0.0.0.0", port=7777):
        self.host = host  # The IP address the server will bind to (default: all interfaces)
        self.port = port  # The port number the server will listen on
        self.secret_number = random.randint(1, 100)  # Generate a random secret number between 1 and 100
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket

    # Start the server and handle client connections
    def start(self):
        self.server_socket.bind((self.host, self.port))  # Bind the socket to the specified host and port
        self.server_socket.listen()  # Start listening for incoming connections
        print(f"Server listening on {self.host}:{self.port}")

        while True:  # Continuously accept new connections
            conn, addr = self.server_socket.accept()  # Accept a new client connection
            print(f"Connected by {addr}")  # Log the client's address
            with conn:  # Ensure the connection is properly closed when done
                while True:
                    data = conn.recv(1024).decode().strip()  # Receive data from the client
                    if not data:  # If no data is received, break the loop
                        break
                    try:
                        guess = int(data)  # Convert the received data to an integer
                        diff = abs(guess - self.secret_number)  # Calculate the difference from the secret number

                        # Check if the guess is lower, higher, or equal to the secret number
                        if guess < self.secret_number:
                            response = "Too low! "  # Hint for lower guess
                        elif guess > self.secret_number:
                            response = "Too high! "  # Hint for higher guess
                        else:
                            response = "Correct! You win!"  # Player guessed correctly
                            self.secret_number = random.randint(1, 100)  # Reset the secret number for a new game

                        # Provide additional feedback based on how close the guess was
                        if diff <= 5:
                            response += "Very Good!"
                        elif diff <= 10:
                            response += "Good!"
                        else:
                            response += "Fair!"

                        conn.sendall(response.encode())  # Send the response back to the client
                    except ValueError:
                        # Handle the case where the input is not a valid number
                        conn.sendall("Invalid input! Please enter a number.".encode())

    # Stop the server and release the socket
    def stop(self):
        self.server_socket.close()  # Close the server socket


# Main function to initialize and start the game server
def main():
    server = GuessingGameServer()  # Create an instance of the GuessingGameServer
    try:
        server.start()  # Start the server
    except KeyboardInterrupt:
        # Handle graceful shutdown when the user interrupts (Ctrl+C)
        print("\nServer shutting down...")
    finally:
        server.stop()  # Ensure the socket is properly closed on shutdown


# Entry point for the script
if __name__ == "__main__":
    main()
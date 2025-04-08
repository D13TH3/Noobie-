import socket  # Import the socket module for networking

# Define a class to handle the client's operations for the guessing game
class NumberGuessClient:
    def __init__(self, server_ip="127.0.0.1", server_port=8888):  # Changed port to 8888
        self.server_ip = server_ip
        self.server_port = server_port

    def start_game(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.server_ip, self.server_port))
            print("Connected to the server. Start guessing!")

            while True:
                user_input = input("Enter your guess (1-100): ")
                sock.sendall(user_input.encode())
                feedback = sock.recv(1024).decode()
                print(feedback)

                if feedback.startswith("Correct!"):
                    break

def main():
    game_client = NumberGuessClient()
    try:
        game_client.start_game()
    except KeyboardInterrupt:
        print("Client interrupted.")
    finally:
        pass

if __name__ == "__main__":
    main()
    
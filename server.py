import random
import socket

class NumberGuessServer:
    def __init__(self, listen_ip="127.0.0.1", listen_port=8888):  # Changed port to 8888
        self.listen_ip = listen_ip
        self.listen_port = listen_port
        self.target_number = random.randint(1, 100)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def launch(self):
        self.server_socket.bind((self.listen_ip, self.listen_port))
        self.server_socket.listen()
        print(f"Server listening on {self.listen_ip}:{self.listen_port}")

        while True:
            client_conn, client_addr = self.server_socket.accept()
            print(f"Connected by {client_addr}")
            with client_conn:
                while True:
                    raw_data = client_conn.recv(1024).decode().strip()
                    if not raw_data:
                        break
                    try:
                        user_guess = int(raw_data)
                        difference = abs(user_guess - self.target_number)

                        if user_guess < self.target_number:
                            feedback = "Too low! "
                        elif user_guess > self.target_number:
                            feedback = "Too high! "
                        else:
                            feedback = "Correct! You win!"
                            self.target_number = random.randint(1, 100)

                        if "Correct!" not in feedback:
                            if difference <= 5:
                                feedback += "Very Good!"
                            elif difference <= 10:
                                feedback += "Good!"
                            else:
                                feedback += "Fair!"

                        client_conn.sendall(feedback.encode())
                    except ValueError:
                        client_conn.sendall("Invalid input! Please enter a number.".encode())

    def shutdown(self):
        self.server_socket.close()

def main():
    game_server = NumberGuessServer()
    try:
        game_server.launch()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        game_server.shutdown()

if __name__ == "__main__":
    main()
    
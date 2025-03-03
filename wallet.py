import hashlib
import time

class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.address = self.generate_address()

    def generate_address(self):
        # Simulate address generation using a hash of the owner's name and timestamp
        data = f"{self.owner}{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added {amount} to {self.owner}'s wallet. New balance: {self.balance}")
        else:
            print("Amount must be greater than 0.")

    def send_funds(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Sent {amount} from {self.owner}'s wallet to {recipient.owner}'s wallet.")
            print(f"{self.owner}'s new balance: {self.balance}")
            print(f"{recipient.owner}'s new balance: {recipient.balance}")

    def __str__(self):
        return f"Wallet [Owner: {self.owner}, Address: {self.address}, Balance: {self.balance}]"

# Example usage
if __name__ == "__main__":
    # Create two wallets
    alice_wallet = Wallet("Alice")
    bob_wallet = Wallet("Bob")

    # Print initial wallet details
    print(alice_wallet)
    print(bob_wallet)

    # Add funds to Alice's wallet
    alice_wallet.add_funds(100)

    # Send funds from Alice to Bob
    alice_wallet.send_funds(bob_wallet, 50)

    # Print updated wallet details
    print(alice_wallet)
    print(bob_wallet)

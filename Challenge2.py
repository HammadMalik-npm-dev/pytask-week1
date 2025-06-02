class User:
    def __init__(self, username, email):
        if not username or not email or '@' not in email:
            raise ValueError("Invalid username or email")
        self.username = username
        self.email = email

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"


class Message:
    def __init__(self, sender, recipient, content):
        if not isinstance(sender, User) or not isinstance(recipient, User):
            raise ValueError("Sender and recipient must be User instances")
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}: {self.content}"


class ChatManager:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        if any(u.username == user.username for u in self.users):
            print(f"User '{user.username}' already exists!")
        else:
            self.users.append(user)
            print(f"User '{user.username}' added.")

    def send_message(self, sender_username, recipient_username, content):
        sender = next((u for u in self.users if u.username == sender_username), None)
        recipient = next((u for u in self.users if u.username == recipient_username), None)

        if not sender:
            print(f"Sender '{sender_username}' not found.")
            return
        if not recipient:
            print(f"Recipient '{recipient_username}' not found.")
            return

        msg = Message(sender, recipient, content)
        self.messages.append(msg)
        print(f"Message sent: {msg}")

    def show_conversation(self, user1, user2):
        print(f"Conversation between '{user1}' and '{user2}':")
        for msg in self.messages:
            if {msg.sender.username, msg.recipient.username} == {user1, user2}:
                print(f"  {msg}")


if __name__ == "__main__":
    manager = ChatManager()

    user1 = User("alice", "alice@example.com")
    user2 = User("bob", "bob@example.com")
    user3 = User("charlie", "charlie@example.com")

    manager.add_user(user1)
    manager.add_user(user2)
    manager.add_user(user3)

    manager.send_message("alice", "bob", "Hi Bob, how are you?")
    manager.send_message("bob", "alice", "Hey Alice! I'm good, thanks.")
    manager.send_message("charlie", "bob", "Hello Bob, want to join the project?")

    manager.show_conversation("alice", "bob")

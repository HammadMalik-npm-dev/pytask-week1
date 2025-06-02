class User:
    def __init__(self, username, email):
        if not username or not email or '@' not in email:
            raise ValueError("Invalid username or email")
        self.username = username
        self.email = email
    
    def __str__(self):
        return f"User(username={self.username}, email={self.email})"
    
    def send_message(self, msg, recipient):
        print(f"{self.username} sends message to {recipient.username}: {msg}")


class Intern(User):
    def __init__(self, username, email, mentor=None):
        super().__init__(username, email)
        self.mentor = mentor
    
    def __str__(self):
        mentor_name = self.mentor.username if self.mentor else "None"
        return f"Intern(username={self.username}, email={self.email}, mentor={mentor_name})"
    
    def request_help(self, question):
        if self.mentor:
            print(f"{self.username} asks mentor {self.mentor.username}: {question}")
        else:
            print(f"{self.username} has no mentor assigned.")


class Mentor(User):
    def __init__(self, username, email, expertise):
        super().__init__(username, email)
        self.expertise = expertise
    
    def __str__(self):
        return f"Mentor(username={self.username}, email={self.email}, expertise={self.expertise})"
    
    def give_advice(self, intern, advice):
        print(f"Mentor {self.username} advises {intern.username}: {advice}")

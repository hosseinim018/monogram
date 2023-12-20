class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

class GameHighScore:
    def __init__(self, position: int, user: User, score: int):
        self.position = position
        self.user = user
        self.score = score

# Create a sample User object
user = User(user_id=123456, username="JohnDoe")

# Create a sample GameHighScore object
game_high_score = GameHighScore(position=1, user=user, score=1000)

# Access the fields of the GameHighScore object
print(f"Position: {game_high_score.position}")
print(f"User ID: {game_high_score.user.user_id}")
print(f"Username: {game_high_score.user.username}")
print(f"Score: {game_high_score.score}")
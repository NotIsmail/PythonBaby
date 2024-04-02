class Games:
    def __init__(self,games,genre) -> None:
        self.games = games
        self.genre = genre

def main():
    user=get_game()
    user.genre="Action"
    print(user)

def get_game():
    game=input("Enter your favorite game:")
    genre=input("What is the genre of that game?")
    return Games(game,genre)

if __name__=="__main__":
    main()
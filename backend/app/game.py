import threading
import time
from fastapi_socketio import SocketManager

sio = SocketManager()

def collect_votes(player_names):
    votes = []
    for player in player_names:
        vote = get_vote_from_player(player)
        votes.append(vote)
    return votes

def get_vote_from_player(player):
    vote = None
    timer = threading.Timer(30.0, lambda: None)
    timer.start()
    
    # Simulate player voting process
    print(f"{player}, vous avez 30 secondes pour voter.")
    start_time = time.time()
    while time.time() - start_time < 30:
        vote_input = input(f"{player}, entrez votre vote (ou appuyez sur Entrée pour passer): ")
        if vote_input:
            try:
                vote = int(vote_input)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    timer.cancel()
    return vote
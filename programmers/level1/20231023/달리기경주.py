# 예상 시간복잡도: O(N)

def solution(players, callings):
    players_ranking = {player: int(idx) for idx, player in enumerate(players)}
    for call in callings:
        current_rank = players_ranking[call] 
        players_ranking[call] -= 1
        players_ranking[players[current_rank - 1]] += 1
        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]
    return players

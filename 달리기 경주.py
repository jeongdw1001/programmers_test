# 문제 설명
# 얀에서는 매년 달리기 경주가 열립니다. 
# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 
# 추월한 선수의 이름을 부릅니다. 
# 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 
# 순서대로 달리고 있을 때, 
# 해설진이 "soe"선수를 불렀다면 
# 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
# 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.
# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 
# 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 
# 배열에 담아 return 하는 solution 함수를 완성해주세요.

# 다른 풀이1
def solution(players, callings):    
    player_dict = {player:rank for rank, player in enumerate(players)}
    rank_dict = {rank:player for rank, player in enumerate(players)}
    
    for call in callings:
        rank = player_dict[call]
        
        player_dict[rank_dict[rank-1]], player_dict[rank_dict[rank]] = player_dict[rank_dict[rank]], player_dict[rank_dict[rank-1]]
        rank_dict[rank-1], rank_dict[rank] = rank_dict[rank], rank_dict[rank-1]
    
    return list(rank_dict.values())

# 다른 풀이2
def solution(players, callings):
    idx = {rank:player for rank, player in enumerate(players)} # 등수 : 선수 딕셔너리
    r = {player:rank for rank, player in enumerate(players)} # 선수 : 등수 딕셔너리

    for i in callings:
        loc = r[i]  # 현재 등수
        loc2 = loc-1  # 앞 등수
        pre_player = idx[loc2]  # 앞 선수

        idx[loc] = pre_player  # 등수 : 선수 딕셔너리에서 현재 등수의 선수를 앞 선수로 업 (앞 선수에 현재 등수 loc 부여)
        idx[loc2] = i  # 등수 : 선수 딕셔너리에서 앞 등수의 선수를 현재 선수로 다운 (현재 선수 i에 앞 등수 loc2 부여)

        r[i] = loc2  # 선수 : 등수 딕셔너리에서 현재 선수의 등수를 앞 등수로 업
        r[pre_player] = loc # 선수 : 등수딕셔너리에서 앞 선수의 등수를 현재 등수로 다운

    return list(idx.values())


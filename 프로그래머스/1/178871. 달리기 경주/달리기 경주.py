def solution(players, callings):
    dic_ = {}
    for i,name in enumerate(players):
        dic_[name] = i
    
    for name in callings:
        idx = dic_.get(name)
        players[idx], players[idx-1] = players[idx-1], players[idx]
        dic_[players[idx-1]] = idx-1
        dic_[players[idx]] = idx
        
    return players
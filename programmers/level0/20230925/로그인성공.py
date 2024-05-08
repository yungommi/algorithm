# 예상 시간복잡도: O(n)

def solution(id_pw, db):
    db_ = {}
    for itm in db:
        db_[itm[0]] = itm[1]
    if id_pw[0] in db_:
        if db_[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail" 
        


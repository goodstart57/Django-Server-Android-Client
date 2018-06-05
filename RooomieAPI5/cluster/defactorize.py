def df_GENDER(gender):
    if gender==1:
        return "남성"
    else:
        return "여성"

def df_CLEAN(clean):
    if clean==5: return "매일 청소한다."
    elif clean==4: return "3일에 한 번 한다."
    elif clean==3: return "일주일에 한 번 한다."
    elif clean==2: return "보름에 한 번 한다."
    else: return "하고 싶을 때 한다."

def df_YASIK(yasik):
    if yasik==3: return "매우 잘 먹는다."
    elif yasik==2: return "자주 먹는다."
    elif yasik==1: return "가끔 먹는다."
    else: return "안 먹는다."

def df_CHARACTER(character):
    character=int(character)
    if character<0: return "내향적인 성향"
    elif character==0: return "중립적인 성향"
    else: return "외향적인 성향"

def df_OUTACT(outact):
    if outact==4: return "4개 이상"#"대외활동 4개 이상 하고 있다."
    elif outact==3: return "3개"#"대외활동 3개 하고 있다."
    elif outact==2: return "2개"#"대외활동 2개 하고 있다."
    elif outact==1: return "1개"#"대외활동 1개 하고 있다."
    else: return "0개"#"대외활동 하지 않는다."

def df_DRINK(drink):
    return str(drink)+"병"#"주량은 "+str(drink)+"병"

def df_FREQ_DRINK(fdrink):
    if fdrink==6: return "주 4회 이상 마신다."
    elif fdrink==5: return "주 3회 마신다."
    elif fdrink==4: return "주 2회 마신다."
    elif fdrink==3: return "주 1회 마신다."
    elif fdrink==2: return "한달에 2번 마신다."
    elif fdrink==1: return "한달에 한 번 마신다."
    else: return "안 마신다."

def df_SMOKE(smoke):
    if smoke==1: return "흡연자"
    else: return "비흡연자"

def df_op_age(opage):
    if opage==3: return "나보다 나이가 많았으면 좋겠다."
    elif opage==2: return "나랑 동갑이었으면 좋겠다."
    elif opage==1: return "나보다 어렸으면 좋겠다."
    else: return "상관 없다."

def df_op_grade(grade):
    if grade==3: return "나보다 나이가 많았으면 좋겠다."
    elif grade==2: return "나랑 동갑이었으면 좋겠다."
    elif grade==1: return "나보다 어렸으면 좋겠다."
    else: return "상관 없다."

def df_op_clean(clean):
    if clean==3: return "나보다 깨끗했으면 좋겠다."
    elif clean==2: return "나와 비슷하면 좋겠다."
    elif clean==1: return "나보다 청소를 덜 하면 좋겠다."
    else: return "상관 없다."

def df_op_yasik(ya):
    if ya==4: return "매우 잘 먹었으면 좋겠다."
    elif ya==3: return "자주 먹었으면 좋겠다."
    elif ya==2: return "가끔 먹었으면 좋겠다."
    elif ya==1: return "안 먹었으면 좋겠다."
    else: return "상관 없다."

def df_op_outact(oa):
    if oa==3: return "그 이상이면 좋겠다."
    elif oa==2: return "2개면 좋겠다."
    elif oa==1: return "1개면 좋겠다."
    else: return "상관 없다."

def df_op_fdrink(fdrink):
    if fdrink==4: return "매일 마셨으면 좋겠다."
    elif fdrink==3: return "자주 마셨으면 좋겠다."
    elif fdrink==2: return "가끔 마셨으면 좋겠다."
    elif fdrink==1: return "안 마셨으면 좋겠다."
    else: return "상관 없다."

def df_op_drink(drink):
    if drink==3: return "나보다 잘 마시면 좋겠다."
    elif drink==2: return "나와 비슷하면 좋겠다."
    elif drink==1: return "나보다 덜 잘마시면 좋겠다"
    else: return "상관 없다."

def df_op_smoke(smoke):
    if smoke==2: return "흡연자면 좋겠다."
    elif smoke==1: return "비흡연자면 좋겠다."
    else: return "상관 없다."

def df_AGREE_WITH(agree):
    if agree==1: return "예, 괜찮아요"
    else: return "아니요, 안 돼요" # 아니요, 안 돼요





def f_GENDER(gender):
    if gender=="남성": return 1
    else: return 2 # 여성

def f_CLEAN(clean):
    if clean=="매일 청소한다.": return 5
    elif clean=="3일에 한번 꼴로 한다.": return 4
    elif clean=="일주일에 한번 정도 한다.": return 3
    elif clean=="보름에 한번 한다.": return 2
    else: return 1 #"하고싶을 때 한다."

def f_YASIK(yasik):
    if yasik=="매우 잘 먹는다.": return 3
    elif yasik=="자주 먹는다.": return 2
    elif yasik=="가끔 먹는다.": return 1
    else: return 0 # "안먹는다."

def f_CHARACTER(character):
    result = 0
    for ch in character:
        if ch=="외향적이다.": result = result + 2
        elif ch in ["충동적이다.", "의지가 강한 편이다.", "독립심이 강하다.", "적극적이다.", "덤벙댄다."]:
            result = result + 1
        elif ch=="내향적이다.": result = result -2
        else: result = result - 1  # 조금 내향적인 성격들
    return result

def f_OUTACT(outact):
    if outact=="4개 이상": return 4 #"대외활동 4개 이상 하고 있다."
    elif outact=="3개": return 3 #"대외활동 3개 하고 있다."
    elif outact=="2개": return 2#"대외활동 2개 하고 있다."
    elif outact=="1개": return 1#"대외활동 1개 하고 있다."
    else: return  0# "0개"# "대외활동 하지 않는다."

def f_FREQ_DRINK(fdrink):
    if fdrink=="그 이상 마신다.": return 6
    elif fdrink=="일주일에 3번 마신다.": return 5
    elif fdrink=="일주일에 2번 마신다.": return 4
    elif fdrink=="일주일에 1번 마신다.": return 3
    elif fdrink=="한 달에 2,3번 마신다.": return 2
    elif fdrink=="한 달에 1번 마신다.": return 1
    else: return 0 # "안마신다."

def f_SMOKE(smoke):
    if smoke=="예, 맞습니다.": return 1 # 흡연자
    else: return 0 # "비흡연자"

def f_DRINK(drink):
    return drink[0]


def f_OP_SMOKE(smoke):
    if smoke=="흡연자": return 1 # 흡연자
    else: return 0 # "비흡연자"

def f_AGREE_WITH(agree):
    if agree=="예, 괜찮아요": return 1
    else: return 0 # 아니요, 안 돼요

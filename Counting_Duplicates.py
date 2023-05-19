def duplicate_count(t):
    text=t.lower()
    txt=[]
    duplicate=[]
    score=0
    for i in text:
        txt.append(i)

    dub=set([x for x in txt if txt.count(x)>1])
    for a in dub:
        score +=1

    print(score)

    









x=input("Enter here:")
duplicate_count(x)

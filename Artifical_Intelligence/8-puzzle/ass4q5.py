import copy
visited=[]
q=[]

def uniform_cost_search(g,S,G):
    global visited
    l=q.pop(0)
    cost=l[0]
    node=l[1][-1]
    while 1:
        if node=='G':
            print("The cost is:",cost)
            print("The path is:",l[1])
            return
        for i in g[node]:
            q.append([cost+i[1],l[1]+[i[0]]])
            
        q.sort()
        l=q.pop(0)
        cost=l[0]
        node=l[1][-1]
        


def main():
    g={'S':[['A',1],['B',5],['C',15]],'A':[['S',1],['G',10]],'B':[['S',5],['G',5]],'C':[['S',15],['G',5]],'G':[['A',10],['B',5],['C',5]]}
    global q
    global visited
    q.append([0,['S']])
    visited+='S'
    uniform_cost_search(g,'S','G')
    


if __name__=="__main__":
    main()

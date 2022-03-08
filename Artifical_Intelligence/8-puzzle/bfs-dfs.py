import copy
from pprint import pprint
def find_idx(state,element):                  #for finding index of element 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == element:
                return([i,j])

def swap(state,o1,o2,p1,p2):                  #finding the next state
    new_state=copy.deepcopy(state)
    new_state[o1][o2],new_state[p1][p2]=new_state[p1][p2],new_state[o1][o2]
    return new_state

def find_nxt_st(string, pos,c_st):            #finding index of next state
    if string=="up":
        id1=pos[0]-1
        id2=pos[1]
    elif string=="down":
        id1=pos[0]+1
        id2=pos[1]
    elif string=="left":
        id1=pos[0]
        id2=pos[1]-1
    else:
        id1=pos[0]
        id2=pos[1]+1
    n_st=swap(c_st,pos[0],pos[1],id1,id2)
    return n_st
        
d_visited=[]
b_visited=[]
flag=0
d_moves=0
b_moves=0

def bfs(current_state,goal_state):
    nxt_st=[]
    global b_visited
    global b_moves
    queue=[]
    b_visited.append(current_state)
    b_moves+=1
    while current_state!=goal_state:
         pos=find_idx(current_state,0)
         if pos[0]>0:
             nxt_st=find_nxt_st("up",pos,current_state)
             if nxt_st not in b_visited:
                 queue.append(nxt_st)
         if pos[0]<2:
             nxt_st=find_nxt_st("down",pos,current_state)
             if nxt_st not in b_visited:
                 queue.append(nxt_st)
         if pos[1]>0:
             nxt_st=find_nxt_st("left",pos,current_state)
             if nxt_st not in b_visited:
                 queue.append(nxt_st)
         if pos[1]<2:
             nxt_st=find_nxt_st("right",pos,current_state)
             if nxt_st not in b_visited:
                 queue.append(nxt_st)
         current_state=queue.pop(0)
         b_visited.append(current_state)
         b_moves+=1

def dfs(current_state,goal_state):
    nxt_st=[]
    global d_visited
    global flag
    global d_moves
    d_visited.append(current_state)
    d_moves+=1
    if current_state==goal_state:
        flag=1
        return
    pos=find_idx(current_state,0)
    if flag==0 and pos[0]!=0:
        nxt_st=find_nxt_st("up",pos,current_state)
        if nxt_st not in d_visited:
            dfs(nxt_st,goal_state)
    if flag==0 and pos[0]!=2:
        nxt_st=find_nxt_st("down",pos,current_state)
        if nxt_st not in d_visited:
            dfs(nxt_st,goal_state)
    if flag==0 and pos[1]!=0:
        nxt_st=find_nxt_st("left",pos,current_state)
        if nxt_st not in d_visited:
            dfs(nxt_st,goal_state)
    if flag==0 and pos[1]!=2:
        nxt_st=find_nxt_st("right",pos,current_state)
        if nxt_st not in d_visited:
            dfs(nxt_st,goal_state)
    return
"""

def dfs(initial_state,final_state):
    c_st=copy.deepcopy(initial_state)              
    pos=find_idx(c_st,0)
    nxt_st=[]
    global visited
    global flag
    global moves
    visited.append(c_st)
    print(visited)
    moves+=1
    if c_st==final_state:
        print(flag)
        flag=1
        return
    if pos in ([1,0],[1,1],[1,2],[2,0],[2,1],[2,2]):               #checking if up move is possible
        nxt_st=find_nxt_st("up",pos,c_st)
        print(nxt_st)
        if nxt_st not in visited and flag==0:                                  #checking if next move has not been visited yet
            dfs(nxt_st,final_state)
    if pos in ([0,0],[0,1],[0,2],[1,0],[1,1],[1,2]):
        nxt_st=find_nxt_st("down",pos,c_st)
        print(pos,nxt_st)
        if nxt_st not in visited and flag==0:
            dfs(nxt_st,final_state)
    if pos in ([0,0],[0,1],[1,0],[1,1],[2,0],[2,1]):
        nxt_st=find_nxt_st("right",pos,c_st)
        print(pos,nxt_st)
        if nxt_st not in visited and flag==0:
            dfs(nxt_st,final_state)
    if pos in ([0,2],[0,1],[1,2],[1,1],[2,2],[2,1]):
        nxt_st=find_nxt_st("left",pos,c_st)
        if nxt_st not in visited and flag==0:
            dfs(nxt_st,final_state)
    return
        """




def main():
    initial_state = [[1, 2, 3],[ 8, 0, 4], [7, 6, 5]]
    final_state = [[8,1 ,3 ],[ 7, 0, 4],[ 6, 2, 5]]
    dfs(initial_state,final_state)
    bfs(initial_state,final_state)
    print("Using dfs:")
    print("No of moves:",d_moves)
    print("States:")
    for i in d_visited:
        for j in i:
            print(j)
        print()
    
    print("Using bfs:")
    print("No of moves:",b_moves)
    print("States:")
    for i in b_visited:
        for j in i:
            print(j)
        print()
    
    

if __name__=="__main__":
    main()
    

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

def heuristic(state,goal_state):
    cnt=0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j]!=goal_state[i][j]:
                cnt+=1
    return cnt
        
d_visited=[]
b_visited=[]
flag=0
d_moves=0
b_moves=0

def bfs(current_state,goal_state):
    nxt_st=[]
    global b_visited
    global b_moves
    global flag
    queue=[]
    prev_cnt=heuristic(current_state,goal_state)
    b_visited.append(current_state)
    b_moves+=1
    while current_state!=goal_state:
         pos=find_idx(current_state,0)
         if pos[0]>0:
             nxt_st=find_nxt_st("up",pos,current_state)
             if nxt_st not in b_visited:
                 cnt=heuristic(nxt_st,goal_state)
                 if(cnt<prev_cnt):
                     queue.append([cnt,nxt_st])
                     flag=1
         if pos[1]<2 and flag==0:
             nxt_st=find_nxt_st("right",pos,current_state)
             if nxt_st not in b_visited:
                 cnt=heuristic(nxt_st,goal_state)
                 if(cnt<prev_cnt):
                     queue.append([cnt,nxt_st])
                     flag=1
         if pos[1]>0 and flag==0:
             nxt_st=find_nxt_st("left",pos,current_state)
             if nxt_st not in b_visited:
                 cnt=heuristic(nxt_st,goal_state)
                 if(cnt<prev_cnt):
                     queue.append([cnt,nxt_st])
                     flag=1
         if pos[0]<2 and flag==0:
             nxt_st=find_nxt_st("down",pos,current_state)
             if nxt_st not in b_visited:
                 cnt=heuristic(nxt_st,goal_state)
                 if(cnt<prev_cnt):
                     queue.append([cnt,nxt_st])
                     flag=1
         flag=0 
         l=queue.pop(0)
         current_state=l[1]
         prev_cnt=l[0]
         b_visited.append(current_state)
         b_moves+=1

def main():
    initial_state = [[2, 0, 3],[ 1, 8, 4], [7, 6, 5]]
    final_state = [[1,2,3],[8,0,4],[7,6,5]]
    bfs(initial_state,final_state)
    print("Using bfs:")
    print("No of moves:",b_moves)
    print("States:")
    for i in b_visited:
        for j in i:
            print(j)
        print()
if __name__=="__main__":
    main()
    



import copy
visited=[]
q=[]

def generate_children(cur_state,depth):
    depth=depth+1
    for i in range(len(cur_state)):
        if(len(cur_state[i])>0):
            temp1=copy.deepcopy(cur_state)
            x=temp1[i].pop()
            for j in range(len(temp1)):
                if j!=i:
                    temp2=copy.deepcopy(temp1)
                    temp2[j]+=x
                    if temp2 not in visited:
                        q.append([temp2,depth])
                        
def iterative_dfs(initial_state,final_state,depthlimit):
    depth=0
    global visited
    global q
    cur_state=copy.deepcopy(initial_state)
    while(1):
        if(cur_state==final_state):
            print("Final state found at depth ",depth)
            print("Intermediate states are:")
            for i in visited:
                for j in i:
                    print(j)
                print()
            return True
        if depth<=depthlimit:
            generate_children(cur_state,depth)
        if len(q)<=0:
            print("Solution does not exist")
            return False
        nxt=q.pop()
        cur_state=nxt[0]
        depth=nxt[1]
        visited.append(cur_state)

        
def main():
    initial_state=[[],['A'],['B','C']]
    final_state=[[],[],['A','B','C']]
    global visited
    global queue
    visited.append(initial_state)
    depth_limit=1
    while(1):
        print(depth_limit)
        status=iterative_dfs(initial_state,final_state,depth_limit)
        if status== True:
            break
        depth_limit+=1
        visited.clear()
        visited.append(initial_state)
        q.clear()
    
if __name__ =="__main__":
    main()







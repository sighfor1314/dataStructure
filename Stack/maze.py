import random
# dirs=[(0,1),(1,0),(0,-1),(-1,0)] #當前位置四個方向的偏移量
# path=[]              #存找到的路徑
#
# def mark(maze,pos):  #給迷宮maze的位置pos標"2"表示“倒過了”
#     maze[pos[0]][pos[1]]=2
#
# def passable(maze,pos): #檢查迷宮maze的位置pos是否可通行
#     return maze[pos[0]][pos[1]]==0
#
# def find_path(maze,pos,end):
#     mark(maze,pos)
#     if pos==end:
#         print(pos,end=" ")  #已到達出口，輸出這個位置。成功結束
#         path.append(pos)
#         return True
#     for i in range(4):      #否則按四個方向順序檢查
#         nextp=pos[0]+dirs[i][0],pos[1]+dirs[i][1]
#         #考慮下一個可能方向
#         if passable(maze,nextp):        #不可行的相鄰位置不管
#             if find_path(maze,nextp,end):#如果從nextp可達出口，輸出這個位置，成功結束
#                 print(pos,end=" ")
#                 path.append(pos)
#                 return True
#     return False
#
# def see_path(maze,path):     #使尋找到的路徑可視化
#     for i,p in enumerate(path):
#         if i==0:
#             maze[p[0]][p[1]] ="E"
#         elif i==len(path)-1:
#             maze[p[0]][p[1]]="S"
#         else:
#             maze[p[0]][p[1]] =3
#     print("\n")
#     for r in maze:
#         for c in r:
#             if c==3:
#                 print('\033[0;31m'+"*"+" "+'\033[0m',end="")
#             elif c=="S" or c=="E":
#                 print('\033[0;34m'+c+" " + '\033[0m', end="")
#             elif c==2:
#                 print('\033[0;32m'+"#"+" "+'\033[0m',end="")
#             elif c==1:
#                 print('\033[0;;40m'+" "*2+'\033[0m',end="")
#             else:
#                 print(" "*2,end="")
#         print()
#
# if __name__ == '__main__':
#     maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
#           [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
#           [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
#           [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
#           [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
#           [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
#           [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
#           [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
#           [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
#           [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#     start=(1,1)
#     end=(10,12)
#     find_path(maze,start,end)
#     see_path(maze,path)

# maze=[[1,1,1,1,1,1],
#       [1,0,1,0,1,1],
#       [1,0,1,0,0,1],
#       [1,0,0,0,1,1],
#       [1,0,1,0,0,1],
#       [1,1,1,1,1,1]
#       ]
# maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
#           [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
#           [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
#           [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
#           [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
#           [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
#           [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
#           [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
#           [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
#           [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
maze=[]
b=[]
for j in range(8):
    for i in range(8):
        b.append(random.randint(0,1))
    maze.append(b)
    b=[]

for i in maze:
    print(i)
direction=[
    lambda x,y:(x-1,y),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
]
# for dir in direction:
#     print(dir(1,1))


def maze_solved(x,y,gold_x,gold_y):
    stack = []
    maze[x][y] = 2
    stack.append((x,y))
    print("迷宮開始")
    while (len(stack)>0):
        cur = stack[-1]
        if cur[0]== gold_x and cur[1] == gold_y:
            print("找到出口")

            return True
        for dir in direction:
            next = dir(cur[0],cur[1])
            if maze[next[0]][next[1]] == 0:
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:
            maze[cur[0]][cur[1]] = 3
            stack.pop()

    else:
        print("沒有路徑")
        return False

maze_solved(1,1,3,3)
for i in maze:
    print(i)
#
# a=[1,2,3,4,5]
# b=a[2::-1]
# print(b)
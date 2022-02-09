# def is_OK(row,col):
#     for i in range(1,row+1):
#         if (queens[row-i]==col or queens[row-i] ==col-i or queens[row-i] == col+i): #檢察同一行和左上 右上‘
#             return False
#     return True
# def location(row):
#     start = queens[row]+1
#     for col in range(start,SIZE):
#         if is_OK(row,col):
#             return col
#     return -1
# def solve():
#     row = 0
#     while row >=0 and row<=7:
#         col = location(row)
#         if col <0:
#             queens[row]=-1
#             row-=1
#         else:
#             queens[row] =col
#             row +=1
#     if row == -1:
#         return False
#     else:
#         return True
# SIZE = 8
# queens=[-1]*8
# solve()
# for i in range(SIZE):
#     for j in range(SIZE):
#         if queens[i]==j:
#             print('■',end='')
#         else:
#             print('□',end='')
#     print()


#
# board = [-1] * 8
#
# def printboard(result):
#     for v in result:
#         length = len(result)
#         print('□ '*v + '■ ' + '□ '* (length-v-1))
#     print('\n')
#
# def is_valid(board, row, col):
#     for r in range(row):
#         if col == board[r] or abs(row - r) == abs(col - board[r]):
#             return False
#         continue
#     return True
#
# def eightQueen(board, row):
#     if row >= len(board):
#         printboard(board)
#         return True
#
#     for col in range(len(board)):
#         if is_valid(board, row, col):
#             board[row] = col
#             if eightQueen(board, row+1):
#                 pass
#                 #return True
#     return False
#
# eightQueen(board, 0)
num=0 #用来计数
def huangHou(A,hang=0):#A是一个列表，hang表示第n行
    global num
    if len(A)==hang:#递归终止条件
        num += 1
        print(num,end='：')
        for i in range(len(A)):#坐标形式输出
            print('('+str(i+1)+','+str(A[i])+')',end='')
        print('')
        return
    else:
        for i in range(len(A)):#遍历第hang行的每一个位置
            tem = True#用于标记是否满足条件
            A[hang] = i#填入列表
            for j in range(hang):#判断两个条件
                if (A[j]==A[hang])or(abs(A[j]-A[hang])==hang-j):
                    tem = False
                    break
            if tem:huangHou(A,hang+1)#若满足条件，进入下一行
huangHou([None]*8)#只要填入有N个元素的列表即可解决N皇后问
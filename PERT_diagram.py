from collections import deque
import numpy as np
import sys

def main():
    node_num, path_num, start, goal, path = input_data()
    Graph, Graph_critical, Graph_reverse, need_day = made_graph(node_num, path_num, path)
    earliest_node_time = bfs_normal(node_num, start, Graph, need_day)
    latest_node_time = bfs_reverse(node_num, goal, earliest_node_time, Graph_reverse, need_day)
    candidate = check_critical_candidate(node_num, latest_node_time, earliest_node_time)
    temp = list(check_critical_path(start, goal, candidate, Graph_critical))
    critical_path = [str(path) for path in temp]

    #-------------出力部分-----------------
    print('------------------')
    print('Earliest_node_time')
    print(earliest_node_time)
    print('------------------')
    print('Latest_node_time')
    print(latest_node_time)
    print('------------------')
    print('Critical path')
    print(' -> '.join(critical_path))

    return 0

#---------------入力部分--------------------    
def input_data():
    node_num, path_num = map(int, input().split())
    start, goal = 1, node_num
    path = [input().split() for i in range(path_num)]
    return node_num, path_num, start, goal, path


#---------------グラフ作成-------------------
def made_graph(node_num, path_num, path):
    Graph = [deque([]) for i in range(node_num+1)] 
    Graph_critical = [deque([]) for i in range(node_num+1)]
    Graph_reverse = [deque([]) for i in range(node_num+1)]

    #Graph[0], Graph_reverse[0]は捨てている(グラフ構造の作成で頂点番号を1から取っているため）

    need_day = np.zeros((node_num, node_num))

    for i in range(path_num):
        Graph[int(path[i][0])].append(int(path[i][1]))
        Graph_critical[int(path[i][0])].append(int(path[i][1]))
        Graph_reverse[int(path[i][1])].append(int(path[i][0]))     #逆向き有向グラフの作成
        need_day[int(path[i][0]) - 1][int(path[i][1]) - 1] = int(path[i][2])
        need_day[int(path[i][1]) - 1][int(path[i][0]) - 1] = int(path[i][2])

    return Graph, Graph_critical, Graph_reverse, need_day


#------------BFS作業部分(最早結合点時刻を求める）------------------
def bfs_normal(node_num, start, Graph, need_day):
    stack = deque([start])
    earliest_node_time = [0 for i in range(node_num)]

    while stack:    #stackが空になるまで継続
        tmp = stack[0]
        if Graph[tmp]:
            w = Graph[tmp].popleft() 
            if earliest_node_time[w-1] < earliest_node_time[tmp-1] + need_day[tmp-1][w-1]:
                earliest_node_time[w-1] = int(earliest_node_time[tmp-1] + need_day[tmp-1][w-1])
                stack.append(w)
        else:
            stack.popleft()
    return earliest_node_time


#------------BFS作業部分(最遅結合点時刻を求める）------------------
def bfs_reverse(node_num, goal, earliest_node_time, Graph_reverse, need_day):
    stack = deque([goal])
    latest_node_time = [float('inf') for i in range(node_num)]
    latest_node_time[goal-1] = earliest_node_time[goal-1]
    while stack:    #stackが空になるまで継続
        tmp = stack[0]
        if Graph_reverse[tmp]:
            w = Graph_reverse[tmp].popleft() 
            if latest_node_time[w-1] > latest_node_time[tmp-1] - need_day[tmp-1][w-1]:
                latest_node_time[w-1] = int(latest_node_time[tmp-1] - need_day[tmp-1][w-1])
                stack.append(w)
        else:
            stack.popleft()
    return latest_node_time


#--------------EL = TLとなる点を抜き出す-------------------
def check_critical_candidate(node_num, latest_node_time, earliest_node_time):
    critical_candidate = [False for i in range(node_num)]
    for i in range(node_num):
        if latest_node_time[i] == earliest_node_time[i]:
            critical_candidate[i] = True
    return critical_candidate


#--------------DFS作業部分（クリティカルパスの候補点を辿ってゴールまで探索する）-----------
def check_critical_path(start, goal, candidate, Graph_critical):
    stack = [start]
    seen = deque([start])

    while stack:    #stackが空になるまで継続
        tmp = stack[-1]
        if Graph_critical[tmp]:
            w = Graph_critical[tmp].popleft() 
            if w == goal:
                seen.append(w)
                return seen
            elif candidate[w - 1]:
                seen.append(w)
                stack.append(w)
            else:
                continue
        else:
            stack.pop()
            seen.pop()
    return seen


if __name__ == '__main__':
    sys.exit(main())

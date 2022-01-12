# -*- coding: utf-8 -*-


import sys

QUEUE_MAX = 10
circular_queue = [''] * QUEUE_MAX
front = QUEUE_MAX - 1
rear = QUEUE_MAX - 1
flag = 0 #當front=rear時，0表示為空佇列，1則是佇列已滿

# 新增函數
def add_queue():
    global QUEUE_MAX
    global circular_queue
    global front
    global rear
    global flag

    if front == rear and flag == 1 : # 當佇列已滿，則顯示訊息
        print('\n The queue is full！')
    else:
        rear = (rear + 1) % QUEUE_MAX
        circular_queue[rear] = input('\n Insert data please(String)：')

        if front == rear:
            flag = 1
    print()

# 刪除函數
def del_queue():
    global QUEUE_MAX
    global circular_queue
    global front
    global rear
    global flag

    if front == rear and flag == 0: # 當佇列為空，則顯示訊息
        print('\n The queue is empty! \n')
    else:
        front = (front + 1) % QUEUE_MAX
        print('\n   %s Deleted！' % circular_queue[front])

        if front == rear:
            flag = 0
        print()

# 輸出函數
def list_queue():
    global QUEUE_MAX
    global circular_queue
    global front
    global rear
    global flag

    count = 0

    if front == rear and flag == 0:
        print('\n The queue is empty！\n')
    else:
        print('\n\n All we have：')
        print('********************')
        i = (front + 1) % QUEUE_MAX
        while i != rear:
            print('   ', end = '')
            print(circular_queue[i])
            count += 1
            i = (i + 1) % QUEUE_MAX
        print('   ', end = '')
        print(circular_queue[i])
        print('********************')

        count += 1
        print(' %d data(s) in total \n' % count)

# 主函數
def main():
    option = 0

    while True:
        print('****Function Manu****')
        print('      1. Insert      ')
        print('      2. Delete      ')
        print('      3. List        ')
        print('      4. Exit        ')
        print('*********************')

        option = int(input(' Your option is：'))
        
        if option == 1:
            add_queue() # 新增函數
        elif option == 2:
            del_queue() # 刪除函數
        elif option == 3:
            list_queue() # 輸出函數
        else:
            sys.exit('Goodbye!')

main()

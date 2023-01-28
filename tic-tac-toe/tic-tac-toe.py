def print_board():
    print()
    print(f'{values[0]} | {values[1]} | {values[2]}')
    print('----------')
    print(f'{values[3]} | {values[4]} | {values[5]}')
    print('----------')
    print(f'{values[6]} | {values[7]} | {values[8]}')
    print()
    
def check_win():
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    for win in wins:
        if set(win)<=(set(users_seq[users[user_no]])) and user_no == 0 :
            
            return 0
        elif set(win)<=(set(users_seq[users[user_no]])) and user_no == 1 :
            
            return 1
        elif len(users_seq['O']) + len(users_seq['X']) == 9:
            return 2
    return -1


if __name__ == '__main__':

    values = ['0','1','2','3','4','5','6','7','8']
    users = ['X','O'] 
    user_no = 0
    users_seq = {'X':[],'O':[]}
    
    for _ in range(9):
        print_board()

        input1 = int(input('Enter the number to choose box: '))

        values[input1] = users[user_no]

        users_seq[users[user_no]].append(input1)

        print_board()
        
        #print(users_seq)

        win=check_win()
        if win == 0:
            print()
            print(f'{users[user_no]} has won the game')
            break
        elif win==1:
            print()
            print(f'{users[user_no]} has won the game')
            break
        elif win==2:
            print()
            print('Match Over')
        # else:
        #     print()
        #     print('The game has drawn')
            
        user_no=1-user_no

  
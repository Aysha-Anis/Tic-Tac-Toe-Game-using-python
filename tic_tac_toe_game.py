def main():
    print(f"Let's play Tic Tac TOe Game : ")
    xuser = [0,0,0,0,0,0,0,0,0]
    yuser = [0,0,0,0,0,0,0,0,0]

    steps=9
    turn = 1
    game_over = False
    checkboard(xuser,yuser)
    while not game_over:
        
        if turn==1:# x's turn 
            num = int(input(f"X user : "))
            xuser[num] = 1
            turn = 0
        else :
            num = int(input(f"Y user : "))
            yuser[num] = 1
            turn = 1
        checkboard(xuser,yuser)
        
        if (resultCheck(xuser,yuser)!=-1):
            print("Game Over ")
            game_over = True
        steps-=1
        if(steps==0):game_over=True

        
def resultCheck(xuser,yuser):
    win =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combination in win:
        if all(xuser[pos] == 1 for pos in combination):
            print("x wins")
            return 1
           
    
    for combination in win:
        if all(yuser[pos] == 1 for pos in combination):
            print("Y wins")
            return 0
            
    
    return -1


def checkboard(xuser,yuser):
    zero = 'X' if xuser[0]==1 else 'O' if yuser[0]==1  else 0
    one = 'X' if xuser[1]==1 else 'O' if yuser[1]==1 else 1
    two = 'X' if xuser[2]==1 else 'O' if yuser[2]==1 else 2
    three = 'X' if xuser[3]==1 else 'O' if yuser[3]==1 else 3
    four = 'X' if xuser[4]==1 else 'O' if yuser[4]==1 else 4
    five = 'X' if xuser[5]==1 else 'O' if yuser[5]==1 else 5
    six = 'X' if xuser[6]==1 else 'O' if yuser[6]==1 else 6
    seven = 'X' if xuser[7]==1 else 'O' if yuser[7]==1 else 7 
    eight = 'X' if xuser[8]==1 else 'O' if yuser[8]==1 else 8

    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")
    print("\n")


if __name__=='__main__':
    main()
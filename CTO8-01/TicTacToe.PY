
def initialiseboard():                                  
    board=[]                                  
    for i in range(3):                                  
        row=[]                                  
        for i in range(3):                                  
            row.append(" ")                                  
        board.append(row)                                  
    return board                                  

def printboard(board):                                  
    print("\nBoard Layout:")                                  
    cellnum=1                                  
    for row in board:                                  
        for cell in row:                                  
            if cell !=" ":                                  
                print(f" {cell} ",end="")                                  
            else:                                  
                print(f" {cellnum} ",end="")                                  
            if cellnum %3!=0:                                  
                print("|",end="")                                  
            cellnum+=1                                  
        if cellnum<=9:                                  
            print("\n----------")                                  

def getmove(board,current_player):                                  
    print("\n")                                  
    moveinput=input(f"Player {current_player}, enter your move(1-9): ")                                  
    if not moveinput.isdigit():                                  
        print("Invalid input. Please enter a number!")                                  
    else:                                  
        move=int(moveinput)-1                                  
        row=move//3                                  
        col=move%3                                  
    if not 1<=int(moveinput) <=9:                                  
        print("Invalid input. Please enter a number between 1 and 9!")                                  
    elif move >=0 and move <9:                                  
        if board[row][col]==" ":                                  
            board[row][col]=current_player                                  
        else:                                  
            print("Invalid input. The cell is already occupied!")                                  

def check_win(board):                                  
    win_conditions=[                                  
    [board[0][0],board[0][1],board[0][2]],                                  
    [board[1][0],board[1][1],board[1][2]],                                  
    [board[2][0],board[2][1],board[2][2]],                                  
    [board[0][0],board[1][0],board[2][0]],                                  
    [board[0][1],board[1][1],board[2][1]],                                  
    [board[0][2],board[1][2],board[2][2]],                                  
    [board[0][2],board[1][1],board[2][0]],                                  
    [board[0][0],board[1][1],board[2][2]]]                                  

    for condition in win_conditions:                                  
        if  condition[0]==condition[1]==condition[2]  and                                   condition[0] != " ":                                  
            return True                                  
    return False                                  

def check_draw(board):                                  
    for row in board:                                  
        for cell in row:                                  
            if cell==" ":                                  
                return False                                  
    return True 
    


def switch_player(current_player):                                  
    if current_player=="X":                                  
        return "O"                         
    return "X"                                  

                                  


# Main Loop                                  
board=initialiseboard()                                  
currentplayer="X"                                  
                              
while True:                      
    printboard(board)   
    getmove(board,currentplayer)
    
    if check_win(board)==False and check_draw(board)==True:           
        {printboard(board)}     
        print("\n")              
        print("It's a draw!")     
        break                   
    if check_win(board):
        {printboard(board)}        
        print("\n")               
        print(f"Player {currentplayer} wins!")            
        break                                  
    currentplayer=switch_player(currentplayer)                                  
import time, os, random



maze = []

path = []


def displaymaze():
    #Slow down to watch simulation
    time.sleep(0.2)
    os.system("cls")

    #Adjust output to make it look better on the screen
    map = "\n\n"
    for row in range(0,len(maze)):
        for col in range(0,len(maze[row])):
            if maze[row][col] == "1":
                map = map + "[X]"

            if maze[row][col] == "0":
                map = map +  "   "

            if maze[row][col] == ".":
                map = map + " . "

            if maze[row][col] == "2":
                map = map + "   "

            if maze[row][col] == "E":
                map = map + " E "

            if maze[row][col] == "S":
                map = map + " S "

        map = map + "\n"

    print(map)

def move(row,col):
    global path
    global maze

    possible_moves = [[row, col+1],[row,col-1],[row+1,col],[row-1,col]]
    random.shuffle(possible_moves)
    
    if maze[row][col]== "0" or maze[row][col]=="S":
        maze[row][col]="."
        path.append([row,col])
        
        
        displaymaze()

        if move(possible_moves[0][0], possible_moves[0][1]):
            return True
        
        if move(possible_moves[1][0], possible_moves[1][1]):
            return True
        if move(possible_moves[2][0], possible_moves[2][1]):
            return True
        if move(possible_moves[3][0], possible_moves[3][1]):
            return True
        else:
            maze[row][col]="2"
            path.remove([row,col])
            displaymaze()
            return False
    
    elif maze[row][col]=="E":
        maze[row][col]="."
        path.append([row,col])
        return True
    
    return False

def main():
    os.system("cls")
    global maze
    file = open("maze.txt", "r")

    while True:
        line = file.readline()
        if line == "":
            break
        else:
            values = line.rstrip("\n").split(",")
            maze.append(values)

    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            if maze[i][j]=="S":
                startrow=i
                startcol=j
                break
    
    move(startrow,startcol)

    displaymaze()    
    print("maze solved")
    print(path)

main()

















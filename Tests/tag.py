#position and printing the map
pos = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
print("_________________________________________________\n|     |     |     |     |     |     |     |     |\n| ",pos[0]," | ",pos[1]," | ",pos[2]," | ",pos[3]," | ",pos[4]," | ",pos[5]," | ",pos[6]," | ",pos[7]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[8]," | ",pos[9]," | ",pos[10]," | ",pos[11]," | ",pos[12]," | ",pos[13]," | ",pos[14]," | ",pos[15]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[16]," | ",pos[17]," | ",pos[18]," | ",pos[19]," | ",pos[20]," | ",pos[21]," | ",pos[22]," | ",pos[23]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[24]," | ",pos[25]," | ",pos[26]," | ",pos[27]," | ",pos[28]," | ",pos[29]," | ",pos[30]," | ",pos[31]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[32]," | ",pos[33]," | ",pos[34]," | ",pos[35]," | ",pos[36]," | ",pos[37]," | ",pos[38]," | ",pos[39]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[40]," | ",pos[41]," | ",pos[42]," | ",pos[43]," | ",pos[44]," | ",pos[45]," | ",pos[46]," | ",pos[47]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n\n")

#variables and starting location
px = 1
py = 1
ex = 5
ey = 5
x = "X"
enemy1 = "Y"
caught = False
endgame = False

while endgame == False:
    
    #teleporting player after tagging
    px = 2
    px = 2
    caught = False
    
    while caught == False:

        #enemy movement
        if ex < px:
            ex = ex + 1
        elif ex > px:
            ex = ex - 1
        else:
            if ey < py:
                ey = ey + 1
            elif ey > py:
                ey = ey - 1


        #input move and moving x/y axis
        move = input("Move ")
        #move up
        if move == "up":
            if py == 1:
                py = py
            else:
                py = py - 1
        #move down
        if move == "down":
            if py == 6:
                py = py
            else:
                py = py + 1
        #move left
        if move == "left":
            if px == 1:
                px = px
            else:
                px = px - 1
        #move right
        if move == "right":
            if px == 8:
                px = px
            else:
                px = px + 1


        #emptying map
        pos = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

            
        #set player loaction
        if px == 1:
            if py == 1:
                pos[0] = "X"
            elif py == 2:
                pos[8] = "X"
            elif py == 3:
                pos[16] = "X"
            elif py == 4:
                pos[24] = "X"
            elif py == 5:
                pos[32] = "X"
            elif py == 6:
                pos[40] = "X"
        elif px == 2:
            if py == 1:
                pos[1] = "X"
            elif py == 2:
                pos[9] = "X"
            elif py == 3:
                pos[17] = "X"
            elif py == 4:
                pos[25] = "X"
            elif py == 5:
                pos[33] = "X"
            elif py == 6:
                pos[41] = "X"
        elif px == 3:
            if py == 1:
                pos[2] = "X"
            elif py == 2:
                pos[10] = "X"
            elif py == 3:
                pos[18] = "X"
            elif py == 4:
                pos[26] = "X"
            elif py == 5:
                pos[34] = "X"
            elif py == 6:
                pos[42] = "X"
        elif px == 4:
            if py == 1:
                pos[3] = "X"
            elif py == 2:
                pos[11] = "X"
            elif py == 3:
                pos[19] = "X"
            elif py == 4:
                pos[27] = "X"
            elif py == 5:
                pos[35] = "X"
            elif py == 6:
                pos[43] = "X"
        elif px == 5:
            if py == 1:
                pos[4] = "X"
            elif py == 2:
                pos[12] = "X"
            elif py == 3:
                pos[20] = "X"
            elif py == 4:
                pos[28] = "X"
            elif py == 5:
                pos[36] = "X"
            elif py == 6:
                pos[44] = "X"
        elif px == 6:
            if py == 1:
                pos[5] = "X"
            elif py == 2:
                pos[13] = "X"
            elif py == 3:
                pos[21] = "X"
            elif py == 4:
                pos[29] = "X"
            elif py == 5:
                pos[37] = "X"
            elif py == 6:
                pos[45] = "X"
        elif px == 7:
            if py == 1:
                pos[6] = "X"
            elif py == 2:
                pos[14] = "X"
            elif py == 3:
                pos[22] = "X"
            elif py == 4:
                pos[30] = "X"
            elif py == 5:
                pos[38] = "X"
            elif py == 6:
                pos[46] = "X"
        elif px == 8:
            if py == 1:
                pos[7] = "X"
            elif py == 2:
                pos[15] = "X"
            elif py == 3:
                pos[23] = "X"
            elif py == 4:
                pos[31] = "X"
            elif py == 5:
                pos[39] = "X"
            elif py == 6:
                pos[47] = "X"


        #set enemy1 loaction
        if ex == 1:
            if ey == 1:
                pos[0] = enemy1
            elif ey == 2:
                pos[8] = enemy1
            elif ey == 3:
                pos[16] = enemy1
            elif ey == 4:
                pos[24] = enemy1
            elif ey == 5:
                pos[32] = enemy1
            elif ey == 6:
                pos[40] = enemy1
        elif ex == 2:
            if ey == 1:
                pos[1] = enemy1
            elif ey == 2:
                pos[9] = enemy1
            elif ey == 3:
                pos[17] = enemy1
            elif ey == 4:
                pos[25] = enemy1
            elif ey == 5:
                pos[33] = enemy1
            elif ey == 6:
                pos[41] = Enemy1
        elif ex == 3:
            if ey == 1:
                pos[2] = enemy1
            elif ey == 2:
                pos[10] = enemy1
            elif ey == 3:
                pos[18] = enemy1
            elif ey == 4:
                pos[26] = enemy1
            elif ey == 5:
                pos[34] = enemy1
            elif ey == 6:
                pos[42] = enemy1
        elif ex == 4:
            if ey == 1:
                pos[3] = enemy1
            elif ey == 2:
                pos[11] = enemy1
            elif ey == 3:
                pos[19] = enemy1
            elif ey == 4:
                pos[27] = enemy1
            elif ey == 5:
                pos[35] = enemy1
            elif ey == 6:
                pos[43] = enemy1
        elif ex == 5:
            if ey == 1:
                pos[4] = enemy1
            elif ey == 2:
                pos[12] = enemy1
            elif ey == 3:
                pos[20] = enemy1
            elif ey == 4:
                pos[28] = enemy1
            elif ey == 5:
                pos[36] = enemy1
            elif ey == 6:
                pos[44] = enemy1
        elif ex == 6:
            if ey == 1:
                pos[5] = enemy1
            elif ey == 2:
                pos[13] = enemy1
            elif ey == 3:
                pos[21] = enemy1
            elif ey == 4:
                pos[29] = enemy1
            elif ey == 5:
                pos[37] = enemy1
            elif ey == 6:
                pos[45] = enemy1
        elif ex == 7:
            if ey == 1:
                pos[6] = enemy1
            elif ey == 2:
                pos[14] = enemy1
            elif ey == 3:
                pos[22] = enemy1
            elif ey == 4:
                pos[30] = enemy1
            elif ey == 5:
                pos[38] = enemy1
            elif ey == 6:
                pos[46] = enemy1
        elif ex == 8:
            if ey == 1:
                pos[7] = enemy1
            elif ey == 2:
                pos[15] = enemy1
            elif ey == 3:
                pos[23] = enemy1
            elif ey == 4:
                pos[31] = enemy1
            elif ey == 5:
                pos[39] = enemy1
            elif ey == 6:
                pos[47] = enemy1
        
        if ex == px and ey == py:
            caught = True
            
        #printing map
        print("_________________________________________________\n|     |     |     |     |     |     |     |     |\n| ",pos[0]," | ",pos[1]," | ",pos[2]," | ",pos[3]," | ",pos[4]," | ",pos[5]," | ",pos[6]," | ",pos[7]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[8]," | ",pos[9]," | ",pos[10]," | ",pos[11]," | ",pos[12]," | ",pos[13]," | ",pos[14]," | ",pos[15]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[16]," | ",pos[17]," | ",pos[18]," | ",pos[19]," | ",pos[20]," | ",pos[21]," | ",pos[22]," | ",pos[23]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[24]," | ",pos[25]," | ",pos[26]," | ",pos[27]," | ",pos[28]," | ",pos[29]," | ",pos[30]," | ",pos[31]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[32]," | ",pos[33]," | ",pos[34]," | ",pos[35]," | ",pos[36]," | ",pos[37]," | ",pos[38]," | ",pos[39]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[40]," | ",pos[41]," | ",pos[42]," | ",pos[43]," | ",pos[44]," | ",pos[45]," | ",pos[46]," | ",pos[47]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n\n")
    
	

    print("Tag! You are IT")

    #teleporting enemy after tag
    ex = 5
    ey = 5
    caught = False
    
    while caught == False:
        
        #enemy movement
        if ex < px:
            if  ex != 1:
                ex = ex - 1
            else:
                ex = ex + 1
        elif ex > px:
            if ex != 8:
                ex = ex + 1
            else:
                ex = ex - 1
        else:
            if ey < py:
                if  ey > 1:
                    ey = ey - 1
                else:
                    ey = ey + 1
            elif ey > py:
                if  ey < 8:
                    ey = ey + 1
                else:
                    ey = ey - 1

        #input move and moving x/y axis
        move = input("Move ")
        #move up
        if move == "up":
            if py == 1:
                py = py
            else:
                py = py - 1
        #move down
        if move == "down":
            if py == 6:
                py = py
            else:
                py = py + 1
        #move left
        if move == "left":
            if px == 1:
                px = px
            else:
                px = px - 1
        #move right
        if move == "right":
            if px == 8:
                px = px
            else:
                px = px + 1


        #emptying map
        pos = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

            
        #set player loaction
        if px == 1:
            if py == 1:
                pos[0] = "X"
            elif py == 2:
                pos[8] = "X"
            elif py == 3:
                pos[16] = "X"
            elif py == 4:
                pos[24] = "X"
            elif py == 5:
                pos[32] = "X"
            elif py == 6:
                pos[40] = "X"
        elif px == 2:
            if py == 1:
                pos[1] = "X"
            elif py == 2:
                pos[9] = "X"
            elif py == 3:
                pos[17] = "X"
            elif py == 4:
                pos[25] = "X"
            elif py == 5:
                pos[33] = "X"
            elif py == 6:
                pos[41] = "X"
        elif px == 3:
            if py == 1:
                pos[2] = "X"
            elif py == 2:
                pos[10] = "X"
            elif py == 3:
                pos[18] = "X"
            elif py == 4:
                pos[26] = "X"
            elif py == 5:
                pos[34] = "X"
            elif py == 6:
                pos[42] = "X"
        elif px == 4:
            if py == 1:
                pos[3] = "X"
            elif py == 2:
                pos[11] = "X"
            elif py == 3:
                pos[19] = "X"
            elif py == 4:
                pos[27] = "X"
            elif py == 5:
                pos[35] = "X"
            elif py == 6:
                pos[43] = "X"
        elif px == 5:
            if py == 1:
                pos[4] = "X"
            elif py == 2:
                pos[12] = "X"
            elif py == 3:
                pos[20] = "X"
            elif py == 4:
                pos[28] = "X"
            elif py == 5:
                pos[36] = "X"
            elif py == 6:
                pos[44] = "X"
        elif px == 6:
            if py == 1:
                pos[5] = "X"
            elif py == 2:
                pos[13] = "X"
            elif py == 3:
                pos[21] = "X"
            elif py == 4:
                pos[29] = "X"
            elif py == 5:
                pos[37] = "X"
            elif py == 6:
                pos[45] = "X"
        elif px == 7:
            if py == 1:
                pos[6] = "X"
            elif py == 2:
                pos[14] = "X"
            elif py == 3:
                pos[22] = "X"
            elif py == 4:
                pos[30] = "X"
            elif py == 5:
                pos[38] = "X"
            elif py == 6:
                pos[46] = "X"
        elif px == 8:
            if py == 1:
                pos[7] = "X"
            elif py == 2:
                pos[15] = "X"
            elif py == 3:
                pos[23] = "X"
            elif py == 4:
                pos[31] = "X"
            elif py == 5:
                pos[39] = "X"
            elif py == 6:
                pos[47] = "X"


        #set enemy1 loaction
        if ex == 1:
            if ey == 1:
                pos[0] = enemy1
            elif ey == 2:
                pos[8] = enemy1
            elif ey == 3:
                pos[16] = enemy1
            elif ey == 4:
                pos[24] = enemy1
            elif ey == 5:
                pos[32] = enemy1
            elif ey == 6:
                pos[40] = enemy1
        elif ex == 2:
            if ey == 1:
                pos[1] = enemy1
            elif ey == 2:
                pos[9] = enemy1
            elif ey == 3:
                pos[17] = enemy1
            elif ey == 4:
                pos[25] = enemy1
            elif ey == 5:
                pos[33] = enemy1
            elif ey == 6:
                pos[41] = Enemy1
        elif ex == 3:
            if ey == 1:
                pos[2] = enemy1
            elif ey == 2:
                pos[10] = enemy1
            elif ey == 3:
                pos[18] = enemy1
            elif ey == 4:
                pos[26] = enemy1
            elif ey == 5:
                pos[34] = enemy1
            elif ey == 6:
                pos[42] = enemy1
        elif ex == 4:
            if ey == 1:
                pos[3] = enemy1
            elif ey == 2:
                pos[11] = enemy1
            elif ey == 3:
                pos[19] = enemy1
            elif ey == 4:
                pos[27] = enemy1
            elif ey == 5:
                pos[35] = enemy1
            elif ey == 6:
                pos[43] = enemy1
        elif ex == 5:
            if ey == 1:
                pos[4] = enemy1
            elif ey == 2:
                pos[12] = enemy1
            elif ey == 3:
                pos[20] = enemy1
            elif ey == 4:
                pos[28] = enemy1
            elif ey == 5:
                pos[36] = enemy1
            elif ey == 6:
                pos[44] = enemy1
        elif ex == 6:
            if ey == 1:
                pos[5] = enemy1
            elif ey == 2:
                pos[13] = enemy1
            elif ey == 3:
                pos[21] = enemy1
            elif ey == 4:
                pos[29] = enemy1
            elif ey == 5:
                pos[37] = enemy1
            elif ey == 6:
                pos[45] = enemy1
        elif ex == 7:
            if ey == 1:
                pos[6] = enemy1
            elif ey == 2:
                pos[14] = enemy1
            elif ey == 3:
                pos[22] = enemy1
            elif ey == 4:
                pos[30] = enemy1
            elif ey == 5:
                pos[38] = enemy1
            elif ey == 6:
                pos[46] = enemy1
        elif ex == 8:
            if ey == 1:
                pos[7] = enemy1
            elif ey == 2:
                pos[15] = enemy1
            elif ey == 3:
                pos[23] = enemy1
            elif ey == 4:
                pos[31] = enemy1
            elif ey == 5:
                pos[39] = enemy1
            elif ey == 6:
                pos[47] = enemy1

        if ex == px and ey == py:
            caught = True

        #printing map
        print("_________________________________________________\n|     |     |     |     |     |     |     |     |\n| ",pos[0]," | ",pos[1]," | ",pos[2]," | ",pos[3]," | ",pos[4]," | ",pos[5]," | ",pos[6]," | ",pos[7]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[8]," | ",pos[9]," | ",pos[10]," | ",pos[11]," | ",pos[12]," | ",pos[13]," | ",pos[14]," | ",pos[15]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[16]," | ",pos[17]," | ",pos[18]," | ",pos[19]," | ",pos[20]," | ",pos[21]," | ",pos[22]," | ",pos[23]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[24]," | ",pos[25]," | ",pos[26]," | ",pos[27]," | ",pos[28]," | ",pos[29]," | ",pos[30]," | ",pos[31]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[32]," | ",pos[33]," | ",pos[34]," | ",pos[35]," | ",pos[36]," | ",pos[37]," | ",pos[38]," | ",pos[39]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n|     |     |     |     |     |     |     |     |\n| ",pos[40]," | ",pos[41]," | ",pos[42]," | ",pos[43]," | ",pos[44]," | ",pos[45]," | ",pos[46]," | ",pos[47]," |\n|_____|_____|_____|_____|_____|_____|_____|_____|\n\n")
	    
			
    print("Tag! The enemy is IT")
    

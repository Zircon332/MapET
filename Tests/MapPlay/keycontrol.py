#This is a module, 
#a prototype for INPUT.py of the main program


##    Welcome to keycontrol
##    
##    To import, 'import keycontrol'
##    To call, type 'set_controls(root)' in the program
##
##
##    OTHER IMPORTANT DETAILS:
##    The bindings bind to the entire program
##    The name of the tk is 'root'
##    The positions x and y are posx and posy
##    Player movement is measured in grids
    

import config
#actual module starts here

def set_controls():
    def move(x,y):
        test_x = config.pos[0] + x
        test_y = config.pos[1] - y
        if [test_x,test_y] not in config.wall:            
            if (config.pos[0] + x) != 0 and (config.pos[0] + x) != (config.bordersize-1):
                config.pos[0] += x
            if (config.pos[1] - y) != 0 and (config.pos[1] - y) != (config.bordersize-1):
                config.pos[1] -= y
            config.player.grid(column=config.pos[0],row=config.pos[1])

    config.root.bind_all("<Up>", lambda event, x=0,y=1: move(x,y))
    config.root.bind_all("<Down>", lambda event, x=0,y=-1: move(x,y))
    config.root.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
    config.root.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))

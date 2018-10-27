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
        config.posx += x
        config.posy -= y
        config.player.grid(column=config.posx,row=config.posy)

    config.root.bind_all("<Up>", lambda event, x=0,y=1: move(x,y))
    config.root.bind_all("<Down>", lambda event, x=0,y=-1: move(x,y))
    config.root.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
    config.root.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))

def derecha():
    turn_left()
    turn_left()
    turn_left()
def movi():
    move()
    turn_left()
    move()
    derecha()
    move()
    derecha()
    move()
    turn_left()
 
control = True 
    
while control:
    movi()
    if at_goal():
        control = False

    



        
        
       

    



    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def caminar ( ):
    move()
    move()
    move()
    
    
        
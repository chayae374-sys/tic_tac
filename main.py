from working import *

def x_o():
    for i in range(9):
        show_table()
        if i % 2 == 0:
            line_o()
        elif i % 2 != 0:
            line_x()
        if check_winner() == False:
            break
        # print("it's a drow")    

if __name__ == "__main__":
    x_o()
    
                
      
        
    
        
      
        
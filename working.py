from data import s,winner


count = 0


def show_table():
    
    print(f"""
        [1]{s[1]} | [2]{s[2]} | [3]{s[3]}
    ------+-------+----
        [4]{s[4]} | [5]{s[5]} | [6]{s[6]}
    ------+-------+----
        [7]{s[7]} | [8]{s[8]} | [9]{s[9]}
""")

def check_num():
    user = False
    while not user:
        try:
            user_choise = int(input("enter your choise! "))
            if 0 < user_choise < 10 and s[user_choise] == "" :
               user = True
            else: 
                print("just between 1-9, or the number is already taken")
        except ValueError:
            print("just a number")
    return user_choise 

def line_o():
    print("now it's your turn o")
    user = check_num()
    global count
    count += 1
    s[user] = "o"
        

def line_x():
    print("now it's your turn x")
    user = check_num()
    global count
    count += 1
    s[user] = "x"   
    
def check_winner():
    global count
    print(f"{count}")
    
    for item in winner:
        if "x" == s[item[0]] and "x" == s[item[1]] and "x" == s[item[2]]:
            print("x won")
            return False
        if "o" == s[item[0]] and "o" == s[item[1]] and "o" == s[item[2]]:
            print("o won")       
            return False
        
        
    if count == 8: print("it's a draw")
    
    return True
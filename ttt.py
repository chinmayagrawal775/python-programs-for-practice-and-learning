p1='X'
p2='O'
roundr=1
int(roundr)
p1p=0
int(p1p)
p2p=0
int(p2p)

def display() :
    print("\n\n\t\t\t\tTIC TAC TOE\n\n")
    print("\nSymbol of player 1: X")
    print("\nSymbol of player 2: O")
    print("\nround {}".format(roundr))
    global roundr
    roundr+=1

def show() :
    print("\n\n\n\n")
    print("\t\t\t\t {} | {} | {}".format(a[0],a[1],a[2]))
    print("\t\t\t\t---|---|---")
    print("\t\t\t\t {} | {} | {}".format(a[3],a[4],a[5]))
    print("\t\t\t\t---|---|---")
    print("\t\t\t\t {} | {} | {}".format(a[6],a[7],a[8]))

def start() :
    i=0
    for i in range(9) :
        
        if i%2==0 :
            choice=int(input('"\nplayer 1 chance(X): "'))
            a[choice-1]=p1
            r=end()
            if r=='o' :
                print('\n'*100)
                show()
                print("\n\n\t\t\tplayer 1 won the round{}....!!!!".format(roundr-1))
                global p1p
                p1p+=1
                break
            elif r=='t' :
                print('\n'*100)
                show()
                print("\n\n\t\t\tplayer 2 won the round{}....!!!!".format(roundr-1))
                global p2p
                p2p+=1
                break
            print('\n'*100)
            show()

        else :
            choice=int(input('"\nplayer 2 chance(O): "'))
            a[choice-1]=p2
            r=end()
            if r=='o' :
                print('\n'*100)
                show()
                print("\n\n\t\t\tplayer 1 won the round{}....!!!!".format(roundr-1))
                global p1p
                p1p+=1
                break
            elif r=='t' :
                print('\n'*100)
                show()
                print("\n\n\t\t\tplayer 2 won the round{}....!!!!".format(roundr-1))
                global p2p
                p2p+=1
                break
            print('\n'*100)
            show()
    r=end()
    if r==48 :
        print("\n\n\t\t\tGame is drawn....!!!!")

def end() :
    w1='o'
    w2='t'
    if( (a[0]==a[1]==a[2]==p1) or (a[3]==a[4]==a[5]==p1) or (a[6]==a[7]==a[8]==p1) ) :
     return w1;
    elif( (a[0]==a[1]==a[2]==p2) or (a[3]==a[4]==a[5]==p2) or (a[6]==a[7]==a[8]==p2) ) : 
     return w2;
    elif( (a[0]==a[3]==a[6]==p1) or (a[1]==a[4]==a[7]==p1) or (a[2]==a[5]==a[8]==p1) ) :
     return w1;
    elif( (a[0]==a[3]==a[6]==p2) or (a[1]==a[4]==a[7]==p2) or (a[2]==a[5]==a[8]==p2) ) :
     return w2;
    elif( (a[0]==a[4]==a[8]==p1) or (a[2]==a[4]==a[6]==p1) ) :
     return w1;
    elif( (a[0]==a[4]==a[8]==p2) or (a[2]==a[4]==a[6]==p2) ) :
     return w2;
    else :
        return 48;

def winner() :
    print('\n'*100)
    print("\n\n\n\n\n")
    print("\n\t\t\tpoints of player one:- {}".format(p1p))
    print("\n\t\t\tpoints of player two:- {}".format(p2p))
    if p1p>p2p :
        print("\n\n\n\n\t\t!!!!....player 1 won the game....!!!!")
    elif p1p<p2p :
        print("\n\n\n\n\t\t!!!!....player 2 won the game....!!!!")
    elif p1p==p2p :
        print("\n\n\n\n\t\t!!!!....game is drawn....!!!!")


while roundr!=3 :
    print('\n'*100)
    display()
    a=['1','2','3','4','5','6','7','8','9']
    show()
    start()
    if roundr<3 :
        input("\n\n\n\n\n\n\n\n\npress enter to start the next round....")
    else :
        input("\n\n\n\n\n\n\n\n\npress enter to see the results....")
winner()

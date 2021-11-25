input_bet = input("Enter All Bid : ").split()
input_bet.sort(key=int)
input_bet.reverse()
if len(input_bet) == 1 :
    print("not enough bidder")
    exit()
if input_bet[0] == input_bet[1] :
    print("error : have more than one highest bid")
    exit()
print("winner bid is %s"% (input_bet[0]) +" need to pay %s"  % (input_bet[1]))

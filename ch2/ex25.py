def bon(w):
    a_Z  ="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(w)):
        if w[i]==w[i+1]:
             out = w[i]
             break
        else: pass
    for k in range(1,len(a_Z)+1) :
         if out == a_Z[k-1]:
            return (k)*4
            break
	### Enter Your Code Here ###
secretCode = input("Enter secret code : ")
print(bon(secretCode))
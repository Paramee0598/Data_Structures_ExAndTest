def mod_position(arr, s):
 showArr = []
 for i in range(len(arr)):
     if i == (s-1):
         showArr.append(arr[i])
     if (i+1) % s == 0 and (i+1) != s :
         showArr.append(arr[i])
 return showArr
print('*** Mod Position ***')
arr,s = input("Enter Input : ").split(',')
print(mod_position(str(arr),int(s)))
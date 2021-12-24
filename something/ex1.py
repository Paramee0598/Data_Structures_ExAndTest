print('*** Converting hh.mm.ss to seconds ***')
h , m , s = input("Enter hh mm ss : ").split()

if 60 <= int(m) or int(m) < 0:
    print("mm" +  '('+str(m)+')' + ' is invalid!')
    exit()

seconds = ((int(h)*3600)+(int(m)*60)+int(s))

if(0 <= int(h) < 10):
    h = '0'+str(h)
    pass
if(0 <= int(m) < 10):
    m = '0'+str(m)
    pass

if (0 <= int(s) < 10):
    s = '0'+str(s)
    pass
#list = (h,m,s)

#print(':'.join(list) +' = '+ (f'{seconds:,}')+' seconds')
print(h+":"+m+":"+s,"=",(f'{seconds:,}'),"seconds")




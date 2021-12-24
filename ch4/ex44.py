class Queue:
    def __init__(self):
        self.men = []
        self.women = []
        self.activity = ["Eat", "Game", "Learn", "Movie"]
        self.location = ["Res.", "ClassR.", "SuperM.", "Home"]
        self.parkmen = ""
        self.Acmen = 0
        self.Lomen = 0
        self.acwomen = 0
        self.lowomen = 0
        self.real_ac_men = []
        self.real_lo_men = []
        self.real_ac_wo_men = []
        self.real_lo_wo_men = []
        self.saveprint_men = []
        self.saveprint_women = []
        self.loveScore = 0
        # ------------------------
    def enQueue(self, i, j):
        self.men.append(i)
        self.women.append(j)

q = Queue()
inpt = input("Enter Input : ").split(",")  # แต่ละวัน

for i in inpt:
    tempmen, tempwomen = i.split()
    q.enQueue(tempmen, tempwomen) #แจกแจง men , women
   # print(q.men)
   # print(q.women)
for i in q.men:
    tempAcmen, tempLomen = str(i).split(":") #แจกแจง
    #print(f'TAm: {tempAcmen}  TLm: {tempLomen}')
    q.Acmen = int(tempAcmen)
    q.Lomen = int(tempLomen)
    parkmen = q.activity[q.Acmen] + ":" + q.location[q.Lomen] #เช็คทำ ac กับ lo
    #print(f'park{parkmen}')
    q.real_ac_men.append(q.activity[q.Acmen])
    q.real_lo_men.append(q.location[q.Lomen])

    q.saveprint_men.append(parkmen)

for i in q.women:#แจกแจงอีก
    tempAcmen, tempLomen = str(i).split(":")
    q.acwomen = int(tempAcmen)
    q.lowomen = int(tempLomen)
    parkmen = q.activity[q.acwomen] + ":" + q.location[q.lowomen]

    q.real_ac_wo_men.append(q.activity[q.acwomen])
    q.real_lo_wo_men.append(q.location[q.lowomen])

    q.saveprint_women.append(parkmen)

# ----------------
print(f'My   Queue = { ", ".join(q.men)}')
print(f'Your Queue = { ", ".join(q.women)}')
print(f'My   Activity:Location = {", ".join(q.saveprint_men)}')
print(f'Your Activity:Location = {", ".join(q.saveprint_women)}')

for i in range(len(inpt)): #เปรียบเทียบ
    if (q.real_ac_men[i] == q.real_ac_wo_men[i] and q.real_lo_men[i] != q.real_lo_wo_men[i]):q.loveScore += 1
    elif (q.real_ac_men[i] != q.real_ac_wo_men[i] and q.real_lo_men[i] == q.real_lo_wo_men[i]):q.loveScore += 2
    elif (q.real_ac_men[i] == q.real_ac_wo_men[i] and q.real_lo_men[i] == q.real_lo_wo_men[i]):q.loveScore += 4
    else:q.loveScore -= 5

if (q.loveScore >= 7):print(f'Yes! You\'re my love! : Score is {str(q.loveScore)}.')
elif (q.loveScore > 0 and q.loveScore < 7):print(f'Umm.. It\'s complicated relationship! : Score is {str(q.loveScore)}.')
else:print(f'No! We\'re just friends. : Score is {str(q.loveScore)}.')
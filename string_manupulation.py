S1="e#fee"
S2="fe#fe"
#replaced the special charater with f
S1=S1.replace("#","f")
#replaced the special charater with f
S2=S2.replace("#","e")
print(S1,S2)
#check S1 and S2 are same or not
if S1==S2:
  print("Match")
else:
    print("Different")
#convert string to list of easy manipulation 
l1=list(S1)
l2=list(S2)
#change the list position  0 with f
l1[0]="f"
#change the list position  2 with f
l1[2]="e"
#convert list into string
S1= ' '.join(map(str, l1))
S2 = ' '.join(map(str, l2))
print(S1,"\n",S2)
#check S1 and S2 are same or not
if S1==S2:
  print("Match")
else:
    print("Different")
#change the list position  1 with e
l1[1]="e"
#change the list position  3 with f
l1[3]="f"
#convert list into string
S1= ' '.join(map(str, l1))
S2 = ' '.join(map(str, l2))
print(S1,"\n",S2)
#check S1 and S2 are same or not
if S1==S2:
  print("Match")
else:
    print("Different")

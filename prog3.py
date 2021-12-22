
import csv
arr=[]

with open('./trainingdata.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        arr.append(row)
        print(row)

a= arr[1:]
num_attributes= len(a[0])-1
print('the initial value of the hypothesis:' )
S= ['0']*num_attributes
G=['?']*num_attributes
print('most specific hypothesis is S0:',S)
print('most general hypothesis is G0:',G)

for j in range (num_attributes):
    S[j]=a[0][j]

print('candidate Elimination hypothesis version space')
temp= []

for i in range (len(a)):
    print('_________________________________________________')
    if a[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if a[i][j]!=S[j]:
                S[j]='?'
        for j in range (num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j]!='?' and temp[k][j]!= S[j]:
                    del temp[k]
        print('S{}:'.format(i+1),S)
        if len(temp)==0:
            print('G{}:'.format(i+1),G)
        else:
            print('G{}:'.format(i+1),temp)
    
    if a[i][num_attributes] == "No":
        for j in range(num_attributes):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j]= S[j]
                temp.append(G)
                G= ['?']* num_attributes
        print('S{}:'.format(i+1),S)
        print('G{}'.format(i+1),temp)





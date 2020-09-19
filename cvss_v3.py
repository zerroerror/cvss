def RoundUp(num):
    num=int(num*100)
    if (num%10>0):
        num=num+10-num%10
    return num/100
def Dengerlevel(BaseScore):
    if (BaseScore==0):
        print('No danger')
    if (BaseScore>=0.1 and BaseScore<=3.9):
        print('Low Danger Level')
    if (BaseScore>=4 and BaseScore<=6.9):
        print('Medium Danger Level')
    if (BaseScore>=7 and BaseScore<=8.9):
        print('High Danger Level')
    if (BaseScore>=9):
        print('Critical Danger Level')
AV=float(input('Please, input AV : \n'))
AC=float(input('Please, input AC : \n'))
PR=float(input('Please, input PR : \n'))
UI=float(input('Please, input UI : \n'))
S=float(input('Please, input S : \n'))
C=float(input('Please, input C : \n'))
I=float(input('Please, input I : \n'))
A=float(input('Please, input A : \n'))
ImpactBase=1-((1-C)*(1-I)*(1-A))
Exploitability=8.22*AV*AC*PR*UI
if (S==0):
    Impact=6.42*ImpactBase
else:
    Impact=7.52*(ImpactBase-0.029)-3.25*(ImpactBase-0.02)**15
if (Impact<=0):
    BaseScore=0
else:
    if (S==0):
        BaseScore=RoundUp(min(Impact+Exploitability),10)**2
    if (S==1):
        BaseScore=RoundUp(min(1.08*(Impact+Exploitability),10))
print('-------------------\n')
print('BaseScore = ',BaseScore)
print('-------------------\n')
Dengerlevel(BaseScore)

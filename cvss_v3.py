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
print('----For BaseMitric----')
print('\n')
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
Dengerlevel(BaseScore)
print('-------------------\n')
print('\n')
print('----For TimeMitric----')
print('\n')
E=float(input('Please, input E : \n'))
RL=float(input('Please, input RL : \n'))
RC=float(input('Please, input RC : \n'))
TemporalScore=RoundUp(BaseScore*E*RL*RC)
print('-------------------\n')
print('TimeMetric = ',TemporalScore)
print('-------------------\n')
print('\n')
print('----For Contextualmetric----')
print('\n')
MAV=float(input('Please, input MAV : \n'))
MAC=float(input('Please, input MAC : \n'))
MPR=float(input('Please, input MPR : \n'))
MUI=float(input('Please, input MUI : \n'))
MS=float(input('Please, input MS : \n'))
MC=float(input('Please, input MC : \n'))
MI=float(input('Please, input MI : \n'))
MA=float(input('Please, input MA : \n'))
CR=float(input('Please, input CR : \n'))
IR=float(input('Please, input IR : \n'))
AR=float(input('Please, input AR : \n'))
MExploitability=8.22*MAV*MAC*MPR*MUI
MImpactBase=min((1-(1-MC*CR)*(1-MI*IR)*(1-MA*AR)), 0.915)
if (MS==1):
    MImpact=7.52*(MImpactBase-0.029)-3.25*(MImpactBase-0.02)**15
else:
    Mimpact=6.42*MImpactBase
if (MImpact<0):
    EnvironmentalScore=0
else:
    if (MS==0):
        EnvironmentalScore=RoundUp(RoundUp(min(MImpact+MExploitability,10))*E*RL*RC)
    else:
        EnvironmentalScore=RoundUp(RoundUp(min(1.08*(MImpact+MExploitability),10))*E*RL*RC)
print('-------------------\n')
print('Contextualmetric = ',TemporalScore)
print('-------------------\n')
print('\n')

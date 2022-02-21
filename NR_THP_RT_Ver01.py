#!/usr/bin/env python
# coding: utf-8

# In[7]:
#import math for calculation of MOD in Available PRBs
import math
#determine the 5G RAT type according to BAnd and SCS
while(True):
    BW=input('Enter the 5G channel bandwidth in MHz : ')
    SCS=input('Enter the 5G subcarrier spacing in kHz : ')
    if int(BW) in (10,15,20,30,40) and int(SCS) in (15,30,60):
        FRAME_Type=str('FDD')        
        #Break out of loop and continue code  
        break
    elif int(BW)==5 and int(SCS) ==15:
        FRAME_Type=str('FDD')        
        #Break out of loop and continue code  
        break    
    
    elif int(BW) in (60,80,100) and int(SCS) in (30,60):
        FRAME_Type=str('FR1_TDD')        
        #Break out of loop and continue code  
        break 
    elif int(BW)==50 and int(SCS) in (15,30,60):
        FRAME_Type=str('FR1_TDD')        
        #Break out of loop and continue code  
        break 
    elif int(BW) in (100,200) and int(SCS)==120:
        FRAME_Type=str('FR2_TDD')        
        #Break out of loop and continue code  
        break
    else:
        #Rerun loop, and asks user to re-enter data 
        print ("Invalid Input. Please try again")
        continue 
        
print(FRAME_Type)

#input for CA and  Mimo used 
CC=input('Enter the number of aggregated Component Carriers : ')
MIMO=input('Enter the no of dl mimo layers : ')
#From RF conditions at test loaction enter BLER and based on CQI available MCS and  calculate TBS
bler=input('Enter the percentage Bler value (5,10 etc) :')
MCS_index=input('Enter the achieved MCS Index :')
Speceff=[0.2344, 0.3770, 0.6016, 0.8770, 1.1758, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.7305, 3.0293, 3.3223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.3320, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141, 7.1602, 7.4063]
Spec_eff=Speceff[int(MCS_index)]
print ('Spectral efficincy: '+str(Spec_eff))

#Calculate available resources as per frame type for DL data
if str(FRAME_Type)=='FR1_TDD':
    no_of_slots_DL=82
    no_of_slots_SP=32
    Slot_Pattern_Length1=float(1000/80)
    DATA_REs_DL=int(144) #subcarrier(12)xdata Symbols(12)
    DATA_REs_SP=int(84) #subcarrier(12)xdata Symbols(7)
    Number_of_PRBs=math.floor((int(BW)*1000/(int(SCS)*12))-4)  
    TBS_DL=float(82*144*int(MIMO)*float(Spec_eff)*int(Number_of_PRBs))
    TBS_SP=float(32*84*int(MIMO)*float(Spec_eff)*int(Number_of_PRBs))
    
    
elif str(FRAME_Type)=='FDD':
    no_of_slots_DL=19
    Slot_Pattern_Length1=float(1000/20)
    DATA_REs_DL=int(132) #subcarrier(12)xdata Symbols(11)
    Number_of_PRBs=math.floor((int(BW)*1000/(int(SCS)*12))-5)
    TBS_DL=float(19*132*int(MIMO)*float(Spec_eff)*int(Number_of_PRBs))
    TBS_SP=0
      
    
elif str(FRAME_Type)=='FR2_TDD':
    no_of_slots_DL=360
    no_of_slots_SP=112
    Slot_Pattern_Length1=float(1000/80)
    DATA_REs_DL=int(144) #subcarrier(12)xdata Symbols(12)
    DATA_REs_SP=int(84) #subcarrier(12)xdata Symbols(7)
    Number_of_PRBs=math.floor((int(BW)*1000/(int(SCS)*12))-4)  
    TBS_DL=float(360*144*int(MIMO)*float(Spec_eff)*int(Number_of_PRBs))
    TBS_SP=float(112*84*int(MIMO)*float(Spec_eff)*int(Number_of_PRBs))
    
#Calculatre the L1 DL thruput for  
print("PRBs for DL Data : " +str(Number_of_PRBs))
NR_DL_Thp1=(float(TBS_DL)+float(TBS_SP))*int(Slot_Pattern_Length1)*((100-int(bler))/100)*int(CC)/1024/1024
            
NR_DL_Thp=round(NR_DL_Thp1,2)
        
print ("NR THRUPUT : " +str(NR_DL_Thp)+" Mbps")


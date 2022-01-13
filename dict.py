#!/usr/bin/python3
#----------------- NOTES
#InstLabel in elephants = MurexGeneratorLabel in giraffes 
#plins = "mxgeneratorlabel"
#cur   = input_elephants.Cur

import pandas as pd 

giraffes = pd.read_csv('input_giraffes.csv')
elephant = pd.read_csv('input_elephants.csv')
dictionary = pd.read_csv('dictionary_zoo.csv', encoding = "ISO-8859-1")

df = pd.DataFrame(columns=dictionary['CSV Header'])


def setgid(i):                                                                
	if i <10:                        
		return f"REC421_01_000"+str(i)                                    
	elif i>=10 and i < 100:          
		return f"REC421_01_00"+str(i)                                     
	elif i>=100 and i<1000:          
		return f"REC421_01_0"+str(i)                                      
	elif i>=1000:                    
		return "REC421_01_"+str(i)

trndat = 20211101                    
src = 'mx'                           
ext = ''                             
trn_ie = 'E'                         
ctp_ie = 'E'                         
usr_grp = 'DD_ALL'                                                            
usr = 'MXMLUSER'                                                              
pfl = 'DOEX CDE PTEI'                
ctp = 'DOEX MHU PTEI'                
lo = 'L'                             
fml = 'COM'

def grp(mx):
	if "FUT,FWD" in mx:
		return 'FUT'
	elif 'OFT,OFW' in mx:
		return 'OFUT'
	elif "CLR.ASN" in mx:
		return "ASIAN"
	elif 'SWAP' in mx:
		return "SWAP"
	elif 'ASIAN' in mx:
		return 'ASIAN'
	else:
		return ""
def typ(mx):
	if "OFT,OFW" in mx:
		return "LST"
	elif "CLR.ASN" in mx:
		return "CLR"
def typo(mx):
	if "FUT,FWD" in mx:
		return 'Future COM'
	elif 'OFT,OFW' in mx:
		return 'Option on Future COM'
	elif "CLR.ASN" in mx:
		return "Cleared Asian COM"
	elif 'SWAP' in mx:
		return "Swap COM"
	elif 'ASIAN' in mx:
		return 'Asian Option COM'
	else:
		return ""
def eff(mx):
	if "SWAP" in mx or "ASIAN" in mx:
		return "20211101"
	else:
		return ""
def span(mx):
	if "SWAP" in mx or "ASIAN" in mx:
		return "1m"
	else:
		return ""
mat0="NOV-21"
def cfst0(mx):
	if "SWAP" in mx or "ASIAN" in mx:
		return "20211101"
	else:
		return ""
def clst0(mx):
	if "SWAP" in mx or "ASIAN" in mx:
		return "20211130"
	else:
		return ""
def stl(mx):
	if "ASIAN" in mx:
		return "20211103"
	else:
		return ""
def exrsty(mx):
	if "OFT,OFW" in mx:
		return "EUR"
	elif "CLR.ASN" in mx:
		return "ASN"
	elif "ASIAN" in mx:
		return "ASN"
	else:
		return ""
def exrmod(mx):
	if "OFT,OFW" in mx:
		return "DLV"
	elif "CLR.ASN" in mx:
		return "CSH"
	elif "ASIAN" in mx:
		return "CSH"
	else:
		return ""	
def rgt(mx):
	if "OFT,OFW" in mx:
		return "C"
	elif "CLR.ASN" in mx:
		return "F"
	elif "ASIAN" in mx:
		return "C"
	else:
		return ""
def stk(mx):
	if "OFT,OFW" in mx:
		return "1.25"
	elif "CLR.ASN" in mx:
		return "11"
	elif "ASIAN" in mx:
		return "70"
	else:
		return ""
def prc(mx):
	if "FUT,FWD" in mx:
		return "250"
	elif "SWAP" in mx:
		return "-800"
	else:
		return ""
def prm(mx):
	if "OFT,OFW" in mx:
		return "0.5"
	elif "CLR.ASN" in mx:
		return "2.5"
	elif "ASIAN" in mx:
		return "5"
	else:
		return ""
dir_ = "B"
def nom0(mx):
	if "FUT,FWD" in mx:
		return '100'
	elif 'OFT,OFW' in mx:
		return '100'
	elif "CLR.ASN" in mx:
		return "10000"
	elif 'SWAP' in mx:
		return "10000"
	elif 'ASIAN' in mx:
		return '10000'
	else:
		return ""
def qty(mx):
	if 'SWAP' in mx:
		return "10000"
	elif 'ASIAN' in mx:
		return '10000'
	else:
		return ""





print(len(giraffes))
for i in range(len(giraffes)):
	mx = giraffes['mxTypology'][i]
	#elephant.loc[elephant['InstLabel'] == giraffes['MurexGeneratorLabel'][i]]
	cor = elephant.loc[elephant['InstLabel'] == giraffes['MurexGeneratorLabel'][i]]
	try:	
		if "FUT,FWD" in mx or "OFT,OFW" in mx or "CLR.ASN" in mx:
			uod = "LOTS"
		elif  "SWAP" in mx or "ASIAN" in mx:
			uod = cor['UOD'].values[0]
		else:
			uod = ""

		row = {'TRNDAT':trndat, 'SRC':src, 'EXT':ext, 'GID':setgid(i), 'TRN_IE':trn_ie, "CTP_IE":ctp_ie, "USRGRP":usr_grp, "USR":usr, "PFL":pfl, 'CTP':ctp, 'LO':lo, 'FML':fml, 'GRP\xa0':grp(mx), 'TYP':typ(mx), 'TYPO':typo(mx), 'PLINS':giraffes['MurexGeneratorLabel'][i], 'CUR':cor['Cur'].values[0], 'UOD':uod, 'UOV':cor['UOQ'].values[0], 'EFF':eff(mx), 'SPAN':span(mx), "MAT0":mat0, "CFST0":cfst0(mx), 'CLST0':clst0(mx), 'STL':stl(mx), 'EXRSTY':exrsty(mx), 'EXRMOD':exrmod(mx), 'RGT':rgt(mx), 'STK':stk(mx), 'PRC':prc(mx), 'PRM':prm(mx), "DIR":dir_, 'NOM0':nom0(mx), 'QTY':qty(mx)}
	except:
		print(f"error : {i+1}")
		continue
	df = df.append(row, ignore_index=True)
df.to_csv('try1.csv', sep="|", index=False, encoding = "ISO-8859-1")
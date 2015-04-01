import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
if __name__ == '__main__': 

	call_reasons = pd.read_csv('data/BOC/CALLREASON.csv')

	trcode = pd.read_csv('data/BOC/TRCODE.csv', names=["TRID","TRTTYPEID","TRNAME","TRHOSTTIMEOUT","TRCLTTIMEOUT","TRHOSTTRID","TRBEGINTIME","TRENDTIME","TRLOGTABLE","TRPAGE","TRXSL"])
	names = ["CLCALLID","CLSVRNO","CLCALLTIME","CLCALLDURATION","CLCLITELNO","CLCUSTID","CLCUSTTYPE","CLCUSTRANK","CLCERTTYPE","CLCERTID","CLCONTACTID","CLCUSTNAME","CLSEX","CLUNITNAME","CLTEL","CLMOBILE","CLFAX","CLEMAIL","CLADDR","CLZIP","CLIVRCSR","CLCALLFLAG","CLCALLTYPE","CLCALLREASON","CLCALLQUESTION","CLORGID","CLQUESTION","CLRESULT","CLCSRID","CLAGENTID","CLACDGROUPID","CLCOMMEN"]
	calllog1 = pd.read_table('data/CALLLOG_tsv/part-m-00001',header=None,names=names,low_memory=False)

	clcustid = calllog1["CLCUSTID"]
	print(clcustid.value_counts()[:10])



	nums = range(0,9)
	pieces = [] 
	for num in nums: 
		path = 'data/CALLLOG_tsv/part-m-0000%d' % num
		frame = pd.read_table(path,header=None,names=names,low_memory=False)
		pieces.append(frame)
		names = pd.concat(pieces, ignore_index=True)
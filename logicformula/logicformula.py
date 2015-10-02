from django.http import HttpResponse
import os
import subprocess
cp=os.path.dirname(os.path.abspath(__file__))

def getres(request):
	logicf=request.GET['q']
	f=os.popen(cp+'/logic_formula \"'+logicf+'\"')
	res=f.readlines()
	resdict={}
	resdict['reverse_poland']=res[0].strip()
	resdict['argnum']=int(res(1).strip())
	resdict['arglist']=res[2].strip().split('\t')
	resdict['value_table']=[]
	for i in range(0,1<<resdict['argnum']):
		row=res[3+i].strip().split('\t')
		resdict['value_table'].append(row)
	resdict['true_list']=res[-2].strip().split('\t')
	resdict['false_list']=res[-1].strip().split('\t')
	f.close()

	return HttpResponse(resdict)
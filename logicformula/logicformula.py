from django.http import HttpResponse
import os
import subprocess
cp=os.path.dirname(os.path.abspath(__file__))

def getres(request):
	logicf=request.GET['q']
	# tmp=subprocess.call([cp+'/logic_formula \"'+logicf+'\"'],shell=True)
	f=os.popen(cp+'/logic_formula \"'+logicf+'\"')
	#f=open(os.path.dirname(cp)+'/output.txt')
	res=f.readlines()
	f.close()
	text='<html><body><p>%s</p></body></html>'%(res)
	return HttpResponse(text)

if (__name__=='__main__'):
	logicf='\"a%c|e\"'
	subprocess.call([cp+'/logic_formula '+logicf],shell=True)
	f=open(cp+'/output.txt')
	res=f.read()
	print res
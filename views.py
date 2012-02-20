from django.shortcuts import render_to_response
from django.http import HttpResponse
import urllib2
import urllib
import json
#LAPIKey
#Token
def login(request):
	return render_to_response('Templates2/login.html')
def main(request):
	if ('key' in request.GET) and ('token' in request.GET):
		LAPIKey= request.GET['key']
		Token = request.GET['token']
		username= getUserName(LAPIKey,Token)
		modules = getModules(LAPIKey,Token)
		parsedm=parseModule(modules)
		resultm= json.dumps(parsedm)
		#forum = 
		return render_to_response('Templates/main.html',{'username':username, 'modules':resultm})
	else:
		return HttpResponse("Not enough data")		

def rmain(request):
	return render_to_response('Templates/main.html')

def getUserName(LAPIKey,Token):
	getUsernameURL = "https://ivle.nus.edu.sg/api/Lapi.svc/UserName_Get?APIKey=%s&Token=%s&output=json" % (LAPIKey,Token)
	content = urllib2.urlopen(getUsernameURL)
	name_json_raw = content.read()
	name = json.loads(name_json_raw)
	return name
def getModules(LAPIKey,Token):
	getModulesURL="https://ivle.nus.edu.sg/api/Lapi.svc/Modules?APIKey=%s&AuthToken=%s&Duration=0&IncludeAllInfo=false&output=json"%(LAPIKey, Token)
	content = urllib2.urlopen(getModulesURL)
	modules_json_raw = content.read()
	modules = json.loads(modules_json_raw)
	return modules
def getForum(LAPIKey,Token,CourseID):
	getForumURL="https://ivle.nus.edu.sg/api/Lapi.svc/Forums?APIKey=%s&AuthToken=%s&CourseID=%s&Duration=0&IncludeThreads=true&TitleOnly=false"%(LAPIKey,Token,CourseID)
	content = urllib2.urlopen(getForumURL)
	forum_json_raw=content.read()
	forum = json.loads(forum_json_raw)
	return forum
def postNewThread(LAPIKey,Token,HeadingID, Title, Body):
	data = urllib.urlencode({'APIKey':'%s' %(LAPIKey),'AuthToken':'%s'%(Token),'HeadingID':'%s' %(HeadingID),'Title':'%s'%(Title),'Reply':'%s'%(Body)})
	u = urllib2.urlopen("https://ivle.nus.edu.sg/api/Lapi.svc/Forum_PostNewThread_JSON",data)
	return u.read()
def replyNewThread(LAPIKey,Token,ThreadID,Title, Body):
	data = urllib.urlencode({'APIKey':'%s' %(LAPIKey),'AuthToken':'%s'%(Token),'ThreadID':'%s' %(ThreadID),'Title':'%s'%(Title),'Reply':'%s'%(Body)})
	u = urllib2.urlopen("https://ivle.nus.edu.sg/api/Lapi.svc/Forum_ReplyThread_JSON",data)
	return u.read()

def parseModule(module):
	i=0
	parsed_modules = []
	for result in module["Results"]:
		parsed_module={"CourseCode":result["CourseCode"], "ID":result["ID"]}
		#bla = json.dumps(parsed_module)
		parsed_modules.append(parsed_module)
	
	return parsed_modules

	












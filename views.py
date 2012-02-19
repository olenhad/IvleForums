from django.shortcuts import render_to_response
import urllib2
import urllib
import json
global LAPIKey
global Token
def login(request):
	return render_to_response('inputLAPI.html')
def main(request):
	if ('key' in request.GET) and ('token' in request.GET):
		global LAPIKey= request.GET['key']
		global Token = request.GET['token']
		


def getUserName():
	getUsernameURL = "https://ivle.nus.edu.sg/api/Lapi.svc/UserName_Get?APIKey=%s&Token=%s&output=json" % (LAPIKey, Token)
	content = urllib2.urlopen(getUsernameURL)
	name_json_raw = content.read()
	name = json.loads(name_json_raw)
	return name
def getModules():
	getModulesURL="https://ivle.nus.edu.sg/api/Lapi.svc/Modules?APIKey=%s&AuthToken=%s&Duration=0&IncludeAllInfo=false&output=json"%(LAPIKey, Token)
	content = urllib2.urlopen(getModulesURL)
	modules_json_raw = content.read()
	modules = json.loads(modules_json_raw)
	return modules
def getForum(CourseID):
	getForumURL="https://ivle.nus.edu.sg/api/Lapi.svc/Forums?APIKey=%s&AuthToken=%s&CourseID=%s&Duration=0&IncludeThreads=true&TitleOnly=false"%(LAPIKey,Token,CourseID)
	content = urllib2.urlopen(getForumURL)
	forum_json_raw=content.read()
	forum = json.loads(forum_json_raw)
	return forum
def postNewThread(HeadingID, Title, Body):
	data = urllib.urlencode({'APIKey':'%s' %(LAPIKey),'AuthToken':'%s'%(Token),'HeadingID':'%s' %(HeadingID),'Title':'%s'%(Title),'Reply':'%s'%(Body))
	u = urllib2.urlopen("https://ivle.nus.edu.sg/api/Lapi.svc/Forum_PostNewThread_JSON",data)
	return u.read()
def replyNewThread(ThreadID,Title, Body):
	data = urllib.urlencode({'APIKey':'%s' %(LAPIKey),'AuthToken':'%s'%(Token),'ThreadID':'%s' %(ThreadID),'Title':'%s'%(Title),'Reply':'%s'%(Body))
	u = urllib2.urlopen("https://ivle.nus.edu.sg/api/Lapi.svc/Forum_ReplyThread_JSON",data)
	return u.read()

	












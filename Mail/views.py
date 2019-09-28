from django.shortcuts import render
from django.http import HttpResponse
from django.template import context,loader
import sqlite3
from Mail.models import emails
from Mail.models import users
from datetime import date


def index(request):
	t=loader.get_template("index.html")
	c={}
	v=t.render(c)
	resp=HttpResponse(v)
	return(resp)

def register(request):
	return render(request,'register.html')

def registerSave(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	cpwd=request.POST["cpwd"]
	unm=request.POST["unm"]
	gen=request.POST["gen"]
	cnty=request.POST["cnty"]
	u=users(EmailId=eid,Password=pwd,Username=unm,Gender=gen,Country=cnty)
	u.save()
	a="<h1>Record Saved </h1>"
	resp=HttpResponse(a)
	return(resp)

def login(request):
	return render(request,'login.html')

def loginCheck(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]

	qs=users.objects.filter(EmailId=eid,Password=pwd)
	if qs:
		request.session['eid']=eid
		request.session['pwd']=pwd
		return render(request,"emailHome.html",{"uname":qs[0]})
	else:
		msg="<h1>Invalid User ID or Password </h1>"
		resp=HttpResponse(msg)
		return(resp)

def compose(request):
	return render(request,'compose.html')
def composeSave(request):
	toeid=request.POST["toeid"]
	sub=request.POST["sub"]
	msg=request.POST["msg"]
	curdate=date.today()
	edate=curdate.strftime("%Y-%m-%d")
	feid=request.session.get("eid")
	u=emails(EmailDate=edate,FromEmailId=feid,ToEmailId=toeid,Subject=sub,Message=msg)
	u.save()
	a="<h1>MESSAGE SEND </h1>"
	resp=HttpResponse(a)
	return(resp)
'''def inbox(request):
	return render(request,'inbox.html')'''
def inbox(request):
	eid=request.session.get("eid")
	inbox=emails.objects.filter(ToEmailId=eid)

	v="<table width='100%' border='1'>"	
	v+="<tr><th> Email Date</th>"
	v+="<th>Email Id</th>"
	v+="<th>Subject</th>"

	v+="<th>Message</th></tr>"
	for rec in inbox:
		v+="<tr><td align=center>"+str(rec.EmailDate)+"</td>"
		v+="<td align=center>"+rec.FromEmailId+"</td>"
		v+="<td align=center>"+rec.Subject+"</td>"
		v+="<td align=center>"+rec.Message+"</td></tr>"
	v+="</table>"

	resp=HttpResponse(v)
	return(resp)


def sent(request):
	eid=request.session.get("eid")
	inbox=emails.objects.filter(FromEmailId=eid)
	v="<table width='100%' border='1'>"
	v+="<tr><th> Email Date</th>"
	v+="<th>Email Id</th>"
	v+="<th>Subject</th>"
	v+="<th>Message</th></tr>"
	for rec in inbox:
		v+="<tr><td align=center>"+str(rec.EmailDate)+"</td>"
		v+="<td align=center>"+rec.ToEmailId+"</td>"
		v+="<td align=center>"+rec.Subject+"</td>"
		v+="<td align=center>"+rec.Message+"</td></tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)
def changePassword(request):
	return render(request,'changePassword.html')
def changePasswordSave(request):
	eid=request.session.get('eid')
	pwd=request.session.get('pwd')
	cp=request.POST['cp']
	np=request.POST['np']
	qs=users.objects.filter(EmailId=eid)
	if pwd==cp and qs:
		qs[0].Password=np
		qs[0].save()
		msg="<h1>PASSSWORD CHANGED SUCCESSFULLY</H1>"
	else:
		msg="<h1>INVALID PASSWORD</h1>"
	resp=HttpResponse(msg)
	return(resp)
	
def signout(request):
	request.session.flush()
	return render(request,'index.html')
def checkEmail(request):
	id=request.GET["eid"]
	qs=Users.objects.filter(emailId=id)
	if qs:
		msg="<h1> Not-Available </h1>"
	else:
		msg="<h1> Available </h1>"
	resp=HttpResponse(msg)
	return(resp)
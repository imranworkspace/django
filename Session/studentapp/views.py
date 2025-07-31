from django.shortcuts import render

# Create your views here.
def set_session_view(request):
    resp=request.session['fname']='imran'
    resp=request.session['lname']='shaikh'
    request.session.set_expiry(10)# session expires in  10 seconds 
    resp = render(request,'set_session.html')
    return resp

def get_session_view(request):
    # fname=request.session.get('fname')
    fname=request.session.get('fname','guest')
    lname=request.session.get('lname','guest')
    return render(request,'get_session.html',{'fname':fname,'lname':lname})

def flush_session_view(request):
    request.session.flush()
    return render(request,'flush.html')

def view_methods(request):
    keys=request.session.keys()
    items=request.session.items()
    getexpireatbrowser = request.session.get_expire_at_browser_close()
    get_expiry_age = request.session.get_expiry_age()
    expiry_date = request.session.get_expiry_date()
    return render(request,'view_method.html',{'keys':keys,'items':items,'getexpireatbrowser':getexpireatbrowser,'expiry_date':expiry_date,
    'get_expiry_age':get_expiry_age})
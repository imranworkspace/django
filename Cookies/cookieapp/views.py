from django.shortcuts import render

# Create your views here.
def set_cookieview(request):
    resp = render(request,'cookieapp/setcookie.html')
    resp.set_cookie('token','tk123')
    return resp

def get_cookieview(request):
    # get_Token=request.COOKIES.get('token')
    get_Token=request.COOKIES.get('token','guest123')
    print(get_Token)
    return render(request,'cookieapp/getcookie.html',{'token':get_Token})

def del_cookieview(request):
    resp = render(request,'cookieapp/del_cookie.html')
    resp.delete_cookie('token')
    return resp

def set_signed_cookie_view(request):
    resp = render(request,'cookieapp/set_cookiesignedin.html')
    resp.set_signed_cookie('token','tk1234',salt='tk')
    return resp

def get_signed_cookie_view(request):
    # request.get_signed_cookie('token',salt='tk')
    token=request.get_signed_cookie('token',default='guest123',salt='tk')
    return render(request,'cookieapp/get_cookiesignedin.html',{'token':token})
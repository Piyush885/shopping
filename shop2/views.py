from django.shortcuts import render,HttpResponse,redirect
from shop2.models import adminlogin,userlogin,items,cart
import shop2
from passlib.hash import pbkdf2_sha256
# Create your views here.
adminuser=[]
adminpass=[]
user=[]
userpass=[]
#iname=[]
#iprice=[]
display={}
display2={}
# p=adminlogin.objects.raw('SELECT id, username,passwd FROM shop2_adminlogin')
# q=userlogin.objects.raw('SELECT id, username,passwd FROM shop2_userlogin')
# r=items.objects.raw('SELECT id,pname,price FROM shop2_items')
p=adminlogin.objects.all()
q=userlogin.objects.all()
r=items.objects.all()
for i in p:
    adminuser.append(i.username)
    adminpass.append(i.passwd)
for i in q:
    user.append(i.username)
    userpass.append(i.passwd)        
def home(request):
    return render(request,'index.html')
# def adminpage(request):
#     return render(request,'admin.html')
# def userpage(request):
#     return render(request,'user.html')
def adminvalidate(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        if(username in adminuser and passwd in adminpass):
            r=items.objects.all()
            # for i in r:
            #     display[i.pname] = i.price
            #     display2[i.price] = i.pname
            # content4={"message4":display,"message5":display2}
            # output = items()
            # content4={"message4":output}
            # print(content4)

            return render(request,'admin2.html',{'message4':r})
        else:
            content = {"message":"Wrong entry"}
            return render(request,"index.html",content)        
def uservalidate(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        print(username,passwd)
        user=[]
        userpass=[]
        q=userlogin.objects.all()
        for i in q:
            user.append(i.username)
            userpass.append(i.passwd) 
        print(user,userpass)    
        flag=0
        for i in range(len(userpass)):
            if(pbkdf2_sha256.verify(passwd,userpass[i])):
                flag=1
                break
        if(username in user and flag==1):
            r=items.objects.all()
            print("loop chl rha h bhai")
            content={"name":username,"message5":r}
            return render(request,'order.html',content)
        else:
            content1 = {"message1":"Wrong entry"}
            return render(request,"index.html",content1)
def additems(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        price = request.POST.get('price')
        item = items(pname = pname,price = price)
        item.save()
        # r=items.objects.raw('SELECT id,pname,price FROM shop2_items')
        # for i in r:
        #     display[i.pname] = i.price
        #     display
        # content4={"message4":display}
        return HttpResponse("Item added successfully")
def update(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        price = request.POST.get('price')
        items.objects.filter(pname=pname).update(price = price)
        for i in r:
            display[i.pname] = i.price
        content4={"message4":display}
        #return render(request,'admin2.html',content4)
        return HttpResponse("Updated")
    else:
        HttpResponse(request,"hello")    
def delete(request):
    if request.method == 'POST':
        pname=request.POST.get('pname')
        items.objects.filter(pname =pname).delete()
        return HttpResponse("Deleted")
def addtocart(request,pname,price,name):
    cart1=cart(username=name,pname=pname,price=price)
    cart1.save()
    return HttpResponse("added to cart")
def showcart(request,name):
    cartitems = cart.objects.filter(username = name)
    bill=0
    for i in cartitems:
        bill = bill + int(i.price)
    content = {"message6":cartitems,"total":bill,"Total":"Total Amount","name":i.username}
    return render(request,'cart.html',content)
def cartremove(request,pname,name):
    cart.objects.filter(username=name,pname=pname).delete()
    return HttpResponse("Removed from cart")    
def newuserpage(request):
    return render(request,"newuser.html")    
def usersave(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # s = string.ascii_letters + string.digits + string.punctuation
        # random.shuffle(s)
        # salt = s[0:4]
        username = request.POST.get('username')
        # hashing password(ship hash)
        password = request.POST.get('password')
        password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
        m=userlogin(username=username,email=email,passwd=password)       
        m.save()
        return redirect(home) 


    
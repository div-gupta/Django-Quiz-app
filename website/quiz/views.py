from django.shortcuts import render,redirect
from .models import Java
from django.contrib.auth.models import User,auth


from django.contrib import messages


from django import forms
# Create your views here.
def index(request):
    return render(request,'index.html')


def aboutus(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def editprofile(request):
   
         return render(request,'editprofile1.html')
    

marks=0
def quiz(request):
    questions= Java.objects.all()
    return render(request,'quiz.html',{'questions':questions})

    
def score(request):
	questions = Java.objects.all()
	global marks
	for question in questions:
		correct_answer = question.correct 
		entered_answer = request.POST.get(str(question.id)) 
		if(entered_answer == correct_answer): 
			marks+=1 
    

	context = {'marks':marks}
    
	return render(request, 'scoreboard.html', context)

		







def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
      
        user = auth.authenticate(request,username = username,password = password)
        # use= check_password(password1 , password)
        # print(username)
        # print(password)
        # print(username1)
        # print(password1)
        #print(user)
        
        if user is not None :
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')

    else:
        return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect("index")
def register(request):
    
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        print(password)
         
      

        if User.objects.filter(email=email ).exists():
                messages.info(request,"email taken")
                return redirect('register')
        elif User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')

      
        else:
           
			


            
            
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save();
            print('user created')
            return render(request,'signin.html')
          
            
           
    else:
        

       
       
        return render(request,'register.html')
        


        

   
 
    






# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import Users, Data
import json
import random

@csrf_exempt
def gen(request):
    for i in xrange(0, 50):
        data = Data(
    				eating = random.randint(1, 5),
                    #1-5
                    drinking = random.randint(1,8),
                    #0-8

                    toileting = random.randint(1,10),
                    #1-10
                    
                    showering = random.randint(1,3),
                    #1-3
                    
                    leaving = random.randint(1,12),
                    #1-12
                    sleeping = random.randint(4,10),
                    #4-10
                    
                    weight = random.uniform(40, 130) )


        data.save()
    #return JsonResponse({'error':"1"})     
    return JsonResponse({'foo':'bar'})
    


@csrf_exempt
def req(request):
    data = json.loads(request.body)
    print("data recieved=", data)


    dataToBeSend = {}
    dataToBeSend['error'] = "1"
    
    

    eatingMean = 0
    drinkingMean = 0
    toiletingMean = 0
    showeringMean = 0 
    leavingMean = 0
    sleepingMean = 0 
    weightMean = 0

    eatingMin = 1000
    drinkingMin = 1000
    toiletingMin = 1000
    showeringMin = 1000 
    leavingMin = 1000
    sleepingMin = 1000 
    weightMin = 1000

    eatingMax = -1000
    drinkingMax = -1000
    toiletingMax = -1000
    showeringMax = -1000 
    leavingMax = -1000
    sleepingMax = -1000 
    weightMax = -1000


    count=0

    all_entries = Data.objects.all()


        
    for entry in all_entries:
        count=count+1

        eating=entry.eating
        drinking = entry.drinking
        toileting = entry.toileting
        showering = entry.showering
        leaving = entry.leaving
        sleeping = entry.sleeping
        weight = entry.weight

        eatingMean=eatingMean+eating
        drinkingMean = drinkingMean+drinking
        toiletingMean = toiletingMean+toileting
        showeringMean = showeringMean+ showering
        leavingMean = leavingMean+leaving
        sleepingMean = sleepingMean+ sleeping
        weightMean = weightMean+weight
    
    eatingMean=eatingMean/count
    drinkingMean = drinkingMean/count
    toiletingMean = toiletingMean/count
    showeringMean = showeringMean/count
    leavingMean = leavingMean/count
    sleepingMean = sleepingMean/count
    weightMean = weightMean/count

    for entry in all_entries:
        eating=entry.eating-eatingMean
        drinking = entry.drinking-drinkingMean
        toileting = entry.toileting-toiletingMean
        showering = entry.showering-showeringMean
        leaving = entry.leaving-leavingMean
        sleeping = entry.sleeping-sleepingMean
        weight = entry.weight-weightMean

        if(eatingMin>eating):
            eatingMin=eating
        if(eatingMax<eating):
            eatingMax=eating

        if(drinkingMin>drinking):
            drinkingMin=drinking
        if(drinkingMax<drinking):
            drinkingMax=drinking
            
        if(toiletingMin>toileting):
            toiletingMin=toileting
        if(toiletingMax<toileting):
            toiletingMax=toileting

        if(showeringMin>showering):
            showeringMin=showering
        if(showeringMax<showering):
            showeringMax=showering

        if(leavingMin>leaving):
            leavingMin=leaving
        if(leavingMax<leaving):
            leavingMax=leaving 
        
        if(sleepingMin>sleeping):
            sleepingMin=sleeping
        if(sleepingMax<sleeping):
            sleepingMax=sleeping

        if(weightMin>weight):
            weightMin=weight
        if(weightMax<weight):
            weightMax=weight 

    
    eating = data['eating']
    drinking = data['drinking']
    toileting = data['toileting']
    showering = data['showering']
    leaving = data['leaving']
    sleeping = data['sleeping']
    weight = data['weight'] 

    data = Data(
                    eating = eating,
                    #1-5
                    drinking = drinking,
                    #0-8

                    toileting = toileting,
                    #1-10
                    
                    showering = showering,
                    #1-3
                    
                    leaving = leaving,
                    #1-12
                    sleeping = sleeping,
                    #4-10
                    
                    weight = weight )


    data.save()

    dataToBeSend['eating'] = (((eating - eatingMin)/(eatingMax - eatingMin))*(4)) -2
    dataToBeSend['drinking'] = (((drinking - drinkingMin)/(drinkingMax - drinkingMin))*(4)) -2
    dataToBeSend['toileting'] = (((toileting - toiletingMin)/(toiletingMax - toiletingMin))*(4)) -2
    dataToBeSend['showering'] = (((showering - showeringMin)/(showeringMax - showeringMin))*(4)) -2
    dataToBeSend['leaving'] = (((leaving - leavingMin)/(leavingMax - leavingMin))*(4)) -2
    dataToBeSend['sleeping'] = (((sleeping - sleepingMin)/(sleepingMax - sleepingMin))*(4)) -2
    dataToBeSend['weight'] = (((weight - weightMin)/(weightMax - weightMin))*(4)) -2

    print("data sent=", dataToBeSend)
    
    

    return JsonResponse(dataToBeSend)








        
        

        
    # return JsonResponse({'foo':'bar'})
    # if (request.method=='POST' and  not( data['eating']=='' or data['drinking']==''  or data['toileting']==''
    #     or data['showering']==''  
    #     or data['leaving']==''  or data['sleeping']==''  or data['weight']=='' ) )  :


    #     all_entries = data.objects.all()
        
    #     for entry in all_entries:
    #         print entry



    #     print ("Got the post req")
    #     # user = Users(
    #     #     name=str(request.POST.get('name')),
    #     #     password=str(request.POST.get('password')),
    #     #     email=str(request.POST.get('email')),
    #     #     address=str(request.POST.get('address')),
    #     #     )
        
    #     returnRespone['error'] = "0"
    #     return JsonResponse(returnRespone)
    # else:
    #     return JsonResponse(returnRespone)


def index(request):
    return HttpResponse("Hello, world")

def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)    
  
@csrf_exempt
def signup(request):
    #return JsonResponse({'foo':'bar'})
    #print(request.body.get('name'))
    #print(request.get_json())


    print(request.body)   
    data = json.loads(request.body)

    print(data['name'])
    # {"email":"a","password":"a","name":"a","address":"a"}

    # #s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
    # json_acceptable_string = (request.body).replace("'", "\"")
    # d = json.loads(request.body)
    # print(d)
    # print(d.name)

    #print("post=", request.POST)
	
    returnRespone = {}
    returnRespone['error'] = "1"
    # print(request.POST.get('flat'),request.POST.get('flong'),request.POST.get('dlat'),request.POST.get('dlong'))

    #if (request.method=='POST' and  not( request.POST.get('name')=='' or request.POST.get('email')==''  or request.POST.get('password')=='' or request.POST.get('address')=='') )  :
    if (request.method=='POST' and  not( data['name']=='' or data['email']==''  or data['password']=='' or data['address']=='') )  :
        print ("Got the post req")
        # user = Users(
        #     name=str(request.POST.get('name')),
        #     password=str(request.POST.get('password')),
        #     email=str(request.POST.get('email')),
        #     address=str(request.POST.get('address')),
        #     )
        user = Users(
            name=str(data['name']),
            password=str(data['password']),
            email=str(data['email']),
            address=str(data['address']),
            )
        user.save()
        returnRespone['error'] = "0"
        return JsonResponse(returnRespone)
    else:
        return JsonResponse(returnRespone)
     

@csrf_exempt
def login(request):
    
    print(request.body)   
    data = json.loads(request.body)
    #if (request.method=='POST' and  not( request.POST.get('email')==''  or request.POST.get('password')=='' ) ) :
    if (request.method=='POST' and  not( data['email']==''  or data['password']==''))  :
    
        
        print(request)
        print(data['email'])
        print(data['password'])
        email=str(data['email'])
        password=str(data['password'])
        
        dataToBeSend = {}
        dataToBeSend['login_value'] = 'not ok'
        dataToBeSend['error'] = "1"

        if(Users.objects.filter(password=password, email=email).exists()):
            request.session['email'] = email
            email=request.session['email']
            user=(Users.objects.get(email=email))
            
            
            name=user.name
            print ("name=", name)
            dataToBeSend['name'] =str(name)
            dataToBeSend['login_value'] = 'ok'
            dataToBeSend['error'] = "0"
            print (JsonResponse(dataToBeSend))
            return JsonResponse(dataToBeSend)

        else:
            print (JsonResponse(dataToBeSend))
            return JsonResponse(dataToBeSend)
    else:
        return JsonResponse({'error':"1"})        

@csrf_exempt
def logout(request):
    print request
    try:
        print request.session._session_key
        print request.session.items()
        del request.session['email']
        print request.session.items()
        return JsonResponse({'error':0})
    except:
        return JsonResponse({'error':1})
    

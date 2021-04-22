from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request,"index.html")

def process_money(request,start,end):
    gold = random.randrange(int(start),int(end))
    request.session['gold'] += gold
    if gold < 0:
        activity = {
            'color':'red',
            'text':f'You lost {gold} ',
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
    else:
        activity = {
            'color':'green',
            'text':f'You won bro {gold} ',
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }
    request.session['activity'].append(activity)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

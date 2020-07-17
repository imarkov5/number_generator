from django.shortcuts import render, HttpResponse, redirect
import random
from .models import Player

def index(request):
    context = {
        'all_players' : Player.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    print(request.method)
    if request.method == 'POST':
        #play the game
        com_num = int(random.random()*10)
        if int(request.POST['user_guess']) > com_num:
            result = "guessed too high"
            request.session['style'] = 'high'
        elif int(request.POST['user_guess']) < com_num:
            result = "you guessed too low"
            request.session['style'] = 'low'
        else:
            result = "you guessed the number!"
            request.session['style'] = 'right'
         
        print(com_num, "This is the com generated number")
        # print(request.POST, "This is my request.POST")
        # print(request.POST['username'])
        # print(request.POST['user_guess'])
        print(result, "This was my result")
        new_player = Player.objects.create(name=request.POST['username'], guess=request.POST['user_guess'], result=result)
        print(new_player, 'This is the player that was just created')
        return redirect('/')
    return redirect('/')

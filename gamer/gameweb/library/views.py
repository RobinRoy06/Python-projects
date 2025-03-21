from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game
from .forms import GameForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    
    games = Game.objects.all() #Links games variable to the game model

    if request.method =="POST": #When user sends a postrequest
        form = GameForm(request.POST) #Variable form becomes the game form

        if form.is_valid(): #Checks if the form is valid
                form.save() #Saves form to database
                context = {"form":GameForm(), "games":games}
                return render(request, "library/index.html", context) #Renders the index page with game form and games
    else:
        form = GameForm() # If its something other then a post request it returns the empty form
        
    context = {"form":form, "games": games}
    return render(request, "library/index.html", context)


def account_creation(request):

    pass


def delete_game(request, game_id):

    game = get_object_or_404(Game, pk=game_id)

    # If the request method is POST, it means the user has confirmed the deletion
    if request.method == "POST":
        game.delete()  # Delete the game
        return redirect("index")  # Redirect to the index page after deletion

    # If the request method is GET, show the confirmation page
    return render(request, 'library/delete_confirmation.html', {'game': game})

 
def update_game(request, pk):
    game = get_object_or_404(Game, id=pk) # finds game object or returns 404 
    
    if request.method =="POST": #If request is post
        form = GameForm(request.POST, instance=game) 
        if form.is_valid(): #Checks if the form is valid
            form.save() #Saves form to database
            return redirect("index") # Redirects to index
    else:
        form = GameForm(instance=game)    

    context = {'form':form, "game":game} #Passes form and game for further handling
    return render(request, "library/update_game.html", context) #If its GET then renders update_game page
    

def view_game(request,pk):
    game = get_object_or_404(Game, id=pk)  # Fetches the game object by primary key (pk)
    
    # Render the 'view_game' template with the 'game' object
    return render(request, "library/view_game.html", {"game": game})
 #If its GET then renders update_game page
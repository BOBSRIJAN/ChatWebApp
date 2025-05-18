from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.http import JsonResponse

# Connect to MongoDB
client = MongoClient('mongodb+srv://srijan:1234@cluster0.yrnd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['massage12']
massage = db['msg']
active_users = db['active_users']


def login_view(request):
    user1_active = active_users.find_one({'user': 'user1'}) is not None
    user2_active = active_users.find_one({'user': 'user2'}) is not None

    if request.method == 'POST':
        username = request.POST.get('username')

        # Check if already taken
        if active_users.find_one({'user': username}):
            return render(request, 'msgapp/login.html', {
                'error': 'User already in use.',
                'user1_active': user1_active,
                'user2_active': user2_active,
            })

        # Save user in session and mark as active
        request.session['username'] = username
        active_users.insert_one({'user': username})
        return redirect('home')

    return render(request, 'msgapp/login.html', {
        'user1_active': user1_active,
        'user2_active': user2_active,
    })

def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    if request.method == 'POST':
        msg = request.POST.get('msg')
        massage.insert_one({'user': username, 'msg': msg})

    all_msgs = list(massage.find())
    return render(request, 'msgapp/home.html', {'messages': all_msgs, 'username': username})

def logout_view(request):
    username = request.session.get('username')
    if username:
        active_users.delete_one({'user': username})
        request.session.flush()
    return redirect('login')


def UsClear(request):
    active_users.delete_many({})
    return HttpResponse("All active users cleared.")





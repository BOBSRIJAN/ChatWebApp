from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dbconf import db, massage, active_users
import json

# Connect to MongoDB
db = db
massage = massage
active_users = active_users

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
        if msg:  # Ensure the message is not empty
            massage.insert_one({'user': username, 'msg': msg})
        all_msgs = list(massage.find())
        return render(request, 'msgapp/home.html', {'messages': all_msgs, 'username': username})

    all_msgs = list(massage.find())
    return render(request, 'msgapp/home.html', {'messages': all_msgs, 'username': username})

@csrf_exempt  # Allow AJAX POST without CSRF for simplicity (see security note below)
def messages_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg = data.get('msg')
        username = request.session.get('username')
        if username and msg:
            massage.insert_one({'user': username, 'msg': msg})
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

    # GET: Return all messages
    all_msgs = list(massage.find({}, {'_id': 0, 'user': 1, 'msg': 1}))  # Exclude _id
    return JsonResponse({'messages': all_msgs})

def logout_view(request):
    username = request.session.get('username')
    if username:
        active_users.delete_one({'user': username})
        request.session.flush()
    return redirect('login')

def UsClear(request):
    active_users.delete_many({})
    return HttpResponse("All active users cleared.")
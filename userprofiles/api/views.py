import json
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from userprofiles.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


def userprofiles_list(request):
    """
    Retrieve (GET)
    List of data
    """

    up_list = UserProfile.objects.all()

    data_list = list()

    for up in up_list:
        up_dict = dict()

        up_dict["username"] = up.user.username
        up_dict["first_name"] = up.user.first_name
        up_dict["last_name"] = up.user.last_name
        up_dict["email"] = up.user.email
        up_dict["is_active"] = up.user.is_active
        up_dict["birth_date"] = up.birth_date
        up_dict["location"] = up.location
        up_dict["bio"] = up.bio
        up_dict["id"] = up.id
        up_dict["avatar"] = up.avatar.name

        data_list.append(up_dict)

    # data = {"results": list(up_list.values("bio", "location", "birth_date", "avatar", "user_id"))}

    data = {"results": data_list}

    return JsonResponse(data)


def userprofile_detail(request, pk):
    """
    Retrieve (GET)
    Detail of data
    """
    up_detail = get_object_or_404(UserProfile, pk=pk)

    data = {
        "result": {
            "username": up_detail.user.username,
            "first_name": up_detail.user.first_name,
            "last_name": up_detail.user.last_name,
            "email": up_detail.user.email,
            "is_active": up_detail.user.is_active,
            "birth_date": up_detail.birth_date,
            "location": up_detail.location,
            "bio": up_detail.bio,
            "id": up_detail.id,
            "avatar": up_detail.avatar.name
        }
    }

    return JsonResponse(data)


@csrf_exempt
def create_user(request):

    """
    Create (POST)
    http://127.0.0.1:8000/api/userprofiles/create/
    """

    if request.method == 'POST':

        """
        <QueryDict: {'first_name': ['First name'], 'last_name': ['Last name'], 'email': ['testuser@gmail.com'], 'username': ['testuser1']}>
(Pdb) request.POST.get('email')
'testuser@gmail.com'
        """
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_active = request.POST.get('is_active')

        data = {
            "result": {
                'message': 'You have successfully register'
            }
        }

        try:
            if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username, email, password)
                user.first_name(first_name)
                user.last_name(last_name)
                user.is_active(is_active)
                user.save()

                data['result']['message'] = 'You have successfully register'
                data['result']['user_id'] = User.objects.filter(username=username).id

                return JsonResponse(data)
            else:

                data['result']['message'] = 'The user already exists'

                return JsonResponse(data)

        except Exception as e:
            data['result']['message'] = 'User can not be created due to an exception.'
            data['result']['error'] = e.message
            return JsonResponse(data)


@csrf_exempt
def create_profile(request):
    """
    Create (POST)

    """

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        birth_date = request.POST.get('birth_date')
        location = request.POST.get('location')
        bio = request.POST.get('bio')
        avatar = request.data['file']

        data = {
            "result": {
                'message': 'You have successfully created profile'
            }
        }

        try:
            if User.objects.filter(id=user_id).exists():
                user = User.objects.filter(id=user_id)
                user_profile = UserProfile(user=user, birth_date=birth_date, location=location, bio=bio, avatar=avatar)
                user_profile.save()

                data['result']['message'] = 'You have successfully created user profile'
                return JsonResponse(data)
            else:
                data['result']['message'] = 'User does not exists. Can not update user profile.'

                return JsonResponse(data)

        except Exception as e:
            data['result']['message'] = 'User can not be created due to an exception.'
            data['result']['error'] = e.message
            return JsonResponse(data)


@csrf_exempt
def update_profile(request):
    """
    Update (PUT)
    """

    if request.method == 'PUT':

        user_id = request.POST.get('user_id')
        birth_date = request.POST.get('birth_date') if request.POST.get('birth_date') else ''
        location = request.POST.get('location') if request.POST.get('location') else ''
        bio = request.POST.get('bio') if request.POST.get('bio') else ''
        avatar = request.data['file'] if request.data['file'] else ''

        data = {
            "result": {
                'message': 'You have successfully updated profile'
            }
        }

        try:
            if User.objects.filter(id=user_id).exists():
                user = User.objects.filter(id=user_id)

                if UserProfile.objects.filter(user=user).exists():

                    # bad code need to optimize
                    if birth_date:
                        UserProfile.objects.update(user=user, birth_date=birth_date)
                    if location:
                        UserProfile.objects.update(user=user, location=location)
                    if bio:
                        UserProfile.objects.update(user=user, bio=bio)
                    if avatar:
                        UserProfile.objects.update(user=user, avatar=avatar)

                    data['result']['message'] = 'User profile updated successfully.'

                    return JsonResponse(data)
                else:
                    data['result']['message'] = 'User profile does not exists.'

                    return JsonResponse(data)
            else:

                data['result']['message'] = 'User does not exists.'

                return JsonResponse(data)

        except Exception as e:
            data['result']['message'] = 'User can not be updated due to an exception.'
            data['result']['error'] = e.message
            return JsonResponse(data)


@csrf_exempt
def delete_profile(request):
    """
    Delete (DELETE)

    """
    if request.method == 'DELETE':
        user_id = request.POST.get('user_id')

        data = {
            "result": {
                'message': 'You have successfully deleted'
            }
        }

        try:
            if User.objects.filter(id=user_id).exists():
                user = User.objects.get(id=user_id)
                user.delete()

                data['result']['message'] = 'User deleted successfully.'

                return JsonResponse(data)
            else:
                data['result']['message'] = 'User does not exists.'

                return JsonResponse(data)

        except Exception as e:
            data['result']['message'] = 'User can not be deleted due to an exception.'
            data['result']['error'] = e.message
            return JsonResponse(data)

import json
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

        # json_data = json.loads(str(request.body))
        # json_data = request.body

        """
        <QueryDict: {'first_name': ['First name'], 'last_name': ['Last name'], 'email': ['testuser@gmail.com'], 'username': ['testuser1']}>
(Pdb) request.POST.get('email')
'testuser@gmail.com'
        """
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        import pdb;pdb.set_trace()
        pass

    pass

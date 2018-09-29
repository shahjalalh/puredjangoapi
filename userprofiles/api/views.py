from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from userprofiles.models import UserProfile
from django.core.serializers import serialize


def userprofiles_list(request):

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
    up_detail = get_object_or_404(UserProfile, pk=pk)

    up_detail_dict = dict()

    up_detail_dict["username"] = up_detail.user.username
    up_detail_dict["first_name"] = up_detail.user.first_name
    up_detail_dict["last_name"] = up_detail.user.last_name
    up_detail_dict["email"] = up_detail.user.email
    up_detail_dict["is_active"] = up_detail.user.is_active
    up_detail_dict["birth_date"] = up_detail.birth_date
    up_detail_dict["location"] = up_detail.location
    up_detail_dict["bio"] = up_detail.bio
    up_detail_dict["id"] = up_detail.id
    up_detail_dict["avatar"] = up_detail.avatar.name

    data = {"result": up_detail_dict}

    return JsonResponse(data)

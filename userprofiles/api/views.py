from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from userprofiles.models import UserProfile
from django.core.serializers import serialize


def userprofiles_list(request):

    up_list = UserProfile.objects.all()

    data = {"results": list(up_list.values("bio", "location", "birth_date", "avatar", "user_id"))}

    return JsonResponse(data)


def userprofile_detail(request, pk):
    pass

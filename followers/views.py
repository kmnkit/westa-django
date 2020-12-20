from django.shortcuts import reverse, redirect
from users.models import User
from .models import FollowerList, FollowedList


def toggle_follow(request, pk):
    user = request.user
    post_user = User.objects.get(pk=pk)
    if user.is_authenticated:
        if post_user is not None:
            # 유저의 팔로우 리스트
            follow_list, _ = FollowerList.objects.get_or_create(user=user)
            # 상대방의 팔로워 리스트
            author_followed_list, _ = FollowedList.objects.get_or_create(user=post_user)

            if post_user in follow_list.following_list.all():
                follow_list.following_list.remove(post_user)
                author_followed_list.followed_list.remove(user)
            else:
                follow_list.following_list.add(post_user)
                author_followed_list.followed_list.add(user)
            follow_list.save()
            author_followed_list.save()
            return redirect(reverse("users:user", kwargs={"pk": pk}))

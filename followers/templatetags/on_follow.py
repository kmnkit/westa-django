from django import template
from followers.models import FollowedList, FollowerList

register = template.Library()


@register.simple_tag(takes_context=True)
def on_followed(context, post_user):
    user = context.request.user
    followed_list, _ = FollowedList.objects.get_or_create(user=user)
    return post_user in followed_list.followed_list.all()


@register.simple_tag(takes_context=True)
def on_following(context, post_user):
    user = context.request.user
    following_list, _ = FollowerList.objects.get_or_create(user=user)
    return post_user in following_list.following_list.all()

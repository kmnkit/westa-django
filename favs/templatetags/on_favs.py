from django import template
from favs.models import FavList

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, post):
    user = context.request.user
    fav_list, _ = FavList.objects.get_or_create(user=user)
    return post in fav_list.posts.all()

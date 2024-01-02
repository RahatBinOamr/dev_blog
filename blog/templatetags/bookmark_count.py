from django import template
from blog.models import Bookmark
register = template.Library()
@register.filter()
def bookmark_count(user):
  if user.is_authenticated:
    bookmark_count = Bookmark.objects.filter(user=user).count()
    return bookmark_count 
  else:
    return 0


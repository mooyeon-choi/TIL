from django import template

register = template.Library()

@register.filter
def make_link(article):
    content = article.content + ' '
    hashtags = article.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(hashtag.content, f'<a href="/hashtags/{hashtag.pk}/">{hashtag.content}</a>')
    return content
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from newsapi import NewsApiClient


NEWS_API_TOKEN = '3384038df26c4de09255dd8e5dbaeb26'

# Create your views here.
def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'inapp/post_list.html', {'posts': posts})

def latest_news(request):
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        all_articles = newsapi.get_everything(sources='bbc-news,the-verge',
        from_parameter='2018-04-04',to='2018-04-05',language='en',sort_by='relevancy',page=10)
        news_status = all_articles['status']
        news_count = all_articles['totalResults']
        news_list = all_articles['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        return render(request, 'inapp/latest_news.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})



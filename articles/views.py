from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Article
import random
from django.http import Http404
from django.shortcuts import render_to_response


#to render articles
def render_with_random_articles(request, template, data):
	data['articles'] = get_random_articles()
	return render(request, template, data)

#to get random articles for what to read next section
def get_random_articles(limit=3):
    
    articles = Article.objects.filter(pub_date__lte=timezone.now())
 
    selected_articles = []
 
    if limit >= len(articles):
        return articles
 
    while len(selected_articles) <= limit:
        article = random.choice(articles)
        if article not in selected_articles:
            selected_articles.append(article)
    
    return selected_articles[0:5]


#to give data to detail page for a particular article and random articles for what to read next section
def detail(request,article_id):
    
    article=get_object_or_404(Article, id=article_id)
    datenow=timezone.now()
    
    return render_with_random_articles(request, "detail.html",{
        "title":article.title,
        "body":article.body,
        "hero_image":article.hero_image,
        "optional_image":article.optional_image,
        "datenow":datenow,
        "author":article.author_name,
    })
    
    
#to give data to index page for display details of articles
def index(request):
    
    datenow=timezone.now()

    selected_articles = get_random_articles(5)
    #article to preview
    featured_article = selected_articles[0]
    #articles for suggestions
    selected_articles = selected_articles[1:]
    
    #to trim the preview article's body
    featured_article.body= featured_article.body[0:20] + "..." if len(featured_article.body) > 2 else featured_article.body
    
    #article list to display, to get the articles lesser than or equal to todays date in ascending order
    sorted_article_list=Article.objects.all().filter(pub_date__lte=timezone.now()).exclude(id=featured_article.id).order_by('pub_date')[0:3]

    
    #to reduce no. of characters in preview of list body
    for sorted_article in sorted_article_list:
        sorted_article.body= sorted_article.body[0:100] + "..." if len(sorted_article.body) > 2 else sorted_article.body
        # if len(sorted_article_list1) < 3:
        #     sorted_article_list1.append(sorted_article)
    
    
    return render(request, 'index.html', {
        'articles': selected_articles,'featured_article': featured_article, 'sorted_article_list': sorted_article_list,
        'datenow':datenow,
    })

    


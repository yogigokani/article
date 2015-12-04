from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Article
import random
from django.http import Http404
from django.shortcuts import render_to_response

def render_with_random_articles(request, template, data):
	data['articles'] = get_random_articles()
	return render(request, template, data)

def get_random_articles(limit=4):
    articles = Article.objects.filter(pub_date__lte=timezone.now())
 
    selected_articles = []
 
    if limit >= len(articles):
        return articles
 
    while len(selected_articles) <= limit:
        article = random.choice(articles)
        if article not in selected_articles:
            selected_articles.append(article)
    #print selected_articles
    return selected_articles[0:4]

def detail(request,article_id):
    #title="arvindan"
    #body="arvindans body"
    # try:
    #     article=get_object_or_404(Article, id=article_id)
    # #return HttpResponse(" "+article.title+" "+article.body)
    # except Article.DoesNotExist:
    #     raise Http404("Article does not exist")
    # return render_with_random_articles(request, "detail.html",{
    # 	"title":article.title,
    # 	"body":article.body
    


    article=get_object_or_404(Article, id=article_id)
    datenow=timezone.now()
    #return HttpResponse(" "+article.title+" "+article.body)
    return render_with_random_articles(request, "detail.html",{
    	"title":article.title,
    	"body":article.body,
    	"hero_image":article.hero_image,
    	"optional_image":article.optional_image,
    	"datenow":datenow,
    	"author":article.author_name,
    })
    

# def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#     was_published_recently.admin_order_field = 'pub_date'




def index(request):
    
    selected_articles = get_random_articles(5)
   
    featured_article = selected_articles[0]
    selected_articles = selected_articles[1:]
    

    featured_article.body= featured_article.body[0:20] + "..." if len(featured_article.body) > 2 else featured_article.body
    
    #to get the articles lesser than or equal to todays date in ascending order
    sorted_article_list=Article.objects.all().filter(pub_date__lte=timezone.now()).exclude(id=featured_article.id).order_by('pub_date')

    #to reduce no. of characters in preview of list body
    sorted_article_list1=[]
    for sorted_article in sorted_article_list:
        sorted_article.body= sorted_article.body[0:20] + "..." if len(sorted_article.body) > 2 else sorted_article.body
        sorted_article_list1.append(sorted_article)
    
    #to get only first three articles
    sorted_article_list2=sorted_article_list1[0:3]
    
    datenow=timezone.now()
    return render(request, 'index.html', {
        'articles': selected_articles[0:4],'featured_article': featured_article, 'sorted_article_list': sorted_article_list2,
        'datenow':datenow, 'author': featured_article.author_name,
    })

    
    

# Create your views here.

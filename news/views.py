from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article
from .forms import NewsLetterForm

# Create your views here.
# def welcome(request):
#     return render(request, "welcome.html")
# refactor 1
# def convert_dates(dates):
#     day_number = dt.date.weekday(dates)
#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
#     day = days[day_number]
#     return day

def news_of_day(request):
    date = dt.date.today()
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day} -{date.month} -{date.year}
    #         </body>
    #     </html>
    # '''
    # return HttpResponse(html) 
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(requets.POST)
        if form.is_valid():
            print("hello peter")
    else:
        form = NewsLetterForm
    return render(request, 'all-news/todays-news.html', {'date':date, 'news': news, 'letterform':form})


def past_days_news(request, past_date):
    # Converts data from the string Url
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404

    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    # return HttpResponse(html)
    if date == dt.date.today():
        return redirect(news_of_day)
    news = Article.days_news(date)

    return render(request, 'all-news/past-news.html', {"date": date, 'news':news})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for anything"
        return render(request, 'all-news/search.html', {'message': message})


def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404

    return render(request, "all-news/article.html",  {"article": article})

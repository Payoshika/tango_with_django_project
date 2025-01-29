import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}]
    
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}]
    
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
        ]
    
    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},    
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
            # get views and likes for each category
            # check if there is a key called 'views' in the dictionary
            if 'views' in cat_data:
                c.views = cat_data['views']
            if 'likes' in cat_data:
                c.likes = cat_data['likes']
            c.save()

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

# The populate() function first defines three dictionaries, each of which contains a list of dictionaries. Each dictionary in the list represents a page, with the keys being the title and URL of the page. 
# The dictionaries are then stored in a dictionary called cats, with the keys being the category names. The function then iterates through the cats dictionary, creating a Category object for each category and then creating a Page object for each page in the list of pages associated with that category. 
# The add_page() function is used to create a Page object, while the add_cat() function is used to create a Category object. 
# Finally, the function prints out the categories and pages that have been created. The script is then executed when the file is run as a standalone script.
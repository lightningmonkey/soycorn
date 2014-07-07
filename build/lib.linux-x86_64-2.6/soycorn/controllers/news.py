import logging
import os

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from soycorn.lib.base import BaseController, render
from soycorn.model import News
from soycorn.model.meta import Session

log = logging.getLogger(__name__)

class NewsController(BaseController):
    def __before__(self):
        self.news_q = Session.query(News)
        self.pic = "./soycorn/public/images/corn.jpg"

    def index(self):
        f = open("./soycorn/public/static/index", "r")
        g = open("./soycorn/public/articles/links", "r")
        c.content = f.read()
        c.location = ""
        c.title = "index"
        #c.pic = self.pic
        c.firstlink = []
        c.article = []
        count = 0
        firstcheck = True
        for l in g.readlines():
            s = l.split(";")
            if len(s) < 2:
                continue
            if firstcheck:
                c.firstlink.append(s)
                firstcheck = False
                continue
            c.article.append(s)
            count += 1
            if count > 8:
                break
        return render('index.mako')
    
    def news(self):
        f = open("./soycorn/public/articles/links", "r")
        c.location = ""
        c.title = "news"
        c.article = []
        for l in f.readlines():
            s = l.split(";")
            c.article.append(s)
        return render('newshome.mako')
    
#    def photo(self, title, dif=9, picStart=75):
#        c.title = title 
#        c.location = "../"
#        pagenum = int(title)
#        if(pagenum == 1):
#            c.back = 1
#            c.forward = 2
#        elif(pagenum == 15):
#            c.back = 14
#            c.forward = 14
#        else:
#            c.back = pagenum - 1
#            c.forward = pagenum + 1
#        start = picStart+(pagenum-1)*dif
#        end = start + dif
#        c.range = []
#        row = -1
#        #col = 0
#        captions = self.getCaptions()
#        #Sine I may be skiping values, need to increment and not do a range
#        while start < end:
#            for col in range(3)
#                curCaption = captions[str(start)]
#                if curCaption == "NONE\n":
#                    continue
#                if col % 3 == 0:
#                    row += 1
#                    c.range.append([])
#                s = str(start)
#                if(start < 100):
#                    s = "0"+s
#                val = (s, curCaption)
#                c.range[row].append(val)
#                col += 1
#                start += 1
#        return render('photo.mako')
    
    def getCaptions(self):
        dict = {}
        f = open("./soycorn/public/static/photocaptions", "r")
        for l in f.readlines():
            sp = l.split(";")
            try:
                dict[sp[0]] = sp[1]
            except:
                continue
        return dict
            
    def photo(self, title, dif=9, picStart=75):
        c.title = title 
        c.location = "../"
        pagenum = int(title)
        if(pagenum == 1):
            c.back = 1
            c.forward = 2
        elif(pagenum == 15):
            c.back = 14
            c.forward = 15
        else:
            c.back = pagenum - 1
            c.forward = pagenum + 1
        start = picStart+(pagenum-1)*dif
        c.range = []
        row = -1
        col = 0
        counter = 0
        captions = self.getCaptions()
        #Sine I may be skiping values, need to increment and not do a range
        while counter < dif:
            curCaption = captions[str(start)]
            if curCaption == "NONE\n":
                start += 1
                continue
            if curCaption =="END":
                break
            if col % 3 == 0:
                row += 1
                c.range.append([])
            s = str(start)
            if(start < 100):
                s = "0"+s
            val = (s, curCaption)
            c.range[row].append(val)
            col += 1
            start += 1
            counter += 1
        return render('photo.mako')
    
    def show(self, title):
        dir = os.path.join("./soycorn/public/static", title)
        if os.path.exists(dir):
            c.title = title
            c.location = ""
            c.pic = self.pic
            f = open(dir, "r")
            c.content = f.read()
            return render('show.mako')
        abort(404)
    
    def article(self, title):
        dir = os.path.join("./soycorn/public/articles", title)
        if os.path.exists(dir):
            c.title = title
            c.location = "../"
            c.pic = self.pic
            f = open(dir, "r")
            c.date = f.readline()
            c.header = f.readline()
            c.content = f.read()
            return render('article.mako')
        abort(404)
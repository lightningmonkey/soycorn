import logging
import os

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort#, redirect_to

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
    
    def get_captions(self, location):
        dict = {}
        f = open("./soycorn/public/static/"+location, "r")
        for l in f.readlines():
            sp = l.split(";")
            try:
                dict[sp[0]] = sp[1]
            except:
                continue
        return dict
    
    def pic_caption(self, pic_num, caption):
        pic_str = str(pic_num).zfill(3)
        #if pic_num < 100:
        #    pic_str = '0'+pic_str
        return (pic_str, caption)
    
    def find_pictures_and_captions(self, page_num, pic_start, dif, caption_file):
        all_captions = self.get_captions(caption_file)
        page_start = dif*(page_num-1)
        page_end = page_start + dif - 1
        counter = 0
        page_captions = []
        cur_pic = pic_start
        while counter <= page_end:
            cur_caption = all_captions[str(cur_pic).zfill(3)]
            if cur_caption == "NONE\n":
                cur_pic += 1
                continue
            if cur_caption =="END":
                break
            if counter >= page_start :
                page_captions.append(self.pic_caption(cur_pic, cur_caption))
            counter += 1
            cur_pic += 1    
        return page_captions
            
    #def photo(self, title, photo_location='images', dif=9, pic_start=75, caption_file='photocaptions'):
    def photo(self, title, photo_location, dif, pic_start, caption_file, last_page):
        c.title = title 
        c.location = "../"
        c.photo_location=photo_location
        page_num = int(title)
        if(page_num == 1):
            c.back = 1
            c.forward = 2
        elif(page_num == last_page):
            c.back = last_page-1
            c.forward = last_page
        else:
            c.back = page_num - 1
            c.forward = page_num + 1
        pics_and_captions = self.find_pictures_and_captions(page_num, pic_start, dif, caption_file)
        c.range = []
        row = -1
        col = 0
        for cur in pics_and_captions:
            if col % 3 == 0:
                row += 1
                c.range.append([])
            c.range[row].append(cur)
            col += 1
        return c
        
    def old_photo(self, title):
        c = self.photo(title, 'images', 9, 75, 'photocaptions', 14)
        c.jpg_caps = "jpg"
        return render('photo.mako')
        
    def new_photo(self, title, dif=9, picStart=210):
        c = self.photo(title, 'newimages', 9, 210, 'newcaptions', 25)
        c.jpg_caps = "JPG"
        return render('photo.mako')
    
    def photo3(self, title, dif=9, picStart=210):
        c = self.photo(title, 'photo3', 9, 1, 'photo3', 28)
        c.jpg_caps = "JPG"
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

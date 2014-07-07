# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400966499.886911
_enable_loop = True
_template_filename = u'/home/brian/www/soycornmeat/soycorn/templates/show.mako'
_template_uri = u'/show.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['body', 'pics', 'javapics', 'dropdown']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n')
        # SOURCE LINE 50
        __M_writer(escape(h.literal(c.content)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pics(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javapics(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n\t<script type="text/javascript">\n\t\tvar str = "";\n\t\tvar used = new Array()\n\t\tfunction getRand(){\n\t\t\tvar n = Math.floor(Math.random() * 249) + 1;\n\t\t\tvar i;\n\t\t\tfor (i = 0; i < used.length; i ++){\n\t\t\t\twhile (n == used[i]){\n\t\t\t\t\tn = Math.floor(Math.random() * 249) + 1;\n\t\t\t\t}\n\t\t\t}\n\t\t\tvar str = "";\n\t\t\tif (n < 10)\n\t\t\t\t{str = "00"};\n\t\t\tif (n < 100 && n > 9)\n\t\t\t\t{str = "0";}\n\t\t\tstr = str+n;\n\t\t\treturn str;\n\t\t}\n\t\tfunction showpic(){\n\t\t\tstr = getRand();\n\t\t\tused[0] = str;\n\t\t\tvar l1 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";\n\t\t\tstr = getRand();\n\t\t\tused[1] = str;\n\t\t\tvar l2 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";\n\t\t\tstr = getRand();\n\t\t\tused[2] = str;\n\t\t\tvar l3 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";\n\t\t\tstr = getRand();\n\t\t\tused[3] = str;\n\t\t\tvar l4 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";\n\t\t\tdocument.getElementById(\'pics\').innerHTML=l1+l2+l3+l4;\n\t\t\tt=setTimeout(\'showpic()\',15000);\n\t\t}\n\t</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dropdown(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div id="menu">\n<ul id="sddm">\n    <li><a href="')
        # SOURCE LINE 6
        __M_writer(escape(c.location))
        __M_writer(u'index">Home</a></li>\n    <li><a href="')
        # SOURCE LINE 7
        __M_writer(escape(c.location))
        __M_writer(u'About-Us">About Us</a></li>\n\t<li><a href="')
        # SOURCE LINE 8
        __M_writer(escape(c.location))
        __M_writer(u'News">News</a></li>\n    <li><a onmouseover="mopen(\'m1\')" onmouseout="mclosetime()">Brazilian Agriculture</a>\n        <div id="m1" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">\n        \t<a href="')
        # SOURCE LINE 11
        __M_writer(escape(c.location))
        __M_writer(u'Brazil-Crop-Acreage">Brazil Crop Acereage</a>\n        \t<a href="')
        # SOURCE LINE 12
        __M_writer(escape(c.location))
        __M_writer(u'Brazil-Crop-Cycles">Brazil Month-By-Month Crop Cycle</a>\n        \t<a href="')
        # SOURCE LINE 13
        __M_writer(escape(c.location))
        __M_writer(u'Brazil-Land-Utilization">Brazil Land Utilization</a>\n        \t<a href="')
        # SOURCE LINE 14
        __M_writer(escape(c.location))
        __M_writer(u'Brazilian-Infrastructure">Brazilian Infrastructure</a>\n        \t<a href="')
        # SOURCE LINE 15
        __M_writer(escape(c.location))
        __M_writer(u'Mato-Grosso-Railroad">Mato Grosso Railroad</a>\n        </div>\n    </li>\n    <li><a onmouseover="mopen(\'m2\')" onmouseout="mclosetime()">South American Agriculture</a>\n        <div id="m2" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">\n        \t<a href="')
        # SOURCE LINE 20
        __M_writer(escape(c.location))
        __M_writer(u'Argentina-Crop-Acreage">Argentina Crop Acreage</a>\n        \t<a href="')
        # SOURCE LINE 21
        __M_writer(escape(c.location))
        __M_writer(u'Argentina-Crop-Cycles">Argentina Month-By-Month Crop Cycle</a>\n        \t<a href="')
        # SOURCE LINE 22
        __M_writer(escape(c.location))
        __M_writer(u'Paraguay-Bolivia-Crop-Acreage">Paraguay and Bolivia Crop Acreage</a>\n        </div>\n    </li>\n\t<li><a onmouseover="mopen(\'m3\')" onmouseout="mclosetime()">PhotoGallery</a>\n        <div id="m3" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">\n        \t<a href="')
        # SOURCE LINE 27
        __M_writer(escape(c.location))
        __M_writer(u'Photo-Gallery-1/1">Classic Brazilian Photos</a>\n        \t<a href="')
        # SOURCE LINE 28
        __M_writer(escape(c.location))
        __M_writer(u'Photo-Gallery-2/1">Photos of Brazilian Ag 2010</a>\n        \t<a href="')
        # SOURCE LINE 29
        __M_writer(escape(c.location))
        __M_writer(u'Photo-Gallery-3/1">Photos of Brazilian Ag 2011</a>\n        </div>\n    </li>\n    \n    \n    <li><a onmouseover="mopen(\'m4\')" onmouseout="mclosetime()">Brazilian Biofuels</a>\n        <div id="m4" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">\n        \t<a href="')
        # SOURCE LINE 36
        __M_writer(escape(c.location))
        __M_writer(u'Brazil-Sugarcane-Ethanol-Industries">Brazil Sugarcane and Ethanol Industries</a>\n        \t<a href="')
        # SOURCE LINE 37
        __M_writer(escape(c.location))
        __M_writer(u'Brazil-US-Ethanol-Production">Brazil vs. U.S. Ethanol</a>\n        \t<a href="')
        # SOURCE LINE 38
        __M_writer(escape(c.location))
        __M_writer(u'How-Brazil-Created-The-International-Ethanol-Boom">How Brazil Created The International Ethanol Boom</a>\n        \t<a href="')
        # SOURCE LINE 39
        __M_writer(escape(c.location))
        __M_writer(u'Tri-Flex-Car">Tri-Flex Car</a>\n        </div>\n    </li>\n    <li><a href="')
        # SOURCE LINE 42
        __M_writer(escape(c.location))
        __M_writer(u'Frequently-Asked-Questions">FAQ</a></li>\n\t<li><a href="')
        # SOURCE LINE 43
        __M_writer(escape(c.location))
        __M_writer(u'Contact-Us">Contact Us</a></li>\n</ul>\n</div>\n<div style="clear:both"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



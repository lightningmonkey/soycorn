# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400966499.8956
_enable_loop = True
_template_filename = u'/home/brian/www/soycornmeat/soycorn/templates/base.mako'
_template_uri = u'/base.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n\t"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\r\n\r\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\r\n<head>\r\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\r\n\r\n  \t<title>Soybean And Corn Advisor</title>\r\n  \t<link rel="stylesheet" href="../style.css" type="text/css" charset="utf-8" />\r\n  \r\n\t<link rel="stylesheet" type="text/css" href="../niftyCorners.css">\r\n  \t<link rel="stylesheet" type="text/css" href="../niftyLayout.css" media="print">\r\n  \t<script type="text/javascript" src="../niftycube.js"></script>\r\n  \t<script type="text/javascript" src="../niftylayou.js"></script>\r\n  \t<script type="text/javascript">\r\n\t\twindow.onload=function()\r\n\t\t{\r\n\t\t\tNifty("#sddm li a","transparent top");\r\n\t\t}\r\n\t</script>\r\n\r\n  ')
        # SOURCE LINE 22
        __M_writer(escape(self.javapics()))
        # SOURCE LINE 23
        __M_writer(u'\t\r\n<script>\r\n\t// Copyright 2006-2007 javascript-array.com\r\n\tvar timeout\t= 500;\r\n\tvar closetimer\t= 0;\r\n\tvar ddmenuitem\t= 0;\r\n\t\r\n\t// open hidden layer\r\n\tfunction mopen(id)\r\n\t{\t\r\n\t\t// cancel close timer\r\n\t\tmcancelclosetime();\r\n\t\r\n\t\t// close old layer\r\n\t\tif(ddmenuitem) ddmenuitem.style.visibility = \'hidden\';\r\n\t\r\n\t\t// get new layer and show it\r\n\t\tddmenuitem = document.getElementById(id);\r\n\t\tddmenuitem.style.visibility = \'visible\';\r\n\t\r\n\t}\r\n\t// close showed layer\r\n\tfunction mclose()\r\n\t{\r\n\t\tif(ddmenuitem) ddmenuitem.style.visibility = \'hidden\';\r\n\t}\r\n\t\r\n\t// go close timer\r\n\tfunction mclosetime()\r\n\t{\r\n\t\tclosetimer = window.setTimeout(mclose, timeout);\r\n\t}\r\n\t\r\n\t// cancel close timer\r\n\tfunction mcancelclosetime()\r\n\t{\r\n\t\tif(closetimer)\r\n\t\t{\r\n\t\t\twindow.clearTimeout(closetimer);\r\n\t\t\tclosetimer = null;\r\n\t\t}\r\n\t}\r\n\t\r\n\t// close layer when click-out\r\n\tdocument.onclick = mclose; \r\n</script>\r\n\t\r\n\r\n</head>\r\n\r\n<body onload="showpic()">\r\n  <div id="header"></div>\r\n  <div id="wrapper">\r\n    \r\n')
        # SOURCE LINE 77
        __M_writer(escape(self.dropdown()))
        __M_writer(u'\r\n    \r\n\t<div id="pics">\r\n\t\t\r\n\t</div>\r\n    <div id="content">\r\n      <div id="section">\r\n\t  \t\t')
        # SOURCE LINE 84
        __M_writer(escape(self.body()))
        # SOURCE LINE 85
        __M_writer(u'\t\t</div>\r\n    </div>\r\n    <div id="footer">\r\n      <h1>Copyright Soybean and Corn Advisor, Inc. 2009-2013</h1>\r\n    </div>\r\n  </div>      \r\n\t<script type="text/javascript">\r\n\t\tvar gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\r\n\t\tdocument.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\r\n\t</script>\r\n\t<script type="text/javascript">\r\n\t\ttry {\r\n\t\t\tvar pageTracker = _gat._getTracker("UA-3543383-2");\r\n\t\t\tpageTracker._trackPageview();\r\n\t\t} catch(err) {}</script>                               \r\n</body>                                       \r\n</html>                                       \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



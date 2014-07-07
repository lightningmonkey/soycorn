# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400969506.731876
_enable_loop = True
_template_filename = '/home/brian/www/soycornmeat/soycorn/templates/photo.mako'
_template_uri = 'photo.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['body', 'javapics']


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
    return runtime._inherit_from(context, u'/show.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div id="photogallery">\n<h2>Photo Gallery Page ')
        # SOURCE LINE 5
        __M_writer(escape(c.title))
        __M_writer(u'</h2>\n<table>\n<tr>\n<td align="left"><a href=')
        # SOURCE LINE 8
        __M_writer(escape(c.back))
        __M_writer(u'><< Back</a></td> <td></td> <td align=right><a href=')
        __M_writer(escape(c.forward))
        __M_writer(u'>Forward >></a></td>\n</tr>\n')
        # SOURCE LINE 10
        for row in c.range:
            # SOURCE LINE 11
            __M_writer(u'<tr>\n')
            # SOURCE LINE 12
            for p in row:
                # SOURCE LINE 13
                __M_writer(u'<td><a href=/')
                __M_writer(escape(c.photo_location))
                __M_writer(u'/')
                __M_writer(escape(p[0]))
                __M_writer(u'.')
                __M_writer(escape(c.jpg_caps))
                __M_writer(u'><img width=200 src=/')
                __M_writer(escape(c.photo_location))
                __M_writer(u'/')
                __M_writer(escape(p[0]))
                __M_writer(u'sm.jpg></a>')
                __M_writer(escape(p[1]))
                __M_writer(u'</td>\n')
            # SOURCE LINE 15
            __M_writer(u'</tr>\n')
        # SOURCE LINE 17
        __M_writer(u'<tr>\n<td align="left"><a href=')
        # SOURCE LINE 18
        __M_writer(escape(c.back))
        __M_writer(u'><< Back</a></td> <td></td> <td align=right><a href=')
        __M_writer(escape(c.forward))
        __M_writer(u'>Forward >></a></td>\n</tr>\n</table>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javapics(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



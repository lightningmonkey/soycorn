# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400966499.876985
_enable_loop = True
_template_filename = '/home/brian/www/soycornmeat/soycorn/templates/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['body']


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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(escape(h.literal(c.content)))
        __M_writer(u'\n<h2>Top News</h2>\n<br/>\n\n\n<br/><a href="news/')
        # SOURCE LINE 9
        __M_writer(escape(c.firstlink[0][0]))
        __M_writer(u'"> ')
        __M_writer(escape(c.firstlink[0][1]))
        __M_writer(u'</a><br/>\n\n')
        # SOURCE LINE 11
        for a in c.article:
            # SOURCE LINE 12
            __M_writer(u'<br/><a href="news/')
            __M_writer(escape(a[0]))
            __M_writer(u'"> ')
            __M_writer(escape(a[1]))
            __M_writer(u'</a><br/>\n')
        # SOURCE LINE 14
        __M_writer(u'<br/><br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



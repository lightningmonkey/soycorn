# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400966505.647104
_enable_loop = True
_template_filename = '/home/brian/www/soycornmeat/soycorn/templates/article.mako'
_template_uri = 'article.mako'
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
        # SOURCE LINE 8
        __M_writer(u'\n\n\n\n')
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
        __M_writer(u'\n<a href="../News">Back</a><br/>\n<h5>')
        # SOURCE LINE 5
        __M_writer(escape(h.literal(c.date)))
        __M_writer(u'</h5>\n<h3>')
        # SOURCE LINE 6
        __M_writer(escape(h.literal(c.header)))
        __M_writer(u'</h3>\n')
        # SOURCE LINE 7
        __M_writer(escape(h.literal(c.content)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



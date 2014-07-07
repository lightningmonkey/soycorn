# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400966501.276237
_enable_loop = True
_template_filename = '/home/brian/www/soycornmeat/soycorn/templates/newshome.mako'
_template_uri = 'newshome.mako'
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
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<h2>Top News</h2>\n<ul>\n')
        # SOURCE LINE 6
        for a in c.article:
            # SOURCE LINE 7
            if len(a) < 2:
                # SOURCE LINE 8
                __M_writer(u'\t\t</ul>\n\t\t<h4>')
                # SOURCE LINE 9
                __M_writer(escape(a[0]))
                __M_writer(u'</h4>\n\t\t<ul>\n')
                # SOURCE LINE 11
            else:
                # SOURCE LINE 12
                __M_writer(u'\t\t<li><a href="news/')
                __M_writer(escape(a[0]))
                __M_writer(u'"> ')
                __M_writer(escape(a[1]))
                __M_writer(u'</a></li>\n')
        # SOURCE LINE 15
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



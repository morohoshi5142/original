from django import template
from django.utils.safestring import mark_safe
import markdown
from markdownx.utils import markdownify
from markdownx.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
from markdown.extensions import Extension
import re


register = template.Library()


@register.filter
def markdown_to_html(text):
    """マークダウンをhtmlに変換する。"""
    print(text)
    md = mark_safe(markdownify(text))
    md = mark_safe(md.replace('<img ','<img class="img-thumbnail" '))
    print(md)
    return md


@register.filter
def mark_down_to_text(text):
    t = text.replace('#',"")
    t = re.sub("\!\[.*\]\(.*\)",'',t)
    return t
    
class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')


@register.filter
def markdown_to_html_with_escape(text):
    """マークダウンをhtmlに変換する。

    生のHTMLやCSS、JavaScript等のコードをエスケープした上で、マークダウンをHTMLに変換します。
    公開しているコメント欄等には、こちらを使ってください。

    """
    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)

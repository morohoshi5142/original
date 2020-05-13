from django.template import Library

register = Library()

@register.filter
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    print( queryset.order_by(*args))
    return queryset.order_by(*args)

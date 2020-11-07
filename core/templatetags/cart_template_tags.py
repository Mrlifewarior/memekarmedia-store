from django import template
from core.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.filter
def cart_item_total(user):
    if user.is_authenticated:
        try:
            order = Order.objects.get(user=user, ordered=False)
            return order.get_total()
        except Order.DoesNotExist:
            return 0
    return 0
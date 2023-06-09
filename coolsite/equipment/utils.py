from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить продукт", 'url_name': "add_product"},
        {'title': "обратная связь", 'url_name': "contact"},
        ]


class DataMixin:
    paginate_by = 5
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

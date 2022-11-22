import json

from django.db import DataError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category


class CatListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        cat = self.object_list.select_related().all()
        response = []
        for i in cat:
            response.append({'id': i.pk,
                             'name': i.name,
                             'slug': i.slug
                             })
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        if len(data['slug']) < 5:
            raise DataError(f"Поле 'slug' не может быть меньше 5 символов")

        res = Category.objects.create(name=data['name'], slug=data['slug'])
        return JsonResponse({
            'id': res.pk,
            'name': res.name,
            'slug': res.slug
        }, safe=False)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name, 'slug': cat.slug}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']
        self.object.save()

        if 'slug' in data:
            self.object.slug = data['slug']
        self.object.save()

        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'slug': self.object.slug,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)

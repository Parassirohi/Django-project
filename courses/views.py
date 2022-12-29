from django.shortcuts import render, get_object_or_404, redirect

from .form import CourseModelForm
from django.views import View
from .models import Course
#   To convert this into a class base view, we inherit
# BASE VIEW CLass = VIEW


# class CoursesObjectMixin(object):
#     model = Course
#
#     def get_object(self):
#         id = self.keargs.get('id')
#         obj = None
#         if id is not None:
#             obj = get_object_or_404(self.model, id=id)
#         return obj


class CourseUpdateView(View):
    template_name = "courses/course_update.html"  # Detail view

    def get_object(self):
        obj = None
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        #    get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context["object"] = obj
            context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # Post method
        context = {}
        obj = self.get_object() 
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context["object"] = obj
            context["form"] = form

        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset() }
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'  # Detailview

    def get(self, request, *args, **kwargs):
        # Get method
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Post method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseDeleteView(View):
    template_name = "courses/course_delete.html"  # Detail view

    def get_object(self):
        obj = None
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        #    get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # Post method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = obj
            return redirect("/courses/")
        return render(request, self.template_name, context)


class CourseView(View):
    template_name = "courses/course_detail.html"  # Detailview

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)
#  HTTP METHOD


def my_fbv(request, *args, **kwargs):

    return render(request, 'about.html', {})

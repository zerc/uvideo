# coding: utf-8
from django.http import Http404
from django.views.generic import UpdateView


class AttiribToContextMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(AttiribToContextMixin, self).get_context_data(*args,
                                                                      **kwargs)
        attr_prefix = 'context__'

        for attr in dir(self):
            if attr.startswith(attr_prefix):
                context[attr.replace(attr_prefix, '')] = getattr(self, attr)

        return context


class CanUpdateMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CanUpdateMixin, self).get_object(*args, **kwargs)

        # For update views - check permissions for object
        if isinstance(self, UpdateView):
            if self.request.user.is_superuser:
                return obj

            if self.user_can_update(obj):
                return obj

            raise Http404

        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(CanUpdateMixin, self).get_context_data(*args, **kwargs)
        context['can_update'] = self.user_can_update(self.object)
        return context

    def user_can_update(self, obj):
        return (self.request.user.is_superuser or
                self.request.user == obj.user)


class AddUserToKwargs(object):
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(AddUserToKwargs, self).get_form_kwargs(*args,
                                                                   **kwargs)
        form_kwargs['user'] = self.request.user
        return form_kwargs

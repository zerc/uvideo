# coding: utf-8
from django import forms
from pyuploadcare.dj.forms import FileGroupField
from pyuploadcare.api_resources import FileGroup

from video.models import Collection, Video


class CollectionForm(forms.ModelForm):
    videos = FileGroupField(required=False)

    class Meta:
        model = Collection
        fields = ('title', 'cover', 'description')

    def save(self, *args, **kwargs):
        obj = super(CollectionForm, self).save(*args, **kwargs)

        videos = self.cleaned_data.get('videos', None)
        if videos:
            self.save_videos(obj, videos)

        return obj

    def save_videos(self, collection, group_cdn_url):
        group = FileGroup(group_cdn_url)

        for i, f in enumerate(group):
            Video(collection=collection, title=group[i].filename(),
                  video_file=f).save()

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from picrev.models import Request, Image


class RequestResource(ModelResource):

    class Meta(object):

        queryset = Request.objects.all()
        resource_name = 'request'
        authorization = Authorization()

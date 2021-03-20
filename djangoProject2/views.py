from rest_framework import mixins
from rest_framework import status, parsers, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
class Test(viewsets.ModelViewSet):
    @staticmethod
    def get_list(self):
        list = [1, 2]
        return list
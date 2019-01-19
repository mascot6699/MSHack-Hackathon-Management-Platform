from rest_framework import serializers
from . import models


#
# class CategorySerializer(serializers.ModelSerializer):
#     """
#     A category serializer for non admin
#     """
#     class Meta:
#         """
#         """
#         model = models.Category
#         exclude = ['internal_name', 'is_deleted', 'enabled', 'created_at', 'modified_at', 'approval_bypass', 'created_by']
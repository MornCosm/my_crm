from django.apps import AppConfig


class PermissionConfig(AppConfig):
    name = 'permission'
    verbose_name = '权限组件'
    help_text = '基于RBAC的权限组件'

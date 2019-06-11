from django.db import models

# Create your models here.

PERMISSION_MODELS = ['User', 'Role', 'AccessUrl']


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.UUIDField(verbose_name="密码", help_text="这里使用uuid加密后的密码作为用户密码")
    roles = models.ManyToManyField(to="Role", related_name="users", verbose_name="用户角色列表")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name="角色名")

    class Meta:
        verbose_name = "role"
        verbose_name_plural = "roles"


class AccessUrl(models.Model):
    url = models.TextField(verbose_name="访问url")
    roles = models.ManyToManyField(to="Role", related_name="access_urls", verbose_name="访问url列表")

    class Meta:
        verbose_name = "access Url"
        verbose_name_plural = "access Urls"

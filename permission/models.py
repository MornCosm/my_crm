from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.UUIDField(verbose_name="密码", help_text="这里使用uuid加密后的密码作为用户密码")
    roles = models.ManyToManyField(to='Role', related_name='users', verbose_name="用户角色列表")


class Role(models.Model):
    pass


class AccessUrl(models.Model):
    pass

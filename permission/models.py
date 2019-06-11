from django.db import models

# Create your models here.

PERMISSION_MODELS = ['User', 'Role', 'AccessUrl']


class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.UUIDField(verbose_name="密码", help_text="这里使用uuid加密后的密码作为用户密码")
    roles = models.ManyToManyField(to="Role", related_name="users",
                                   verbose_name="用户角色列表", blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=32, verbose_name="角色名")
    urls = models.ManyToManyField(to="AccessUrl", related_name="roles",
                                  verbose_name="可以访问的url列表", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "role"
        verbose_name_plural = "roles"


class AccessUrl(models.Model):
    """
    访问url表抑或者叫权限表
    通过url来限制用户访问的权限
    """
    title = models.CharField(verbose_name="url地址名称/权限名称")
    url = models.TextField(verbose_name="访问url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "access Url"
        verbose_name_plural = "access Urls"

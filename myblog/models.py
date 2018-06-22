from django.db import models
from SSO.models import User

# Create your models here.
class  Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    createtime = models.DateField()
    updatetime = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __unicode__(self):
        return u'%s' % self.name

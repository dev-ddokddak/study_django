from django.db import models

from member.models import Member
from view.models import Period


# Create your models here.
class Post(Period):
    post_title = models.CharField(max_length=200, null=False, blank=True)
    post_content = models.CharField(max_length=500, null=False, blank=True)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_post'

    def get_absolute_url(self, page):
        return f"/post/detail/{self.id}/{page}"

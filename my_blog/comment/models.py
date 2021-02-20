from django.db import models
# 引入用户模型
from django.contrib.auth.models import User
# 引入文章模型
from article.models import ArticlePost


# Create your models here.

# 博文的评论
class Comment(models.Model):
    # 被评论的文章
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # 评论发布者
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]

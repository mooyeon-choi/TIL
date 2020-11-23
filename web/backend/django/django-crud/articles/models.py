from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.conf import settings

# Create your models here.
# 1. 모델(스키마) 정의
# 데이터베이스 테이블을 정의하고,
# 각각의 컬럼(필드) 정의

class HashTag(models.Model):
    content = models.TextField(unique=True)
    def __str__(self):
        return self.content


class Article(models.Model):
    # id : integer 자동으로 정의(Primary Key)
    # 아래의 코드가 생략되어있음
    # id = models.AutoField(primary_key=True) -> Integer 값이 자동으로 하나씩 증가(AUTOINCREMENT)
    # CharField - 필수인자로 max_length 지정
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # ImageSpecField : Input 하나만 받고 처리해서 저장
    # ProcessedImageField : Input 받은 것을 처리해서 저장
    # resize to fill : 300*300
    # resize to fit : 긴쪽을(너비 혹은 높이) 300에 맞추고 비율에 맞게 자름
    image_thumbnail = ProcessedImageField(
                                processors=[ResizeToFit(300, 300)],
                                format='JPEG',
                                options={'quality': 80}
                                )
    # DateTimeField
    #   auto_now_add : 생성시 자동으로 저장
    #   auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL : 'accounts.User' (str)
    # 아직 accounts app이 안불러와져 있을경우 에러가 발생할수 있으므로 사용해준다
    like_users = models.ManyToManyField(
                            settings.AUTH_USER_MODEL,
                            related_name='like_articles',
                            blank=True
                            )

    hashtags = models.ManyToManyField(
                            HashTag,
                            blank=True
                            )
                            

    def __str__(self):
        return f'<{self.id}> : {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # on_delete
    # 1. CASCADE : 글이 삭제되었을 때 모든 댓글을 삭제
    # 2. PROTECT : 댓글이 존재하면 글 삭제 안됨.
    # 3. SET_NULL : 글이 삭제되면 NULL로 치환(NOT NULL일 경우 옵션 사용X)
    # 4. SET_DEFAULT : 디폴트 값으로 치환.

# models.py : python 클래스 정의
#           : 모델 설계도
# makemigrations : migration 파일 생성
#           : DB 설계도 작성
# migrate : migration 파일 DB 반영
from django.db import models
from django.utils import timezone


class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 현재 시간
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # 사용자가 읽기 쉬운 모델 객체의 이름, 관리자 화면 등에서 표시
    # 영어를 기준으로 단수형
    class Meta:
        verbose_name = "Diary"

# Create your models here.

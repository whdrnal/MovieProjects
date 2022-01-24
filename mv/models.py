from django.contrib.auth.models import User
from django.db import models


class MovieCategory(models.Model):
    name = models.CharField('이름', max_length=50)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    is_deleted = models.BooleanField('삭제여부', default=False)
    delete_date = models.DateTimeField('삭제날짜', null=True, blank=True)
    name = models.CharField('영화제목(내부용)', max_length=100)
    display_name = models.CharField('영화제목(고객용)', max_length=100)
    category = models.ForeignKey(MovieCategory, on_delete=models.DO_NOTHING)
    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰평점', default=0)
    image = models.ImageField(upload_to=f"mv/", blank=True, null=True)

    def thumb_img_url(self):
        img_name = self.category.name

        return f"https://raw.githubusercontent.com/whdrnal/movie-img/master/{img_name}.jpg"


class MovieReal(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_reals")
    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50)
    option_1_display_name = models.CharField('옵션1 이름(고객용)', max_length=50)
    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50)
    option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)
    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름(내부용)', max_length=50, default='', blank=True)
    option_3_display_name = models.CharField('옵션3 이름(고객용)', max_length=50, default='', blank=True)
    is_hidden = models.BooleanField('노출여부', default=False)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} - {self.mv}"


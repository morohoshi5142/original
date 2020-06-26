from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Seiyu(models.Model):  
    name=models.CharField(max_length=200)
    seiyu_url=models.URLField(null=True,blank=True)
    seiyu_syozoku=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Eshi(models.Model):
    name=models.CharField(max_length=200)
    tw_url=models.URLField(null=True,blank=True)
    px_url=models.URLField(null=True,blank=True)    

    def __str__(self):
        return self.name

class Kansyu(models.Model):
    name=models.CharField(max_length=200)
    is_gunkan=models.BooleanField(default=False)
    setumei = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Oogata(models.Model): 
    typename=models.CharField(max_length=200)
    kansyu=models.ForeignKey(Kansyu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.typename
    
    
class Kanmusu(models.Model):
    name=models.CharField(max_length=200,unique=True)
    kansyu=models.ForeignKey(Kansyu, on_delete=models.CASCADE)
    OOgata=models.ForeignKey(Oogata, on_delete=models.CASCADE)
    number=models.IntegerField(default=0)
    ichinin=models.CharField(max_length=200)
    Fsutairu=models.CharField(max_length=200)
    tokuchou=models.CharField(max_length=200)
    eshi = models.ForeignKey(Eshi, on_delete=models.CASCADE)
    seiyu = models.ForeignKey(Seiyu, on_delete=models.CASCADE)
    like_num = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name
        
        
        
        
        
        
        
    


class Battle(models.Model):
    name=models.CharField(max_length=200)
    naiyo=models.CharField(max_length=1000)
    ido = models.CharField(max_length=100,null = True,blank = True)
    keido = models.CharField(max_length=100,null = True,blank = True)
    
    def __str__(self):
        return self.name
    

class Sanka_kanmusu(models.Model):
    battle=models.ForeignKey(Battle, on_delete=models.CASCADE)
    kanmusu=models.ForeignKey(Kanmusu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.kanmusu.name
        
class Kansyu_setumei(models.Model):
    setumei=models.CharField(max_length=200)
    
    def __str__(self):
        return self.setumei
    
    
class Ivent(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField(null = True,blank = True)
    
    def __str__(self):
        return self.name
    
class Ivent_naiyou(models.Model):
    ivent = models.ForeignKey(Ivent, on_delete=models.CASCADE)
    naiyou = models.CharField(max_length=200)
    
    def __str__(self):
        return self.naiyou
        
class Tokkokanmusu(models.Model):
    ivent_naiyou = models.ForeignKey(Ivent_naiyou, on_delete=models.CASCADE)
    kanmusu = models.ForeignKey(Kanmusu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.kanmusu.name
        
from django.utils import timezone
from django.contrib.auth.models import User

    
class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

        
class Playnikki(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    title = models.CharField(max_length=20)
    nikki = MarkdownxField(max_length=2000)
    image = models.ImageField(upload_to='media',blank=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    
    
    
class Comment(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(Playnikki, on_delete=models.CASCADE, verbose_name='対象記事')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.text[:20]    
        
        
# 質問モデル        
class PlayQuestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question_text = models.TextField('本文')
    pub_date = models.DateTimeField('date published',default=timezone.now)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    image = models.ImageField(upload_to='media',blank=True, null=True)
    title = models.CharField(max_length=20)



# 質問の回答
class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField('本文')
    target = models.ForeignKey(PlayQuestion, on_delete=models.CASCADE, verbose_name='対象記事')
    pub_date = models.DateTimeField('date published',default=timezone.now)
    like_num = models.IntegerField(default=0)

    class Meta:
        ordering = ['-pub_date']

# いいね機能
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    target = models.ForeignKey(Answer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published',default=timezone.now)


#艦娘人気投票
class Kannmusu_like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kannmusu_like_user')
    target = models.ForeignKey(Kanmusu, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    
    
class Map(models.Model):
    map_name = models.CharField(max_length=100)
    jyusyo = models.CharField(max_length=100)
    ido = models.CharField(max_length=100)
    keido = models.CharField(max_length=100)
    kanmusu = models.ManyToManyField(Kanmusu, blank=True)

    def __str__(self):
        return self.map_name

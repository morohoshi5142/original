from django import forms
from .models import Playnikki,Comment,PlayQuestion,Answer

class Nikkiform(forms.ModelForm):
    class Meta:
        model = Playnikki
        exclude = ('tag','user')
        
TagInlineFormSet = forms.inlineformset_factory(
    Playnikki, Playnikki.tag.through, fields='__all__', can_delete=False
)
        
        
class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('target','pub_date')
        
        
class Questionform(forms.ModelForm):
    class Meta:
        model = PlayQuestion
        exclude = ('pub_date','user')#「 , 」を付けないと[python manage.py makemigrations]が出来なかった
        
TagInlineFormSet = forms.inlineformset_factory(
    PlayQuestion, PlayQuestion.tag.through, fields='__all__', can_delete=False
)


class Answerform(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ('user','target','pub_date')

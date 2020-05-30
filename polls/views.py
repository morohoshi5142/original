from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import Question,Kanmusu,Seiyu,Kansyu,Oogata,Sanka_kanmusu,Kansyu_setumei,Battle,Ivent,Ivent_naiyou,Tokkokanmusu,Comment,Kannmusu_like,Map
from django.urls import reverse

from django.views.generic import CreateView,ListView, DetailView
from .models import Playnikki,Tag,PlayQuestion,Answer,Like
from .forms import Nikkiform,TagInlineFormSet,Commentform,Questionform,Answerform
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages



def index(request):
    playnikki_list = Playnikki.objects.order_by('-pub_date')[:6]
    tag = Tag.objects.all()
    context = {'playnikki_list': playnikki_list,'tag' : tag}
    return render(request, 'polls/top_page.html', context)
# Create your views here.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/qestion.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


    
def index2(request):
    latest_kanmusu_list = Kanmusu.objects.order_by('OOgata').order_by('kansyu')[:]
    context = {'latest_kanmusu_list': latest_kanmusu_list}
    return render(request, 'polls/kanmusu_name.html', context)
    
def detail2(request, kanmusu_id):
    kanmusu = get_object_or_404(Kanmusu, pk=kanmusu_id)
    return render(request, 'polls/kanmusu_syousai.html', {'kanmusu': kanmusu})   
    
def detail3(request):
    latest_seiyu_list = Seiyu.objects.order_by('-id')[:]
    tag = Tag.objects.all()
    context = {'latest_seiyu_list': latest_seiyu_list,'tag' : tag}
    return render(request, 'polls/seiyu_list.html', context)
    
def seiyu_syousai(request, seiyu_id):
    seiyu = get_object_or_404(Seiyu, pk=seiyu_id)
    tag = Tag.objects.all()
    return render(request, 'polls/seiyu.syousai.html', {'seiyu': seiyu,'tag':tag})   
    
def seiyu_tanto(request, seiyu_id):
    tantos = Kanmusu.objects.filter(seiyu=seiyu_id)
    return render(request, 'polls/seiyu_tanto.html', {'tantos': tantos})   
    
def kansyu(request):
    latest_kansyu_list = Kansyu.objects.order_by('-id')[:]
    tag = Tag.objects.all()
    context = {'latest_kansyu_list':latest_kansyu_list,'tag':tag}
    return render(request, 'polls/kansyu.html',context)
    
    
def kansyu_by_type(request,kansyu_id):
    oogatas = Oogata.objects.filter(kansyu=kansyu_id)
    context = {'oogatas':oogatas}
    return render(request, 'polls/kansyu_by_type.html',context)
    
    
def kanmusu_by_type(request,oogata_id):
    latest_kanmusu_list = Kanmusu.objects.filter(OOgata=oogata_id)
    context = {'latest_kanmusu_list': latest_kanmusu_list}
    return render(request, 'polls/kanmusu_name.html', context)
    
def kansyu_setumei(request):
    latest_kansyu_setumei = Kansyu_setumei.objects.order_by('-id')[:]
    
    
def battle_name(request):
    latest_battle_name = Battle.objects.order_by('-id')[:]
    map = Map.objects.all()
    tag = Tag.objects.all()
    context  = {'latest_battle_name':latest_battle_name,'tag':tag,'map':map}
    return render(request, 'polls/map_list.html', context)
    
    
def sanka_kanmusu(request,battle_id):
    sanka_kanmusu_list = Sanka_kanmusu.objects.filter(battle = battle_id)
    battle = get_object_or_404(Battle,pk=battle_id)
    context  = {
        'sanka_kanmusu_list':sanka_kanmusu_list,
        'battle':battle
    }
    return render(request, 'polls/battle_in_kanmusu.html', context)
    
    
def kanmusu_list(request):
    kansyus = Kansyu.objects.all()
    context = {'kansyus': kansyus}
    return render(request, 'polls/kanmusu_list.html', context)

    
def kanmusu_list2(request):
    tag = Tag.objects.all()
    kansyus = Kansyu.objects.all()
    data = {}
    for kansyu in kansyus:
        ogatas = kansyu.oogata_set.all()
        data2 = {}
        for ogata in ogatas:
            data2[ogata.typename] = ogata.kanmusu_set.order_by('number')
        data[kansyu.name] = data2
    print(data)
    context = {'kansyus': data,'tag':tag}
    return render(request, 'polls/kanmusu_list.1.html', context)


    
def ivent(request):
    ivents = Ivent.objects.order_by('-id')[:]
    tag = Tag.objects.all()
    context = {'ivents':ivents,'tag':tag}
    return render (request, 'polls/ivent.html', context)
    
def ivent_naiyou(request,name_id):
    ivent_naiyous = Ivent_naiyou.objects.filter(ivent=name_id)
    tag = Tag.objects.all()
    context = {'ivent_naiyous':ivent_naiyous,'tag':tag}
    print(context)
    return render(request, 'polls/ivent_naiyou.html', context)
    
def vote(request, kanmusu_id):
    kanmusu = get_object_or_404(Kanmusu, pk=kanmusu_id)
    
    kanmusu.ninki += 1
    kanmusu.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('detail2', args=(kanmusu.id,)))   
    


class NikkiCreateView(CreateView):
    model = Playnikki
    form_class = Nikkiform
    template_name = "polls/form.html"
    success_url = "/"  # 成功時にリダイレクトするURL
    
            
    def post(self, request, *args, **kwargs):
        context_object_name = 'sample_create'
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            tag = Tag.objects.all()
            obj = form.save(commit=False)
            obj.user = self.request.user
            if 'image' in self.request.FILES.keys():
                obj.image = self.request.FILES['image']
            
            formset = TagInlineFormSet(request.POST, instance=obj)
            print(formset)
            if formset.is_valid():
                print('a')
                obj.save()
                formset.save()
                messages.success(request, '投稿完了しました')

                return HttpResponseRedirect(reverse('index'))
            else:
                context = {'form':form,'formset':formset}
                messages.error(request, '投稿完了できませんでした', extra_tags='danger')
                return render(self.request, 'polls/form.html', context)
            
    def get_context_data(self, **kwargs):
        tag = Tag.objects.all()
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        formset = TagInlineFormSet()
        context["formset"] = formset
        context["tag"] = tag
        return context
    
class NikkiListView(ListView):
    model = Playnikki
    template_name = "polls/nikkilist.html"
    paginate_by = 8
    
    def get_queryset(self):
        # 公開フラグがTrueで、作成日順に並び替え
        return super().get_queryset().order_by('-pub_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        tag = Tag.objects.all()
        context["tag"] = tag
        return context

    
    
class NikkiDitaltView(DetailView):
    model = Playnikki
    template_name = "polls/nikki.html"  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        tag = Tag.objects.all()
        context["tag"] = tag
        return context
    
    
    
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #入力した名前を username に入れる
            raw_password = form.cleaned_data.get('password1') #入力したパスワードをraw_password に入れる
            user = authenticate(username=username, password=raw_password) #入力した二つの項目をuser に入れる
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})
    
    
class NikkiListQueryView(ListView):
    model = Playnikki
    template_name = "polls/nikkilist.html"
    paginate_by = 8
    
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Playnikki.objects.filter(
                Q(title__icontains=q_word) | Q(nikki__icontains=q_word) | Q(tag__name__exact=q_word)
            ).order_by('-pub_date')
        else:
            object_list = Playnikki.objects.all().order_by('-pub_date')
        return object_list



class NikkiTagListQueryView(ListView):
    model = Playnikki
    template_name = "polls/nikkilist.html"
    paginate_by = 8
    
    def get_queryset(self):
        q_word = self.kwargs['pk']
        if q_word:
            object_list = Playnikki.objects.filter(
                Q(tag__exact=q_word)
            ).order_by('-pub_date')
        else:
            object_list = Playnikki.objects.all().order_by('-pub_date')
        return object_list
        
        
        
class CommentCreateView(CreateView):
    model = Comment
    form_class = Commentform
    template_name = "polls/form_comment.html"
    success_url = "/"  # 成功時にリダイレクトするURL
    
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Playnikki, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('nikki', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Playnikki, pk=self.kwargs['pk'])
        tag = Tag.objects.all()
        context["tag"] = tag
        return context


# 質問投稿    
class QuestionCreateView(CreateView):
    model = PlayQuestion
    form_class = Questionform
    template_name = "polls/question_form.html"    #テンプレート作成後に編集
    success_url = "/"  # 成功時にリダイレクトするURL
    
            
    def post(self, request, *args, **kwargs):
        context_object_name = 'sample_create'
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            if 'image' in self.request.FILES.keys():#画像が保存する場合に行う処理
                obj.image = self.request.FILES['image']
            
            formset = TagInlineFormSet(request.POST, instance=obj)
            print('b')
            if formset.is_valid():
                print('a')
                obj.save()
                formset.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                context = {'form':form,'formset':formset}
                return render(self.request, 'polls/question_form.html', context)
                
        else:
            formset = TagInlineFormSet(request.POST, instance=obj)
            context = {'form':form,'formset':formset}
            return render(self.request, 'polls/question_form.html', context)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        formset = TagInlineFormSet()
        context["formset"] = formset
        tag = Tag.objects.all()
        context["tag"] = tag
        return context

# 質問詳細        
class QuestionDitaltView(DetailView):
    model = PlayQuestion
    template_name = "polls/question.html"    #テンプレート作成後に編集
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        tag = Tag.objects.all()
        context["tag"] = tag
    
        return context
    
    
    
        
        
            
# 質問解答
class AnswerCreateView(CreateView):
    model = Answer
    form_class = Answerform
    template_name = "polls/question_answer.html"    #テンプレート作成後に編集
    success_url = "/"  # 成功時にリダ��レクトするURL
    
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(PlayQuestion, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.user = self.request.user
        comment.save()
        return redirect('question', pk=post_pk) #'  'はurls.pyのnameの部分を入力

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(PlayQuestion, pk=self.kwargs['pk'])
        return context

class QuestionListView(ListView):
    model = PlayQuestion
    template_name ="polls/question_list.html"
    paginate_by = 8
    
    def get_queryset(self):
        # 公開フラグがTrueで、作成日順に並び替え
        return super().get_queryset().order_by('-pub_date')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        tag = Tag.objects.all()
        context["tag"] = tag
        return context
        


def like(request, *args, **kwargs):
    answer = Answer.objects.get(id=kwargs['answer_id'])
    print(kwargs['answer_id'])
    is_like = Like.objects.filter(user=request.user).filter(target=answer).count()
    q_pk= answer.target.id
    # unlike
    if is_like > 0:
        liking = Like.objects.get(target = answer, user=request.user)
        liking.delete()
        answer.like_num -= 1
        answer.save()
        messages.warning(request, 'いいねを取り消しました')
        return redirect('question',pk=q_pk) #'  'はurls.pyのnameの部分を入力
        #ライン341で移動先を設定している
    # like
    answer.like_num += 1
    answer.save()
    like = Like()
    like.user = request.user
    like.target = answer
    like.save()
    messages.success(request, 'いいね！しました')
    return redirect('question',pk=q_pk) #'  'はurls.pyのnameの部分を入力
    #ライン341で移動先を設定している



def kanmusu_ninnki(request, *args, **kwargs):
    print(kwargs)
    kanmusu = Kanmusu.objects.get(id=kwargs['kanmusu_id'])
    is_like = Kannmusu_like.objects.filter(user=request.user).filter(target=kanmusu).count()
    ninnki_pk= kanmusu.id
    # unlike
    if is_like > 0:
        liking = Kannmusu_like.objects.get(target = kanmusu, user=request.user)
        liking.delete()
        kanmusu.like_num -= 1
        kanmusu.save()
        messages.warning(request, '投票を取り消しました')
        return redirect('detail2',kanmusu_id=ninnki_pk) #'  'はurls.pyのnameの部分を入力
        #ライン341で移動先を設定している
    # like
    kanmusu.like_num += 1
    kanmusu.save()
    like = Kannmusu_like()
    like.user = request.user
    like.target = kanmusu
    like.save()
    messages.success(request, '投票しました')
    return redirect('detail2',kanmusu_id=ninnki_pk) #'  'はurls.pyのnameの部分を入力

# def vote(request, kanmusu_id):
#     kanmusu = get_object_or_404(Kanmusu, pk=kanmusu_id)



def graph(request):
    top_5 =  Kanmusu.objects.order_by('-like_num')[:5]
    top5name = [kanmusu.name for kanmusu in top_5]
    top5data = [kanmusu.like_num for kanmusu in top_5]
    
    data = {}
    ogatas = Oogata.objects.all()
    for ogata in ogatas:
        omaga_kanmusus = ogata.kanmusu_set.all()
        ninki = 0
        for k in omaga_kanmusus:
            print(k,k.like_num)
            ninki += k.like_num
        data[ogata.typename] = ninki

    print('A',data)

    sorted_item = sorted(data.items(), key=lambda x:x[1], reverse=True)
    print('B',sorted_item)
    
    k_top5name = []
    k_top5data = []
    for x , y in sorted_item[:5]:
        k_top5name.append(x)
        k_top5data.append(y)
        
    tag = Tag.objects.all()
    context = {'tag' : tag}


    return render(request, 'polls/graph.html',{'top5name': top5name,'top5data': top5data,'k_top5name': k_top5name,'k_top5data': k_top5data,'tag':tag})
    

#艦種全体からの人気投票
def graph1(request):
    kansyu = Kansyu
    oogata = Oogata.objects.all()
    top_5 =  Kanmusu.objects.order_by('kansyu')('-like_num')
    top5kansyuname = [kanmusu.kansyu.name for kanmusu in top_5]
    top5kansyudata = [kanmusu.like_num for kanmusu in top_5]
    
    

    return render(request, 'polls/graph.html',{'top5kansyuname': top5kansyuname,'top5kansyudata': top5kansyudata})

    
def graph2(request):
    data = {}
    ogatas = Oogata.objects.all()
    for ogata in ogatas:
        omaga_kanmusus = ogata.kanmusu_set.all()
        ninki = 0
        for k in omaga_kanmusus:
            print(k,k.like_num)
            ninki += k.like_num
        data[ogata.typename] = ninki

    print('A',data)

    sorted_item = sorted(data.items(), key=lambda x:x[1], reverse=True)
    print('B',sorted_item)
    
    top5name = []
    top5data = []
    for x , y in sorted_item[:5]:
        top5name.append(x)
        top5data.append(y)
        
    return render(request, 'polls/graph.html',{'top5name': top5name,'top5data': top5data})
    
    
    
# def index2(request):
#     latest_kanmusu_list = Kanmusu.objects.order_by('OOgata').order_by('kansyu')[:]
#     context = {'latest_kanmusu_list': latest_kanmusu_list}
#     return render(request, 'polls/kanmusu_name.html', context)
#     seiyu = get_object_or_404(Seiyu, pk=seiyu_id)

def api_map(request,map_id):
    map = get_object_or_404(Map,pk=map_id)
    return render(request, 'polls/api_map.html',{'map': map})


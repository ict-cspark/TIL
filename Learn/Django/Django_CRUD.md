# 사전준비

### 1. 가상환경 생성

```bash
$ python -m venv venv				# 가상환경 생성
$ source venv/Scripts/Activate		# 가상환경 활성화
```



### 2. 장고 설치

```bash
$ pip install django==3.2			# 장고 3.2버전 설치
$ pip freeze > requirements.txt		# requirements.txt에 설치목록 저장
$ pip install -r requirements.txt 	# requirements.txt에 저장된 라이브러리 설치
```



### 3. 프로젝트 및 APP 설치

``` bash
$ django-admin startproject config .	# 프로젝트 최상위 폴더에 생성
$ python manage.py startapp articles		# app 생성
```



### 4. 기본설정

```python
# settings.py 
INSTALLED_APPS = [
    'articles',
    ...
]

최상위 폴더에 templates\base.html 생성

# settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]

# urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('articles/', include('articles.urls')),
]

# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    ...
]
```



### 5. Custom User (User 사용시)

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# settings.py

AUTH_USER_MODEL = 'accounts.User'


# accounts/admin.py

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)


# accounts.forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

 
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```



---

# CRUD

### articles/urls.py

```python
# urls.py

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
]


# + comment_create, comment_delete

    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
```



### articles/models.py

```python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

# Comment
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

# user
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



### articles/admin.py

```python
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):	# 선택옵션
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

    
admin.site.register(Article, ArticleAdmin)


# Comment
from .models import Comment

admin.site.register(Comment)
```

```bash
$ python manange.py createsuperuser
```



### articles/forms.py

```python
# forms.py

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
# CommentForm
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        
        
# ArticleForm + user
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)
```

```python
# forms.py - widget

release_date = forms.DateField(
    widget = forms.DateInput(
        attrs = {
            'type': 'date',
        },
    ),
)


CHOICE = [
    ('A', 'A'),
    ('B', 'B'),
]
genre = forms.CharField(
    widget = forms.Select(choices = CHOICE,),
)


score = forms.FloatField(
    widget = forms.NumberInput(
        attrs = {
            'step': 0.5,
            'min': 0,
            'max': 5,
        },
    ),
)


poster_url = forms.CharField(
    widget = forms.Textarea(
        attrs = {
            'rows': 2,
        },
    ),
)
```



### articles/views.py - index

```python
# views.py

from django.views.decorators.http import require_safe
from django.shortcuts import render
from .models import Article


@require_safe
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': article,
    }
    return render(request, 'articles/index.html', context)
```



### articles/views.py - create

```python
# views.py

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .forms import ArticleForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


# create + user
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
```



### articles/views.py - detail



```python
# views.py

from django.views.decorators.http import require_safe
from django.shortcuts import render, get_object_or_404
from .models import Article


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)


# detail + CommentForm
from .forms import CommentForm

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


# detail + CommentFrom + comments
	comment_form = CommentForm()
    comments = article.comment_set.all()
    
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
```



### articles/views.py - update

```python
# views.py

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)


# update + user
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    ...
    return render(request, 'articles/update.html', context)
```



### articles/views.py - delete

```python
# views.py

from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


# delete + user
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')
```



### articles/views.py - comment_create

```python
# articles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import CommentForm
from django.views.decorators.http import require_POST

@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


# comment_create + user
@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        ...
        if comment_form.is_valid():
           comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```



### articles/views.py - comment_delete

```python
# articles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.views.decorators.http import require_POST

@require_POST
def comment_delete(request, article_pk ,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)


# comment_user + user
@require_POST
def comment_delete(request, article_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```



### articles/templates/articles/index.html + user

```html
<!--index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
    <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
    <p>작성자: {{ article.user }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```



### articles/templates/articles/detail.html

```html
<!--detail.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h3>{{ article.pk }}번째 글</h3>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">수정</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>삭제</button>
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}


<!--detail.html + CommentForm + comments_create-->
...
  <hr>
  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
        <button>Submit</button>
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
  {% endif %}
{% endblock content %}


<!--detail.html + comment_delete + user-->
  <hr>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">수정</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button>삭제</button>
    </form>
  {% endif %}
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <button>삭제</button>
          </form>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
```

```html
<!--detail.html + Comment + user-->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h3>{{ article.pk }}번째 글</h3>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
    <hr>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">수정</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button>삭제</button>
    </form>
  {% endif %}
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <button>삭제</button>
          </form>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
  <hr>
  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
        <button>Submit</button>
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
  {% endif %}
{% endblock content %}
```



### articles/templates/articles/form.html

```html
<!--form.html-->

{% extends 'base.html' %}

{% block content %}

  {% if request.resolver_match.url_name == 'create' %}
    <h1>CREATE</h1>
  {% else %}
    <h1>UPDATE</h1>
  {% endif %}

  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
      
    {% if request.resolver_match.url_name == 'update' %}
      <a href="{% url 'articles:detail' artilce.pk %}">Cancel</a>
    {% endif %}
      
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

```html
<!--부트스트랩 적용시-->
1. $ pip install django-bootstrap-v5
2. settings.py - INSTALLED_APPS - 'bootstrap5',
3. html 상단 {% load bootstrap5 %} 추가
4. {{ form.as_p }} -> {% bootstrap_form form %}
```



---

# Account



```bash
$ python manage.py startapp accounts
settings.py
INSTALLED_APP - 'accounts',
urls.py 등록 및 urls.py 생성 후 app_name = 'accounts'
```

## 회원가입

> 1. urs.py 등록
>
> 2. 회원가입 버튼 생성 (is_authenticated 이용하여 비로그인 상태일 경우에만)
>
> 3. view 함수 작성 (UserCreationForm과 require_http_method, auth_login을 import 후 
>
>    if - else 작성, 필수인자 없음, is_authenticated 이용하여 로그인 상태일 경우 index로 redirect )
>
> 4. signup.html 생성 (기본 form 양식)

### accounts/urls.py

```python
# urls.py

path('signup/', views.signup, name='signup'),
```



### accounts/views.py

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

### accounts/views.py + is_authenticated (인증 확인) 

### + login as auth_login (자동 로그인)

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

```

### accounts/views.py + is_authenticated (인증 확인) 

### + login as auth_login (자동 로그인) + CustomuserCreationsForm (Form 수정)

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

```



### accounts/templates/accounts/signup.html

```html
<!-- signup.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>회원가입</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



### templates/base.html

```html
<!-- base.html -->

<a href="{% url 'accounts:signup' %}">Signup</a>
```

### templates/base.html + is_authenticated 

```html
<!-- base.html -->

{% if request.user.is_authenticated %}
	...
{% else %}
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```



---

## 로그인

> 1. urs.py 등록
>
> 2. 로그인 버튼 생성 (is_authenticated 이용하여 비로그인 상태일 경우에만)
>
> 3. view 함수 작성 (AuthenticationForm과 auth_login, require_http_method를 import 후 if - else 작성,  if문 필수인자 request, 
>
>    유저정보는 form.get_user(), is_authenticated 이용하여 로그인 상태일 경우 index로 redirect, next 쿼리는 reqeust.GET.get('next') 이용 )
>
> 4. login.html 생성 (기본 form 양식)

### accounts/urls.py

```python
# urls.py

path('login/', views.login, name='login'),
```



### accounts/views.py

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def login(request):
 	if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

### accounts/views.py + is_authenticated + next query (GET)

```python
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_link = request.GET.get('next', 0)
            return redirect(next_link or 'articles:index')
```



### accounts/templates/accounts/login.html

```html
<!-- login.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>로그인</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>>
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



### templates/base.html

```html
<!-- base.html -->

<h3>Hello, {{ user }}</h3>
<a href="{% url 'accounts:login' %}">Login</a>
```

### templates/base.html + is_authenticated (인증 확인)

```html
<!-- base.html -->

{% if request.user.is_authenticated %}
    <h3>Hello, {{ user }}</h3>
{% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```

### articles/index.html + is_authenticated (인증 확인)

```html
{% if request.user.is_authenticated %}
  <a href="{% url 'articles:create' %}">CREATE</a>
{% else %}
  <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인 하세요]</a>
{% endif %}
<hr>
```



---

## 로그아웃

> 1. urs.py 등록
>
> 2. 로그아웃 버튼 생성 (is_authenticated 이용하여 로그인 상태일 경우에만 form 버튼으로 생성)
>
> 3. view 함수 작성 (auth_logout과 require_POST를 import 후 is_authenticated 이용하여 로그인 상태일 경우에 로그아웃 진행, 
>
>    auth_logout 필수인자 request)

### accounts/urls.py

```python
# urls.py

path('logout/', views.logout, name='logout'),
```



### accounts/views.py

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

### accounts/views.py + is_authenticated (인증 확인)

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
```



### templates/base.html

```html
<!-- base.html -->

{% if request.user.is_authenticated %}
    <h3>Hello, {{ user }}</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <button>Logout</button>
    </form>
{% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```



---

## 회원정보 수정

> 1. urs.py 등록
>
> 2. 회원정보 수정 버튼 생성 (is_authenticated 이용하여 로그인 상태일 경우에만 생성)
>
> 3. forms.py 생성 후 CustomUserChangeForm 작성 (UserChangeForm과 get_user_model을 import 후 Meta 클래스의 model로 get_use_model())
>
> 4. view 함수 작성 (CustomUserChangeForm과 require_http_methods, login_required를 import 후 if - else 작성.
>
>    필수인자 없음, instance = request.user)
>
> 4. update.html 생성 (기본 form 양식)

### accounts/urls.py

```python
# urls.py

path('update/', views.update, name='update'),
```



### accounts/forms.py

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```



### accounts/views.py  + CustomUserChangeForm + login_required

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import CustomUserChangeForm

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```



### accounts/templates/accounts/update.html

```html
<!-- update.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



### templates/base.html + is_authenticated 

```html
<!-- base.html -->

{% if request.user.is_authenticated %}
    ...
	<a href="{% url 'accounts:update' %}">회원정보수정</a>
{% else %}
    ...
{% endif %}
```



---

## 비밀번호 변경

> 1. urs.py 등록
>
> 2. view 함수 작성 (PasswordChangeForm과 require_http_methods, login_required, update_session_auth_hash를 import 후 if - else 작성.
>
>    필수인자 request.user, update_session_auth_hash 필수 인자 request)
>
> 3. password.html 생성 (기본 form 양식)

### accounts/urls.py

```python
# urls.py

path('password/', views.change_password, name='change_password'),
```



### accounts/views.py  + login_required 

### + update_session_auth_hash (암호 변경 후 로그인 유지)

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```



### accounts/templates/accounts/change_password.html

```html
<!-- change_password.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호변경</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```



---

## 회원탈퇴

> 1. urs.py 등록
>
> 2. 회원탈퇴 버튼 생성 (is_authenticated 이용하여 로그인 상태일 경우에만 form 버튼으로 생성)
>
> 3. view 함수 작성 (auth_logout과 require_POST를 import 후 is_authenticated 이용하여 로그인 상태일 경우에만 request.user.delete() 진행.
>
>    회원탈퇴 후 auth_logout 필수인자 request)

### accounts/urls.py

```python
# urls.py

path('delete/', views.delete, name='delete'),
```



### accounts/views.py + logout as auth_logout (회원탈퇴 후 로그아웃)

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')
```



### templates/base.html + is_authenticated 

```html
<!-- base.html -->

{% if request.user.is_authenticated %}
    ...
	<form action="{% url 'accounts:delete' %}" method="POST">
    	{% csrf_token %}
    	<button>회원탈퇴</button>
	</form>

{% else %}
    ...
{% endif %}
```



---

# Like & Profile & Follow



## Like

### articles/models.py

```python
from django.db import models


# Article
class Article(models.Model):
    ...
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_article')

```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



### articles/urls.py

```python
# urls.py

path('<int:article_pk>/like/', views.like, name='like'),
```



### articles/views.py

```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)
        
        if article.like_user.filter(pk = request.user.pk ).exists():
            article.like_user.remove(request.user)
        else:
            article.like_user.add(request.user)
        return redirect('articles:index')
    else:
        return redirect('accounts:login')
```



### articles/templates/articles/index.html + Like

```html
<!--index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
    ...
    <form action="{% url 'articles:like' article.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_user.all %}
        <button>좋아요 취소</button>
      {% else %}
        <button>좋아요</button>
      {% endif %}
    </form>
    <hr>

  {% endfor %}
{% endblock content %}
```



## Profile

### accounts/urls.py

```python
# urls.py

path('<username>/', views.profile, name='profile'),
```



### accounts/views.py

```python
# views.py

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe


@require_safe
def profile(request, username):
    person = get_object_or_404(get_user_model(), username = username)

    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```



### templates/base.html

```html
<!-- base.html -->

<nav class="container">
    {% if request.user.is_authenticated %}
      <h2>Hello, <a href="{% url 'accounts:profile' request.user %}">{{ request.user }}</a></h2>
      ...
    {% endif %}
    <hr>
  </nav>
```



## Follow

### accounts/models.py

```python
from django.db import models


# User
class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')

```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



### accounts/urls.py

```python
# urls.py

path('<int:user_pk>/follow/', views.follow, name='follow'),
```



### accounts/views.py

```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk = user_pk)
        if request.user != person:
            if person.follower.filter(pk = request.user.pk).exists():
                person.follower.remove(request.user)
            else:
                person.follower.add(request.user)
        return redirect('accounts:profile', person.username )
    return redirect('accounts:login')
```



### accounts/templates/accounts/profile.html

```html
<!-- profile.html -->

{% extends 'base.html' %}

{% block content %}

  <h1>Profile</h1>
  <a href="{% url 'articles:index' %}">HOME</a>
  <hr>
  
  <h3>{{ person.username }}님의 페이지 입니다.</h3>
  <hr>

  <p>팔로잉 : {{ person.following.count }}, 팔로워 : {{ person.follower.count }}</p>
  {% if request.user != person %}
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.follower.all %}
        <button>언팔로우</button>
      {% else %}
        <button>팔로우</button>
      {% endif %}
    </form>
  {% endif %}
  <hr>

  <p>내가 팔로잉한 유저</p>
  {% for following in person.following.all %}
    <p>유저이름 : <a href="{% url 'accounts:profile' following.username %}">{{ following.username }}</a></p>
  {% endfor %}
  <hr>

  <p>나를 팔로워한 유저</p>
  {% for follower in person.follower.all %}
    <p>유저이름 : <a href="{% url 'accounts:profile' follower.username %}">{{ follower.username }}</a></p>
  {% endfor %}
  <hr>

  <p>작성한 게시물</p>
  {% for article in person.article_set.all %}
    <p>제목 : <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>, 
        좋아요 갯수 : {{ article.like_user.count }}</p>
  {% endfor %}
  <hr>

  <p>작성한 댓글</p>
  {% for comment in person.comment_set.all %}
    <p>내용 : <a href="{% url 'articles:detail' comment.article.pk %}">{{ comment.content }}</a></p>
  {% endfor %}
  <hr>

  <p>내가 좋아요한 게시물</p>
  {% for article in person.like_article.all %}
    <p>제목 : <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></p>
  {% endfor %}
  <hr>
  
{% endblock content %}
```



---

# DRF

### 기본 설정

```bash
# 패키지 설치

$ pip install django-seed
$ pip install django-extensions
$ pip install djangorestframework
$ pip freeze > requirements.txt		# requirements.txt에 설치목록 저장
$ pip install -r requirements.txt 	# requirements.txt에 저장된 라이브러리 설치

# settings.py
INSTALLED_APPS = [
    ...
    'django_seed',
    'django_extensions',
    'rest_framework',
    ...
]

# config/urls.py

urlpatterns = [
    path('api/v1/', include('articles.urls')),
]
```



### articles/models.py

```python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

# Comment
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bash
$ python manage.py migrate
$ python manange.py seed articles --number=20
```



### Fixtures

```python
# articles/fixtures/articles/articles.json

# dumpdata
$ python manage.py dumpdata --indent 4 articles.article > article.json

# loaddata
$ python manage.py loaddata articles/articles.json
```



### articles/serializers.py

```python
from rest_framework import serializers
from .models import Article, Comment


class ArticelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticelSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```



### articles/urls.py

```python
# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```



### articles/views.py

```python
# views.py

from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticelListSerializer, ArticelSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticelListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticelSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticelSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticelSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == "DELETE":
        comment.delete()
        data = {
            'delete': f'댓글 { comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```


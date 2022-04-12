# 준비

### 1. 가상환경 생성

```bash
$ python -m venv venv				# 가상환경 생성
$ source venv/Scripts/Activate		# 가상환경 활성화
```

### 2. 장고 설치

```bash
$ pip install django==3.2			# 장고 3.2버전 설치
$ pip freeze > requirements.txt		# requirements.txt에 설치목록 저장
```

### 3. 프로젝트 및 APP 설치

``` bash
$ django-admin startproject config .	# 프로젝트 최상위 폴더에 생성
$ python manage.py startapp article		# app 생성
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
    path('accounts/', include('accounts.urls')),
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

---

# CRUD

### articles/admin.py



```python
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


admin.site.register(Article, ArticleAdmin)
```

### articles/models.py

```python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bas
$ python manage.py makemigrations
$ python manage.py migrate
```

---

### articles/forms.py



```python
# forms.py

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
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
genre = forms.ChoiceField(
    choices = CHOICE,
    widget = forms.Select(),
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

---

### articles/views.py



```python
# views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


@require_safe
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': article,
    }
    return render(request, 'articles/index.html', context)


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


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)


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


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
```

---

### articles/templates/articles/index.html



```html
<!--index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
  <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
  <p>{{ article.content }}</p>
  <hr>
  {% endfor %}
{% endblock content %}
```

---

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

```

---

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
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
    {% if request.resolver_match.url_name == 'update' %}
      <a href="{% url 'articles:detail' artilce.pk %}">Cancel</a>
    {% endif %}
  </form>
  <a href="{% url 'articles:index' %}">back</a>
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
> 2. 회원가입 버튼 생성 (is_authenticated 이용하여 비로그인 상태일 경우에만)
> 3. view 함수 작성 (UserCreationForm과 require_http_method, auth_login을 import 후 
> 4. if - else 작성, 필수인자 없음, is_authenticated 이용하여 로그인 상태일 경우 index로 redirect )
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

<a href="{% url 'accounts:login' %}">Login</a>
<h3>Hello, {{ user }}</h3>
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
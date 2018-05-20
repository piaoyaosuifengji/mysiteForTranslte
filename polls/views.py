#! python3
# -- coding: utf-8
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import get_object_or_404, render
# Create your views here.
# from django.http import HttpResponse

from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choice, Question
# from django.views import generic


from django.views import generic
from pyForTranslate.googleAPIForTranslate import printTranslate

import logging





# 这个就是自定义的视图函数，用来最终返回什么数据，用以显示
# 在 polls/urls.py 中进行指定，最后
#  /mysiteForTranslte/urls.py中会指定polls/urls.py



# 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」是一个非常常用的操作流程
def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # printTranslate()
    return render(request, 'polls/index.html', context)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     # 载入 polls/index.html 模板文件，并且向它传递一个上下文(context)。
#     # 这个上下文是一个字典，它将模板内的变量映射为 Python 对象。
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))



# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)




# 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程。
# 也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 它向模板传递了上下文变量 question 。
    return render(request, 'polls/detail.html', {'question': question})




# 如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常。
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# ...
def vote(request, question_id):
# 这个question_id 是 
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# 中的question_id

# get_object_or_404的介绍： 我们原来调用django 的get方法，如果查询的对象不存在的话，会抛出一个DoesNotExist的异常，
#  现在我们调用django get_object_or_404方法，它会默认的调用django 的get方法， 如果查询的对象不存在的话，
#  会抛出一个Http404的异常，我感觉这样对用户比较友好， 如果用户查询某个产品不存在的话，我们就显示404的页面给用户，比直接显示异常好。


    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。
        # 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。
        # Django 还以同样的方式提供 request.GET 用于访问 GET 数据 


        #这个函数才是最终获取post数据的函数，也就说，无论那个用于用户提交数据的表单提交了多少数据，
        # 只要知道这个choice就可以一一提取了
        selected_choice = question.choice_set.get(pk=request.POST['choice'])



        # 找不到choice抛出异常
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #  HttpResponseRedirect 只接收一个参数：用户将要被重定向的 URL

        #  reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。
        #  它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。
        # 如果id是3的话，这里将返回字符串 '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# 使用两个通用视图： ListView 和 DetailView 。
# 这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。


# 在之前的教程中，提供模板文件时都带有一个包含 question 和 latest_question_list 变量的 context。
# 对于 DetailView ， question 变量会自动提供—— 因为我们使用 Django 的模型 (Question)，
#  Django 能够为 context 变量决定一个合适的名字。然而对于 ListView， 
#  自动生成的 context 变量是 question_list。为了覆盖这个行为，我们提供 context_object_name 属性，
#  表示我们想使用 latest_question_list。作为一种替换方案，你可以改变你的模板来匹配新的 context 变量
#   —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。


class IndexView(generic.ListView):
    # 使用 template_name 来告诉 ListView 使用我们创建的已经存在的 "polls/index.html" 模板。
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'   #为Django 能够为 context 变量  自己设置一个合适的名字


    # 这是因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，
    # 因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，
    # 而小于它的DEBUG和INFO级别的日志记录被丢弃了。
    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    # printTranslate()

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# 每个通用视图需要知道它将作用于哪个模型。 这由 model 属性提供。
# DetailView 期望从 URL 中捕获名为 "pk" 的主键值，所以我们为通用视图把 question_id 改成 pk 。
# 见urlpatterns
# 默认情况下，通用视图 DetailView 使用一个叫做 <app name>/<model name>_detail.html 的模板。
# 在我们的例子中，它将使用 "polls/question_detail.html" 模板


# 上面这段话的意思是，下面这个DetailView的定义中
# model = Question ，表明了一旦这个视图被使用时，就会生成一个
# Question的对象传入模板'polls/detail.html'   中，最终生成一个被展示的页面
class DetailView(generic.DetailView):
    model = Question
    # template_name告诉 Django 使用一个指定的模板名字，而不是自动生成的默认名字。
    template_name = 'polls/detail.html'  


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'











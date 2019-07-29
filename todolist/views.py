from django.shortcuts import render

# Create your views here.

lst = [
	{'待办事项':'遛狗', '已完成':False},
	{'待办事项':'遛狗', '已完成':True},
]

def home(request):
	global lst
	if request.method == "POST":
		if request.POST['待办事项'] == '':
			return render(request,"todolist/home.html", {'警告': '请输入内容！'})
		else:
			lst.append({'待办事项': request.POST['待办事项'], '已完成':False})
			content = { '清单': lst}
			return render(request,"todolist/home.html", content)
	elif request.method == "GET":
		content = { '清单': lst}
		return render(request,"todolist/home.html", content)

def about(request):
	return render(request,"todolist/about.html")

def edit(request):
	return render(request,"todolist/edit.html")
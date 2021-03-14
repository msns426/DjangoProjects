from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"newsapp/index.html")


def movies(request):
    head_msg="latest movie Updates"
    msg1="chiru announces his upcoming movie title"
    msg2="bollywood actor signed work for RRR"
    msg3="Tollywood innagurates the charity for workers"
    msg4="remakes are more demand on B_town"
    my_list={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,"msg4":msg4}
    return render(request,"newsapp/news.html",context=my_list)


def sports(request):
    head_msg = "latest Sports Updates"
    msg1 = "Dhoni announces his Retirement"
    msg2 = "bollywood actor signed work Sachin Biopic"
    msg3 = "donaldo reches the 500 Goals mark"
    list = {"head_msg": head_msg, "msg1": msg1, "msg2": msg2, "msg3": msg3}
    return render(request,"newsapp/news.html",context=list)


def politics(request):
    head_msg = "latest Political Updates"
    msg1 = " Jumbled elections are anounced by central government"
    msg2 = "cine actors migrate to political career"
    msg3 = "usa anounces the fund for poland to improve the  missiles force"
    my_list = {"head_msg": head_msg, "msg1": msg1, "msg2": msg2, "msg3": msg3}
    return render(request,"newsapp/news.html",context=my_list)



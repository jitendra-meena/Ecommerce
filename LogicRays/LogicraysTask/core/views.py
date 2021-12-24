from django.shortcuts import render
from users.models import User
from django.http import HttpResponse, JsonResponse


def user_data(request):
    user_obj =  User.objects.filter(is_active = True, is_superuser =False)        

    if request.method == 'POST':
        first_name =  request.POST.get('first_name','')
        last_name =  request.POST.get('last_name','')
        email =  request.POST.get('email','')
        phone =  request.POST.get('phone','')
        password =  request.POST.get('password','')
        confirm_password =  request.POST.get('confirm_password','')
        image =  request.FILES.get('image')
        images =  request.POST.get('image')
        print(images)
        print(image)
        print(email)
        user_exs = User.objects.filter(phone = phone, is_active = True).exists()
        if user_exs:
            return render(request,'user_form.html',{'msg':'Phone number already taken'})
        user_exs = User.objects.filter(email = email, is_active = True).exists()
        if user_exs:
            return render(request,'user_form.html',{'msg':'Email already taken'})
        if password == confirm_password:
            user = User.objects.create_user(email = email, phone = phone, password= password, first_name = first_name, last_name = last_name, profile_pic = images, is_active = True)
    return render(request,'user_form.html',{'user_obj':user_obj})





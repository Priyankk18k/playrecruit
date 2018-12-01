from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
import requests
import os
from pytesseract import image_to_string
import json
# from pprint import pprint
import re
# import cv2
from pdf2image import convert_from_path
from django.core.mail import EmailMessage
# Create your views here.
def vw_index(request):
    application = connection.cursor()
    application.execute('''SELECT * FROM abc''')
    data = application.fetchall()
    print(data)
    return render(request, 'admin/index.html', {'data':data})


def vw_candidate(request):
    
    return render(request, 'admin/index.html', {'data':data})

def vw_data(request):
    print("dcddcdc")

    return JsonResponse({"hello":"hello"} )

def vw_download(request):
    fname = request.POST['name']
    resume = request.POST['link']
    mail = request.POST['mail']


# URL of the image to be downloaded is defined as image_url 
    r = requests.get(resume) # create HTTP response object 
  
# send a HTTP request to the server and save 
# the HTTP response in a response object called r 
    with open(os.getcwd()+"/media/{}".format(fname),'wb') as f: 
  
    # Saving received content as a  file in 
    # binary format 
  
    # write the contents of the response (r.content) 
    # to a new file in binary mode. 
        f.write(r.content) 

    root = os.getcwd()+"/media/{}".format(fname)
    out = os.getcwd()+"/media/output_images/"
    print(root)
    pages = convert_from_path(root, 500)
    flag = 1
    for page in pages:
        page.save(os.getcwd()+'/media/output_images/{}.png'.format(flag), 'PNG')
        flag+=1   
    
    convert=''
    for file in os.listdir(out):
        # print(file)
        convert+= image_to_string(out+'/'+file)
        # print("##########",convert)
    
    phone = r'\d{10}'
    skills = r'SKILLS[\WA-Za-z]*[A-Z]'
    project = r'PROJECTS[\WA-Za-z]*[A-Z]'

    data={}

    temp=re.search(skills, convert).group()
    txt_sp = list(filter(None, temp))
    txt_sp1 = "".join(txt_sp)
    data['skills']=txt_sp1

    temp=re.search(phone, convert).group()
    data['phone']=temp

    temp=re.search(project, convert).group()
    txt_sp = list(filter(None, temp))
    txt_sp1 = "".join(txt_sp)
    data['project']=temp


    data['mail'] = mail
    data['open'] = "/media/{}".format(fname)
    print("$$$$$$$$$$",convert)
    return JsonResponse({"data":data} )

def vw_email(request):
    mail = request.POST['mail']
    email = EmailMessage('Response regarding your mail', 'Your profile is fit as perour requirements, So, congratulations you are selected.', to=[mail])
    email.send()
    return JsonResponse({"mail":'sended'})
    
    
    # import re
    # re.search(phone, convert).group()
    # temp=re.search(skills, convert).group()
    # txt_sp = list(filter(None, temp))
    # print(txt_sp)
    # txt_sp1 = "".join(txt_sp)
    # print(txt_sp1)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
       # param = {'name':'rajnish','age':12}

       return HttpResponse('remove punc')
       #return render(request,'index.html',param)

# def home(request):
#     return HttpResponse('''
#               <ul>
#                     <li><a href='https://www.facebook.com/'>Log In to FaceBook</a></li>
#                     <li><a href='https://www.instagram.com/'>Log In to Instagram</a></li>
#                     <li><a href='https://www.linkedin.com/'>Log In to Linkedin</a></li>
#               </ul>
#     ''')

def home(request):
    return render(request,'home.html')

def analyze(request):
    txt = request.POST.get('text','default')
    check = request.POST.get('removepuc', 'off')
    fullCaps = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceRemover = request.POST.get('extraspaceRemover', 'off')
    charCounter = request.POST.get('charCounter', 'off')
    # analyzed = txtMessage
    print(check)
    print(txt)
    if check == 'on':
        puncuation = '''()-{}[];:''""/.|%@$!&^_~`*#POST'''
        analyzed =""
        for char in txt:
            if char not in puncuation:
                analyzed = analyzed + char

        params = {'remove_punc': 'remove Puncuations', 'analyzed_text': analyzed}
        txt = analyzed

    if(fullCaps == 'on'):
        analyzed = ''
        for char in txt:
            analyzed = analyzed + char.upper();
        params = {'ramove-punc':'capitalze the Text' , 'analyzed_text':analyzed}
        txt = analyzed
        # return render(request,'analyze.html',params)
    if(newlineremover =='on'):
        analyzed = ''
        for char in txt :
            if char !='/n' and char !='/r':
                analyzed = analyzed + char
        params = {'remove_punc':'new LIne Remover' , 'analyzed_text':analyzed}
        txt = analyzed
        # return  render(request,'analyze.html',params)
    if(extraspaceRemover == 'on'):
        analyzed = ''
        for index,char in enumerate(txt):
            if not(txt[index] == ' ' and txt[index + 1] == ' '):
                analyzed = analyzed + char

        params = {'remove_punc':'Extra space Remover','analyzed_text':analyzed}
        txt = analyzed
        # return render(request,'analyze.html',params)
    if(charCounter == 'on'):
        analyzed = 0
        for char in txt :
            if not(char == ' '):
                analyzed += analyzed ;
        params = {'ramove_punc':'count the Character','analyze_text':analyzed}
        # return render(request,'analyze.html',params)

    if(check !='on' and fullCaps != 'on' and newlineremover !='on' and newlineremover !='on' and extraspaceRemover != 'on' ):
        return HttpResponse('error ,Please check any option ')

    return render(request, 'analyze.html', params)

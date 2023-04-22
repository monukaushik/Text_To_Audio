from django.shortcuts import render
import os
from gtts import gTTS

def index(request):
   if request.method == 'POST':
      text_file=request.POST.get('text')
      language = 'en'
      myobj = gTTS(text=text_file, lang=language, slow=False)
      myobj.save("welcome.mp3")

   return render(request,'index.html')
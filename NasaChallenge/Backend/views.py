

import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from .nlp import predict_sent
from keras.models import load_model
from pickle import load

os.environ['REPLICATE_API_TOKEN']='d75fe507c43c0c1df6ec23333fa5d05a522ebf6a'
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import replicate
import webbrowser

# Create your views here.

def main (request):



    #webbrowser.open(output_url)
    return render(request, 'index.html')

def create(request):
    if request.method=='POST':
        model = replicate.models.get("stability-ai/stable-diffusion")
        input= request.POST.get("textfield")
        splited=input.split(" ")
        print(splited)
        with open("D:/Users/LaZa/Desktop/____/Github/NASA_hack/NasaChallenge/Backend/spe.txt") as f :
            str_text=f.read()
            
            str_text.lower()
            find=False
            for i in range (len(splited))  :
                print(i)
                w=splited[i].lower()
                if w in str_text and w !="":
                    find=True   
                
            if find ==True :
                #image generation 
                print('related')
                output_url = model.predict(prompt=input)[0]
            else:
                num_words = 3
                modelnlp = load_model("D:/Users/LaZa/Desktop/____/Github/NASA_hack/NasaChallenge/Backend/word_pred_Model4.h5")
                tokenizer = load(open("D:/Users/LaZa/Desktop/____/Github/NASA_hack/NasaChallenge/Backend/tokenizer_Model4",'rb'))
                out_sent , probs = predict_sent(input , modelnlp , tokenizer , num_words=[4], num_sent=3 )
                output_url= '*'.join(out_sent)

    else :
        input= request.POST.get("textfield")
        output_url=""

    liste=[output_url]

    return HttpResponse(liste)




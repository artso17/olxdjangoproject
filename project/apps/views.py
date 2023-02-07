from .forms import PredictForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import pandas as pd
import pickle

# variabel untuk menyimpan hasil prediksi default 0
RESULT=0
  
def predict_list_view(request):
    '''Fungsi untuk menampilkan hasil prediksi oleh Machine Learning 
    yang dieksekusi di fungsi predict_form_view'''
    
    currency="{:20,.2f}".format(float(RESULT))
    currency=currency.replace('.','-')
    currency=currency.replace(',','.')
    currency=currency.replace('-',',')
    context={
        'result': currency
    }
    return render(request,'result.html',context)


def predict_form_view(request):
    '''Fungsi untuk menampilkan form dan menerima input dari klien 
    lalu melakukan prediksi menggunakan Machine Learning 
    lalu menyimpan hasilnya ke variabel RESULT 
    yang akan digunakan oleh fungsi predict_list_view'''
    
    context={
        'form':PredictForm
    }
    
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        df=pd.DataFrame([request.POST.dict()]).drop('csrfmiddlewaretoken',axis=1)
        result=pickled_model.predict(df)
        global RESULT 
        RESULT=result
        return HttpResponseRedirect('result')
        
    return render(request,'index.html',context)

    
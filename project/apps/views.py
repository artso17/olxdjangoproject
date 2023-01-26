from .forms import PredictForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pandas as pd
import pickle
    
def predict_list_view(request):
    result=request.GET.get('result')
    currency="{:20,.2f}".format(float(result))
    currency=currency.replace('.','-')
    currency=currency.replace(',','.')
    currency=currency.replace('-',',')
    context={
        'result': currency
    }
    return render(request,'result.html',context)



def predict_form_view(request):
    context={
        'form':PredictForm
    }
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        # print(request.POST.dict())
        df=pd.DataFrame([request.POST.dict()]).drop('csrfmiddlewaretoken',axis=1)
        # print(df.columns)
        result=pickled_model.predict(df)
        return HttpResponseRedirect(f'/result1?result={result[0]}')
        
    return render(request,'index.html',context)

    
from multiprocessing import context
from django.shortcuts import render
import pickle
from numpy import array
import numpy as np

def home (request):
    models=[]
    if request.method=='POST':
        with open('Model_GradientBoostingClassifierGridSearchCV', 'rb') as f:
            models.append(pickle.load(f))

        values=[]
        values.append(np.int(request.POST.get('Gender')))
        values.append(np.int(request.POST.get('married')))
        values.append(np.int(request.POST.get('dependents')))
        values.append(np.int(request.POST.get('Graduate')))
        values.append(np.int(request.POST.get('Self_Employed')))
        values.append(np.int(request.POST.get('Salary')))
        values.append(np.int(request.POST.get('CoapplicantIncome')))
        values.append(np.int(request.POST.get('LoanAmount')))
        values.append(np.int(request.POST.get('Loan_Amount_Term')))
        values.append(np.int(request.POST.get('Credit_History')))
        values.append(np.int(request.POST.get('Property_Area')))

        values = array(values).reshape(1, -1)
        
        r=0
        for model in models:
            r=model.predict(values)
            
        
        f_res=""
        # if(res[0]< res[1])
        if(r): f_res = " شخص غير مضمون,الرجاء الابتعاد عنه "
        else: f_res = " شخص مضمون , يمكنك البدء في عملية الاقراض "

        context={'f_res':f_res}
        return render(request,'res.html',context)
    


    return render(request,'home.html')



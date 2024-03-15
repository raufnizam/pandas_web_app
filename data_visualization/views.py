from django.shortcuts import render, redirect
from .models import UploadedFile
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        if 'file' in request.FILES:

            uploaded_file = request.FILES['file']
            uploaded_file_instance = UploadedFile.objects.create(file=uploaded_file)
            df = pd.read_csv(uploaded_file_instance.file)
            
            column_names = df.columns.tolist()
            shape = df.shape

            in_string = df.to_string()
            
            data_types = df.dtypes
            describe = df.describe()


            
            file_contents = df.to_json(orient='records')
            context = {
                'file_contents': file_contents,
                'column_names': column_names,
                'shape': shape,
                'in_string': in_string,
                'data_types': data_types,  
                'describe': describe,
            }

            
            return render(request, 'upload_file.html', context ) 
        else: 
            return render(request, 'upload_file.html', {'error_message': 'No file selected'})        
    return render(request, 'upload_file.html')


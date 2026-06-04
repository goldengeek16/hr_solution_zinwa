import xlsxwriter  
from django.contrib import admin

from django.http import HttpResponse
@admin.action(description="Download selected items as csv")
def download_csv(modeladmin, request, queryset):
    
    model_name = modeladmin.model.__name__
    response = HttpResponse(content_type ='application/vnd.opnxmlformarts-officdocument.spreadsheethtml.sheet')
    response['Content-Disposition'] = f'attachment; filename={model_name}.xlsx'
    
    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()
    
    headers = [field for field in modeladmin.model._meta.fields]
    for col_num, header in enumerate(headers):
        print("Col", col_num)    
        print("Header", header) 
        
    for row_num, obj in enumerate(queryset, 1):
        print("Row", row_num)
        print("Obj", obj)
        for col_num, field in enumerate(modeladmin.model._meta.fields):
            value = str(getattr(obj, field.name))
            worksheet.write(row_num, col_num, value)    
            
    workbook.close()
    return response    
        
actions = [download_csv]
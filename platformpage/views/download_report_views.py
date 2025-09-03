from django.http import FileResponse
#测试通过，点击后会直接通过浏览器下载这个文件

#定义一个新的数据报告下载功能
def download_report(request):
    #点击后，页面将会跳转到该函数
    # 然后从我们的download_report文件夹里面获取我们的test_PDF.pdf文件
    #将这个文件下载到浏览器的本地地址中
    file = open('download_report/test_PDF.pdf', 'rb')
    response = FileResponse(file)
    # 设置响应头，告知浏览器下载文件
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="test_PDF.pdf"'
    return response

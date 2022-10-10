from django.shortcuts import render
# View for connection page. 
def connections(request):
	return render(request, 'en/public/connection.html')
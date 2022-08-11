from django.core.paginator import Paginator

def paginate(request,data_list,number):

    paginator = Paginator(data_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
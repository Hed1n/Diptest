# Create your views here.
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, HttpResponse
from baseapp.models import  Product, Category, Linses, News, Order, OrderProduct, AuthUser
from baseapp.forms import filterform, add_form_lins
from django.contrib.auth.models import User
import datetime
from django.db.models import F


def index(request, template_name="index.html"):
    new_set = News.objects.order_by('-datecreated')[:3]
    new_main_set = News.objects.filter(main_news__exact = True).order_by('-datecreated')
    context = RequestContext(request, {'news' : new_set, 'main_news' : new_main_set})

    return render_to_response(template_name, context)

def testcataloh(request, template_name="testcat.html"):
    products = Product.objects.all()
    product_lensess = Linses.objects.select_related()

    context = {'products' : product_lensess}
    return render_to_response(template_name, context )

def catalogfull(request, template_name="Catalogfull/catalog.html"):
    form1 = filterform(request.POST)
#   product_lensess = Product.objects.filter(category__Name__exact="контактные линзы")


    product_lensess = Linses.objects.select_related('fk_product').all()


    sel1 = Linses.objects.order_by('optical_power').distinct('optical_power') # оптическая сила

    sel2 = Linses.objects.order_by('replacment_time').distinct('replacment_time') # срок замены
    sel3 = Linses.objects.order_by('manufacturer').distinct('manufacturer') # производитель
    sel3 = sel3.exclude(manufacturer__exact = "")
    sel4 = Linses.objects.order_by('radius_of_cutvature').distinct('radius_of_cutvature') # радиус кревизны
    sel5 = Linses.objects.order_by('optical_power_cylinder').distinct('optical_power_cylinder') # оптическая сила цилиндра
    sel6 = Linses.objects.order_by('mode_of_wearing').distinct('mode_of_wearing') # режим ношения
    if request.method == 'POST':

        qs = Linses.objects.select_related("fk_product").all()
        postdata = request.POST.copy()
        q1 = postdata.get('manufacturer', '')
        q2 = postdata.get('opt_power', '')
        q2 = float(q2)
        q3 = postdata.get('repl_time', '')
        q4 = float(postdata.get('radius', ''))
        q5 = float(postdata.get('opt_power_cil', ''))
        q6 = postdata.get('m_o_w', '')
        q7 = postdata.get('manufacturer', '')

        if q1 == '0' and q2 == 0 and q3 == '0' and q4 == 0 and q5 == 0 and q6 == '0':
            context = RequestContext(request, {'product_lensess' : product_lensess, 'sel1' : sel1, 'sel2' : sel2, 'sel3' : sel3, 'sel4' : sel4, 'sel5' : sel5, 'form1' : form1, 'sel6' : sel6, } )

        if q1 != '0':
            qs = qs.filter(manufacturer__exact = q1)
        if q2 != 0.0:
            qs = qs.filter(optical_power__exact = q2)
        if q3 != '0':
            qs = qs.filter(replacment_time__exact = q3)
        if q4 != 0.0:
            qs = qs.filter(radius_of_cutvature__exact = q4)
        if q5 != 0.0:
            qs = qs.filter(optical_power_cylinder__exact = q5)
        if q6 != '0':
            qs = qs.filter(mode_of_wearing__exact = q6)
        context = RequestContext(request, {'product_lensess' : qs, 'sel1' : sel1, 'sel2' : sel2, 'sel3' : sel3, 'sel4' : sel4, 'sel5' : sel5, 'form1' : form1, 'sel6' : sel6, } )
    else:
        context = RequestContext(request, {'product_lensess' : product_lensess, 'sel1' : sel1, 'sel2' : sel2, 'sel3' : sel3, 'sel4' : sel4, 'sel5' : sel5, 'form1' : form1, 'sel6' : sel6, } )







#    context = RequestContext(request, {'product_lensess' : product_lensess, 'sel1' : sel1, 'sel2' : sel2, 'sel3' : sel3, 'sel4' : sel4, 'sel5' : sel5, 'form1' : form1, 'sel6' : sel6, } )

    return render_to_response(template_name, context)

def product_detail(request, offset, template_name = "CatalogFull/detail.html"):
    form = add_form_lins
    offset = int(offset)
    queryset = Linses.objects.filter(fk_product__slug__exact = offset)
    set_opt = queryset.get(fk_product__slug = offset)
    set_opt_norm = Linses.objects.filter(fk_product__product_name__exact = set_opt.fk_product.product_name)
    set_opt_pow = set_opt_norm.order_by('optical_power').distinct('optical_power')
    set_opt_rad = set_opt_norm.order_by('radius_of_cutvature').distinct('radius_of_cutvature')



    context = RequestContext(request, {'test' : queryset, 'rad' : set_opt_rad, 'pow' : set_opt_pow})
    return render_to_response(template_name, context)

def profile_test(request, template_name="registration/profile_test.html"):
    if request.user.is_authenticated():
        i = request.user.id
        request.session["user_id"] = request.user.id
        us = User.objects.filter(id__exact = request.user.id)

        con = RequestContext(request, {'users' : us})
        return render_to_response(template_name, con)

def add_to_cart(request, tmplate_name = "index22.html"):
    if request.user.is_authenticated():
        postdata = request.POST.copy()
        prod_name = postdata.get('prod_name', '')
        power = float(postdata.get('opt_power','').replace(',','.'))
        rad = float(postdata.get('radius','').replace(',','.'))
        queryset = Linses.objects.all()
        queryset = queryset.filter(fk_product__product_name__exact = prod_name)
        queryset = queryset.filter(optical_power__exact = power)
        queryset = queryset.filter(radius_of_cutvature__exact = rad)
        qr = Product.objects.get(product_name = prod_name)
        qs = qr.pk_product_id
        request.session.__setitem__('cart', False)
#        qs = qr.fk_product.pk_product_id
        response = HttpResponse()
        response.set_cookie('cart', value=False)


        if request.session['cart'] == False:
            us = request.user.id
            aus = AuthUser.objects.get(id = us)
            order1 = Order(order_status = 5, order_date = datetime.date.today(), fk_user = aus )
            order1.save()
            i = order1.pk_order_id
            request.session["cart"] = True
            request.session.__setitem__('cart_id', i)
        order_prod1 = OrderProduct(fk_order = Order.objects.get(pk_order_id = i), fk_product = qr)
        product_for_saving = Product.objects.get(pk_product_id = qs)
        product_for_saving.balance = F('balance') - 1
        product_for_saving.save()
        order_prod1.save()
        return render_to_response(template_name="index22.html")


    return render_to_response()
from django.db import models
from PIL import Image
from django.db.models import F
# Create your models here.

from django.db import models






class Cart(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    fk_username = models.ForeignKey('AuthUser', unique=False, db_column='fk_username')
    product = models.ForeignKey('Product', unique=False, db_column='product')
    kol = models.IntegerField(db_column='kol', default=1, )
    date_added = models.DateField(db_column='date_added', )
    class Meta:
        db_table='Cart'

class News(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    main_news = models.BooleanField(default=False, db_column='main_news')
    text_news = models.TextField(max_length=500, db_column='text_news' )
    link_news = models.URLField(db_column='link_news')
    datecreated = models.DateField(db_column='datecreated')
    class Meta:
        db_table = 'News'




class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='category_id',unique=True)
    Name = models.CharField(db_column='Name', max_length=30, verbose_name='Название категории',blank=False)
    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.Name



class Linses(models.Model):
    REPL_TIME = (
        ('1 день','Однодневные ( 1 день)'),
        ('1-2 недели','1-2 недели'),
        ('1  месяц','Ежемесячной замены'),
        ('3-6 месяцев','3-6 месяцев'),
        ('1 год','Традиционные (1 год)'),
    )

    MODE = (
        ('дневной', 'дневной'),
        ('пролонгированный', 'пролонгированный ( на 7 дней не снимая ночью)'),
        ('гибкий', 'гибкий (1-2 дня не снимая)'),
        ('непрерывный', '30 дней не снимая'),
    )
    fk_product = models.ForeignKey('Product', unique=True, db_column='FK_PRODUCT_ID') # Field name made lowercase.
    manufacturer = models.CharField(db_column='MANUFACTURER', max_length=50, blank=False, verbose_name='Приозводитель') # Field name made lowercase.
#    brand = models.CharField(db_column='BRAND', max_length=50, blank=True, verbose_name='брэнд') # Field name made lowercase.
    replacment_time = models.CharField(db_column='REPLACMENT_TIME', max_length=20, blank=False, verbose_name='срок замены', choices=REPL_TIME) # Field name made lowercase.
    colored = models.BooleanField(null=False, db_column='COLORED', blank=False, verbose_name='цветные?') # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=15, blank=True, verbose_name='цвет') # Field name made lowercase.
    optical_power = models.FloatField(null=True, db_column='OPTICAL_POWER', blank=False, verbose_name='оптическая сила') # Field name made lowercase.
    radius_of_cutvature = models.FloatField(null=True, db_column='RADIUS_OF_CUTVATURE', blank=False, verbose_name='радиус кривизны') # Field name made lowercase.
#    type = models.CharField(db_column='TYPE', max_length=20, blank=True, verbose_name='тип') # Field name made lowercase.
    optical_power_cylinder = models.FloatField(null=True, db_column='OPTICAL_POWER_CYLINDER', blank=True, verbose_name='оптическая сила цилиндра') # Field name made lowercase.
    axis = models.SmallIntegerField(null=True, db_column='AXIS', blank=True, verbose_name='ось') # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    moistire_content = models.SmallIntegerField(null=True, db_column='MOISTIRE_CONTENT', blank=True, verbose_name='влазгосодержание, %') # Field name made lowercase.
    diameter = models.FloatField(null=True, db_column='DIAMETER', blank=True, verbose_name='диаметр, мм') # Field name made lowercase.
    dcl = models.FloatField(null=True, db_column='DCL', blank=True, verbose_name='ДКЛ') # Field name made lowercase.
    indicator_inversion = models.BooleanField(db_column='INDICATOR_INVERSION', verbose_name='индикатор инверсии') # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=20, blank=True, verbose_name='материал') # Field name made lowercase.
    mode_of_wearing = models.CharField(max_length=100, blank=False, verbose_name='режим ношения', choices=MODE)
    country_of_origin = models.CharField(max_length=50, blank=True, verbose_name='страна производитель')
    packing = models.CharField(max_length=30, blank=True, verbose_name='упаковка')
    uv_filter = models.BooleanField(db_column='UV_filter', verbose_name='УФ фильтр') # Field name made lowercase.
    design = models.CharField(max_length=30, blank=True, verbose_name='дизайн')
    img = models.ImageField(upload_to='photos/', db_column='imagel')
    class Meta:
        db_table = 'LINSES'

    def __str__(self):
#        return u' %s %s' (self.fk_product.product_name, self.brand)
        return self.fk_product.product_name


class Order(models.Model):
    STATUS = (
        ('1','в обработке'),
        ('2','отложен'),
        ('3','готов'),
        ('4','отменен'),
        ('5','не оформлен'),
#        ('6',''),
    )

    pk_order_id = models.AutoField(primary_key=True, unique=True, db_column='PK_ORDER_ID', verbose_name='ИД заказа') # Field name made lowercase.
    fk_user = models.ForeignKey('AuthUser', unique=False, db_column='FK_USER_ID') # Field name made lowercase.
    order_status = models.SmallIntegerField(null=True, db_column='ORDER_STATUS', blank=True, verbose_name='статус заказа', choices=STATUS) # Field name made lowercase.
    order_date = models.DateField(db_column='ORDER_DATE', verbose_name='Дата заказа') # Field name made lowercase.
    payment_date = models.DateField(null=True, db_column='PAYMENT_DATE', blank=True, verbose_name='Дата оплаты') # Field name made lowercase.
    sum = models.FloatField(db_column='SUM', verbose_name='сумма заказа') # Field name made lowercase.
    shop = models.SmallIntegerField(null=True, db_column='SHOP', blank=True, verbose_name='магазин', default=5) # Field name made lowercase.
#    canceled = models.BooleanField(null=False, db_column='CANCELED', blank=True, verbose_name='отменён?', default='false') # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50, blank=True, verbose_name='имя') # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50, blank=True, verbose_name='фамилия') # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=50, blank=True, verbose_name='отчество') # Field name made lowercase.
#    number = models.AutoField(unique=True, db_column='NUMBER', verbose_name='номер заказа') # Field name made lowercase.
    class Meta:
        db_table = 'ORDER'




class OrderProduct(models.Model):
    fk_order = models.ForeignKey( 'Order', unique=False, db_column='FK_ORDER_ID') # Field name made lowercase.
    fk_product = models.ForeignKey( 'Product', unique=False, db_column='FK_PRODUCT_ID') # Field name made lowercase.
    product_kol = models.SmallIntegerField(null=True, db_column='PRODUCT_KOL', blank=True, verbose_name='количество продукта', default=1) # Field name made lowercase.
    price = models.FloatField(null=True, db_column='PRICE', blank=True, verbose_name='цена продукта') # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'ORDER_PRODUCT'

class Product(models.Model):
    VALUTE_LIST = (
        ('dollar','доллары ($)'),
        ('euro','евро'),
    )

#    kolvo_id = models.ForeignKey(Kolvo, db_column='kolvo_id', verbose_name='Количество продукта в магазинах' )
    pk_product_id = models.AutoField(primary_key=True, unique=True, db_column='PK_PRODUCT_ID') # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=60, blank=True, verbose_name='наименование продукта') # Field name made lowercase.
    category = models.ForeignKey('Category', db_column='CATEGORY',  verbose_name='категория') # Field name made lowercase.
    price = models.CharField(db_column='PRICE', verbose_name='цена в рублях, пересчитанная', max_length=10, help_text='Данная цена зависит от выбранной валюты (доллар или евро) и её текущего значения') # Field name made lowercase. This field type is a guess.
    valute = models.CharField(db_column='valute', verbose_name='выберите валюту', max_length=10, choices=VALUTE_LIST)
    price_2 = models.CharField(db_column='PRICE_2', blank=True, verbose_name='цена в рублях', max_length=10, help_text='эта цена постоянна, не меняется и нужна только налоговой службе') # Field name made lowercase. This field type is a guess.
#    price_3 = models.CharField(db_column='PRICE_3', blank=True, verbose_name='цена в евро', max_length=10) # Field name made lowercase. This field type is a guess.
    shop = models.CharField(db_column='SHOP', max_length=30, blank=True, verbose_name='магазин') # Field name made lowercase.
    balance = models.SmallIntegerField(null=True, db_column='BALANCE', blank=True, verbose_name='количество') # Field name made lowercase.
    prod_discount = models.SmallIntegerField(null=True, db_column='PROD_DISCOUNT', blank=True, verbose_name='скидка, %') # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, verbose_name='описание/комментарий') # Field name made lowercase.
    price_4 = models.TextField(db_column='PRICE_4', blank=True) # Field name made lowercase. This field type is a guess.
    slug = models.SlugField(max_length= 150, help_text='здесь хранится уникальный номер товара, используемый в магазине')
    LSD = models.SmallIntegerField(db_column='LSD', null=True, blank = True, verbose_name='приход', help_text='заполнять при приходе товара', default=0)

#    img = models.ImageField()
    class Meta:
        db_table = 'PRODUCT'

    def __str__(self):
        return self.product_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Product, self).save(force_insert, force_update)
        if self.LSD != 0:
            self.balance = F('balance') + self.LSD
            self.LSD = 0
            super(Product,self).save(force_update, force_insert)



class History(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    fk_subuser = models.ForeignKey('Subusers', unique=False, db_column='FK_SUBUSER_ID') # Field name made lowercase.
    repl_date = models.DateField(db_column='REPL_DATE', verbose_name='Дата замены') # Field name made lowercase.
    dotnr = models.DateField(db_column='DOTNR', verbose_name='Дата следующей замены') # Field name made lowercase.
    fk_product = models.ForeignKey('Product', unique=False, db_column='FK_PRODUCT_ID', related_name='product_linses') # Field name made lowercase.

    class Meta:
        db_table = 'HISTORY'


class Subusers(models.Model):
    SEX = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    pk_subuser_id = models.AutoField(primary_key=True, unique=True, db_column='PK_SUBUSER_ID', verbose_name='ID subuser') # Field name made lowercase.
#    fk_user = models.ForeignKey('AuthUser', unique=False, db_column='FK_USER_ID', verbose_name='ИД пользователя') # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50, verbose_name='Имя') # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50, verbose_name='фамилия') # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=50, blank=True, verbose_name='отчество') # Field name made lowercase.
    date_of_birth = models.DateField(db_column='DATE_OF_BIRTH', verbose_name='дата рождения') # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=15, verbose_name='номер телефона') # Field name made lowercase. This field type is a guess.
    sex = models.CharField(db_column='sex', max_length=10, blank=True, verbose_name='пол M/F', choices=SEX) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'SUBUSERS'



class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'


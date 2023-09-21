from django.db.models import F, Count, Subquery, Q, OuterRef, Max
from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product



# Create your tests here.
# 2일차 테스트
# class CartTest(TestCase):
#     # print(Cart.objects.values("member__member_name").query)
#     # print(Cart.objects.values("product__product_name").query)
#     print(Member.objects.values("cart__product_count").query)


# 3일차 테스트
# Create your tests here.
class CartTest(TestCase):
    # member = Member.objects.get(id=11)
    # products = list(Product.objects.all())
    #
    # for product in products:
    #     Cart(product_count=3, member=member, product=product).save()

    # 각 회원의 장바구니 목록 조회
    print(Cart.objects.filter(member_id=4).annotate(member_name=F('member__member_name'))
          .values('create_date', 'update_date', 'product_count', 'product_id'))
    # 전체 회원의 장바구니에서 가장 많이 담긴 상품 정보 조회
    print(Cart.objects.all().values('product_id','product__product_name','product__product_price').annotate(
    product_count=Count('product_id')).order_by('-product_count').first())
    # 장바구니에 담긴 상품의 전체 개수가 가장 많은 회원의 정보 조회
    print(Cart.objects.all().values('member__member_name','member__member_email','member__member_password','member__member_age','member__create_date','member__update_date')
          .annotate(product_count=Count('product_id')).order_by('-product_count').first())
    # 장바구니에 아무것도 담지 않은 회원의 정보 조회
    print(Member.objects.values('member_name','member_age','member_email').filter(cart__isnull=True))
    # 장바구니에 한 번이라도 담긴 상품 목록 조회
    print(Cart.objects.all().values('product__product_name','product__product_price').distinct())

    pass
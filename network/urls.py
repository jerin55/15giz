
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import article_list_by_tag


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pageindex", views.pageindex, name="pageindex"),
    path("intrest_page", views.intrest_page, name="intrest_page"),
    path("intrest_create", views.intrest_create, name="intrest_create"),
    path("login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:username>", views.profile, name='profile'),
    path('tag/<str:tag>/', article_list_by_tag, name='article_list_by_tag'),
 
    path("n/saved", views.saved, name="saved"),
    path("n/user_create_post", views.user_create_post, name="user_create_post"),
    path("n/create_pagepost/<int:pageid>", views.create_pagepost, name="create_pagepost"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:userid>/commentz", views.commentz, name="commentz"),
   
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path('n/page_registration/<int:pk>',views.page_registration,name="page_registration"),
    path('n/page_creation/<int:pk>',views.page_creation,name="page_creation"),
    path('n/pag/<int:pk>',views.pag,name="pag"),
    path('pageprofile/<int:pageid>',views.pageprofile,name="pageprofile"),
    path('n/cart',views.cart,name="cart"),
    path('n/checkout',views.checkout,name="checkout"),
    path('n/product_detail/<int:id>',views.product_detail,name="product_detail"),
    path('topicpage/<int:pk>',views.topicpage,name='topicpage'),
    path('upvote/<int:pk>', views.upvote, name='upvote'),
    path('downvote/<int:pk>', views.downvote, name='downvote'),
    path('intrest_follow/<int:pk>', views.intrest_follow, name='intrest_follow'),
    path('intrest_unfollow/<int:pk>', views.intrest_unfollow, name='intrest_unfollow'),



   
  
    path('article_list',views.article_list_by_tag,name='article_list'),

    path('add_cart/<int:id>',views.add_cart,name='add_cart'),

    path('zip',views.zip,name='zip'),

    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),

    path('remove_cart_all',views.remove_cart_all,name='remove_cart_all'),

    
    path('shipping_address',views.shipping_address,name='shipping_address'),
    

    
    
    path('track_order',views.track_order,name='track_order'),

    path('n/my_order',views.my_order,name='my_order'),

    path('manage_order/<int:id>',views.manage_order,name='manage_order'),
    path('n/pagepost/<int:pk>',views.pagepost,name='pagepost'),
    path('n/mypage/<int:pk>',views.mypage,name='mypage'),
  
    path('n/edit_profile/<int:pk>',views.edit_profile,name='edit_profile'),
    path('n/edit_pr/<int:pk>',views.edit_pr,name='edit_pr'),
    path('n/edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('n/edit_pages/<int:pk>',views.edit_pages,name='edit_pages'),
    path('search/', views.search, name='search'),
    path('sent_friend_request/<int:userid>',views.sent_friend_request,name='sent_friend_request'),
    path('accept_friend_request/<int:requestid>',views.accept_friend_request,name='accept_friend_request'),
    path('notification/<int:nid>',views.notification,name='notification'),
    path('userfriends/<int:id>',views.userfriends,name='userfriends'),
    path('sent_invite_request/<int:userid>/<int:id>',views.sent_invite_request,name='sent_invite_request'),
    path('accept_invite_request/<int:requestid>',views.accept_invite_request,name='accept_invite_request'),
    path('userinviters/<int:id>',views.userinviters,name='userinviters'),
    path('delete_inv/<int:pk>',views.delete_inv,name='delete_inv'),
    path('delete_frd/<int:pk>',views.delete_frd,name='delete_frd'),
    path('delete_post/<int:pk>',views.delete_post,name='delete_post'),
    path('pages_accept_invites/<int:pk>',views.pages_accept_invites,name='pages_accept_invites'),
    path('post_comment/<int:pk>',views.post_comment,name='post_comment'),
    path('nsale_post_share/<int:pk>',views.nsale_post_share,name='nsale_post_share'),
    path('sale_post_share/<int:pk>',views.sale_post_share,name='sale_post_share'),
    path('wishlis/<int:pk>',views.wishlis,name='wishlis'),
    path('add_to_wish/<int:pk>',views.add_to_wish,name='add_to_wish'),
    path('delete_wishlist/<int:pk>',views.delete_wishlist,name='delete_wishlist'),










]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


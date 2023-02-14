from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from distutils.command.upload import upload
from itertools import product
from django.shortcuts import reverse
from pyexpat import model
from autoslug import AutoSlugField
from unicodedata import category
from venv import create
from django.db import models
from django.contrib.auth.models import User
from .validators import file_size
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager




class intrest(models.Model):
    intrest_name=models.CharField(max_length=255,blank=True)    


    def __str__(self):
        return self.intrest_name





class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='posts/',default='static/std.jpg')
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(upload_to='posts', default="card2.webp")
    friends=models.ManyToManyField("User",blank=True,related_name="frnd")
    
    

    def __str__(self):
        return self.username

    def serialize(self):
        return {
            'id': self.id,
            "username": self.username,
            "profile_pic": self.profile_pic.url,
        
        }



class page(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=255,null=True)
    pagename=models.CharField(max_length=255,null=True)
    website=models.CharField(max_length=255,null=True)
    category=models.CharField(max_length=255,null=True)
    emial=models.CharField(max_length=255,null=True)
    cover = models.ImageField(upload_to='posts', default="card2.webp")
    image=models.ImageField(upload_to='posts/', blank=True)   


    
class Post(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    page_name=models.CharField(max_length=255,null=True)
    page_id=models.ForeignKey(page, on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    content_text = models.TextField(max_length=140, blank=True)
    status=models.CharField(max_length=255,null=True)
    doc=models.FileField(upload_to='posts/', blank=True,default=True)
    vedio=models.FileField(upload_to='posts/', blank=True,default=True,validators=[file_size])
    slug = models.SlugField(unique=True,default=True,max_length=100)

    Product_Price = models.IntegerField(null=True,blank=True,default=True)
    content_image = models.FileField(upload_to='posts/', blank=True,default=True,validators=[file_size])
    likers = models.ManyToManyField(User,blank=True , related_name='likes')
    savers = models.ManyToManyField(User,blank=True , related_name='saved')
    comment_count = models.IntegerField(default=0)
    posts_type = models.CharField(max_length=255,null=True)
    slug = models.CharField(max_length=130,default=True)
    views=models.IntegerField(default=True)
    title=models.CharField(max_length=255,default=True)
    categories=models.CharField(max_length=255,default=True)
    tages_n=models.CharField(max_length=255,default=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)




    def post_link(self):
        return reverse("post", kwargs={
            'slug': self.slug
        })



    def __str__(self):
        return f"Post ID: {self.id} (creater: {self.creater})"

    def img_url(self):
        return self.content_image.url

    def append(self, name, value):
        self.name = value

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenters')
    comment_content = models.TextField(max_length=90)
    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post: {self.post} | Commenter: {self.commenter}"

    def serialize(self):
        return {
            "id": self.id,
            "commenter": self.commenter.serialize(),
            "body": self.comment_content,
            "timestamp": self.comment_time.strftime("%b %d %Y, %I:%M %p")
        }
    
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.user}"
        



class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class sell(models.Model):
    creater=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    picture=models.ImageField(upload_to='posts/',blank=True)
    Title=models.CharField(max_length=255,null=True)
    price=models.IntegerField()
    category=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(default=timezone.now)




class pageposts(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pageposts')
    date_created = models.DateTimeField(default=timezone.now)
    content_text = models.TextField(max_length=140, blank=True)
    content_image = models.ImageField(upload_to='posts/', blank=True)
    likers = models.ManyToManyField(User,blank=True , related_name='pagelikes')
    savers = models.ManyToManyField(User,blank=True , related_name='pagesaved')
    comment_count = models.IntegerField(default=0)



# Create your models here.




class Category(models.Model):
    Category_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Category_Name



class Product(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Product_Name = models.CharField(max_length=150)
    Product_Image = models.ImageField(upload_to='posts',null=True)
    Product_Description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    Product_Price = models.IntegerField()



    def __str__(self):
        return self.Product_Name 



class Zip(models.Model):
    zip_code = models.IntegerField()

    def __str__(self):
        return self.zip_code





class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    product =  models.ForeignKey(Post,on_delete=models.CASCADE)
    product_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name





class Shipping_address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    Full_name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=12)
    House  = models.CharField(max_length=255)
    Area = models.CharField(max_length=60)
    Landmark = models.CharField(max_length=60)
    Town =  models.CharField(max_length=60)
    State =  models.CharField(max_length=60)
    Zip = models.IntegerField()
    
    def __str__(self):
        return self.Full_name


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    shipping_address = models.ForeignKey(Shipping_address,on_delete=models.CASCADE) 
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=255,null=False)
   
    Order_statuses = (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),

    )
    


    status =models.CharField(max_length=150,choices=Order_statuses,default='Pending')
    tracking_no = models.CharField(max_length=150,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    
class Order_Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    quanty = models.IntegerField(null=False)   


class friend_request(models.Model):
    from_user=models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    stat=models.TextField(max_length=255,blank=True)

class invite_request(models.Model):
    from_user=models.ForeignKey(User,related_name='fr_inv',on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name='to_inv',on_delete=models.CASCADE)
    pages=models.ForeignKey(page,related_name='pagz',on_delete=models.CASCADE,null=True)
    stat=models.TextField(max_length=255,blank=True)    




class invited(models.Model):
    to_user=models.ForeignKey(User,related_name='toinvit',on_delete=models.CASCADE,blank=True,default=True) 
    fr_user=models.ForeignKey(User,related_name='frinvit',on_delete=models.CASCADE,blank=True,default=True)
    fr_pages=models.ForeignKey(page,related_name='pagez',on_delete=models.CASCADE,blank=True,default=True)


class commentz(models.Model):
    fr_user=models.ForeignKey(User,related_name='comm',on_delete=models.CASCADE,blank=True,default=True)    
    user_post=models.ForeignKey(Post,related_name='pos',on_delete=models.CASCADE,blank=True,default=True)
    comment=models.TextField(max_length=255,blank=True)



class friend(models.Model)  :
    to=models.ForeignKey(User,related_name='toreq',on_delete=models.CASCADE,blank=True,default=True) 
    fr=models.ForeignKey(User,related_name='freq',on_delete=models.CASCADE,blank=True,default=True)


class wishlist(models.Model):
    usr=models.ForeignKey(User,related_name='whs',on_delete=models.CASCADE,blank=True,default=True)
    post=models.ForeignKey(Post,related_name='postz',on_delete=models.CASCADE,blank=True,default=True)


class intrest_followers(models.Model):
    followig_user=models.ForeignKey(User,related_name='intr',on_delete=models.CASCADE,blank=True,default=True)
    topic=models.ForeignKey(intrest,on_delete=models.CASCADE,default=True,related_name='top',blank=True)
   







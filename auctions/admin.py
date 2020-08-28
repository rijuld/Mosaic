from django.contrib import admin
from .models import User,auctionlisting,comments,bid,Categories,watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(auctionlisting)
admin.site.register(comments)
admin.site.register(bid)
admin.site.register(watchlist)

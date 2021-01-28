 #The movie project-
The project is divided into three parts, one the movie finder, the discussions group and mosaic the buying applications.
Each of the applications are built on Django and mainly comprise of python and javascript.

#how to run the code on your local machine->
Add the run python manage.py runserver terminal with the protect folder open on terminal

#uses
- google oauth
- django's Paginator
- chartjs
-markdown2
- auth.decorators
and many of other modules and packages and api's

#The movie finder
- User can 
-add,edit their favourite movie is markdown 2.
- can easily add their movies to their calendar
-can watch the top 5 popular movies on the graph
-can see the most popular movie on the top of the home page
-can edit the movie from the calendar
- can search the entire movie name or substring of it and get directed to a page displaying all such movies and user can click the item to go to that page
-can get a random movie by using the random movie button 


#The movie discussion app

- User can add their, like their or others post, edit their post.
-can follow someone, see the number of followers they have
-can also see the posts of people they follow and their own post on different pages
-uses paginator to go to different pages

#The buy and sell app(for movie posters and stuff)

-User can add a bidding of a movie poster 
-can bid on another item 
-can add an item to their watchlist

-Users who are signed in are able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.

-The “All Posts” link in the navigation bar takes the user to a page where they can see all posts from all users, with the most recent posts first.
Each post includes the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).

Profile Page: Clicking on a username loads that user’s profile page. 
and it
-Displays the number of followers the user has, as well as the number of people that the user follows.
-Displays all of the posts for that user, in reverse chronological order.
For any other user who is signed in, this page displays a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are following this user’s posts.

 -The “Following” link in the navigation bar takes the user to a page where they see all posts made by users that the current user follows.
-This page behaves just as the “All Posts” page does, just with a more limited set of posts.
-This page is only be available to users who are signed in.
-USES PAGINATION

-The user IS able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
For security, application is designed such that it is not possible for a user, via any route, to edit another user’s posts.
“Like” and “Unlike”: Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
Using JavaScript it asynchronously lets the server know to update the like count (as via a call to fetch) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.

Hope you like it!



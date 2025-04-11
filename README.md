# 🎬 The Movie Project  
**Demo Link:** [Watch on YouTube](https://www.youtube.com/watch?v=jt_bFwAqxxI)

This project is split into three interconnected Django-based applications:  
1. **Movie Finder** – for discovering and managing movies  
2. **Discussion Board** – for sharing opinions and posts  
3. **Mosaic (Buy & Sell)** – a marketplace for movie-related items like posters

Each app is built using **Django**, with a stack primarily involving **Python** and **JavaScript**.

---

## 🚀 Running the Project Locally

Make sure you're inside the project directory in your terminal, then run:  
```bash
python manage.py runserver
```

---

## 🛠️ Tech Stack and Features Used

- Google OAuth for secure sign-in  
- Django’s Paginator for clean navigation  
- Chart.js for interactive graphs  
- Markdown2 for rich-text rendering  
- `auth.decorators` for route protection  
- ...and many other APIs, modules, and custom utilities  

---

## 🎥 Movie Finder App Features

- Add and edit your favorite movies using **Markdown2**
- Add movies directly to your calendar  
- View the **Top 5 Most Popular Movies** on an interactive graph  
- Always see the most trending movie pinned on the homepage  
- **Edit movies from your calendar** for easy updates  
- Use the powerful **search** feature to find movies via full or partial names  
- Feeling lucky? Click the **Random Movie** button to discover something new  

---

## 💬 Movie Discussion App

- Create, edit, and like posts (yours or others’)  
- Follow other users and view follower/following counts  
- View posts from people you follow on a separate feed  
- Paginated views to browse older posts easily  

---

## 🛍️ Buy & Sell App – Marketplace for Movie Posters

- Post listings for movie-related merchandise with optional bidding  
- Bid on other users’ posters  
- Add items to your **watchlist** to track them  
- Only signed-in users can post listings  

---

## 📄 Social Features & Profiles

- All signed-in users can post using a simple text area  
- “All Posts” shows every user’s posts (most recent first), including:
  - Username  
  - Content  
  - Timestamp  
  - Number of likes  

### Profile Page
- Displays follower and following counts  
- Lists all of the user’s posts (newest first)  
- Follow/Unfollow button available for other users’ profiles  

### “Following” Feed
- Shows posts **only** from users you follow  
- Paginated just like the main feed  
- Only accessible to logged-in users  

---

## ✨ Smooth JavaScript Experience

- **Edit posts in-place** with a seamless UI—no page reloads  
- **Like/Unlike posts** asynchronously via `fetch()` calls, updating like counts instantly  
- Built with security in mind: users can’t modify posts that aren’t theirs  

---

Hope you enjoy exploring the project as much as I enjoyed building it! 😊  
Feel free to clone, run, or contribute!

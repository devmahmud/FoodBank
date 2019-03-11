# FoodBank
Food bank is a food review posting site developed in Django. Where user can Register, Login Then add review. User can like review, Update their own profile, Edit their posted review also can delete them. There is a comment system implement for each review.

<h2>Requirements</h2>
<pre>open requirements.txt file to see requirements</pre>

<h2>Installing</h2>
<pre>open terminal and type</pre>
<code>git clone https://github.com/devmahmud/FoodBank.git</code><br><br>

<h4>or simply download using the url below</h4>
<code>https://github.com/devmahmud/FoodBank.git</code><br>

<h2>To migrate the database open terminal in project directory and type</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>Static files collection</h2>
<pre>open terminal and type</pre>
<code>python manage.py collectstatic</code>

<h2>Creating Superuser</h2>
<pre>To create superuser open terminal and type</pre>
<code>python manage.py createsuperuser</code>

<h2> For password Reset functionality by email fill up the information in Your Project setting </h2>
<code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code><br>
<code>EMAIL_HOST = 'smtp.gmail.com'</code><br>
<code>EMAIL_PORT = 587</code><br>
<code>EMAIL_USE_TLS = True</code><br>
<code>EMAIL_HOST_USER = 'your email'</code><br>
<code>EMAIL_HOST_PASSWORD = 'your email password'</code><br>

<h2> To run the program in local server use the following command </h2>
<code>python manage.py runserver</code>

<p>Then go to http://127.0.0.1:8000 in your browser</p>

<h2>Project snapshot</h2>
<h3>FoodBank Home Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54106748-5304f280-4401-11e9-8651-c8febbf0bd91.png" width="100%"</img> 
</div>

<h3>User Login Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54106807-80ea3700-4401-11e9-9446-f8fd7aa15b1f.png" width="100%"</img> 
</div>

<h3>User Registration Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54106864-b000a880-4401-11e9-92d4-8b743ade01ad.png" width="100%"</img> 
</div>

<h3>Dashboard Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54106920-e5a59180-4401-11e9-8f01-e79fe229ef78.png" width="100%"</img> 
</div>

<h3>Profile Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54107006-1a194d80-4402-11e9-898a-1673e7ca5f31.png" width="100%"</img> 
</div>

<h3>Create Post Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54107051-41701a80-4402-11e9-9139-ca71c74ef670.png" width="100%"</img> 
</div>

<h3>Post Details Page</h3>
<div align="center">
    <img src="https://user-images.githubusercontent.com/19981097/54107124-6e243200-4402-11e9-9f4c-20c1c83503e9.png" width="100%"</img> 
</div>

<h2>Author</h2>
<blockquote>
  Mahmudul alam<br>
  Email: expelmahmud@gmail.com
</blockquote>

<div align="center">
    <h3>========Thank You !!!=========</h3>
</div>


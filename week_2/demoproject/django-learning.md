### Django is like a magic box that helps you make websites. You tell Django what you want your website to do, and it will do all the hard work for you! It's kind of like having a robot helper who knows how to build websites.

To make a website using Django, we need to follow some rules. First, we need to tell Django what we want our website to be called (like "My Awesome Website"). Then we need to tell Django what pages we want on our website (like a home page, an about page, and a contact page). Finally, we need to tell Django what we want each page to say and do.

For example, to print "Hello World" on our website, we would tell Django that we want a page called "Hello World" that says "Hello World" when someone visits it. And then Django would make that happen!

Now, let's make a project together to print "Hello World". First, we need to set up our Django magic box. Here's what we need to do:

To make a project that prints "Hello World" using Django, you would follow these steps:

    Install Django on your computer (with the help of a grown-up or a teacher, of course).

   1.  Open up your computer's terminal (which is like a magic box that lets you talk to your computer).

   2.  Use the terminal to tell Django to create a new project for you. You can do this by typing   ```django-admin startproject demoproject.```

   3.  Now, you need to create an "app" within your project that will handle the "Hello World" message. You can do this by typing ```python manage.py startapp testapp```.

   4. Open up the file called views.py within your new app's directory (which is in the helloworldapp folder), and add the following code:
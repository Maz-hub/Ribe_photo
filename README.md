# Ribe Photo Portfolio Web App

#### Video Demo: [Video YouTube](https://www.youtube.com/watch?v=36bm5_MyEng)

## Live Site

You can view the live version of the Ribe Photo portfolio here:
[https://ribe.photo](https://ribe.photo)

## Project Overview

The Ribe Photo Portfolio Web App is a simple, responsive website built to showcase a photographer’s work in different galleries. In this version, users can browse through photos that are hosted on Cloudinary for fast loading and good image quality. The app does not have a backend system or database, and all the content is managed manually.

The goal of this project is to provide a clean design and smooth user experience for browsing photo galleries. In the future, I plan to add a backend system for managing galleries, as well as a blog to share stories and tips about photography.

### Target Audience

- **Casual Browsers**: People who enjoy viewing artistic photography.
- **Nature and Photography Lovers**: Enthusiasts seeking inspiration from high-quality images of natural landscapes and scenes.
- **Hobbyists**: Beginner photographers who want to explore and appreciate different styles of photography.

---

## Initial Setup and Planning

### Main Technologies and Tools

- **Backend**: Flask (Python) with Jinja for dynamic template rendering.
- **Frontend**: Bootstrap 5 for responsive design and SCSS for advanced styling.
- **Image Hosting**: Cloudinary for storing and serving optimized images.
- **Deployment**: Heroku for hosting the web app.
- **Version Control**: Git for tracking changes, with the repository hosted on GitHub under https://github.com/Maz-hub/ribe_photo

### Project Structure

The project is organized into several folders and files:

- **templates/**: contains all HTML files. Each file corresponds to a specific page in the app (e.g., index.html for the homepage, about.html for the about page). These files use Jinja templating for reusable components like headers and footers.

To avoid repetitive code, a global header and footer were created in templates/base.html. This file serves as a layout template that other HTML files extend using the following Jinja syntax:

````html
{% extends "base.html" %} ```{% block content %}

<!-- Page-specific content -->

{% endblock %}
````

- **static/**: stores all static assets, including compiled CSS files in the css/ directory, a logo and favicon in the img/ directory, JavaScript files in the js/ directory, and fonts in the webfonts/ directory.

- **scss/**: contains SCSS files for styling. These include bootstrap.scss for framework styles, fontawesome.scss for icons, and styles.scss for custom styles.

- **virt/**: is the virtual environment configuration for Python dependencies, ensuring that all required packages are installed and isolated.

- **node_modules/**: contains Node.js dependencies for compiling SCSS and managing frontend tools.

- **pycache/**: is an auto-generated directory created by Python to store bytecode files for improved performance.

- **.env**: stores sensitive configuration variables, such as the Cloudinary API keys.

- **requirements.txt**: lists all Python libraries required for running the app.

- **app.py**: the main Python file that runs the Flask application and connects all components of the project.

- **Procfile**: specifies the command Heroku uses to deploy and run the app.

- **package.json**: and package-lock.json manage Node.js dependencies and frontend tools.

- **Google Analytics Integration**: Tracks user interactions such as page views, scrolls, and outbound link clicks to provide insights into how users engage with the website.

**Note:** `virt/`, `node_modules/`, and `__pycache__/` are excluded from version control using `.gitignore` to keep the repository clean and avoid unnecessary files.

## Key Features and Functionalities

### Contact Form with Email Notifications

The app includes a Contact Form that allows users to send messages or inquiries to the photographer. This feature is powered by SendGrid, which handles the email delivery process. When a user submits the contact form, an email is sent directly to the photographer's Gmail account at ribephoto@gmail.com.

- **Email Service**: The app uses SendGrid's free tier to send emails.
- **Photographer's Email**: Emails are sent to the photographer's Gmail account (ribephoto@gmail.com).
- **No Professional Email**: The app does not use a custom domain email. Instead, it uses the free Gmail account for simplicity.

### Gallery Pages

The app features visually distinct gallery pages showcasing the following categories:

1. **Sahara Sands**: Photos of Riviera Vaudoise covered by a cloud of Saharan dust
2. **Lake Leman**: Photos of Lake Leman during different seasons and lighting conditions.
3. **Croatia**: Images from Dubrovnik and Plitvice Lakes National Park, Croatia.
4. **Mountains Autumn**: Pictures of Swiss mountains during autumn.
5. **Mushrooms**: A gallery featuring close-up photos of mushrooms in their natural habitats.

### Responsive Design

The app works seamlessly on **mobile**, **tablet**, and **desktop** devices, thanks to Bootstrap 5. SCSS is used to enhance the styling and create a polished interface

### Integration with Cloudinary

**Why Cloudinary?**

- Photos are stored on Cloudinary to overcome GitHub's storage limitations and to ensure fast and optimized image delivery.

## Version Control

- Repository: [ribe_photo GitHub Repository](https://github.com/Maz-hub/ribe_photo).

---

## Future Features and Enhancements

1. **User Comments**: Add a user comments section so visitors can leave feedback on photos.
2. **Enhanced Backend Features**: Build a backend system to allow the photographer to log in and manage galleries dynamically.
3. **Search and Filters**: Implement search and filter options to make browsing galleries easier.
4. **Blog Section**: Introduce a blog to share photography-related stories and tips.

---

## Deployment and Hosting

The app is deployed on **Heroku**, a cloud platform for hosting web apps. The deployment process involved:

## Deployment Steps

1. Set up **Heroku account** and create a new app.
2. Add the Heroku remote repository to project:
   ```bash
   heroku git:remote -a your-heroku-app-name
   ```
3. Create a `Procfile` to specify the command to run Flask app:
   ```text
   web: gunicorn app:app
   ```
4. Set environment variables (e.g., `CLOUDINARY_API_KEY`, `SENDGRID_API_KEY`) in the Heroku dashboard.

5. Install Python dependencies locally and ensure they are listed in requirements.txt:

```bash
pip install -r requirements.txt
```

6. Deploy the app:

   ```bash
   git push heroku master
   ```

Instructions [Heroku's Deployment Documentation](https://devcenter.heroku.com/articles/getting-started-with-python).

---

## Summary

The Ribe Photo Portfolio Web App is a responsive and user-friendly website for showcasing photography galleries. Built with Flask, Bootstrap, and Cloudinary, it offers a simple but effective browsing experience. While this is a basic version with manual content management, it lays the groundwork for future improvements, such as adding dynamic content management and a blog.

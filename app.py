from flask import Flask, render_template
from cloudinary.utils import cloudinary_url
from cloudinary.api import resource
import cloudinary
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

# Flask instance
app = Flask(__name__)  # This must come before any use of 'app'

@app.route('/')
def index():
    # Public IDs for the slides
    public_ids = [
        "Leman_Ribe_Photo_2_kjqykc",
        "Plitvice_Ribe_Photo_25_pwpx4p",
        "Autumn_Ribe_Photo_8_h78clf",
        "Sahara_Ribe_Photo_3_mgyyrr"
    ]

    # Generate URLs dynamically for the public IDs
    slide_urls = [cloudinary_url(public_id)[0] for public_id in public_ids]

    # Pass the URLs to the template
    return render_template("index.html", slide_urls=slide_urls)

@app.route("/galleries")
def galleries():
    # Public ID for the banner photo
    banner_id = "ribe_About_wnx8bn"

    # Public IDs for the project images
    project_ids = [
        "Title_dbotoo",
        "Title_tpdmtb",
        "Title_2_oza264",
        "Title_le3xqj",
        "title_rmcb2a",
        "Title_cxofnz",
        
    ]

    # Generate URLs dynamically
    banner_url = cloudinary_url(banner_id)[0]
    project_urls = [cloudinary_url(project_id)[0] for project_id in project_ids]

    # Pass the URLs to the template
    return render_template("galleries.html", banner_url=banner_url, project_urls=project_urls)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)

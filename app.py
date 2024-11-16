from flask import Flask, render_template
from cloudinary.api import resource
from cloudinary.utils import cloudinary_url
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
app = Flask(__name__)

@app.route('/')
def index():
    # Public IDs for the slides
    public_ids = [
        "Leman_Ribe_Photo_2_kjqykc",
        "Plitvice_Ribe_Photo_25_pwpx4p",
        "Autumn_Ribe_Photo_8_h78clf",
        "Sahara_Ribe_Photo_3_mgyyrr"
    ]

    # Fetch metadata for each image
    slides = []
    for public_id in public_ids:
        metadata = resource(public_id)
        slide = {
            "url": cloudinary_url(public_id)[0],
            "title": metadata.get("context", {}).get("custom", {}).get("caption", "Untitled"),
            "description": metadata.get("context", {}).get("custom", {}).get("alt", "No description available"),
            "tags": metadata.get("tags", [])
        }
        slides.append(slide)

    # Pass the slides to the template
    return render_template("index.html", slides=slides)

if __name__ == "__main__":
    app.run(debug=True)

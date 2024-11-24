from flask import Flask, render_template, request
from cloudinary.utils import cloudinary_url
from cloudinary.api import resource
import cloudinary
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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
    # Slides
    public_ids = [
        "Leman_Ribe_Photo_2_kjqykc",
        "Plitvice_Ribe_Photo_25_pwpx4p",
        "Autumn_Ribe_Photo_8_h78clf",
        "Sahara_Ribe_Photo_3_mgyyrr"
    ]

    slide_urls = [cloudinary_url(public_id)[0] for public_id in public_ids]

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

    banner_url = cloudinary_url(banner_id)[0]
    project_urls = [cloudinary_url(project_id)[0] for project_id in project_ids]

    return render_template("galleries.html", banner_url=banner_url, project_urls=project_urls)


@app.route("/about")
def about():
    # Banner Image
    banner_id = "Andrea_Ribero_bio_photo_qltpgn"
    banner_url = cloudinary_url(banner_id)[0]

    # Other Images
    first_image_id = "5dmk4-Canon_cug99m"
    first_image_url = cloudinary_url(first_image_id)[0]

    second_image_id = "70-200mm_2_rysn1h"
    second_image_url = cloudinary_url(second_image_id)[0]

    return render_template(
        "about.html", 
        banner_url=banner_url,
        first_image_url=first_image_url,
        second_image_url=second_image_url
    )


@app.route("/contact")
def contact():
    banner_id = "Leman_Ribe_Photo_10_znewj3"
    banner_url = cloudinary_url(banner_id)[0]
    
    return render_template("contact.html", banner_url=banner_url)

@app.route("/privacy_terms")
def privacy_terms():
    banner_id = "Mushroom_ribe_photo_3_xrfsdr"
    banner_url = cloudinary_url(banner_id)[0]
    
    return render_template("privacy_terms.html", banner_url=banner_url)



@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        import certifi

        os.environ['SSL_CERT_FILE'] = certifi.where()

        # Get form data
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')

        # Debugging: Print form data and API Key
        print(f"SendGrid API Key: {os.getenv('SENDGRID_API_KEY')}")
        print(f"Name: {user_name}, Email: {user_email}, Message: {user_message}")

        # Ensure all fields are populated
        if not user_name or not user_email or not user_message:
            return "All form fields are required", 400

        # Compose the email
        message = Mail(
            from_email='ribephoto@gmail.com',  # The sender email (must be verified in SendGrid)
            to_emails='ribephoto@gmail.com',  # The recipient email
            subject=f"New Contact Form Submission from {user_name}",
            html_content=f"""
                <p>You have a new contact form submission:</p>
                <p><strong>Name:</strong> {user_name}</p>
                <p><strong>Email:</strong> {user_email}</p>
                <p><strong>Message:</strong></p>
                <p>{user_message}</p>
            """
        )

        # Send email using SendGrid
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)

        # Debugging: Print response details
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {response.headers}")

        return "Email sent successfully!", 200
    except Exception as e:
        # Print and return the error
        print(f"Error sending email: {e}")
        return f"Failed to send email: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)

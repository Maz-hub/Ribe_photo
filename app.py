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

@app.route("/lake_leman")
def lake_leman():
    # Public ID for the banner photo
    banner_id = "Title_2_oza264"

    # Public IDs for the images in the Lake Léman project
    lake_leman_ids = [
        "Leman_Ribe_Photo_7_dizy6f",
        "Leman_Ribe_Photo_14_kcu4ua",
        "Leman_Ribe_Photo_13_tcedfr",
        "Leman_Ribe_Photo_15_xygour",
        "Leman_Ribe_Photo_5_lrlbxn",
        "Leman_Ribe_Photo_12_fydbps",
        "Leman_Ribe_Photo_11_swtdus",
        "Leman_Ribe_Photo_9_i3ozk1",
        "Leman_Ribe_Photo_10_znewj3",
        "Leman_Ribe_Photo_3_ols2wh",
        "Leman_Ribe_Photo_4_noe41u",
        "Leman_Ribe_Photo_8_ug0yhi",
        "Leman_Ribe_Photo_6_bw9mwm",
        "Leman_Ribe_Photo_1_zb9tbz",
        "Leman_Ribe_Photo_2_rdyged",
    ]

    banner_url = cloudinary_url(banner_id)[0]

    # List to hold image URLs and titles
    project_images = []

    # Fetch URLs and titles
    for image_id in lake_leman_ids:
        # Generate the image URL
        url = cloudinary_url(image_id)[0]
        
        # Fetch metadata from Cloudinary
        resource = cloudinary.api.resource(image_id, context=True)
        title = resource.get('context', {}).get('custom', {}).get('caption', 'No Title') 
        
        # Image data to the list
        project_images.append({
            'url': url,
            'title': title
        })

    return render_template("lake_leman.html", banner_url=banner_url, project_images=project_images)


#plitvice_national_park_croatia

@app.route("/plitvice_national_park_croatia")
def plitvice_national_park_croatia():
    # Public ID for the banner photo
    banner_id = "Title_2_swksfw"

    # Public IDs for the images in the Lake Léman project
    plitvice_national_park_croatia_ids = [
        "Plitvice_Ribe_Photo_4_j0abpa",
        "Plitvice_Ribe_Photo_21_horvk7",
        "Plitvice_Ribe_Photo_32_cqicg6",
        "Plitvice_Ribe_Photo_36_ca7jdg",
        "Plitvice_Ribe_Photo_31_pfffpr",
        "Plitvice_Ribe_Photo_37_iry8rq",
        "Plitvice_Ribe_Photo_40_empdnd",
        "Plitvice_Ribe_Photo_30_tjilw6",
        "Plitvice_Ribe_Photo_14_fh0va0",
        "Plitvice_Ribe_Photo_39_ghuhwi",
        "Plitvice_Ribe_Photo_13_j3eby0",
        "Plitvice_Ribe_Photo_35_wwzyte",
        "Plitvice_Ribe_Photo_38_gu15z6",
        "Plitvice_Ribe_Photo_26_bvo9jo",
        "Plitvice_Ribe_Photo_22_gvcbie",
        "Plitvice_Ribe_Photo_23_kueffb",
        "Plitvice_Ribe_Photo_19_rrfsby",
        "Plitvice_Ribe_Photo_20_fanw9x",
        "Plitvice_Ribe_Photo_33_tcddfm",
        "Plitvice_Ribe_Photo_10_nroywl",
        "Plitvice_Ribe_Photo_27_kafihk",
        "Plitvice_Ribe_Photo_12_niaq4f",
        "Plitvice_Ribe_Photo_1_lldipa",
        "Plitvice_Ribe_Photo_16_emnhqi",
        "Plitvice_Ribe_Photo_29_p2ixan",
        "Plitvice_Ribe_Photo_8_zkwhxb",
        "Plitvice_Ribe_Photo_9_rab9le",
        "Plitvice_Ribe_Photo_17_lnywdw",
        "Plitvice_Ribe_Photo_28_jlh6ft",
        "Plitvice_Ribe_Photo_34_oqlpcd",
        "Plitvice_Ribe_Photo_25_uokiki",
        "Plitvice_Ribe_Photo_24_pgrtcr",
        "Plitvice_Ribe_Photo_7_csevjh",
        "Plitvice_Ribe_Photo_11_vpn400",
    ]

    banner_url = cloudinary_url(banner_id)[0]

    # List to hold image URLs and titles
    project_images = []

    # Fetch URLs and titles
    for image_id in plitvice_national_park_croatia_ids:
        # Generate the image URL
        url = cloudinary_url(image_id)[0]
        
        # Fetch metadata from Cloudinary
        resource = cloudinary.api.resource(image_id, context=True)
        title = resource.get('context', {}).get('custom', {}).get('caption', 'No Title') 
        
        # Image data to the list
        project_images.append({
            'url': url,
            'title': title
        })

    return render_template("plitvice_national_park_croatia.html", banner_url=banner_url, project_images=project_images)

#dubrovnik_croatia

@app.route("/dubrovnik_croatia")
def dubrovnik_croatia():
    # Public ID for the banner photo
    banner_id = "Title_tpdmtb"

    # Public IDs for the images in the Lake Léman project
    dubrovnik_croatia_ids = [
        "Dubrovnik_Ribe_Photo_30_mhljnj",
        "Dubrovnik_Ribe_Photo_29_thunur",
        "Dubrovnik_Ribe_Photo_25_poveta",
        "Dubrovnik_Ribe_Photo_34_kt9zcr",
        "Dubrovnik_Ribe_Photo_35_gybydv",
        "Dubrovnik_Ribe_Photo_37_lodc5m",
        "Dubrovnik_Ribe_Photo_23_yslhze",
        "Dubrovnik_Ribe_Photo_32_forgbx",
        "Dubrovnik_Ribe_Photo_39_wznlqk",
        "Dubrovnik_Ribe_Photo_36_zfut1f",
        "Dubrovnik_Ribe_Photo_20_lpv7vx",
        "Dubrovnik_Ribe_Photo_9_stegic",
        "Dubrovnik_Ribe_Photo_40_brznpw",
        "Dubrovnik_Ribe_Photo_24_cfmhv2",
        "Dubrovnik_Ribe_Photo_10_g5m1eq",
        "Dubrovnik_Ribe_Photo_15_yfkf2z",
        "Dubrovnik_Ribe_Photo_28_qpskjv",
        "Dubrovnik_Ribe_Photo_4_mspapj",
        "Dubrovnik_Ribe_Photo_41_ymmaij",
        "Dubrovnik_Ribe_Photo_1_skhd2i",
        "Dubrovnik_Ribe_Photo_31_rfnrzo",
        "Dubrovnik_Ribe_Photo_21_f36prs",
        "Dubrovnik_Ribe_Photo_22_zu5khy",
        "Dubrovnik_Ribe_Photo_13_rgiscs",
        "Dubrovnik_Ribe_Photo_2_swxhh6",
        "Dubrovnik_Ribe_Photo_18_vcid89",
        "Dubrovnik_Ribe_Photo_19_kz4fbh",
        "Dubrovnik_Ribe_Photo_17_pkzq3q",
        "Dubrovnik_Ribe_Photo_5_h8slmo",
        "Dubrovnik_Ribe_Photo_7_dmxqdk",
        "Dubrovnik_Ribe_Photo_11_yqnaiu",
        "Dubrovnik_Ribe_Photo_6_icvydy",
        "Dubrovnik_Ribe_Photo_12_nrtyni",
        "Dubrovnik_Ribe_Photo_14_olao4q",
        "Dubrovnik_Ribe_Photo_26_qgkl9r",
        "Dubrovnik_Ribe_Photo_8_mz22ij",
        "Dubrovnik_Ribe_Photo_16_lfroz2",
        "Dubrovnik_Ribe_Photo_3_zw4rbt",
    ]

    banner_url = cloudinary_url(banner_id)[0]

    # List to hold image URLs and titles
    project_images = []

    # Fetch URLs and titles
    for image_id in dubrovnik_croatia_ids:
        # Generate the image URL
        url = cloudinary_url(image_id)[0]
        
        # Fetch metadata from Cloudinary
        resource = cloudinary.api.resource(image_id, context=True)
        title = resource.get('context', {}).get('custom', {}).get('caption', 'No Title') 
        
        # Image data to the list
        project_images.append({
            'url': url,
            'title': title
        })

    return render_template("dubrovnik_croatia.html", banner_url=banner_url, project_images=project_images)    



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

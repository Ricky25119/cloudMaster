from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)

# Secret key for flash messages
app.config['SECRET_KEY'] = 'your-secret-key-here-change-this'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Change this
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')      # Change this (use App Password)
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # Change this

mail = Mail(app)

# Admin email address
ADMIN_EMAIL = 'aarizmohammad92@gmail.com'

# Example dynamic data for courses and testimonials
courses = [
    {
        "img": "img/AWS_devops.png",
        "title": "AWS DevOps",
        "desc": "AWS DevOps focuses on implementing DevOps practices using Amazon Web Services, including CI/CD pipelines, infrastructure as code, monitoring, and automation"
    },
    {
        "img": "img/Azure_devops_hd.png",
        "title": "Azure DevOps",
        "desc": "Azure DevOps enables teams to plan, build, test, and deploy applications using Microsoft Azure tools such as Azure Repos, Pipelines, Boards, and Artifacts"
    },
    {
        "img": "img/DE.png",
        "title": "Data Engineering",
        "desc": "Data Engineering involves designing, building, and maintaining data pipelines and architectures to process, store, and analyze large-scale data efficiently."
    },
    {
        "img": "img/AIML.jpg",
        "title": "AI/ML Engineering",
        "desc": "AI/ML Engineering focuses on building intelligent systems using machine learning algorithms, data modeling, deep learning, and deploying AI solutions at scale."
    }
]

testimonials = [
    {
        "img": "img/testimonial-1.jpg",
        "name": "Anvesh",
        "role": "DevOps Engineer",
        "text": "CloudCademy gave me the confidence and skills to land my dream job in tech!"
    },
    {
        "img": "img/testimonial-2.jpg",
        "name": "Prashanth",
        "role": "Data Engineer",
        "text": "The hands-on approach and real-world projects made all the difference."
    },
    {
        "img": "img/testimonial-3.jpg", 
        "name": "Sarath",
        "role": "DevOps Engineer",
        "text": "Supportive mentors and a great community. Highly recommended!"
    }
]

@app.route('/')
def index():
    return render_template('Home2.html', courses=courses, testimonials=testimonials)

@app.route('/course')
def course():
    return render_template('courses2.html', courses=courses)

@app.route('/book-demo', methods=['GET', 'POST'])
def book_demo():
    if request.method == 'POST':
        # Get form data
        full_name = request.form.get('fullName')
        phone = request.form.get('phone')
        email = request.form.get('email')
        course_interested = request.form.get('course')
        visa_status = request.form.get('visaStatus')
        expiry = request.form.get('expiry')
        
        try:
            # Format expiry date
            expiry_date = datetime.strptime(expiry, '%Y-%m-%d').strftime('%B %d, %Y')
            
            # Send email to user
            user_msg = Message(
                subject='Demo Booking Confirmation - CloudCademy',
                recipients=[email]
            )
            user_msg.html = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9;">
                        <div style="background-color: #FF5722; padding: 20px; text-align: center;">
                            <h1 style="color: white; margin: 0;">CloudCademy</h1>
                        </div>
                        <div style="background-color: white; padding: 30px; margin-top: 20px;">
                            <h2 style="color: #FF5722;">Thank You for Booking a Demo!</h2>
                            <p>Dear {full_name},</p>
                            <p>We have received your demo booking request. Our team will contact you shortly to schedule your personalized demo session.</p>
                            
                            <div style="background-color: #f5f5f5; padding: 20px; margin: 20px 0; border-left: 4px solid #FF5722;">
                                <h3 style="margin-top: 0; color: #FF5722;">Your Details:</h3>
                                <p><strong>Course:</strong> {course_interested}</p>
                                <p><strong>Phone:</strong> {phone}</p>
                                <p><strong>Email:</strong> {email}</p>
                                <p><strong>Visa Status:</strong> {visa_status}</p>
                                <p><strong>Visa Expiry:</strong> {expiry_date}</p>
                            </div>
                            
                            <p>In the meantime, feel free to explore our courses and reach out if you have any questions.</p>
                            
                            <p style="margin-top: 30px;">Best regards,<br><strong>CloudCademy Team</strong></p>
                        </div>
                        <div style="text-align: center; padding: 20px; color: #777; font-size: 12px;">
                            <p>Icon Offices, East Ham, E6 2JA<br>
                            Email: info.cloudmaster@gmail.com | Phone: +44 7777174006</p>
                        </div>
                    </div>
                </body>
            </html>
            """
            
            # Send email to admin
            admin_msg = Message(
                subject=f'New Demo Booking - {full_name}',
                recipients=[ADMIN_EMAIL]
            )
            admin_msg.html = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                        <h2 style="color: #FF5722;">New Demo Booking Request</h2>
                        <p>A new student has requested a demo session.</p>
                        
                        <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                            <tr style="background-color: #f5f5f5;">
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Full Name</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{full_name}</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Email</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{email}</td>
                            </tr>
                            <tr style="background-color: #f5f5f5;">
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Phone</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{phone}</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Course Interested</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{course_interested}</td>
                            </tr>
                            <tr style="background-color: #f5f5f5;">
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Visa Status</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{visa_status}</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Visa Expiry</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{expiry_date}</td>
                            </tr>
                            <tr style="background-color: #f5f5f5;">
                                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Submitted At</strong></td>
                                <td style="padding: 10px; border: 1px solid #ddd;">{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</td>
                            </tr>
                        </table>
                        
                        <p style="color: #FF5722; font-weight: bold;">Please follow up with this student as soon as possible.</p>
                    </div>
                </body>
            </html>
            """
            
            # Send both emails
            mail.send(user_msg)
            mail.send(admin_msg)
            
            # Redirect to success page
            return render_template('Sucess.html', name=full_name)
            
        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'error')
            return redirect(url_for('book_demo'))
    
    return render_template('Newbooking.html')

@app.route('/success')
def success():
    name = request.args.get('name', 'Student')
    return render_template('Sucess.html', name=name)

@app.route('/about')
def about():
    return render_template('About_us.html')

if __name__ == '__main__':
    app.run(debug=False)



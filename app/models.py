# In app/models.py, the ContactForm class is created using WTForms, a popular form handling library in Python for web applications.
# This class defines various fields for a contact form, each with specific validators to ensure the data entered is valid and meets defined criteria.
# The form includes fields for the user's name, phone number, email, inquiry type, county, and a message.
# These fields range from simple string inputs to select fields with predefined options,
# catering to different types of user input. Validators are employed extensively to enforce minimum and maximum lengths,
# email format validation, and to ensure that all fields are filled out, thereby guaranteeing the form's data integrity and usability.
# This structured approach in ContactForm not only simplifies form creation and validation but also enhances user
# experience and data reliability in the web application.

from wtforms import Form, StringField, TextAreaField, SelectField, validators


class ContactForm(Form):
    name = StringField(
        'Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    phone = StringField(
        'Phone', [validators.Length(min=6, max=20), validators.DataRequired()])
    email = StringField(
        'Email', [validators.Length(min=6, max=50), validators.Email(), validators.DataRequired()])
    inquiryType = SelectField(
        'Inquiry Type', choices=[('general', 'General Inquiry'), ('sales', 'Sales'), ('support', 'Support'), ('other', 'Other')], validators=[validators.DataRequired()])
    county = SelectField(
        'County', choices=[('dublin', 'Dublin'), ('cork', 'Cork')], validators=[validators.DataRequired()])
    message = TextAreaField('Message', [validators.DataRequired()])



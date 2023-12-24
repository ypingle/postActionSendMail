import xml.etree.ElementTree as ET
import sys
import smtplib
from email.mime.text import MIMEText
# Function to extract attribute from XML

def extract_attribute_from_xml(xml_string, attribute_name):
    try:
        root = ET.fromstring(xml_string)
        attribute_value = root.get(attribute_name)
        return attribute_value
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
# Function to send email
def send_email(sender, recipient, subject, body):
    message = MIMEText(body)
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)  # Change this to your SMTP server
        smtp_obj.starttls()
        smtp_obj.login('idoneamani@gmail.com', 'uwdx zhlj bmqp ervv')  # Replace with your email credentials
        smtp_obj.sendmail(sender, recipient, message.as_string())
        smtp_obj.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py path_to_xml_file email_recipients")
        return
    
    xml_file_path = sys.argv[1]
    email_recipients = sys.argv[2]
    
    try:
        with open(xml_file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()
    except FileNotFoundError:
        print(f"File '{xml_file_path}' not found.")
        return

    # Specify the attribute you want to extract (e.g., "DeepLink")
    desired_attribute = "DeepLink"

    # Extract the value of the specified attribute from the XML content
    attribute_value = extract_attribute_from_xml(xml_content, desired_attribute)

    # Output the extracted attribute value
    print(f"The value of '{desired_attribute}' attribute is: {attribute_value}")

       # Set email variables
    email_from = "name@domain.com"
    email_to = email_recipients
    email_subject = "New Checkmarx Scan is done!"
    email_body = f"Scan results URL={attribute_value}"
    # Send email
    send_email(email_from, email_to, email_subject, email_body)


if __name__ == "__main__":
    main()

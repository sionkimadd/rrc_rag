import pdfkit

path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

url_filename_pairs = [
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/Overview", "Application_Development_and_Delivery/Application_Development_and_Delivery_Overview.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/AdmissionRequirements", "Application_Development_and_Delivery/Application_Development_and_Delivery_Admission_Requirements.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/EnglishLanguageAssessments", "Application_Development_and_Delivery/Application_Development_and_Delivery_English_Language_Assessments.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/WhoShouldEnrol", "Application_Development_and_Delivery/Application_Development_and_Delivery_Who_Should_Enrol.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/LocationsDatesandFees", "Application_Development_and_Delivery/Application_Development_and_Delivery_Locations_Dates_and_Fees.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/CoursesandDescriptions", "Application_Development_and_Delivery/Application_Development_and_Delivery_Courses_and_Descriptions.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/COOPPracticumInformation", "Application_Development_and_Delivery/Application_Development_and_Delivery_CO_OP_Practicum_Information.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/ComputerLaptopRequirements", "Application_Development_and_Delivery/Application_Development_and_Delivery_Computer_Laptop_Requirements.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/RecognitionofPriorLearning", "Application_Development_and_Delivery/Application_Development_and_Delivery_Recognition_of_Prior_Learning.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/AwardsandScholarships", "Application_Development_and_Delivery/Application_Development_and_Delivery_Awards_and_Scholarships.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/GraduationRequirements", "Application_Development_and_Delivery/Application_Development_and_Delivery_Graduation_Requirements.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/EmploymentPotential", "Application_Development_and_Delivery/Application_Development_and_Delivery_Employment_Potential.pdf"),
]

for url, filename in url_filename_pairs:
    try:
        pdfkit.from_url(url, filename, configuration=config)
    except Exception as e:
        print(f"Error-{url}-{e}")
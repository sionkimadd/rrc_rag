import pdfkit

path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

url_filename_pairs = [
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADEVF-DP/PrinterFriendly", "RRC/ADD_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/DATSF-DP/PrinterFriendly", "RRC/DSML_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/FUSTF-DP/PrinterFriendly", "RRC/FULLSTACK_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/ISECF-PG/PrinterFriendly", "RRC/INFOSEC_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/CYBEF-DP/PrinterFriendly", "RRC/CYBER_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ITOPF-DP/PrinterFriendly", "RRC/ITOPS_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/NETSF-CT/PrinterFriendly", "RRC/NETSYS_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Parttime/ADVMP-PG/PrinterFriendly", "RRC/NETSYS_Print_Friendly.pdf"),
]

for url, filename in url_filename_pairs:
    try:
        pdfkit.from_url(url, filename, configuration=config)
    except Exception as e:
        print(f"Error-{url}-{e}")
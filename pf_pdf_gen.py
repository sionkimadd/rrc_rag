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
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ADMAF-CT/PrinterFriendly", "RRC/ADMASSI_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Parttime/ADVMP-PG/PrinterFriendly", "RRC/ADVMANU_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/AERMF-CT/PrinterFriendly", "RRC/AEROMANU_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/AIRMF-DP/PrinterFriendly", "RRC/AIRMANUEN_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ANIMF-DP/PrinterFriendly", "RRC/ANIMI_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/APACF-CT/PrinterFriendly", "RRC/APPACC_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/BUADF-NA/PrinterFriendly", "RRC/BUSADM_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/COMMF-PG/PrinterFriendly", "RRC/COMMDES_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/SOCCF-DP/PrinterFriendly", "RRC/SOCICDEV_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/PRSSF-CT/PrinterFriendly", "RRC/PROSSMAR_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/PRBPF-CT/PrinterFriendly", "RRC/PROBP_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/PAITF-SA/PrinterFriendly", "RRC/PAITP_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/INELF-CT/PrinterFriendly", "RRC/INTROEET_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/HOSTF-DP/PrinterFriendly", "RRC/HOSTM_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/GRADF-DP/PrinterFriendly", "RRC/GP_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/GAMPF-AD/PrinterFriendly", "RRC/GAMEDEVP_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/GAMDF-AD/PrinterFriendly", "RRC/GAMEDEVA_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/ENTPF-CT/AdmissionRequirements", "RRC/ENTPRO_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/ELEEF-DP/PrinterFriendly", "RRC/EET_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/FullTime/EAWPF-DP/PrinterFriendly", "RRC/ECEW_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/DIGVF-DP/PrinterFriendly", "RRC/DMDMG_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/DIGIF-DP/PrinterFriendly", "RRC/DMDDD_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/DIMDF-CT/PrinterFriendly", "RRC/DMD_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/DIGFF-PG/PrinterFriendly", "RRC/DFMP_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/CULAF-DP/PrinterFriendly", "RRC/CULIA_Print_Friendly.pdf"),
    ("https://catalogue.rrc.ca/Programs/WPG/Fulltime/CRECF-DP/PrinterFriendly", "RRC/CREATCOM_Print_Friendly.pdf"),
]

for url, filename in url_filename_pairs:
    try:
        pdfkit.from_url(url, filename, configuration=config)
    except Exception as e:
        print(f"Error-{url}-{e}")
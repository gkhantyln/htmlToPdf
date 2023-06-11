import pdfkit
import glob
import os

# Giriş ve çıkış klasörlerini tanımla
giris_klasoru = 'html_files'
cikis_klasoru = 'pdf_files'

# PDF seçeneklerini belirle
pdf_secenekleri = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

# 'pdfler' klasörünü oluştur
os.makedirs(cikis_klasoru, exist_ok=True)

# 'sinavlar' klasöründeki tüm HTML dosyalarını al
html_dosyalari = glob.glob(os.path.join(giris_klasoru, '*.html'))

# Yapılandırma nesnesini oluştur
pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

# Her HTML dosyasını PDF'ye dönüştür ve 'pdfler' klasörüne kaydet
for html_dosyasi in html_dosyalari:
    dosya_adi = os.path.basename(html_dosyasi)
    cikis_dosyasi = os.path.join(cikis_klasoru, f'{dosya_adi}.pdf')
    pdfkit.from_file(html_dosyasi, cikis_dosyasi, options=pdf_secenekleri, configuration=pdfkit_config)
    print(f'{dosya_adi} dosyasi PDF\'ye dönüştürüldü ve kaydedildi.')

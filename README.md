# İHA Üretim ve Montaj Uygulaması

Bu proje, İHA (İnsansız Hava Aracı) üretim sürecini yönetmek için bir web uygulamasıdır. Uygulama, parçaların üretiminden montajına kadar tüm süreçleri takip etmeyi ve kullanıcıların takımlara göre çalışma düzenini sağlamayı amaçlamaktadır.

## **Özellikler**
- Kullanıcı kaydı ve giriş sistemi
- Kullanıcıların bir takıma atanması
- Takımların sadece kendi parçalarını üretme yetkisi
- Montaj takımının eksiksiz parçalarla uçak üretmesi
- Envanter yönetimi ve eksik parça kontrolü
- CRUD işlemleri (oluşturma, listeleme, güncelleme, silme)

---

## **Teknolojiler**
- **Python**: Backend geliştirme
- **Django**: Web framework
- **PostgreSQL**: Veritabanı
- **HTML/CSS**: Basit bir frontend tasarımı
- **Django Admin**: Yönetim paneli

---

## **Kurulum**

### **1. Gerekli Yazılımlar**
- Python 3.x
- PostgreSQL
- Django
- Virtualenv (opsiyonel)

### **2. Adımlar**
1. Projeyi klonlayın:
   ```bash
   git clone <REPO_URL>
   cd myproject
Virtual environment oluşturun ve etkinleştirin:
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt
Veritabanı ayarlarını güncelleyin: settings.py içinde aşağıdaki bölümü ayarlayın:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'iha_db',
        'USER': 'postgres',
        'PASSWORD': 'erkan',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Migration işlemlerini yapın:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Uygulamayı tarayıcıdan ziyaret edin:

http://127.0.0.1:8000



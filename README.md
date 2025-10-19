# Random Password Generator

Bu proje, kullanıcı dostu bir grafik arayüz (GUI) üzerinden rastgele şifre üreten ve tek tıklamayla kopyalama imkânı sunan bir Python uygulamasıdır.

## Özellikler
- Her çalıştırıldığında 10 adet sayıdan oluşan rastgele bir şifre üretir.
- "Parola Oluştur" düğmesine tıklandığında, NumPy kütüphanesiyle rastgele sayılardan oluşan 10 haneli bir şifre üretilir.
- "Kopyala" düğmesine tıklayarak şifre otomatik olarak panoya (clipboard) kopyalanır.
- Kullanıcı dostu, sade bir arayüz ile kolay kullanım sağlar.
- Uygulamanın yükseklik ve genişliği sabittir.

## Gereksinimler
- Python 3.x
- PyQt5 kütüphanesi - Arayüz (GUI) oluşturma
- NumPy kütüphanesi - Rastgele sayı üretimi

## Kullanım
1. Gerekli kütüphaneleri yükle:

   ```bash
   pip install PyQt5 numpy
   ```
2. Script’i çalıştır:

   ```bash
   python password_generator.py
   ```
3. “Parola Oluştur” düğmesine tıkla → rastgele bir parola üretilecek.
4. “Kopyala” düğmesine tıklayarak şifreyi panoya al.

## Notlar
* Şifreler tamamen rastgele oluşturulur ve güvenlik amaçlı kullanılabilir.
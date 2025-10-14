# Random Password Generator

Bu proje, her 3 saniyede bir rastgele şifreler oluşturan basit bir Python scriptidir.

## Özellikler
- Her çalıştırıldığında 10 adet sayıdan oluşan rastgele bir şifre üretir.
- Üretilen şifreler konsola yazdırılır.
- Script sürekli çalışır ve her 3 saniyede bir yeni şifre üretir.

## Gereksinimler
- Python 3.x
- NumPy kütüphanesi (`pip install numpy`)

## Kullanım
```bash
python password_generator.py
````

Çalıştırdığınızda, her 3 saniyede bir yeni şifre konsola yazdırılacaktır:

```
[[79878   786  4215 27458 84199  7220  1443 31632 99148 48209]]
1- Password Created : 798787864215274588419972201443316329914848209
[[ 5942 38804 52245 46519 25390 79983 71441 64965 88418 27869]]
2- Password Created : 5942388045224546519253907998371441649658841827869
[[  121 27764 63748 51636 13922 32796 74447 35125 61693  3944]]
3- Password Created : 12127764637485163613922327967444735125616933944
...
```

## Notlar

* Script sonsuz döngüde çalıştığı için durdurmak için `Ctrl + C` kullanın.
* Şifreler tamamen rastgele oluşturulur ve güvenlik amaçlı kullanılabilir.
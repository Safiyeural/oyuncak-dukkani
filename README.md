# Oyuncak Dükkanı Stok ve Satış Takip Programı

Python ile yazılmış, konsol tabanlı oyuncak dükkanı stok ve satış takip programıdır. Veriler JSON dosyasında saklandığı için program kapatılıp açılsa bile kayıtlar korunur.

## Özellikler

- **Ekleme:** Yeni oyuncak ekler veya mevcut oyuncağın stoğunu artırır.
- **Silme:** Belirtilen oyuncaktan istenen adedi düşer, stok sıfırlanırsa ürünü listeden kaldırır.
- **Arama:** İsmi girilen oyuncağın stok ve fiyat bilgisini gösterir.
- **Güncelleme:** Kayıtlı oyuncağın stok ve fiyatını değiştirir (stok 0 girilirse ürün silinir).
- **Listeleme:** Tüm oyuncakları ekrana yazdırır ve `oyuncak_dukkani.txt` dosyasına aktarır.
- **Fiyatlar:** Fiyat tarifesini ekrana yazdırır ve `fiyatlar.txt` dosyasına aktarır.
- **Satış yap:** Birden fazla ürünlü satış yapar, stoktan düşer, toplam kazancı hesaplar ve `satis_gecmisi.txt` dosyasına tarih ve saatle kaydeder.
- **Satılanlar:** Geçmiş satış kayıtlarını gösterir.
- **Kalanlar:** Toplam stok miktarını gösterir, stoğu 3 ve altına düşen ürünler için kritik stok uyarısı verir.

## Kullanılan Teknolojiler ve Kavramlar

- Python 3 (ek kütüphane gerekmez, yalnızca standart kütüphaneler kullanılır)
- JSON ile kalıcı veri saklama (`json`, `os`)
- Tarih ve saat damgalı kayıt tutma (`datetime`)
- Dosya okuma/yazma işlemleri
- Hata yakalama (`try/except`) ve kullanıcı girdisi doğrulama
- Fonksiyonlarla modüler yapı

## Kurulum ve Çalıştırma

Bilgisayarınızda Python 3 yüklü olmalıdır.

```bash
git clone https://github.com/Safiyeural/oyuncak-dukkani.git
cd oyuncak-dukkani
python oyuncak_dukkani.py
```

Program açıldığında menüden `1-10` arasında bir seçim yapılır.

## Veri Dosyaları

Program çalışırken aşağıdaki dosyaları otomatik oluşturur (`.gitignore` ile repoya dahil edilmez):

| Dosya | Açıklama |
| :--- | :--- |
| `oyuncaklar.json` | Oyuncak envanteri (ana veri) |
| `satis_gecmisi.txt` | Satış kayıtları |
| `fiyatlar.txt` | Fiyat tarifesi çıktısı |
| `oyuncak_dukkani.txt` | Oyuncak listesi çıktısı |

## Notlar

- Oyuncak isimleri küçük harfe çevrilerek saklanır (`Lego` ve `lego` aynı ürün sayılır).
- Stoğu sıfırlanan ürünler listeden silinir, tekrar eklenirken fiyat yeniden girilir.

## Geliştirme Fikirleri

- SQLite veritabanına geçiş
- Birim testler (`unittest`)
- Sınıflar (OOP) ile yeniden yapılandırma
- Grafik arayüz (Tkinter veya PyQt)
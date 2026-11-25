import json
import os
from datetime import datetime

# Verilerin kalıcı olarak saklanacağı JSON dosyasının adı
DOSYA_ADI = "oyuncaklar.json"

def verileri_yukle():
    """Program başlangıcında kayıtlı JSON dosyası varsa oyuncak listesi verilerini yükler."""
    if os.path.exists(DOSYA_ADI):
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as f:
                veriler = json.load(f)
        except json.JSONDecodeError:
            # Bozuk dosyayı silmeden yedekle, boş listeyle devam et
            os.replace(DOSYA_ADI, "oyuncaklar_bozuk.json")
            print("Uyarı: oyuncaklar.json okunamadı, oyuncaklar_bozuk.json olarak yedeklendi. Boş listeyle başlanıyor.")
            return {}

        # Stok miktarı sıfır olan ürünleri listeye dahil etme
        veriler = {
            isim: bilgi
            for isim, bilgi in veriler.items()
            if bilgi.get("adet", 0) > 0
        }
        return veriler

    return {}

def verileri_kaydet():
    """Güncel oyuncak listesi sözlüğünü Türkçe karakterleri koruyarak JSON dosyasına kaydeder."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(oyuncaklar, f, ensure_ascii=False, indent=4)

oyuncaklar = {}

def ekleme():
    """Oyuncak listesine yeni oyuncak ekler veya mevcut oyuncağın stoğunu artırır."""

    isim = input("Eklemek istediğiniz oyuncak ismini giriniz: ").strip().lower()

    if isim == "":
        print("Oyuncak ismi boş bırakılamaz.")
        return

    while True:
        try:
            adet = int(input("Eklemek istediğiniz adeti giriniz: "))

            if adet <= 0:
                print("\nAdet sıfırdan büyük olmalıdır. Tekrar giriniz.\n")
                continue

            break

        except ValueError:
            print("\nLütfen geçerli bir sayı giriniz.\n")

    if isim in oyuncaklar:
        oyuncaklar[isim]["adet"] += adet
        print(f"\n{isim.capitalize()} oyuncağının stoğu {adet} adet artırıldı.")

    else:
        while True:
            try:
                fiyat = float(input("Oyuncak fiyatını giriniz: "))

                if fiyat <= 0:
                    print("\nFiyat sıfırdan büyük olmalıdır. Tekrar giriniz.\n")
                    continue

                break

            except ValueError:
                print("\nLütfen geçerli bir fiyat giriniz.\n")

        oyuncaklar[isim] = {
            "adet": adet,
            "fiyat": fiyat
        }

        print(f"\n{isim.capitalize()} oyuncağı başarıyla eklendi.")

    print("\nGüncel oyuncak bilgisi:")
    print(f"Adet: {oyuncaklar[isim]['adet']}, Fiyat: {oyuncaklar[isim]['fiyat']} TL")

    verileri_kaydet()

    print("\nİşlem başarıyla tamamlandı!")

def silme():
    """Belirtilen oyuncaktan istenilen adedi düşer."""

    isim = input("Silinmesini istediğiniz oyuncağın ismini giriniz: ").strip().lower()

    if isim not in oyuncaklar:
        print("Silinmesi istenen oyuncak bulunamadı.")
        return

    try:
        adet = int(input("Silinmesini istediğiniz adeti giriniz: "))

        if adet <= 0:
            print("Silinecek adet sıfırdan büyük olmalıdır.")
            return

        if adet > oyuncaklar[isim]["adet"]:
            print("Silinmesi istenilen adet karşılanamadı, yetersiz stok.")
            return

    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        return

    oyuncaklar[isim]["adet"] -= adet
    print(f"{isim.capitalize()} oyuncağından {adet} adet silinmiştir.")

    if oyuncaklar[isim]["adet"] == 0:
        del oyuncaklar[isim]
        print("Ürün stok sıfırlandığı için oyuncak listesinden silindi.")

    else:
        print(f"Yeni stok bilgisi - Adet: {oyuncaklar[isim]['adet']}, Fiyat: {oyuncaklar[isim]['fiyat']} TL")

    verileri_kaydet()

def arama():
    """İsmi girilen oyuncağın stok ve fiyat bilgilerini sorgular."""
    isim = input("Aradığınız oyuncağın ismini giriniz: ").strip().lower()
    if isim not in oyuncaklar:
        print("Kayıtlı böyle bir oyuncak yoktur.")
    else:
        print(f"{isim.capitalize()} - Adet: {oyuncaklar[isim]['adet']}, Fiyat: {oyuncaklar[isim]['fiyat']} TL")

def guncelleme():
    """Kayıtlı bir oyuncağın stok miktarını ve birim fiyatını günceller."""

    isim = input("Güncellemek istediğiniz oyuncak ismini giriniz: ").strip().lower()

    if isim not in oyuncaklar:
        print("Böyle bir oyuncak bulunmamaktadır.")
        return

    try:
        adet = int(input("Güncel stok miktarını giriniz: "))
        fiyat = float(input("Güncel fiyatı giriniz: "))

        if adet < 0 or fiyat <= 0:
            print("Stok sıfırdan küçük, fiyat ise sıfırdan büyük olmalıdır.")
            return

    except ValueError:
        print("Lütfen geçerli sayılar giriniz.")
        return

    # Stok 0 girilirse silme fonksiyonundaki gibi ürün listeden kaldırılır
    if adet == 0:
        del oyuncaklar[isim]
        verileri_kaydet()
        print("Ürün stok sıfırlandığı için oyuncak listesinden silindi.")
        return

    oyuncaklar[isim] = {
        "adet": adet,
        "fiyat": fiyat
    }

    verileri_kaydet()

    print("Oyuncak bilgileri güncellendi.")
    print(f"Adet: {oyuncaklar[isim]['adet']}, Fiyat: {oyuncaklar[isim]['fiyat']} TL")



def listeleme():
    """Tüm oyuncak listesini oyuncak_dukkani.txt dosyasına aktarır ve konsolda listeler."""
    print("OYUNCAK LİSTESİ")
    if not oyuncaklar:
        print("Oyuncak listesinde kayıtlı oyuncak bulunmamaktadır.")
        return

    with open("oyuncak_dukkani.txt", "w", encoding="utf-8") as dosya:
        for isim, bilgi in oyuncaklar.items():
            dosya.write(f"{isim},{bilgi['adet']},{bilgi['fiyat']}\n")

    for isim, bilgi in oyuncaklar.items():
        print(f"{isim.capitalize()}: {bilgi['adet']} adet, {bilgi['fiyat']} TL")


def fiyatlar():
    """Ürünlerin fiyat tarifesini fiyatlar.txt dosyasına yazar ve ekrana bastırır."""
    if not oyuncaklar:
        print("Listelenecek oyuncak bulunmamaktadır.")
        return

    with open("fiyatlar.txt", "w", encoding="utf-8") as f:
        for isim, bilgi in oyuncaklar.items():
            f.write(f"{isim}:{bilgi['fiyat']}TL\n")

    print("OYUNCAK FİYATLARI")

    for isim, bilgi in oyuncaklar.items():
        print(f"{isim.capitalize()}: {bilgi['fiyat']} TL")


def satis_yap():
    """Müşteri satış işlemini yürütür, stoktan düşer ve kazancı hesaplar."""

    toplam_satilan_adet = 0
    devam = True
    satilan_oyuncak = []
    satilan_oyuncak_adedi = []

    toplam_kazanc = 0

    while devam:

        isim = input("Satılacak oyuncak ismini giriniz: ").strip().lower()

        if isim in oyuncaklar:

            try:
                adet = int(input("Kaç adet satmak istiyorsunuz: "))

                if adet <= 0:
                    print("Satış adedi sıfırdan büyük olmalıdır.")

                elif adet <= oyuncaklar[isim]["adet"]:

                    fiyat = oyuncaklar[isim]["fiyat"]

                    print(f"{isim.capitalize()} {adet} tane satıldı.")

                    satilan_oyuncak.append(isim.capitalize())
                    satilan_oyuncak_adedi.append(adet)

                    oyuncaklar[isim]["adet"] -= adet

                    toplam_satilan_adet += adet
                    toplam_kazanc += adet * fiyat

                    if oyuncaklar[isim]["adet"] == 0:
                        del oyuncaklar[isim]

                else:
                    print("Mevcut oyuncak adetimiz yeterli değil!")

            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")

        else:
            print("Böyle bir oyuncağımız yok.")

        while True:
            tercih = input("Başka bir oyuncak satılacak mı? (E/H): ").strip().upper()
            if tercih == "E":
                break
            elif tercih == "H":
                devam = False
                break
            else:
                print("Lütfen geçerli bir cevap giriniz (E veya H).")

    print("Satılan oyuncak isimleri:", ", ".join(satilan_oyuncak) if satilan_oyuncak else "Yok")
    print("Satılan oyuncak adetleri:", satilan_oyuncak_adedi)
    print("Toplam satılan oyuncak adedi:", toplam_satilan_adet)
    print("Toplam kazanç:", round(toplam_kazanc, 2), "TL")

    verileri_kaydet()

    if satilan_oyuncak:

        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("satis_gecmisi.txt", "a", encoding="utf-8") as dosya:
            dosya.write(
                f"[{zaman}] Satılanlar: {satilan_oyuncak} | "
                f"Adetler: {satilan_oyuncak_adedi} | "
                f"Kazanç: {round(toplam_kazanc, 2)} TL\n"
            )

def satilanlar():
    """Geçmiş satış kayıtlarını ekrana yazdırır."""
    print("SATILAN OYUNCAKLAR GEÇMİŞİ")
    if os.path.exists("satis_gecmisi.txt"):
        with open("satis_gecmisi.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            if icerik.strip() == "":
                print("Henüz satış yapılmamıştır.")
            else:
                print(icerik.strip())
    else:
        print("Henüz satış yapılmamıştır.")


def kalanlar():
    """Oyuncak listesindeki toplam oyuncak miktarını ve kritik stokları gösterir."""
    kalan_oyuncak_adedi = 0
    if not oyuncaklar:
        print("Oyuncak listesinde kayıtlı oyuncak bulunmamaktadır.")
        return

    for isim in oyuncaklar:
        adet = oyuncaklar[isim]["adet"]
        kalan_oyuncak_adedi += adet
        print(f"{isim.capitalize()} {adet} adet var")
        # Kritik stok eşiği kontrolü
        if adet <= 3:
            print(f"   [UYARI] {isim.capitalize()} stoğu kritik seviyede!")

    print("Kalan oyuncak adedi:", kalan_oyuncak_adedi)


def temel_kontrol():
    """Ana uygulama menüsünü çalıştırır ve kullanıcı seçimlerini yönetir."""
    while True:
        print("1-Ekleme")
        print("2-Silme")
        print("3-Arama")
        print("4-Güncelleme")
        print("5-Listeleme")
        print("6-Fiyatlar")
        print("7-Satış yap")
        print("8-Satılanlar")
        print("9-Kalanlar")
        print("10-Çıkış")
        try:
            secim = int(input("Seçiminizi yapınız (1 ile 10 arasında): "))
        except ValueError:
            print("Lütfen 1 ile 10 arasında geçerli bir sayı giriniz!\n")
            continue

        if secim == 1:
            ekleme()
        elif secim == 2:
            silme()
        elif secim == 3:
            arama()
        elif secim == 4:
            guncelleme()
        elif secim == 5:
            listeleme()
        elif secim == 6:
            fiyatlar()
        elif secim == 7:
            satis_yap()
        elif secim == 8:
            satilanlar()
        elif secim == 9:
            kalanlar()
        elif secim == 10:
            print("Çıkış yapıldı!!!")
            break
        else:
            print("Hatalı seçim yaptınız!")

        print()

if __name__ == "__main__":
    temel_kontrol()

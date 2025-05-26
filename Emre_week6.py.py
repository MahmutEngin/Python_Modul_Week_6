from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# 🔹 Özel tarih kelimeleri sözlüğü
OZEL_TARIH_KELIMELERI = {
    "bugün": datetime.now().date(),
    "yarın": datetime.now().date() + timedelta(days=1),
    "gelecek hafta": datetime.now().date() + timedelta(days=7)
}

# 🔹 Soyut Görev Sınıfı
class Gorev(ABC):
    def __init__(self, gorev_id, ad, teslim_tarihi, oncelik="Düşük", durum="Bekliyor"):
        self.gorev_id = gorev_id
        self.ad = ad
        self.teslim_tarihi = self.tarih_donustur(teslim_tarihi)
        self.oncelik = oncelik
        self.durum = durum
        self.renk = None

    def kac_gun_kaldi(self):
        return (self.teslim_tarihi - datetime.now().date()).days

    def tarih_donustur(self, tarih_str):
        if tarih_str in OZEL_TARIH_KELIMELERI:
            return OZEL_TARIH_KELIMELERI[tarih_str]
        return datetime.strptime(tarih_str, "%Y-%m-%d").date()

    @abstractmethod
    def rengini_belirle(self):
        pass

# 🔹 Kişisel Görev Sınıfı
class KisiselGorev(Gorev):
    def __init__(self, gorev_id, ad, teslim_tarihi):
        super().__init__(gorev_id, ad, teslim_tarihi, oncelik="Düşük")

    def rengini_belirle(self):
        self.renk = "Yeşil"

# 🔹 İş Görevi Sınıfı
class IsGorevi(Gorev):
    def __init__(self, gorev_id, ad, teslim_tarihi):
        super().__init__(gorev_id, ad, teslim_tarihi, oncelik="Yüksek")

    def rengini_belirle(self):
        self.renk = "Kırmızı"

# 🔹 Görev Yöneticisi Sınıfı
class GorevYoneticisi:
    def __init__(self):
        self.gorevler = []
        self.sonraki_id = 1

    def gorev_ekle(self, tur, ad, teslim_tarihi):
        if tur == "kisisel":
            gorev = KisiselGorev(self.sonraki_id, ad, teslim_tarihi)
        elif tur == "is":
            gorev = IsGorevi(self.sonraki_id, ad, teslim_tarihi)
        else:
            print("Geçersiz görev türü.")
            return
        gorev.rengini_belirle()
        self.gorevler.append(gorev)
        print(f"Görev eklendi: {gorev.ad} (ID: {gorev.gorev_id})")
        self.sonraki_id += 1

    def gorevleri_listele(self):
        if not self.gorevler:
            print("Henüz görev eklenmedi.")
        for gorev in self.gorevler:
            print(f"ID: {gorev.gorev_id} | Ad: {gorev.ad} | Durum: {gorev.durum} | "
                  f"Teslim: {gorev.teslim_tarihi} | Öncelik: {gorev.oncelik} | Renk: {gorev.renk}")

# 🔹 Görev Düzenleyici Sınıfı
class GorevDuzenleyici:
    def __init__(self, yonetici: GorevYoneticisi):
        self.yonetici = yonetici

    def guncelle(self, gorev_id, durum=None, oncelik=None, teslim_tarihi=None):
        gorev = self.gorev_bul(gorev_id)
        if durum:
            gorev.durum = durum
        if oncelik:
            gorev.oncelik = oncelik
        if teslim_tarihi:
            gorev.teslim_tarihi = gorev.tarih_donustur(teslim_tarihi)
        print(f"Görev güncellendi: {gorev.ad}")

    def gorev_bul(self, gorev_id):
        for gorev in self.yonetici.gorevler:
            if gorev.gorev_id == gorev_id:
                return gorev
        print("Görev bulunamadı.")
        return None

# 🔹 Görev İzleyici Sınıfı
class GorevIzleyici:
    def __init__(self, yonetici: GorevYoneticisi):
        self.yonetici = yonetici

    def takip_et(self, gorev_id):
        gorev = self.gorev_bul(gorev_id)
        if gorev:
            print(f"Ad: {gorev.ad} | Durum: {gorev.durum} | Kalan Gün: {gorev.kac_gun_kaldi()} | Renk: {gorev.renk}")

    def gorev_bul(self, gorev_id):
        for gorev in self.yonetici.gorevler:
            if gorev.gorev_id == gorev_id:
                return gorev
        print("Görev bulunamadı.")
        return None

# 🔹 Örnek Kullanım
if __name__ == "__main__":
    yonetici = GorevYoneticisi()
    duzenleyici = GorevDuzenleyici(yonetici)
    izleyici = GorevIzleyici(yonetici)

    # Görev ekleme
    yonetici.gorev_ekle("kisisel", "Kitap oku", "yarın")
    yonetici.gorev_ekle("is", "Sunumu hazırla", "2025-06-02")

    # Görev listeleme
    yonetici.gorevleri_listele()

    # Görev güncelleme
    duzenleyici.guncelle(1, durum="Tamamlandı", oncelik="Orta")

    # Görev izleme
    izleyici.takip_et(1)
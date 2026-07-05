# Sosyal Medya İçerik Ajansı — Proje Planı

> **Başlangıç:**  
> **Hedef bitiş:**  
> **Durum:** Faz 2 — devam ediyor

Bu dosya projenin ana planıdır. Her faz tamamlandıkça `[x]` işaretlenir.

Proje dokümantasyonu → [`docs/`](./docs/)  
Yaptıkça yazdığımız notlar → [`docs/calisma-notlari/`](./docs/calisma-notlari/)

---

## Timeline Özeti

| Faz | Konu | Başlangıç | Bitiş | Süre |
|-----|------|-----------|-------|------|
| 0 | Proje ön dokümantasyonu | 30 Haz 2026 | 30 Haz 2026 | 1 gün |
| 1 | Docker + local n8n kurulumu | 30 Haz 2026 | 30 Haz 2026 | 1 gün |
| 2 | Workflow 1 — Manuel içerik üretme | | | |
| 3 | Data Table + Telegram bildirimi | | | |
| 4 | Workflow 2 — Kaynaktan içerik üretme | | | |
| 5 | Error handling + retry / fallback | | | |
| 6 | Final dokümantasyon | | | |

---

## Faz 0 — Proje Ön Dokümantasyonu

**Başlangıç:**  
**Bitiş:**  
**Amaç:** Proje planı, araştırma, kapsam ve akış şemasını hazırlamak.

### Yapılacaklar

- [x] Proje araştırması ve teknoloji seçimi
- [x] Proje dokümantasyonu → `docs/`
- [x] Genel akış şeması (Mermaid)
- [x] Faz bazlı proje planı → bu dosya

### Çıktılar

- `docs/` altındaki dokümantasyon dosyaları
- `proje-plani.md`

---

## Faz 1 — Docker + Local n8n Kurulumu

**Başlangıç:**  
**Bitiş:**  
**Amaç:** n8n'i Docker ile local ortamda çalışır hale getirmek.

### Yapılacaklar

- [x] `docker compose up -d` ile n8n'i ayağa kaldır
- [x] http://localhost:5678 üzerinden arayüze erişimi doğrula
- [x] `.env` dosyasında n8n şifresini ayarla
- [x] Kurulum notlarını dokümante et → `docs/calisma-notlari/n8n-kurulum.md`

### Çıktılar

- Çalışan local n8n instance
- `docs/calisma-notlari/n8n-kurulum.md`

---

## Faz 2 — Workflow 1: Manuel İçerik Üretme

**Başlangıç:**  
**Bitiş:**  
**Amaç:** Kullanıcının girdiği konuya göre AI ile sosyal medya içeriği üreten ilk workflow.

### Yapılacaklar

- [x] Platform seçimi kesinleştir → **LinkedIn** ve **Instagram**
- [ ] İçerik türlerini belirle
- [ ] AI prompt tasarımı
- [ ] n8n workflow kur: Manual Trigger → Set Node → AI Agent → Structured Output
- [ ] Workflow test et (örnek konu ile)
- [ ] Workflow JSON export al

### Akış

```
Manual Trigger → Set Node → AI Agent → Structured Output
```

### Çıktılar

- Çalışan Workflow 1
- Prompt dosyası
- Test çıktısı ekran görüntüsü

---

## Faz 3 — Data Table + Telegram Bildirimi

**Başlangıç:**  
**Bitiş:**  
**Amaç:** Üretilen içerikleri kaydetmek ve Telegram'a taslak göndermek.

### Yapılacaklar

- [ ] `social_media_contents` Data Table oluştur
- [ ] Status alanlarını tanımla (draft, waiting_approval, approved, rejected, scheduled, published, failed)
- [ ] Workflow 1'e Data Table kayıt node'u ekle
- [ ] Telegram bot oluştur ve kanala bağla
- [ ] Taslak bildirim mesaj şablonu hazırla
- [ ] Onay süreci — ilk aşama: manuel Telegram kontrolü
- [ ] End-to-end test: konu gir → içerik üret → kaydet → Telegram'a gönder

### Akış (Workflow 1 genişletilmiş)

```
Manual Trigger → Set Node → AI Agent → Structured Output → Data Table → Telegram
```

### Çıktılar

- Data Table yapısı
- Telegram bildirim sistemi
- Ekran görüntüleri

---

## Faz 4 — Workflow 2: Kaynaktan İçerik Üretme

**Başlangıç:**  
**Bitiş:**  
**Amaç:** RSS / HTTP kaynaklarından otomatik içerik çekip AI ile dönüştürmek.

### Yapılacaklar

- [ ] İçerik kaynaklarını belirle (en az 1 RSS)
- [ ] Schedule Trigger ile periyodik çalıştırma ayarla
- [ ] RSS Feed / HTTP Request node kur
- [ ] Veri temizleme adımı ekle
- [ ] Duplicate kontrolü (URL + title)
- [ ] AI agent ile sınıflandırma ve içerik üretimi
- [ ] Data Table kaydı + Telegram bildirimi
- [ ] Workflow test et

### Akış

```
Schedule Trigger → RSS/HTTP → Veri Temizleme → Duplicate Kontrolü → AI Agent → Data Table → Telegram
```

### Çıktılar

- Çalışan Workflow 2
- Kaynak listesi
- Duplicate kontrol mekanizması

---

## Faz 5 — Error Handling + Retry / Fallback

**Başlangıç:**  
**Bitiş:**  
**Amaç:** Hataları yakalamak, loglamak ve workflow'un tamamen durmasını engellemek.

### Yapılacaklar

- [ ] Error Trigger workflow oluştur
- [ ] `social_media_errors` Data Table oluştur
- [ ] Telegram error kanalına bildirim gönder
- [ ] `social_media_execution_logs` tablosu ile loglama ekle
- [ ] Retry senaryoları: API timeout, Telegram fail, AI bozuk çıktı
- [ ] Fallback senaryoları: yedek kaynak, basit template, telegram_failed status
- [ ] Tüm workflow'lara error workflow bağla

### Çıktılar

- Error handling workflow
- Log tabloları
- Retry / fallback dokümantasyonu

---

## Faz 6 — Final Dokümantasyon

**Başlangıç:**  
**Bitiş:**  
**Amaç:** Projeyi kapatmak, öğrenilenleri ve karşılaşılan problemleri dokümante etmek.

### Yapılacaklar

- [ ] Tüm workflow export'larını kaydet
- [ ] Karşılaşılan problemler ve çözüm notları yaz
- [ ] Öğrenilen kavramlar listesini güncelle
- [ ] Ekran görüntülerini toparla

### Beklenen Final Çıktılar

- [x] Docker ile local çalışan n8n
- [ ] Manuel içerik üretim workflow'u
- [ ] Kaynaktan içerik üretim workflow'u
- [ ] Error handling workflow'u
- [ ] Data Table yapıları
- [ ] Telegram bildirim sistemi
- [ ] En az 2 platform için içerik üretimi
- [ ] Duplicate kontrolü
- [ ] Retry / fallback senaryosu
- [ ] Proje dokümantasyonu + akış şeması

---

## İlerleme Takibi

| Faz | Durum | Tamamlanma |
|-----|-------|------------|
| 0 — Ön dokümantasyon | Tamamlandı | |
| 1 — n8n kurulumu | Tamamlandı | |
| 2 — Workflow 1 | Devam ediyor | |
| 3 — Data Table + Telegram | Bekliyor | |
| 4 — Workflow 2 | Bekliyor | |
| 5 — Error handling | Bekliyor | |
| 6 — Final dokümantasyon | Bekliyor | |

---

## Notlar

- **Platform seçimi:** LinkedIn ve Instagram
- Brand voice, içerik takvimi, multi-agent vb. özellikler ilk versiyon sonrasında eklenebilir → [`docs/proje-amaci.md`](./docs/proje-amaci.md#sonradan-eklenebilecek-özellikler)

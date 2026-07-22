# Sosyal Medya İçerik Ajansı — Proje Planı

> **Başlangıç:** 30 Haz 2026  
> **Bitiş:** Tem 2026 (onay + görsel + Buffer yayın dahil)  
> **Durum:** Tamamlandı  

Ana sistem özeti → [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md)  
Onay/görsel/yayın → [`docs/yol-haritasi-onay-gorsel-yayin.md`](./docs/yol-haritasi-onay-gorsel-yayin.md)

Bu dosya projenin ana planıdır. Her faz tamamlandıkça `[x]` işaretlenir.

Proje dokümantasyonu → [`docs/`](./docs/)  
Yaptıkça yazdığımız notlar → [`docs/calisma-notlari/`](./docs/calisma-notlari/)

---

## Timeline Özeti

| Faz | Konu | Başlangıç | Bitiş | Süre |
| --- | ---- | --------- | ----- | ---- |
| 0 | Proje ön dokümantasyonu | 30 Haz 2026 | 30 Haz 2026 | 1 gün |
| 1 | Docker + local n8n kurulumu | 30 Haz 2026 | 30 Haz 2026 | 1 gün |
| 2 | Workflow 1 — Manuel içerik üretme | | | |
| 3 | Data Table + Telegram bildirimi | | | |
| 4 | Workflow 2 — Kaynaktan içerik üretme | | | |
| 5 | Error handling + retry / fallback | | 20 Tem 2026 | |
| 6 | Final dokümantasyon | | Tem 2026 | |
| A–D | Telegram onay + görsel + Buffer yayın (WF-04) | | Tem 2026 | |

---

## Faz 0 — Proje Ön Dokümantasyonu

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

**Amaç:** Kullanıcının girdiği konuya göre AI ile sosyal medya içeriği üreten ilk workflow.

### Yapılacaklar

- [x] Platform seçimi kesinleştir → **LinkedIn** ve **Instagram**
- [x] İçerik türlerini belirle → eğitici, duyuru, ürün tanıtımı, problem/çözüm
- [x] AI prompt tasarımı → `prompts/manuel-icerik-prompt.md`
- [x] n8n workflow kur: Manual Trigger → Set Node → AI Agent → Structured Output
- [x] Workflow test et (örnek konu ile)
- [x] Workflow JSON export al → `WF-01 Manuel İçerik Üretme.json`

### Akış

```
Manual Trigger → Set → AI Agent → Code → Data Table → Telegram
```

### Çıktılar

- Çalışan Workflow 1
- Prompt dosyası
- Test çıktısı ekran görüntüsü

---

## Faz 3 — Data Table + Telegram Bildirimi

**Amaç:** Üretilen içerikleri kaydetmek ve Telegram'a taslak göndermek.

### Yapılacaklar

- [x] `social_media_contents` Data Table oluştur
- [x] Status alanlarını tanımla
- [x] Workflow 1'e Data Table kayıt node'u ekle
- [x] Telegram bot oluştur ve gruba bağla
- [x] Taslak bildirim mesaj şablonu → Code + `templates/telegram/taslak-mesaj.md`
- [x] Telegram test mesajı gönderildi
- [x] Onay süreci — ilk aşama: manuel Telegram kontrolü
- [x] End-to-end test

### Akış

```
Manual Trigger → Set → AI Agent → Code → Data Table → Telegram
```

---

## Faz 4 — Workflow 2: Kaynaktan İçerik Üretme

**Amaç:** RSS kaynaklarından otomatik içerik çekip AI ile dönüştürmek.

### Yapılacaklar

- [x] İçerik kaynaklarını belirle → **Webrazzi RSS**
- [x] Schedule Trigger ile periyodik çalıştırma
- [x] RSS Feed node kur
- [x] Veri temizleme adımı ekle
- [x] Duplicate kontrolü → `source_url` + If row doesn't exist
- [x] AI agent ile sınıflandırma ve içerik üretimi
- [x] Data Table kaydı + Telegram bildirimi
- [x] Workflow test et
- [x] Workflow export → `WF-02 Kaynaktan İçerik Üretme.json`

### Akış

```
Schedule Trigger (veya Manual) → RSS → Veri Temizle → Duplicate Kontrol → Limit → AI Agent → Code → Data Table → Telegram
```

---

## Faz 5 — Error Handling + Retry / Fallback

**Amaç:** Hataları yakalamak, loglamak; geçici hatalarda retry.

### Yapılacaklar

- [x] Error Trigger workflow oluştur → `WF-03 Error Handling`
- [x] `social_media_errors` Data Table oluştur
- [x] Telegram hata bildirimi
- [ ] `social_media_execution_logs` insert *(tablo var; kullanım sonraya)*
- [x] Retry senaryoları → node Retry On Fail (AI, Telegram, RSS)
- [ ] Ağır fallback (yedek kaynak, template) *(sonraya — error + retry yeterli)*
- [x] WF-01 / WF-02'ye error workflow bağla
- [x] Export → `WF-03 Error Handling.json`

### Akış

```
Error Trigger → Hata Mesaji (Code) → social_media_errors → Telegram
```

Detay → `docs/calisma-notlari/faz-5-error-handling.md`

---

## Faz 6 — Final Dokümantasyon

**Amaç:** Projeyi kapatmak, öğrenilenleri ve problemleri dokümante etmek.

### Yapılacaklar

- [x] Tüm workflow export'larını kaydet *(WF-04 güncel export kullanıcıda — repoya eklenebilir)*
- [x] Karşılaşılan problemler ve çözüm notları
- [x] Öğrenilen kavramlar / bilgiler listesini güncelle
- [x] Akış şeması güncelle
- [x] Ana sistem dokümanı → `docs/sistem-dokumantasyonu.md`
- [ ] Final ekran görüntüleri *(çekim listesi hazır — `docs/ekran-goruntuleri/README.md`; local n8n’den otomatik alınamadı)*

Detay → `docs/calisma-notlari/faz-6-final.md`

### Beklenen Final Çıktılar

- [x] Docker ile local çalışan n8n
- [x] Manuel içerik üretim workflow'u
- [x] Kaynaktan içerik üretim workflow'u
- [x] Error handling workflow'u
- [x] WF-04: 2 kademeli Telegram onay + görsel + Buffer yayın
- [x] Data Table yapıları (`contents` + `errors`; logs tablosu hazır)
- [x] Telegram bildirim / onay sistemi
- [x] En az 2 platform için içerik üretimi + yayın
- [x] Duplicate kontrolü
- [x] Retry senaryosu
- [x] Proje dokümantasyonu + akış şeması

---

## İlerleme Takibi

| Faz | Durum | Tamamlanma |
| --- | ----- | ---------- |
| 0 — Ön dokümantasyon | Tamamlandı | 30 Haz 2026 |
| 1 — n8n kurulumu | Tamamlandı | 30 Haz 2026 |
| 2 — Workflow 1 | Tamamlandı | | |
| 3 — Data Table + Telegram | Tamamlandı | | |
| 4 — Workflow 2 | Tamamlandı | | |
| 5 — Error handling | Tamamlandı | 20 Tem 2026 |
| 6 — Final dokümantasyon | Tamamlandı | Tem 2026 |
| A–D — Onay / görsel / Buffer (WF-04) | Tamamlandı | Tem 2026 |

---

## Notlar

- **Platform seçimi:** LinkedIn ve Instagram
- Brand voice, içerik takvimi, multi-agent vb. → [`docs/proje-amaci.md`](./docs/proje-amaci.md#sonradan-eklenebilecek-özellikler)
- **Sonraki aşama (tamamlandı):** Telegram 2 kademeli onay + Cloudinary görsel + Buffer LI/IG → [`docs/yol-haritasi-onay-gorsel-yayin.md`](./docs/yol-haritasi-onay-gorsel-yayin.md) · [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md)

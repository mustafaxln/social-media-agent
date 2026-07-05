# Proje Amacı

Belirlenen kaynaklardan sosyal medya içerik fikirleri üretmek ve AI agent ile platforma uygun sosyal medya formatına dönüştürmek.

## Problem

Sosyal medya içerik üretimi zaman alıcı ve tutarsız olabiliyor. Markalar ve ekipler:

- Güncel kaynaklardan içerik fikri bulmakta zorlanıyor
- Platform bazlı format farklarını (LinkedIn vs Instagram) manuel yönetiyor
- Üretilen içerikleri merkezi bir yerde takip edemiyor
- Onay süreci dağınık (WhatsApp, e-posta, not defteri)

## Çözüm

n8n tabanlı bir otomasyon sistemi kurarak:

1. Manuel veya otomatik kaynaklardan içerik fikri al
2. AI agent ile platforma uygun sosyal medya içeriği üret
3. Data Table'a kaydet ve durum takibi yap
4. Telegram üzerinden taslak gönder, onay sürecini başlat

## Somut Hedefler

- Manuel konu girişi ile en az 2 platform için (LinkedIn, Instagram) içerik üretmek
- RSS kaynaklarından otomatik içerik çekip dönüştürmek
- Üretilen içerikleri merkezi tabloda takip etmek
- Telegram üzerinden taslak gönderip onay sürecini başlatmak
- Hata durumlarında sistemin tamamen durmasını engellemek

## Seçilen Platformlar

**LinkedIn** ve **Instagram**

| Platform | Durum |
|----------|-------|
| LinkedIn | Seçildi |
| Instagram | Seçildi |

## İlk Versiyon Kapsamı

- Docker ile local n8n kurulumu
- 3 workflow (manuel, kaynak, error handling)
- n8n Data Table ile içerik ve log kaydı
- Telegram taslak bildirimi
- Manuel onay süreci (Telegram üzerinden kontrol)
- Duplicate kontrolü (URL + title)
- Retry ve fallback senaryoları

## Sonradan Eklenebilecek Özellikler

İlk versiyon tamamlandıktan sonra eklenebilecek gelişmiş özellikler:

- **İçerik takvimi** — haftalık plan, platform bazlı yayın günü önerisi
- **Rakip analizi** — rakip hesap analizi, hashtag analizi
- **Brand voice** — marka tonu, yasaklı kelimeler, emoji kuralları
- **Görsel brief üretimi** — carousel fikri, Canva brief, AI image prompt
- **İçeriği yeniden kullanma** — tek içerikten farklı platformlara adaptasyon
- **Multi-agent yapısı** — research, writer, editor, classification agent'ları
- **Gelişmiş onay mekanizması** — Telegram butonlu onay, n8n Form, Google Sheet

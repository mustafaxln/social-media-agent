# Sosyal Medya İçerik Ajansı

n8n + Docker + OpenAI + Telegram + Buffer ile LinkedIn / Instagram içerik üretimi, 2 kademeli onay, görsel ve otomatik yayın.

## Hızlı başlangıç

```bash
cp .env.example .env   # şifre + WEBHOOK_URL
docker compose up -d
# Telegram Trigger (local): cloudflared tunnel --url http://localhost:5678
```

n8n: http://localhost:5678 (`admin`)

## Sistem özeti

```
WF-01 / WF-02 → taslak + buton
    → WF-04: onay → görsel (Cloudinary) → final onay → Buffer → LI/IG
    → Hata: WF-03
```

Detay → [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md)

## Workflow’lar

| # | Ad | Export |
|---|-----|--------|
| 1 | Manuel İçerik | `WF-01 Manuel İçerik Üretme.json` |
| 2 | Kaynaktan İçerik (RSS + Schedule) | `WF-02 Kaynaktan İçerik Üretme.json` |
| 3 | Error Handling | `WF-03 Error Handling.json` |
| 4 | Onay + Görsel + Buffer Yayın | *(n8n’den export et → `WF-04 …json`)* |

## Dokümantasyon

| Dosya | İçerik |
|--------|--------|
| [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md) | **Ana sistem dokümanı** |
| [`proje-plani.md`](./proje-plani.md) | Faz planı |
| [`docs/yol-haritasi-onay-gorsel-yayin.md`](./docs/yol-haritasi-onay-gorsel-yayin.md) | Onay / görsel / yayın |
| [`docs/karsilasilan-problemler.md`](./docs/karsilasilan-problemler.md) | Problemler |
| [`docs/cozum-notlari.md`](./docs/cozum-notlari.md) | Çözümler |
| [`docs/README.md`](./docs/README.md) | Docs indeksi |

## Durum

**Tamamlandı** (Tem 2026): üretim, 2 kademeli Telegram onayı, Cloudinary görsel URL, Buffer ile LinkedIn/Instagram yayın, WF-03 error handling (WF-04 dahil).

# Sosyal Medya İçerik Ajansı

n8n + Docker + OpenAI + Telegram + Buffer: LinkedIn/Instagram içerik, `/yeni` ile manuel giriş, 2 kademeli onay, görsel, otomatik yayın.

## Hızlı başlangıç

```bash
cp .env.example .env   # şifre + WEBHOOK_URL
docker compose up -d
cloudflared tunnel --url http://localhost:5678
# .env WEBHOOK_URL=https://….trycloudflare.com/  sonra:
docker compose up -d
```

n8n: http://localhost:5678 (`admin`)

**Yeniden çalıştırma (detaylı):** [`docs/calisma-notlari/projeyi-yeniden-calistirma.md`](./docs/calisma-notlari/projeyi-yeniden-calistirma.md)

## Sistem özeti

```
DM /yeni → WF-04 → WF-01 → grup taslak
WF-02 RSS → grup taslak
    → WF-04: Onayla → görsel → Yayınla → Buffer LI/IG
    → Hata: WF-03
```

Ana doküman → [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md)

## Workflow’lar

| # | Ad | Not |
|---|-----|-----|
| 1 | Manuel İçerik | Execute Workflow; giriş = `/yeni` |
| 2 | Kaynaktan İçerik | RSS + Schedule |
| 3 | Error Handling | |
| 4 | Telegram Hub | `/yeni` + onay/görsel/yayın |

## Dokümantasyon

| Dosya | İçerik |
|--------|--------|
| [`docs/sistem-dokumantasyonu.md`](./docs/sistem-dokumantasyonu.md) | Ana sistem |
| [`docs/proje-final-ozeti.md`](./docs/proje-final-ozeti.md) | Yaptık / takıldık / çözdük |
| [`docs/karsilasilan-problemler.md`](./docs/karsilasilan-problemler.md) | Takıldıklarımız |
| [`docs/cozum-notlari.md`](./docs/cozum-notlari.md) | Çözümler |
| [`docs/calisma-notlari/telegram-yeni-komutu.md`](./docs/calisma-notlari/telegram-yeni-komutu.md) | `/yeni` |
| [`docs/README.md`](./docs/README.md) | Docs indeksi |

## Durum

**Final** (Tem 2026): `/yeni` DM, 2 kademeli onay, Cloudinary, Buffer, error handling, cold-start dokümanı.

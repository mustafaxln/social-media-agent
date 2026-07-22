# Kullanılacak Teknolojiler

## Stack (final)

| Teknoloji | Kullanım |
|-----------|----------|
| Docker & Docker Compose | Local n8n |
| n8n (self-hosted) | WF-01…04, Data Tables, AI Agent |
| OpenAI gpt-4o-mini | Metin içerik |
| OpenAI gpt-image-1-mini | Görsel (onay sonrası) |
| Cloudinary | Görsel URL (`secure_url`) |
| Buffer Free (GraphQL API) | LinkedIn + Instagram yayın |
| Telegram Bot API | Taslak, final onay, HATA |
| Webrazzi RSS | Kaynak feed |
| cloudflared | Local HTTPS webhook (Telegram Trigger) |

## Seçim gerekçeleri

| Teknoloji | Neden |
|-----------|-------|
| n8n | Görsel otomasyon, AI, Data Table |
| Docker | Taşınabilir local ortam |
| OpenAI | Metin + görsel aynı ekosistem |
| Cloudinary | ImgBB limit sorunu sonrası stabil URL |
| Buffer | LI+IG tek API; Free plan yeterli (3 kanal, 10 kuyruk/kanal) |
| Telegram | Hızlı human-in-the-loop onay |
| cloudflared | Telegram’ın HTTPS webhook zorunluluğu |

## Değerlendirilip seçilmeyen / değiştirilen

| Alternatif | Sonuç |
|------------|--------|
| ImgBB | Limit/internal error → Cloudinary |
| Native LinkedIn + IG Graph API | Buffer ile sadeleştirildi |
| Zapier / Make | Self-hosted n8n tercih |
| Tek onay + direkt yayın | 2 kademeli onay (görsel kontrolü) |

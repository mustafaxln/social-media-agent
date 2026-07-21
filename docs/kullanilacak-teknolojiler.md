# Kullanılacak Teknolojiler

## Kullanılanlar (ilk versiyon)

| Teknoloji | Kullanım |
|-----------|----------|
| Docker & Docker Compose | Local n8n (`docker-compose.yml`) |
| n8n (self-hosted) | 3 workflow, Data Tables, AI Agent |
| OpenAI (`gpt-4o-mini`) | İçerik üretimi (WF-01, WF-02) |
| n8n Data Tables | `social_media_contents`, `social_media_errors` (+ logs şeması) |
| Telegram Bot API | Taslak + HATA bildirimi (grup) |
| RSS Feed Read | Webrazzi — `https://webrazzi.com/feed` |

## Seçim gerekçeleri

| Teknoloji | Neden |
|-----------|-------|
| **n8n** | Görsel builder, AI agent, Data Table, self-hosted |
| **Docker** | Tek komut kurulum, Mac/Windows taşınabilirlik |
| **OpenAI** | Structured JSON, n8n credential ile kolay entegrasyon |
| **Data Tables** | Ekstra DB kurmadan kayıt + duplicate |
| **Telegram** | Hızlı mobil bildirim, manuel onay için yeterli |
| **Webrazzi RSS** | TR e-ticaret/teknoloji haberleri; tek kaynak yeterli |

## Değerlendirilen alternatifler

| Alternatif | Neden seçilmedi |
|------------|-----------------|
| Zapier / Make | Ücretli, AI esnekliği sınırlı |
| Custom Python | Görsel workflow yok, bakım pahalı |
| Anthropic (Claude) | OpenAI n8n'de hazır; gerekirse eklenebilir |
| Ayrı PostgreSQL | Data Table ilk versiyon için yeterli |

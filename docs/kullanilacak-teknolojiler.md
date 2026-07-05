# Kullanılacak Teknolojiler

- Docker & Docker Compose
- n8n (self-hosted)
- AI Agent / Chat Model (OpenAI, Anthropic vb.)
- n8n Data Tables
- Telegram Bot API
- RSS / HTTP Request

## Teknoloji Seçim Gerekçeleri

| Teknoloji | Neden Seçildi |
|-----------|---------------|
| **n8n** | Görsel workflow builder, AI agent desteği, Data Table, self-hosted |
| **Docker** | Tek komutla local kurulum, taşınabilir ortam |
| **AI Agent** | Structured output ile JSON formatında içerik üretimi |
| **n8n Data Tables** | Ekstra veritabanı kurmadan içerik ve log kaydı |
| **Telegram Bot API** | Hızlı taslak bildirimi, mobil onay kontrolü |

## Değerlendirilen Alternatifler

| Alternatif | Neden Seçilmedi |
|------------|-----------------|
| Zapier / Make | Ücretli, AI agent esnekliği sınırlı |
| Custom Python script | Görsel workflow yok, bakım maliyeti yüksek |
| Google Apps Script | AI entegrasyonu ve otomasyon sınırlı |

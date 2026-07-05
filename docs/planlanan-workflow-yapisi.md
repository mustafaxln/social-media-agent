# Planlanan Workflow Yapısı

| # | Workflow | Tetikleyici |
|---|----------|-------------|
| 1 | Manuel İçerik Üretme | Manual Trigger |
| 2 | Kaynaktan İçerik Üretme | Schedule Trigger |
| 3 | Error Handling | Error Trigger |

## Workflow 1 — Manuel İçerik Üretme

```
Manual Trigger → Set Node → AI Agent → Structured Output → Data Table → Telegram
```

**Set Node girdi örneği:**

```json
{
  "topic": "E-ticarette yapay zeka kullanımı",
  "platform": "LinkedIn",
  "target_audience": "E-ticaret markaları",
  "tone": "Profesyonel ve öğretici"
}
```

**AI çıktı alanları:** title, content, platform, category, target_audience, hashtags, visual_idea, cta, tone, impact_score

## Workflow 2 — Kaynaktan İçerik Üretme

```
Schedule Trigger → RSS/HTTP → Veri Temizleme → Duplicate Kontrolü → AI Agent → Data Table → Telegram
```

**Kaynaktan çekilecek alanlar:** title, description, url, published_at, source_name

## Workflow 3 — Error Handling

```
Error Trigger → Hata Bilgileri → Error Data Table → Telegram Error Kanalı
```

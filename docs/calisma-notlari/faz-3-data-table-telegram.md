# Faz 3 — Data Table + Telegram Notları

## Tamamlanan

- [x] Telegram bot + grup kurulumu
- [x] n8n Telegram credential
- [x] `social_media_contents` Data Table (11 sütun)
- [x] Code node ile mesaj oluşturma → `templates/telegram/taslak-mesaj.md`
- [x] Data Table Insert row eşleştirmesi
- [x] Telegram taslak bildirimi
- [x] End-to-end test başarılı

## Workflow akışı (final)

```
Manual Trigger → Set → AI Agent → Code → Data Table → Telegram
```

## Önemli notlar

- **Code node:** AI çıktısını düzleştirir, `telegram_message` üretir
- **Data Table:** `status` = `waiting_approval` ile kayıt
- **Telegram Text:** `{{ $('Code').item.json.telegram_message }}`  
  (Data Table sonrası `$json.telegram_message` undefined olur — Code node'dan oku)

## Data Table sütunları

title, content, platform, category, target_audience, hashtags, visual_idea, cta, tone, impact_score, status

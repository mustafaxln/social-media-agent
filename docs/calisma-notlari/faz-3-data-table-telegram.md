# Faz 3 — Data Table + Telegram Notları

**Durum:** Tamamlandı

## Tamamlanan

- [x] Telegram bot + **grup** kurulumu (kanal yerine — admin sorunu)
- [x] n8n Telegram credential
- [x] `social_media_contents` Data Table
- [x] Code node ile mesaj → `templates/telegram/taslak-mesaj.md`
- [x] Insert row eşleştirmesi
- [x] Telegram taslak bildirimi
- [x] End-to-end test

## Final akış

```
Manual Trigger → Set → AI Agent → Code (telegram_message) → Insert row → Telegram
```

## Data Table — social_media_contents

| Sütun | Tip | Not |
|-------|-----|-----|
| title, content, platform, category | string | AI'dan |
| target_audience, hashtags, visual_idea, cta, tone | string | AI'dan; hashtags join ile string |
| impact_score | **number** 1–5 | `/5` sadece Telegram metninde |
| status | string | sabit: `waiting_approval` |
| source_url | string | Faz 4'te eklendi (WF-02) |

## Önemli teknik notlar

1. **Code node** AI çıktısını düzleştirir (`output || item`) ve `telegram_message` üretir.
2. Telegram Text **Insert'ten sonra** `$json.telegram_message` olmaz → Code node adından oku.
3. Expression fx açıkken `={{ }}` kullanma → `{{ }}`.
4. Append n8n Attribution **kapalı**.
5. Bot: gruba ekli; Chat ID negatif grup ID.

## Bu fazda yaşananlar

| Sorun | Çözüm |
|-------|--------|
| Kanal admin | Grup kullanımı |
| Mesaj Insert sonrası kayıp | `$('Code').item.json.telegram_message` |
| impact_score | Number tip; gösterimde `/5` |

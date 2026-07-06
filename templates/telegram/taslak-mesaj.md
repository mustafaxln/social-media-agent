# Telegram Taslak Mesajı

## Workflow sırası

```
AI Agent → Code (Mesajı Oluştur) → Data Table → Telegram
```

## Code node — "Telegram Mesajı Oluştur"

Mode: **Run Once for All Items**

```javascript
const item = $input.first().json;
const d = item.output || item;

const hashtags = Array.isArray(d.hashtags)
  ? d.hashtags.join(' ')
  : String(d.hashtags || '');

const message = `Yeni Sosyal Medya Icerik Taslagi

Platform: ${d.platform || ''}
Kategori: ${d.category || ''}
Hedef Kitle: ${d.target_audience || ''}
Etki Skoru: ${d.impact_score || ''}/5

Baslik:
${d.title || ''}

Icerik:
${d.content || ''}

Hashtagler:
${hashtags}

Gorsel Fikri:
${d.visual_idea || ''}

CTA:
${d.cta || ''}

Durum: Onay bekliyor`;

return [{ json: { ...d, telegram_message: message } }];
```

## Telegram node

| Alan | Değer |
|------|-------|
| Chat ID | Grup ID (eksi ile) |
| Text | `{{ $('Code').item.json.telegram_message }}` |
| Parse Mode | None |
| Append n8n Attribution | Kapalı (isteğe bağlı) |

Text alanında **Expression açma** — düz metin modunda `{{ $json.telegram_message }}` yeterli.

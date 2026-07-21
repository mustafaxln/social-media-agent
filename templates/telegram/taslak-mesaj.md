# Telegram Taslak Mesajı

## Workflow sırası

```
AI Agent → Code → Data Table Insert → Telegram
```

Telegram Text her zaman **Code node** adından okunur (Insert sonrası `$json` mesajı taşımaz).

## WF-01 Code (örnek)

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

## WF-02 farkı

Kaynak satırı + `source_url` için Limit'ten oku:

```javascript
const source = $('Limit').first().json;
// mesaja: Kaynak: ${source.source_name} — ${source.url}
// return'a: source_url: source.url
```

Hashtag tire temizliği: `.replace(/-/g, '')`

## Telegram node

| Alan | Değer |
|------|--------|
| Chat ID | Grup ID (eksi ile) |
| Text | `{{ $('telegram mesaj').item.json.telegram_message }}` (node adına göre) |
| Append n8n Attribution | Kapalı |

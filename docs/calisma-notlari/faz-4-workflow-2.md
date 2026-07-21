# Faz 4 — Workflow 2: Kaynaktan İçerik Üretme

**Durum:** Tamamlandı

## Kararlar

| Alan | Seçim |
|------|-------|
| RSS kaynağı | Webrazzi — `https://webrazzi.com/feed` |
| Tetikleyici | Schedule Trigger (+ test için Manual bırakılabilir) |
| Duplicate | `source_url` — Data Table **If row doesn't exist** |
| AI prompt | `prompts/kaynaktan-icerik-prompt.md` |
| Model | gpt-4o-mini |

## Final akış

```
Schedule Trigger (ve/veya Manual) → RSS Read → Veri Temizle → Duplicate Kontrol → Limit (1)
  → AI Agent → telegram mesaj (Code) → Insert row → Telegram
```

> Limit, duplicate'den **sonra** olmalı. Aksi halde hep aynı (ilk) haber denenir.

## Code — kaynak URL

AI sonrası eşleşme bozulmasın diye Limit'ten al (Max Items = 1):

```javascript
const source = $('Limit').first().json;
```

`$('Veri Temizle').first()` kullanma — her zaman ilk RSS haberini verir.
## Duplicate kontrolü

Data Table node — **If row doesn't exist**

| Ayar | Değer |
|------|--------|
| Data table | `social_media_contents` |
| Match column | `source_url` |
| Value | `{{ $json.url }}` |

Get Row + IF yerine bu yöntem kullanıldı; input item korunur, ayrı IF gerekmez.

## Insert row

WF-01 mapping + `source_url` = `{{ $json.source_url }}` (Code node'dan)

## Telegram

Text: `{{ $('telegram mesaj').item.json.telegram_message }}`

## Export

`WF-02 Kaynaktan İçerik Üretme.json`

## Bu fazda yaşananlar

| Sorun | Çözüm |
|-------|--------|
| Get Row duplicate veriyi bozuyor | **If row doesn't exist** |
| Limit önce → hep aynı haber | Duplicate → Limit sırası |
| `.first()` ile sabit URL | `$('Limit').first()` |
| Tireli hashtag | Prompt + Code temizliği |
| Prompt'ta WF-1 notu | Kaldırıldı |

## Tamamlandı

- [x] RSS test (Webrazzi)
- [x] Veri temizleme (Veri Temizle)
- [x] Duplicate kontrolü (If row doesn't exist)
- [x] AI + Code + Insert + Telegram
- [x] End-to-end test (ardışık farklı haberler)
- [x] Workflow export

## Sonraya bırakıldı (PM görüşmesi sonrası)

- Limit node kaldırma / çoklu haber işleme
- Title bazlı ikinci duplicate katmanı (şu an yalnızca URL)

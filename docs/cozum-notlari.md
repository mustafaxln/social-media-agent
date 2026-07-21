# Çözüm Notları

Problem listesi → [`karsilasilan-problemler.md`](./karsilasilan-problemler.md)

| # | Problem | Çözüm | Kalıcı not |
|---|---------|-------|------------|
| 1 | Telegram kanal admin sorunu | **Grup** kullanıldı; bot gruba eklendi, Chat ID eksi ile (`-100...`) | Kanal yerine grup daha sorunsuz |
| 2 | Insert sonrası telegram_message kayboluyor | Telegram Text: `{{ $('Code' veya 'telegram mesaj').item.json.telegram_message }}` | Insert çıktısı mesaj alanını taşımaz |
| 3 | `={{ }}` invalid syntax | Expression (fx) açıkken sadece `{{ }}` kullan | Çift `=` ekleme |
| 4 | impact_score tipi | Data Table'da **Number** (1–5); `/5` sadece mesaj şablonunda | Şablon: `` `${d.impact_score}/5` `` |
| 5 | n8n attribution footer | Telegram node → **Append n8n Attribution** kapalı | Her Telegram node'da kontrol et |
| 6 | Get Row boş / veri kaybı | Data Table **If row doesn't exist** (`source_url` = `$json.url`) | Input item korunur; ayrı IF gerekmez |
| 7 | Limit önce duplicate sonra | Akış: `Veri Temizle → Duplicate → Limit → AI` | Önce ele, sonra 1 haber al |
| 8 | Sabit yanlış source_url | Code: `const source = $('Limit').first().json` | Veri Temizle'de `.first()` yasak (20 item'ın ilki) |
| 9 | Tireli hashtag | Prompt kuralı + Code'da `.replace(/-/g, '')` | Örnek: `#Eticaret` |
| 10 | Prompt'ta WF-1 referansı | System Message'dan kaldırıldı; kategori listesi sadeleştirildi | AI sadece kuralları görsün |
| 11 | Error WF tetiklenmiyor | WF-03 **Active** + WF-01/02 Settings → **Error Workflow** = WF-03 | İkisi de şart |
| 12 | Error alanları boş | Set yerine **Code** (`Hata Mesaji`): `execution.lastNodeExecuted`, `execution.error.message` | Nested path'ler Code'da güvenli |
| 13 | Referenced node doesn't exist | `$('...')` birebir node adı; veya Code ile `telegram_message` üret | Node adını yeniden adlandırarak da çözülür |
| 14 | Kod Telegram'a gidiyor | JS sadece Code node'a; Telegram'a yalnızca `telegram_message` expression | Text ≠ JavaScript |

## Tekrar kullanılacak kalıplar

```
AI Agent → Code (telegram_message + düzleştirme) → Insert → Telegram (Code'dan oku)
```

```
RSS → Veri Temizle → If row doesn't exist → Limit(1) → AI → ...
```

```
Error Trigger → Code (parse) → Insert errors → Telegram HATA
```

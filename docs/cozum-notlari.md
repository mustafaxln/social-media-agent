# Çözüm Notları

Problem listesi → [`karsilasilan-problemler.md`](./karsilasilan-problemler.md)

| # | Problem | Çözüm | Kalıcı not |
|---|---------|-------|------------|
| 1 | Telegram kanal admin | **Grup** + Chat ID `-100…` | Kanal yerine grup |
| 2 | Insert sonrası telegram_message yok | Text: `$('Telegram Mesajı Oluştur').item.json.telegram_message` | Insert mesajı taşımaz |
| 3 | `={{ }}` invalid | fx açıkken sadece `{{ }}` | Çift `=` yok |
| 4 | impact_score tipi | Number 1–5; `/5` sadece şablonda | |
| 5 | n8n footer | **Append n8n Attribution OFF** | Entity hatasına da yol açabilir |
| 6 | Get Row veri kaybı | **If row doesn't exist** (`source_url`) | |
| 7 | Limit önce duplicate | `Temizle → Duplicate → Limit → AI` | |
| 8 | Yanlış source_url | `$('Limit').first().json` | Veri Temizle'de `.first()` yok |
| 9 | Tireli hashtag | Prompt + `.replace(/-/g,'')` | `#Eticaret` |
| 10 | Prompt'ta WF-1 notu | System Message sade | |
| 11 | Error WF tetiklenmiyor | WF-03 Active + Settings Error Workflow | |
| 12 | Error alanları boş | Code ile `execution.*` parse | |
| 13 | Referenced node | `$('...')` = birebir node adı | |
| 14 | Kod Telegram Text'te | JS yalnız Code node'da | |
| 15 | HTTPS zorunlu | cloudflared + `WEBHOOK_URL` + compose up | URL değişince tekrarla |
| 16 | ImgBB | **Cloudinary** unsigned + `secure_url` | |
| 17 | IG Buffer type | `metadata.instagram.type=post` | |
| 18 | content_id kaybı | `$('Callback Parse').item.json.content_id` | |
| 19 | Tunnel / Onayla öldü | Yeni tunnel → `.env` → `docker compose up -d` → WF-04 re-Activate | Quick tunnel kalıcı değil |
| 20 | Switch callback tutmuyor | `Giris Ayir` Code → `route` = `callback`\|`yeni` → Switch equals | Kökte `data`, nested `callbackQuery` yok |
| 21 | `/yeni` tetiklenmiyor | Trigger Updates: **message** + **callback_query**; re-Activate | |
| 22 | Çoklu Telegram Trigger | Yalnızca **WF-04** Trigger | Bot başına 1 webhook |
| 23 | parse entities | Attribution OFF; Parse Mode ekleme | AI metnindeki `*_` Markdown bozar |
| 24 | Grupta `/yeni` yok | **DM'den** `/yeni`; taslak gruba gider | Privacy/admin denendi; DM bilinçli tercih |

## Tekrar kullanılacak kalıplar

```
AI → Code (telegram_message) → Insert → Telegram (Code'dan oku; Attribution OFF)
```

```
RSS → Temizle → If row doesn't exist → Limit(1) → AI
```

```
Error Trigger → Code → errors tablosu → Telegram HATA
```

```
Telegram Trigger → Giris Ayir (route) → Switch
  callback → Callback Parse → … (onay/görsel/Buffer)
  yeni → Parse /yeni → Execute WF-01
```

```
/yeni DM → WF-01 → grup taslak → Onayla → Image → Cloudinary → Yayınla → Buffer
```

## Tunnel checklist (her cold start)

1. `cloudflared tunnel --url http://localhost:5678`  
2. URL → `.env` `WEBHOOK_URL=` (sonda `/`)  
3. `docker compose up -d`  
4. WF-04 Inactive → Active  

Detay: [`calisma-notlari/projeyi-yeniden-calistirma.md`](./calisma-notlari/projeyi-yeniden-calistirma.md)

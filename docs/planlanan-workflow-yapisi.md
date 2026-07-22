# Planlanan / Gerçekleşen Workflow Yapısı

| # | Workflow | Tetikleyici | Export |
|---|----------|-------------|--------|
| 1 | Manuel İçerik Üretme | Execute Workflow (WF-04 `/yeni`) | `WF-01 …json` |
| 2 | Kaynaktan İçerik Üretme | Schedule + Manual | `WF-02 …json` |
| 3 | Error Handling | Error Trigger | `WF-03 …json` |
| 4 | Telegram Hub (onay + `/yeni`) | Telegram message + callback | `WF-04 Telegram Onay.json` |

## Workflow 1 — Manuel

```
When Executed by Another Workflow
  (topic, platform, target_audience, tone)
  → AI Agent → Code → Insert → Telegram grup [Onayla|Reddet]
```

Giriş: Telegram DM `/yeni` (WF-04 Parse → Execute). n8n Edit Fields günlük kullanımda yok.

## Workflow 2 — Kaynak

```
Schedule/Manual → RSS → Veri Temizle → Duplicate → Limit → AI → Code → Insert → Telegram
```

**Duplicate:** If row doesn't exist — `source_url`  
**Kaynak URL:** `$('Limit').first().json`

## Workflow 3 — Error

```
Error Trigger → Hata Mesaji (Code) → social_media_errors → Telegram HATA
```

WF-01, WF-02, WF-04 → Error Workflow = WF-03.

## Workflow 4 — Telegram hub

```
Telegram Trigger (message + callback_query)
  → Giris Ayir → Switch(route)
       ├─ callback → Callback Parse → reject | approve→Image→Cloudinary→FINAL | publish→Buffer | cancel
       └─ yeni → Parse /yeni → Execute WF-01
```

Detay: [`calisma-notlari/telegram-yeni-komutu.md`](./calisma-notlari/telegram-yeni-komutu.md)

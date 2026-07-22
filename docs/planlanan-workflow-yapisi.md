# Planlanan / Gerçekleşen Workflow Yapısı

| # | Workflow | Tetikleyici | Export |
|---|----------|-------------|--------|
| 1 | Manuel İçerik Üretme | Manual Trigger | `WF-01 Manuel İçerik Üretme.json` |
| 2 | Kaynaktan İçerik Üretme | Schedule + Manual | `WF-02 Kaynaktan İçerik Üretme.json` |
| 3 | Error Handling | Error Trigger | `WF-03 Error Handling.json` |
| 4 | Onay + Görsel + Yayın | Telegram Callback | `WF-04` (export et) |

## Workflow 1 — Manuel

```
Manual Trigger → Set (topic + platform) → AI Agent → Code → Insert → Telegram [Onayla|Reddet]
```

## Workflow 2 — Kaynak

```
Schedule/Manual → RSS → Veri Temizle → Duplicate → Limit → AI → Code → Insert → Telegram [Onayla|Reddet]
```

**Duplicate:** If row doesn't exist — `source_url`  
**Kaynak URL (Code):** `$('Limit').first().json`

## Workflow 3 — Error

```
Error Trigger → Hata Mesaji (Code) → social_media_errors → Telegram HATA
```

WF-01, WF-02, WF-04 → Error Workflow = WF-03.

## Workflow 4 — Onay / görsel / Buffer

```
Callback
  reject  → rejected
  approve → Image → Cloudinary → Final Telegram [Yayınla|İptal]
  cancel  → preview_rejected
  publish → Get row → Buffer (LI/IG) → published
```

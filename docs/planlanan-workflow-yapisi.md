# Planlanan Workflow Yapısı

| # | Workflow | Tetikleyici | Export |
|---|----------|-------------|--------|
| 1 | Manuel İçerik Üretme | Manual Trigger | `WF-01 Manuel İçerik Üretme.json` |
| 2 | Kaynaktan İçerik Üretme | Schedule (+ Manual test) | `WF-02 Kaynaktan İçerik Üretme.json` |
| 3 | Error Handling | Error Trigger | `WF-03 Error Handling.json` |

## Workflow 1 — Manuel İçerik Üretme

```
Manual Trigger → Set Node → AI Agent → Code → Data Table → Telegram
```

## Workflow 2 — Kaynaktan İçerik Üretme

```
Schedule Trigger → RSS → Veri Temizle → Duplicate Kontrol → Limit → AI Agent → Code → Data Table → Telegram
```

**Duplicate:** Data Table If row doesn't exist — `source_url` = RSS `url`  
**Kaynak URL (Code):** `$('Limit').first().json`

## Workflow 3 — Error Handling

```
Error Trigger → Hata Mesaji (Code) → social_media_errors → Telegram
```

WF-01 ve WF-02 Settings → Error Workflow = WF-03.

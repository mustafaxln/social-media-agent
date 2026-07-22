# Faz 5 — Error Handling + Retry / Fallback

**Durum:** Tamamlandı

## Amaç

WF-01 / WF-02 hata aldığında:
1. Hata kaybolmasın → `social_media_errors`
2. Haberin olsun → Telegram HATA mesajı
3. Geçici hatalarda tekrar dene → Retry On Fail

## Final akış (WF-03)

```
Error Trigger → Hata Mesaji (Code) → Insert row (social_media_errors) → Telegram
```

## Kararlar

| Alan | Seçim |
|------|--------|
| Error workflow | `WF-03 Error Handling` |
| Hata tablosu | `social_media_errors` |
| Log tablosu | `social_media_execution_logs` (tablo hazır; WF insert sonraya) |
| Telegram | Aynı grup, `HATA` başlıklı mesaj |
| Retry | AI / Telegram / RSS — Max 3, Wait 2000 ms |
| Fallback | İlk versiyonda ağır fallback yok; error workflow + retry yeterli |

## Code — Hata Mesaji

Error Trigger nested alanları Set'te boş kalabiliyor; Code ile parse edildi.
Export: `WF-03 Error Handling.json`

## Bağlantı

- WF-01 Settings → Error Workflow = WF-03
- WF-02 Settings → Error Workflow = WF-03
- **WF-04 Settings → Error Workflow = WF-03** (onay/görsel/yayın hattı)
- WF-03 Active

## Bu fazda yaşananlar

| Sorun | Çözüm |
|-------|--------|
| Error WF hiç çalışmıyor | WF-03 Active + Settings Error Workflow |
| Set'te node/hata boş | Code ile `execution.error` / `lastNodeExecuted` |
| `$('Hata Bilgileri')` yok | Node adı eşleşmeli veya Code `telegram_message` |
| Test: Chat ID boz → WF-01 fail → WF-03 Telegram HATA | Başarılı test edildi |

## Tamamlandı

- [x] `social_media_errors` tablosu
- [x] WF-03 Error Handling
- [x] Telegram hata bildirimi
- [x] WF-01 / WF-02'ye Error Workflow bağla
- [x] Retry ayarları
- [x] Test (bilerek hata)
- [x] Export → `WF-03 Error Handling.json`
- [ ] `social_media_execution_logs` insert (tablo var, kullanım sonraya)
- [ ] Ağır fallback (yedek RSS, template) — sonraya

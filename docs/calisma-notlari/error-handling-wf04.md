# Error handling — onay / görsel / yayın hattı (WF-04)

**Durum:** Tamamlandı — WF-04 → WF-03 bağlı, test OK; Retry On Fail açık

## PM (§12–13) vs final

| PM | Durum |
|----|--------|
| Error Trigger → errors → Telegram | ✅ WF-03 |
| Tüm WF’lere bağla | ✅ WF-01, 02, **04** |
| Retry | ✅ Image, Cloudinary, Buffer, Telegram, AI, RSS |
| İnsan / süreç fallback | ✅ Reddet, İptal |
| Ağır otomatik fallback | ❌ Sonraya |
| execution_logs | ❌ Sonraya |

## İnsan fallback

| Sorun | Aksiyon |
|-------|---------|
| Kötü taslak | Reddet |
| Kötü görsel | İptal |
| API geçici hata | Retry |
| Node fail | WF-03 kayıt + HATA mesajı |

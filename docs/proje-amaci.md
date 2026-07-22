# Proje Amacı

Belirlenen kaynaklardan (manuel konu veya RSS) sosyal medya içerik fikirleri üretmek; AI ile LinkedIn/Instagram formatına dönüştürmek; Telegram’da onaylayıp görsel üretmek; Buffer ile yayınlamak.

## Çözüm (final)

1. Manuel (platform biz) veya RSS (platform AI)  
2. Structured JSON taslak → Data Table  
3. Telegram 1. onay (Onayla/Reddet)  
4. Görsel (gpt-image-1-mini) → Cloudinary  
5. Telegram 2. onay (Yayınla/İptal)  
6. Buffer → LinkedIn / Instagram  
7. Hatalar → WF-03  

## Hedef durumu

| Hedef | Durum |
|-------|--------|
| Manuel LinkedIn/Instagram içerik | ✅ WF-01 |
| RSS otomatik | ✅ WF-02 + Schedule |
| Merkezi tablo | ✅ |
| Telegram buton onayı | ✅ WF-04 |
| Görsel üretimi | ✅ |
| Sosyal yayın | ✅ Buffer |
| Error handling + retry | ✅ WF-03 + Retry |

## Sonraya

execution_logs insert, ağır fallback, PM §15–16 (takvim, brand voice, multi-agent, …)

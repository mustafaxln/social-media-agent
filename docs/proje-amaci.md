# Proje Amacı

Belirlenen kaynaklardan (Telegram `/yeni` veya RSS) sosyal medya içerik fikirleri üretmek; AI ile LinkedIn/Instagram formatına dönüştürmek; Telegram’da 2 kademeli onaylayıp görsel üretmek; Buffer ile yayınlamak.

## Çözüm (final)

1. **Manuel:** Bot DM `/yeni` (platform, konu, hedef, ton) — n8n UI gerekmez  
2. **RSS:** WF-02 Webrazzi (platform AI seçer)  
3. Structured JSON → Data Table  
4. Grupta 1. onay (Onayla/Reddet)  
5. Görsel → Cloudinary  
6. 2. onay (Yayınla/İptal)  
7. Buffer → LinkedIn / Instagram  
8. Hatalar → WF-03  

## Hedef durumu

| Hedef | Durum |
|-------|--------|
| Manuel LinkedIn/Instagram | ✅ WF-01 + `/yeni` DM |
| n8n’siz manuel giriş | ✅ Telegram DM |
| RSS otomatik | ✅ WF-02 + Schedule |
| Merkezi tablo | ✅ |
| 2 kademeli Telegram onay | ✅ WF-04 |
| Görsel + yayın | ✅ Cloudinary + Buffer |
| Error + retry | ✅ WF-03 |

## Sonraya

Sabit tunnel/VPS, execution_logs insert, ağır fallback, PM §15–16 (takvim, brand voice, multi-agent), grupta `/yeni` (bilinçli bırakıldı).

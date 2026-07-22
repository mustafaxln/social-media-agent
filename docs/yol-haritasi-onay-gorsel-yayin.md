# Yol Haritası — Onay + Görsel + Yayın

> **Durum:** Tamamlandı (üretim → 2 kademeli onay → Cloudinary → Buffer → LI/IG)  
> **Kaynak:** PM görüşmesi + manuel hat  
> **Kural:** Başarılı checkpoint → git commit

## Final akış

```
WF-01 Manuel (konu + platform biz)  ─┐
WF-02 RSS (platform AI)             ─┤
                                     ▼
              Insert waiting_approval
              Telegram taslak [Onayla | Reddet]
                     │
        ┌────────────┴────────────┐
        │ reject                  │ approve
        ▼                         ▼
   status=rejected         status=approved
   DUR                     OpenAI Image (gpt-image-1-mini)
                           Cloudinary → image_url
                           Telegram FINAL (foto+caption)
                                [Yayınla | İptal]
                           │
                ┌──────────┴──────────┐
                │ cancel              │ publish
                ▼                     ▼
         preview_rejected      Buffer (platform channel)
         DUR                   LinkedIn veya Instagram
                               status=published
```

## Kullanılan servisler

| Servis | Rol |
|--------|-----|
| OpenAI gpt-image-1-mini | Görsel |
| Cloudinary (unsigned preset) | image_url saklama |
| Buffer Free API (GraphQL) | LI / IG yayın |
| cloudflared + WEBHOOK_URL | WF-04 Telegram Trigger (local) |

## WF-04 callback sözleşmesi

| data | Sonuç |
|------|--------|
| `approve:ID` | Görsel + final Telegram |
| `reject:ID` | rejected |
| `publish:ID` | Buffer → published |
| `cancel:ID` | preview_rejected |

## Error handling (yeni hat)

- WF-04 → Error Workflow = **WF-03** ✅
- Retry On Fail: Image, Cloudinary, Buffer, Telegram ✅
- İnsan fallback: kötü görsel → **İptal**; yanlış taslak → **Reddet**
- Ağır otomatik fallback (yedek RSS / template) — yok (bilinçli)

Detay → [`calisma-notlari/checkpoint-4-buffer-yayin.md`](./calisma-notlari/checkpoint-4-buffer-yayin.md) · [`calisma-notlari/error-handling-wf04.md`](./calisma-notlari/error-handling-wf04.md)

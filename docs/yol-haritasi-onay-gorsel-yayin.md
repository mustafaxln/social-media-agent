# Yol Haritası — Onay + Görsel + Yayın (+ `/yeni`)

> **Durum:** Tamamlandı  
> **Kapsam:** 2 kademeli onay → Cloudinary → Buffer + Telegram DM `/yeni` ile manuel üretim

## Final akış

```
Telegram DM /yeni ──► WF-04 ──► Execute WF-01 ─┐
WF-02 RSS ────────────────────────────────────┤
                                              ▼
                         Insert waiting_approval
                         Grup taslak [Onayla | Reddet]
                                │
                   ┌────────────┴────────────┐
                   │ reject                  │ approve
                   ▼                         ▼
              rejected                Image + Cloudinary
                                      FINAL [Yayınla | İptal]
                                         │
                              ┌──────────┴──────────┐
                              │ cancel              │ publish
                              ▼                     ▼
                       preview_rejected      Buffer → LI/IG
                                             published
```

## Servisler

| Servis | Rol |
|--------|-----|
| Telegram | DM `/yeni`, grup onay, HATA |
| OpenAI Image mini | Görsel |
| Cloudinary | image_url |
| Buffer GraphQL | Yayın |
| cloudflared | Local webhook |

## WF-04 giriş

| Kaynak | route | Sonuç |
|--------|-------|--------|
| Buton callback | `callback` | approve/reject/publish/cancel |
| `/yeni` mesajı | `yeni` | Parse → WF-01 |

## Error / fallback

- WF-04 → WF-03 ✅ · Retry ✅ · İnsan Reddet/İptal ✅  

Detay: [`calisma-notlari/telegram-yeni-komutu.md`](./calisma-notlari/telegram-yeni-komutu.md) · [`checkpoint-4-buffer-yayin.md`](./calisma-notlari/checkpoint-4-buffer-yayin.md)

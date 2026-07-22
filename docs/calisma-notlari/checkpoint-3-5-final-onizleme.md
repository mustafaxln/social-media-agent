# Checkpoint 3.5 — Final önizleme + 2. onay (Telegram)

**Durum:** Sırada (görsel üretimi ✅ binary)  
**Amaç:** Görsel oluşunca final post Telegram’a gitsin; **Yayınla** denince sosyal medyaya çıksın.

## Akış

```
callback approve:ID
  → status=approved
  → Get row
  → OpenAI Image (binary)
  → Telegram Send Photo (caption = final post metni)
       butonlar: publish:ID | cancel:ID

callback publish:ID
  → Get row (+ binary yolunda saklı / yeniden üretme)
  → LinkedIn veya Instagram
  → status=published

callback cancel:ID
  → status=preview_rejected (veya cancelled)
  → DUR

callback reject:ID
  → status=rejected → DUR (görsel yok)
```

## callback_data sözleşmesi

| Buton | data | Anlam |
|-------|------|--------|
| Onayla (taslak) | `approve:{{ id }}` | Görsel üret + final Telegram |
| Reddet (taslak) | `reject:{{ id }}` | İptal |
| Yayınla (final) | `publish:{{ id }}` | Sosyal medya post |
| İptal (final) | `cancel:{{ id }}` | Yayınlama |

## Binary sorunu (2. onayda)

Telegram’a foto gidince binary workflow’dan düşebilir. **Yayınla** basılınca:

**Seçenek A (basit):** Publish’te görseli **yeniden üret** (mini ucuz; 2. görsel ~$0.01)  
**Seçenek B:** Fotoğrafı Telegram’a at → `file_id` tabloya yaz → yayın öncesi Telegram’dan indir  
**Seçenek C:** Cloudinary vb. upload → `image_url`

İlk kurulumda **A** en hızlı.

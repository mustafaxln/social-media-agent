# Data Table Yapısı

n8n içinde tanımlı tablolar.

## social_media_contents

WF-01 / WF-02 Insert; WF-04 status + `image_url` günceller.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | auto | Birincil anahtar; Telegram `callback_data` |
| title | string | Başlık |
| content | text | Post metni |
| platform | string | LinkedIn / Instagram |
| category | string | Kategori |
| target_audience | string | Hedef kitle |
| hashtags | string | Hashtag'ler |
| visual_idea | text | Görsel fikri (görsele yazı yazılmamalı) |
| cta | string | CTA |
| tone | string | Ton |
| impact_score | number | 1–5 |
| status | string | Aşağıdaki değerler |
| source_url | string | RSS URL veya boş/manual |
| image_url | string | Cloudinary `secure_url` |
| created_at | datetime | Oluşturma |

### Status akışı

| Status | Ne zaman |
|--------|----------|
| `waiting_approval` | Taslak Telegram'a gitti |
| `approved` | 1. Onayla (görsel üretiliyor / üretildi) |
| `rejected` | 1. Reddet |
| `preview_rejected` | Final İptal (görsel var, yayın yok) |
| `published` | Buffer ile LI/IG'ye gitti |
| `failed` | Teknik hata (opsiyonel) |
| `telegram_failed` | PM fallback — henüz otomatik yok |

**Duplicate (WF-02):** `If row doesn't exist` → `source_url` = haber `url`.

---

## social_media_errors

WF-03 Error Handling. WF-01 / WF-02 / **WF-04** bağlamalı.

| Sütun | Tip |
|-------|-----|
| workflow_name | string |
| execution_id | string |
| node_name | string |
| error_message | text |
| created_at | string |

---

## social_media_execution_logs

Şema hazır; workflow insert yok (PM §14 — sonraya).

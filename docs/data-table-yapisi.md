# Data Table Yapısı

n8n içinde tanımlı tablolar.

## social_media_contents

Üretilen sosyal medya içeriklerinin ana tablosu. WF-01 ve WF-02 Insert eder.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | auto | Birincil anahtar |
| title | string | Başlık |
| content | text | İçerik metni |
| platform | string | LinkedIn / Instagram |
| category | string | İçerik kategorisi |
| target_audience | string | Hedef kitle |
| hashtags | string | Boşlukla birleşik hashtag'ler |
| visual_idea | text | Görsel fikri |
| cta | string | Call to action |
| tone | string | Ton |
| impact_score | number | 1–5 (tam sayı) |
| status | string | `waiting_approval` (üretim anında) |
| source_url | string | RSS URL (WF-02; duplicate anahtarı) |
| created_at | datetime | Oluşturulma (n8n otomatik olabilir) |

**Status değerleri (plan):** draft / waiting_approval / approved / rejected / scheduled / published / failed / telegram_failed

İlk versiyonda üretim → `waiting_approval`. Onay güncellemesi manuel / sonraya.

**Duplicate:** WF-02 `If row doesn't exist` → `source_url` equals haber `url`.

---

## social_media_errors

WF-03 Error Handling Insert eder.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| workflow_name | string | Hata alan workflow |
| execution_id | string | Execution ID |
| node_name | string | Son çalışan / hata node |
| error_message | text | Hata metni |
| created_at | string | ISO zaman |

---

## social_media_execution_logs

Şema hazır; **ilk versiyonda workflow insert yok** (sonraya).

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| workflow_name | string | Workflow adı |
| execution_id | string | Execution ID |
| total_sources | number | Kontrol edilen kaynak |
| generated_contents | number | Üretilen içerik |
| sent_to_telegram | number | Telegram'a giden |
| failed_count | number | Hata sayısı |
| started_at | string | Başlangıç |
| finished_at | string | Bitiş |
| status | string | Durum |

# Data Table Yapısı

## social_media_contents

Üretilen sosyal medya içeriklerinin kaydedildiği ana tablo.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | auto | Birincil anahtar |
| title | string | Başlık |
| content | text | İçerik metni |
| platform | string | LinkedIn, Instagram... |
| category | string | İçerik kategorisi |
| target_audience | string | Hedef kitle |
| hashtags | json | Hashtag listesi |
| visual_idea | text | Görsel fikri |
| cta | string | Call to action |
| tone | string | Ton |
| impact_score | integer | 1–5 |
| status | string | draft / waiting_approval / approved / rejected / scheduled / published / failed |
| source_url | string | Kaynak URL (opsiyonel) |
| created_at | datetime | Oluşturulma tarihi |

> Faz 3'te n8n içinde oluşturulacak.

## social_media_execution_logs

Workflow çalıştırma logları.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | auto | Birincil anahtar |
| workflow_name | string | Workflow adı |
| execution_id | string | Execution ID |
| total_sources | integer | Kontrol edilen kaynak sayısı |
| generated_contents | integer | Üretilen içerik sayısı |
| sent_to_telegram | integer | Telegram'a gönderilen sayı |
| failed_count | integer | Hata sayısı |
| started_at | datetime | Başlangıç |
| finished_at | datetime | Bitiş |
| status | string | Durum |

## social_media_errors

Hata kayıtları.

| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | auto | Birincil anahtar |
| workflow_name | string | Workflow adı |
| execution_id | string | Execution ID |
| node_name | string | Hata alan node |
| error_message | text | Hata mesajı |
| created_at | datetime | Oluşturulma tarihi |

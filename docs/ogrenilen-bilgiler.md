# Öğrenilen Bilgiler

| Tarih | Konu | Not |
|-------|------|-----|
| Haz–Tem 2026 | Docker + n8n | `docker compose up -d`; veri `n8n_data`; `down -v` yasak |
| Tem 2026 | AI Agent | System + User + Structured Output |
| Tem 2026 | Model | `gpt-4o-mini` / görsel `gpt-image-1-mini` |
| Tem 2026 | AI çıktısı | `item.output \|\| item` |
| Tem 2026 | Data Table | status `waiting_approval` … `published` |
| Tem 2026 | Duplicate | If row doesn't exist > Get Row+IF |
| Tem 2026 | `$('Node').first()` | Çok item’da tehlikeli; Limit(1) sonrası OK |
| Tem 2026 | Telegram grup | Chat ID `-100…`; Attribution OFF |
| Tem 2026 | Human-in-the-loop | 2 kademeli onay |
| Tem 2026 | RSS | Webrazzi |
| Tem 2026 | Platform | Manuel: kullanıcı; RSS: AI |
| Tem 2026 | Error Trigger | Active + Settings bağla |
| Tem 2026 | Retry On Fail | Kritik API node’ları |
| Tem 2026 | Buffer | IG `type=post`; Free kota |
| Tem 2026 | Cloudinary | ImgBB yerine |
| Tem 2026 | cloudflared | Quick tunnel URL değişir → WEBHOOK_URL yenile |
| Tem 2026 | Tek Telegram Trigger | Bot başına 1 webhook; hub = WF-04 |
| Tem 2026 | Callback payload | Çoğu zaman kökte `data`, nested `callbackQuery` yok |
| Tem 2026 | `/yeni` | DM güvenilir; grup değil |
| Tem 2026 | parse entities | Attribution/Parse Mode AI metnini bozar |
| Tem 2026 | Execute Workflow | WF-01 input schema: 4 string alan |

## Kavramlar

| Kavram | Bu projedeki karşılığı |
|--------|------------------------|
| Human-in-the-loop | Telegram onay butonları |
| Workflow hub | WF-04 tek Telegram girişi |
| Sub-workflow | Execute → WF-01 |
| Retry / fail-safe | Retry On Fail + WF-03 |
| Duplicate control | `source_url` |
| Structured output | AI JSON şema |
| Webhook tunnel | cloudflared → WEBHOOK_URL |

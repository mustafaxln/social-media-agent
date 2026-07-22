# n8n Kurulum Notları

Docker Compose ile local n8n kuruldu ve çalışır durumda.

## Kurulum

```bash
cd sosyal-medya-icerik-ajani
cp .env.example .env   # N8N_BASIC_AUTH_PASSWORD ayarla
docker compose up -d
```

## Erişim

| Alan | Değer |
|------|--------|
| URL | http://localhost:5678 |
| Kullanıcı | `admin` |
| Şifre | `.env` → `N8N_BASIC_AUTH_PASSWORD` |

## Yapılandırma (`docker-compose.yml`)

- Image: `docker.n8n.io/n8nio/n8n`
- Port: `5678`
- Timezone: `Europe/Istanbul`
- Volume: `n8n_data` → workflow, credential, Data Table kalıcılığı
- Basic auth aktif

## Credential'lar (n8n UI)

| Credential | Kullanım |
|------------|----------|
| OpenAI | WF-01, WF-02 AI Agent |
| Telegram | WF-01, WF-02, WF-03 mesaj |

> Credential'lar export JSON'da secret olarak gitmez; yeni makinede yeniden tanımlanır.

## Doğrulama

Container ayağa kalktıktan sonra tarayıcıdan arayüze girildi; Faz 1 tamamlandı.

## Telegram Trigger (WEBHOOK_URL)

Local n8n'de Telegram Trigger için HTTPS gerekir:

1. Tünel: `cloudflared tunnel --url http://localhost:5678`
2. `.env` içine: `WEBHOOK_URL=https://xxxx.trycloudflare.com/`
3. `docker compose up -d` (yeniden)

Tünel URL değişirse `.env` güncelleyip n8n'i yeniden başlat.  
**Cold start (detaylı):** [`projeyi-yeniden-calistirma.md`](./projeyi-yeniden-calistirma.md)


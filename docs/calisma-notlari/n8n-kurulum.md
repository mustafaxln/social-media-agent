# n8n Kurulum Notları

Docker Compose ile local n8n kuruldu ve çalışır durumda.

## Kurulum

```bash
docker compose up -d
```

## Erişim

- URL: http://localhost:5678
- Kullanıcı: `admin`
- Şifre: `.env` dosyasındaki `N8N_BASIC_AUTH_PASSWORD`

## Yapılandırma

- Timezone: Europe/Istanbul
- Veri kalıcılığı: Docker volume (`n8n_data`)

## Doğrulama

Container ayağa kalktıktan sonra tarayıcıdan `localhost:5678` adresine gidilerek n8n arayüzüne erişildi.

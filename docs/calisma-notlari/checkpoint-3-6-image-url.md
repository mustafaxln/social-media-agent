# Checkpoint 3.6 — Görseli URL olarak sakla

**Sorun:** `approve` run’ında binary var; `publish` ayrı execution → binary yok.  
**Çözüm:** Image’den hemen sonra upload → Data Table `image_url` → Publish’te URL kullan.

## Akış (approve dalı)

```
… → OpenAI Image (binary)
  → Upload (ImgBB)
  → Update image_url
  → Telegram Send Photo (URL veya binary)
```

**Yayın (Checkpoint 4 — Buffer):**

```
publish callback
  → Get row (content, platform, image_url, hashtags…)
  → IF platform
       → Buffer LinkedIn kanalı
       → Buffer Instagram kanalı
  → status = published
```

Buffer Free: max 3 kanal, kanal başına 10 kuyruk slotu (bu proje temposu için yeterli).

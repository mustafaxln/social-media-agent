# Checkpoint 4 — Buffer yayın + kapanış notları

**Durum:** Tamamlandı (LI + IG test OK)

## Publish dalı

```
publish → Get row → Buffer Payload (Code) → HTTP Buffer → Update published
```

- Instagram: `metadata.instagram.type: post`, `shouldShareToFeed: true`
- Update Match: `{{ $('Callback Parse').item.json.content_id }}` (HTTP sonrası `$json.content_id` yok)

## Görsel URL

ImgBB limit → **Cloudinary** unsigned preset → `secure_url` → `image_url`

## Tamamlandı

- [x] Buffer Free + channel id
- [x] GraphQL createPost + image URL
- [x] LinkedIn + Instagram
- [x] status = published

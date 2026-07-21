# Faz A — Telegram Buton Onayı (uygulama notları)

**Durum:** Devam ediyor  
**Hedef:** Taslak mesajda Onayla / Reddet → callback → Data Table `status` güncelle

## Ön koşullar

- [ ] `social_media_contents` tablosunda kayıtlar `id` ile erişilebilir
- [ ] Telegram bot + grup çalışıyor (mevcut WF-01/02)
- [ ] WF-03 Error Handling Active (opsiyonel ama iyi)

## Checkpoint 2 — durum

**Durum:** Tamamlandı (test OK — approved / rejected)  
**Hedef:** Onayla → `approved` | Reddet → `rejected` (görsel/yayın henüz yok)

### Not — Telegram Trigger + local n8n

Active için HTTPS `WEBHOOK_URL` gerekir (cloudflared/ngrok).  
`docker-compose.yml` + `.env` → `WEBHOOK_URL` ayarlı.


Telegram node'da **Reply Markup** / **Inline Keyboard**:

| Buton metni | callback_data |
|-------------|---------------|
| Onayla | `approve:{{ $json.id }}` |
| Reddet | `reject:{{ $json.id }}` |

> Insert **sonrası** Data Table genelde `id` döndürür. Telegram'ı Insert'ten **sonra** tut; Text + butonlarda `$json.id` kullan.
> `telegram_message` hâlâ Code'dan: `{{ $('telegram mesaj').item.json.telegram_message }}`

### A2 — WF-04 oluştur

Ad: `WF-04 Telegram Onay`  
Trigger: **Telegram Trigger** → Updates: **Callback Query** (veya message + callback)

### A3 — Callback parse (Code)

```javascript
const cb = $input.first().json;
const data = cb.callbackQuery?.data || cb.data || '';
const [action, id] = String(data).split(':');

return [{
  json: {
    action: action === 'approve' ? 'approved' : action === 'reject' ? 'rejected' : 'unknown',
    content_id: id || '',
    chat_id: cb.callbackQuery?.message?.chat?.id || cb.chat?.id,
    message_id: cb.callbackQuery?.message?.message_id,
    from_user: cb.callbackQuery?.from?.username || ''
  }
}];
```

### A4 — IF action

- `approved` / `rejected` → Data Table **Update**
- `unknown` → dur veya hata mesajı

### A5 — Data Table Update

| Ayar | Değer |
|------|--------|
| Operation | Update row(s) |
| Match | `id` equals `{{ $json.content_id }}` |
| status | `{{ $json.action }}` |

### A6 — (Opsiyonel) Answer callback + teyit mesajı

Telegram: answerCallbackQuery / send message: "Durum: approved"

## Test checklist

- [ ] WF-02 (veya WF-01) çalışır → Telegram'da butonlu taslak
- [ ] Onayla → tabloda `status = approved`
- [ ] Reddet → `status = rejected`
- [ ] Yanlış/eski buton kırılmaz (bilinen id)

## Commit

Kullanıcı "sorunsuz" dedikten sonra git commit.

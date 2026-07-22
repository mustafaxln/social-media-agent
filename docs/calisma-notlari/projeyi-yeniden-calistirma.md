# Projeyi Yeniden Çalıştırma Rehberi

> Ne zaman bakarsın: 1 ay / 3 ay sonra projeyi tekrar ayağa kaldırmak istediğinde.  
> Son güncelleme: Temmuz 2026 (`/yeni` DM akışı dahil)

Bu dosya **sadece çalıştırma** içindir. Mimari özet → [`sistem-dokumantasyonu.md`](../sistem-dokumantasyonu.md)

---

## 1. Sistem neye ihtiyaç duyar?

| Parça | Ne işe yarar | Yoksa ne olur? |
|--------|----------------|----------------|
| Docker Desktop | n8n container | n8n açılmaz |
| Proje klasörü + `.env` | Şifre + `WEBHOOK_URL` | Auth / Telegram trigger bozulur |
| `n8n_data` volume | Workflow, credential, Data Table | Volume silindiyse her şey sıfırlanır |
| cloudflared | Local n8n’e HTTPS tünel | Onayla / `/yeni` tetiklenmez |
| OpenAI / Telegram / Cloudinary / Buffer | AI, mesaj, görsel URL, yayın | İlgili node hata verir |

**Önemli:** `docker compose down -v` yapma. `-v` volume’u siler; workflow ve credential gider.

---

## 2. Aynı Mac’te, volume duruyorsa (normal senaryo)

### Adım A — Docker’ı aç, n8n’i başlat

1. **Docker Desktop**’ın çalıştığından emin ol.  
2. Terminal:

```bash
cd ~/Desktop/sosyal-medya-icerik-ajani
docker compose up -d
```

3. Tarayıcı: [http://localhost:5678](http://localhost:5678)  
   - Kullanıcı: `admin`  
   - Şifre: proje kökündeki `.env` → `N8N_BASIC_AUTH_PASSWORD`

n8n açılıyorsa container ve volume büyük ihtimalle sağlamdır.

### Adım B — Cloudflare tunnel (Telegram için şart)

Telegram bot’u `localhost`’a ulaşamaz; HTTPS public URL ister. Quick tunnel:

```bash
cloudflared tunnel --url http://localhost:5678
```

Terminalde şuna benzer bir satır çıkar:

```text
https://random-words.trycloudflare.com
```

1. Bu URL’yi kopyala.  
2. `.env` dosyasını aç, şu satırı güncelle (sonda `/` olsun):

```env
WEBHOOK_URL=https://random-words.trycloudflare.com/
```

3. n8n’i yeni URL ile yeniden başlat:

```bash
cd ~/Desktop/sosyal-medya-icerik-ajani
docker compose up -d
```

4. **Tunnel terminalini kapatma** — kapalıyken Onayla ve `/yeni` çalışmaz.  
5. Quick tunnel her açılışta **URL değiştirir** → her seferinde `.env` + `docker compose up -d` gerekir.

### Adım C — Workflow’ları Active yap

n8n UI → Workflows:

| Workflow | Active? | Neden |
|----------|---------|--------|
| **WF-04 Telegram Onay** | Evet | Telegram kapısı: `/yeni` + Onayla/Reddet/Yayınla |
| **WF-03 Error Handling** | Evet | Hataları tabloya + Telegram’a yazar |
| **WF-01 Manuel İçerik** | Evet | WF-04’ten Execute Workflow ile çağrılır |
| **WF-02 Kaynaktan İçerik** | İsteğe bağlı | Schedule ile RSS istiyorsan Active |

**WF-04’ü bir kez Inactive → Active yap** (yeni `WEBHOOK_URL` Telegram’a yazılsın).

Trigger kontrolü (WF-04 → Telegram Trigger → Updates):
- `callback_query` (butonlar)
- `message` (`/yeni` DM)

### Adım D — Credential’lar hâlâ geçerli mi?

n8n → **Credentials**. Süresi dolmuşsa yenile:

- OpenAI  
- Telegram bot token  
- Cloudinary (unsigned preset / upload)  
- Buffer API  

Aynı makinede volume duruyorsa genelde dokunmana gerek kalmaz; 1 ay sonra token expire olmuş olabilir.

### Adım E — Hızlı doğrulama

1. Telegram’da bota **özelden (DM)** yaz:

```text
/yeni
platform: LinkedIn
konu: Test yeniden baslatma
hedef: Test
ton: Profesyonel ve öğretici
```

2. Beklenen: WF-04 + WF-01 çalışır → **grupta** taslak + Onayla/Reddet.  
3. Onayla → görsel → Yayınla (Buffer) zincirini istersen kısaca dene.  
4. RSS için: WF-02’yi Manual Trigger ile bir kez çalıştır.

`/yeni` **grupta** güvenilir değil (Telegram grup kısıtları); kullanım **DM**. Şablon: [`templates/telegram/yeni-komut-sablonu.md`](../../templates/telegram/yeni-komut-sablonu.md)

---

## 3. Günlük kullanım (sistem ayaktayken)

| İhtiyaç | Ne yaparsın |
|---------|-------------|
| Manuel post | Bota DM → `/yeni` şablonu |
| RSS’den post | WF-02 Active (Schedule) veya Manual Trigger |
| Onay / yayın | Gruptaki butonlar (WF-04) |
| Hata | WF-03 → Telegram HATA + `social_media_errors` |

n8n’i her içerik için açmana gerek yok; tunnel + n8n + WF-04 Active yeterli.

---

## 4. Kapatma

```bash
cd ~/Desktop/sosyal-medya-icerik-ajani
docker compose down
```

- Tunnel terminalini `Ctrl+C` ile kapat.  
- **`docker compose down -v` kullanma** (veri silinir).

---

## 5. Volume silindiyse veya yeni bilgisayar

1. Repo’yu klonla / klasörü kopyala.  
2. `.env.example` → `.env` (şifre + sonra tunnel URL).  
3. `docker compose up -d`  
4. n8n’de workflow JSON’ları **Import** et (repo kökündeki `WF-0x …json`).  
5. Credential’ları **sıfırdan** oluştur (JSON’da secret yok).  
6. Data Table şemaları → [`data-table-yapisi.md`](../data-table-yapisi.md)  
7. Tunnel + `WEBHOOK_URL` + WF-04 Active (yukarıdaki Adım B–C).  
8. WF-01/02/04 → Error Workflow = WF-03 bağla.

---

## 6. Sık sorunlar

| Belirti | Ne yap |
|---------|--------|
| Onayla / `/yeni` tepki yok | Tunnel açık mı? `.env` URL güncel mi? `docker compose up -d`? WF-04 Active + kapat-aç? |
| Tunnel URL değişti | Yeni URL → `.env` → `docker compose up -d` → WF-04 re-Activate |
| `/yeni` DM olur, grup olmaz | Bilinen durum; DM kullan |
| `can't parse entities` | Telegram Send Message → Parse Mode yok; **Append n8n Attribution OFF** |
| n8n login olmuyor | `.env` şifresi; Docker ayakta mı? |
| AI / görsel / Buffer hata | İlgili credential ve kota |

Daha fazla → [`karsilasilan-problemler.md`](../karsilasilan-problemler.md), [`cozum-notlari.md`](../cozum-notlari.md)

---

## 7. Tek bakışta checklist

```text
[ ] Docker Desktop açık
[ ] cd proje && docker compose up -d
[ ] http://localhost:5678 açılıyor (admin + .env şifre)
[ ] cloudflared tunnel --url http://localhost:5678  (terminal açık kalsın)
[ ] .env WEBHOOK_URL = yeni tunnel URL (sonunda /)
[ ] docker compose up -d
[ ] WF-03, WF-04, WF-01 Active; WF-04 bir kez kapat-aç
[ ] DM’den /yeni test → grupta taslak
```

---

## 8. İlgili dosyalar

| Dosya | İçerik |
|--------|--------|
| Bu dosya | Çalıştırma / yeniden başlatma |
| [`n8n-kurulum.md`](./n8n-kurulum.md) | İlk kurulum notları |
| [`../sistem-dokumantasyonu.md`](../sistem-dokumantasyonu.md) | Mimari |
| [`../../templates/telegram/yeni-komut-sablonu.md`](../../templates/telegram/yeni-komut-sablonu.md) | `/yeni` pin şablonu |
| [`../../.env.example`](../../.env.example) | Env örneği |
| [`../../docker-compose.yml`](../../docker-compose.yml) | n8n servisi |

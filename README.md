# Sosyal Medya İçerik Ajansı

n8n + Docker + OpenAI ile LinkedIn / Instagram içerik üretimi, Data Table kaydı ve Telegram taslak bildirimi.

## Hızlı başlangıç

```bash
cp .env.example .env   # şifreyi düzenle
docker compose up -d
```

n8n: http://localhost:5678 (kullanıcı: `admin`)

## Workflow'lar

| # | Ad | Tetikleyici | Export |
|---|-----|-------------|--------|
| 1 | Manuel İçerik Üretme | Manual | `WF-01 Manuel İçerik Üretme.json` |
| 2 | Kaynaktan İçerik Üretme | Manual (Schedule sonra) | `WF-02 Kaynaktan İçerik Üretme.json` |
| 3 | Error Handling | Error Trigger | `WF-03 Error Handling.json` |

## Repo yapısı

```
├── proje-plani.md              # Ana plan (fazlar)
├── proje-tanımı.md             # PM gereksinimleri
├── docker-compose.yml
├── docs/                       # Dokümantasyon
├── prompts/                    # AI prompt'ları
├── templates/telegram/         # Mesaj şablonları
├── WF-01 / WF-02 / WF-03.json  # n8n export'ları
```

## Dokümantasyon

- Plan → [`proje-plani.md`](./proje-plani.md)
- Docs → [`docs/README.md`](./docs/README.md)
- Problemler → [`docs/karsilasilan-problemler.md`](./docs/karsilasilan-problemler.md)
- Çözümler → [`docs/cozum-notlari.md`](./docs/cozum-notlari.md)

## Durum

**İlk versiyon tamamlandı** (Haz–Tem 2026); WF-02 Schedule eklendi.  
PM sonrası (duruma göre): execution_logs, fallback, gelişmiş onay, Bölüm 15–16 özellikleri.

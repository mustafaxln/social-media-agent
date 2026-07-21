# Akış Şeması

## Sistem Genel Akışı

```mermaid
flowchart TD
    A[İçerik Kaynağı] --> B[Veri Çekme]
    B --> C[Duplicate Kontrolü]
    C --> D[AI Agent ile İçerik Üretimi]
    D --> E[Data Table Kaydı]
    E --> F[Telegram'a Taslak Gönderimi]
    F --> G[Onay Süreci]
    G --> H[Yayın / Arşiv]
    D -.->|Hata| E3[WF-03 Error Handling]
    E -.->|Hata| E3
    F -.->|Hata| E3
```

## Workflow 1 — Manuel İçerik

```mermaid
flowchart TD
    A[Manual Trigger] --> B[Set Node]
    B --> C[AI Agent]
    C --> D[Code / telegram_message]
    D --> E[Data Table]
    E --> F[Telegram]
```

## Workflow 2 — Kaynaktan İçerik

```mermaid
flowchart TD
    A[Schedule / Manual] --> B[RSS Read]
    B --> C[Veri Temizle]
    C --> D[Duplicate Kontrol]
    D --> E[Limit 1]
    E --> F[AI Agent]
    F --> G[Code]
    G --> H[Data Table]
    H --> I[Telegram]
```

## Workflow 3 — Error Handling

```mermaid
flowchart TD
    A[Error Trigger] --> B[Hata Mesaji Code]
    B --> C[social_media_errors]
    C --> D[Telegram HATA]
```

## Onay Süreci (İlk Aşama)

```mermaid
flowchart LR
    A[İçerik Üretildi] --> B[Telegram'a Taslak Gönder]
    B --> C[Manuel Kontrol]
    C --> D{Onay?}
    D -->|Evet| E[Status: approved]
    D -->|Hayır| F[Status: rejected]
```

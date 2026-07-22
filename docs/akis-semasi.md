# Akış Şeması

## Sistem Genel Akışı

```mermaid
flowchart TD
    A[WF-01 Manuel / WF-02 RSS] --> B[Insert waiting_approval]
    B --> C[Telegram taslak Onayla/Reddet]
    C --> D{1. Onay}
    D -->|Reddet| R[rejected]
    D -->|Onayla| E[Image + Cloudinary]
    E --> F[Telegram FINAL Yayınla/İptal]
    F --> G{2. Onay}
    G -->|İptal| P[preview_rejected]
    G -->|Yayınla| H[Buffer LI/IG]
    H --> I[published]
    A -.->|Hata| E3[WF-03]
    E -.->|Hata| E3
    H -.->|Hata| E3
```

## Workflow 1 — Manuel İçerik

```mermaid
flowchart TD
    A[Manual Trigger] --> B[Set Node]
    B --> C[AI Agent]
    C --> D[Code / telegram_message]
    D --> E[Data Table]
    E --> F[Telegram buton]
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
    H --> I[Telegram buton]
```

## Workflow 3 — Error Handling

```mermaid
flowchart TD
    A[Error Trigger] --> B[Hata Mesaji Code]
    B --> C[social_media_errors]
    C --> D[Telegram HATA]
```

WF-01, WF-02, WF-04 → Error Workflow = WF-03.

## Workflow 4 — Onay + Görsel + Yayın

```mermaid
flowchart TD
    A[Telegram Callback] --> B{action}
    B -->|reject| R[rejected]
    B -->|cancel| C[preview_rejected]
    B -->|approve| G[Image + Cloudinary]
    G --> F[Final Telegram]
    B -->|publish| P[Buffer LI/IG]
    P --> S[published]
```

## 2 Kademeli Onay

```mermaid
flowchart LR
    A[Taslak] --> B[Onayla / Reddet]
    B -->|Onayla| C[Görsel + Final]
    B -->|Reddet| D[rejected]
    C --> E[Yayınla / İptal]
    E -->|Yayınla| F[published]
    E -->|İptal| G[preview_rejected]
```

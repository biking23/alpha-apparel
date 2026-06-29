# Current ER Diagram

# Table Purposes
* tickers - Stores the publically traded companies for which Alpah Apparel can generate designs
* themes - Stores reusable investment concepts that define the message of a design
* styles - Stores reusable visual identities that influence how artwork is generated
* designs - Stores unique AI-generated design concepts created from combinations of ticker, theme and style
* product_variants - Stores purchasable merchandise created from a design

# Entity Relationships

## Tickers → Designs

One ticker can have many generated designs.

Example:
* MU
  * Proud Owner
  * Diamond Hands
  * Earnings Survivor
---
## Themes → Designs

One theme can be reused across many companies.
Example:
"Proud Owner"
↓
MU
↓
NVDA
↓
RKLB

---

## Styles → Designs

One style can be reused for many generated designs.
Example:
"Vintage"
↓
Applied to every ticker.

---
## Humor Levels → Designs
One humor level can be reused across many designs.
Example:
"Meme"
↓
Diamond Hands
↓
Bought the Dip
↓
YOLO

# Future Database Expansion

* GeneratedAssets
* Users
* Orders
* Payments
* Reviews
* Analytics
* Coupons
* Inventory
* GenerationJobs

# Database Design Principles

## Alpha Principle

Every piece of data should exist exactly once.

Avoid duplicated information.

Normalize where practical.

---

## Coffee Test

Every table must represent one real-world concept that can be explained in one sentence.

---

## Design for Extension

Prefer architectures that allow new functionality to be added without modifying existing tables.

## Business Question Test
Every table exists to answer a business question. Every column exists to answer a business question

# Parking Lot - Future Ideas
* Real-time earnings-triggered merchandise.
* Trending ticker ingestion.
* AI-generated "Market of the Day" collections.
* Customer design gallery.
* Version history for prompts.
* Browse by sector.
* Personalized shareholder apparel ("I own 247 shares").


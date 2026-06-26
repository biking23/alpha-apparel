# Current ER Diagram

# Table Purposes
tickers - Stores the publically traded companies for which Alpah Apparel can generate designs
themes - Stores reusable investment concepts that define the message of a design
styles - Stores reusable visual identities that influence how artwork is generated
designs - Stores unique AI-generated design concepts created from combinations of ticker, theme and style
product_variants - Stores purchasable merchandise created from a design

# Future Database Expansion

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


---
layout: recipe
title: "Lemon Herb Chicken & Ribeye Steak with Asparagus, Mashed Potatoes"
author: "Jeffrey Heinen"
description: "A simple weeknight dinner: lemon-herb chicken and a seared ribeye with roasted asparagus and mashed potatoes."
prep_time: "PT10M"
cook_time: "PT25M"
total_time: "PT35M"
yield: "2 servings"
category: "Dinner"
cuisine: "American"
ingredients:
  - "1 boneless chicken breast (8 oz)"
  - "1 ribeye steak (8–10 oz)"
  - "1 lemon (juice + zest)"
  - "1 lb asparagus, trimmed"
  - "2 medium potatoes, peeled and diced"
  - "Olive oil"
  - "Salt"
  - "Black pepper"
  - "Garlic powder"
instructions:
  - "Potatoes: Boil until tender (10–12 min). Mash with a splash of milk, salt, and pepper."
  - "Asparagus: Toss in olive oil, roast at 425°F or air fry for about 8 minutes until tender-crisp."
  - "Chicken: Season with lemon juice, zest, garlic powder, salt, and pepper. Air fry at 375°F for about 18 minutes (or until internal temp reaches 165°F)."
  - "Steak: Season with salt and pepper. Pan-sear 3–4 minutes per side for medium-rare (adjust to preference), then rest before slicing."
---

## Ingredients

{% for ingredient in page.ingredients %}
- {{ ingredient }}
{% endfor %}

## Instructions

{% for step in page.instructions %}
{{ forloop.index }}. {{ step }}

{% endfor %}

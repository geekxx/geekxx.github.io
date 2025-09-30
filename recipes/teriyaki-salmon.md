---
layout: recipe
title: "Teriyaki Salmon with Broccoli and Jasmine Rice"
author: "Jeffrey Heinen"
description: "A quick teriyaki salmon dinner with broccoli and jasmine rice — ready in about 20 minutes."
image: "/images/teriyaki-salmon.jpg"
prep_time: "PT5M"
cook_time: "PT15M"
total_time: "PT20M"
yield: "2 servings"
category: "Dinner"
cuisine: "Japanese"
ingredients:
  - "2 salmon fillets (5–6 oz each)"
  - "1/4 cup teriyaki sauce"
  - "2 cups broccoli florets"
  - "1 cup jasmine rice"
instructions:
  - "Cook jasmine rice (1 cup rice + 1¼ cups water)."
  - "Air fry salmon at 400°F for 8–10 minutes, brushing with teriyaki sauce halfway."
  - "Steam broccoli 4–5 minutes until tender."
---

## Ingredients

{% for ingredient in page.ingredients %}
- {{ ingredient }}
{% endfor %}

## Instructions

{% for step in page.instructions %}
{{ forloop.index }}. {{ step }}

{% endfor %}


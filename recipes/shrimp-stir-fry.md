---
layout: recipe
title: "Shrimp Stir-Fry with Peppers, Snow Peas, White Rice"
author: "Jeffrey Heinen"
description: "Quick shrimp stir-fry with bell pepper, snow peas, garlic, and white rice."
prep_time: "PT5M"
cook_time: "PT15M"
total_time: "PT20M"
yield: "2 servings"
category: "Dinner"
cuisine: "Asian"
ingredients:
  - "10 oz shrimp, peeled and deveined"
  - "1 red bell pepper, sliced"
  - "1 cup snow peas"
  - "2 garlic cloves, minced"
  - "2 tbsp soy sauce"
  - "1 tbsp sesame oil"
  - "1 cup white rice"
instructions:
  - "Cook rice (1 cup rice + 1¼ cups water)."
  - "Heat sesame oil in Instant Pot (sauté mode). Add garlic, peppers, snow peas, stir 2–3 min."
  - "Add shrimp and soy sauce. Cook until shrimp are pink (about 3 minutes). Serve over rice."
---

## Ingredients

{% for ingredient in page.ingredients %}
- {{ ingredient }}
{% endfor %}

## Instructions

{% for step in page.instructions %}
{{ forloop.index }}. {{ step }}

{% endfor %}

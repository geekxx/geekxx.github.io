# geekxx.github.io

<!-- Recipe page using schema.org microdata so AnyList (and other recipe importers) can read it -->
<div itemscope itemtype="https://schema.org/Recipe">
  <h1 itemprop="name">Teriyaki Salmon with Broccoli and Jasmine Rice</h1>

  <!-- Optional: include an image if you publish this page so importers can grab it -->
  <img itemprop="image" src="/images/teriyaki-salmon.jpg" alt="Teriyaki Salmon with Broccoli and Jasmine Rice" />

  <p><strong>Author:</strong> <span itemprop="author">Jeffrey Heinen</span></p>
  <p itemprop="description">A quick teriyaki salmon dinner with broccoli and jasmine rice — ready in about 20 minutes.</p>

  <h2>Ingredients</h2>
  <ul>
    <li itemprop="recipeIngredient">2 salmon fillets (5–6 oz each)</li>
    <li itemprop="recipeIngredient">¼ cup teriyaki sauce</li>
    <li itemprop="recipeIngredient">2 cups broccoli florets</li>
    <li itemprop="recipeIngredient">1 cup jasmine rice</li>
  </ul>

  <h2>Instructions</h2>
  <ol>
    <li itemprop="recipeInstructions" itemscope itemtype="https://schema.org/HowToStep">
      <span itemprop="text">Cook jasmine rice (1 cup rice + 1¼ cups water).</span>
    </li>
    <li itemprop="recipeInstructions" itemscope itemtype="https://schema.org/HowToStep">
      <span itemprop="text">Air fry salmon at 400°F for 8–10 minutes, brushing with teriyaki sauce halfway.</span>
    </li>
    <li itemprop="recipeInstructions" itemscope itemtype="https://schema.org/HowToStep">
      <span itemprop="text">Steam broccoli 4–5 minutes until tender.</span>
    </li>
  </ol>

  <meta itemprop="prepTime" content="PT5M" />
  <meta itemprop="cookTime" content="PT15M" />
  <meta itemprop="totalTime" content="PT20M" />
  <meta itemprop="recipeYield" content="2 servings" />
  <meta itemprop="recipeCategory" content="Dinner" />
  <meta itemprop="recipeCuisine" content="Japanese" />
</div>

<!-- JSON-LD fallback: many scrapers prefer JSON-LD; include it alongside microdata for compatibility -->
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Recipe",
  "name": "Teriyaki Salmon with Broccoli and Jasmine Rice",
  "author": { "@type": "Person", "name": "Jeffrey Heinen" },
  "description": "A quick teriyaki salmon dinner with broccoli and jasmine rice — ready in about 20 minutes.",
  "image": ["/images/teriyaki-salmon.jpg"],
  "recipeIngredient": [
    "2 salmon fillets (5–6 oz each)",
    "1/4 cup teriyaki sauce",
    "2 cups broccoli florets",
    "1 cup jasmine rice"
  ],
  "recipeInstructions": [
    { "@type": "HowToStep", "text": "Cook jasmine rice (1 cup rice + 1¼ cups water)." },
    { "@type": "HowToStep", "text": "Air fry salmon at 400°F for 8–10 minutes, brushing with teriyaki sauce halfway." },
    { "@type": "HowToStep", "text": "Steam broccoli 4–5 minutes until tender." }
  ],
  "prepTime": "PT5M",
  "cookTime": "PT15M",
  "totalTime": "PT20M",
  "recipeYield": "2 servings",
  "recipeCategory": "Dinner",
  "recipeCuisine": "Japanese"
}
</script>

## Importing into AnyList

AnyList can import recipes from webpages that contain schema.org Recipe microdata or JSON-LD. To import this recipe:

1. Publish or open the recipe page (the page that contains the HTML above) in your browser.
2. In AnyList, choose "Import Recipe" or "Import from Website" and paste the page URL, or use the AnyList browser extension/web importer if available.

Notes:
- Microdata attributes used: name, author, description, image, recipeIngredient, recipeInstructions, prepTime, cookTime, totalTime, recipeYield, recipeCategory, recipeCuisine.
- The JSON-LD block is included as a fallback and increases compatibility with scrapers and importers.

If you want me to add this markup to all recipe pages or to your site templates (for example, in Jekyll/Eleventy layouts), tell me which templating system you're using and I will update the templates accordingly.


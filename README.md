<p align="center">
  <img src="https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/mascot.png" alt="g2 scraper" />
</p>
<div align="center" style="margin-top: 0;">
  <h1>✨ G2 Scraper 🤖</h1>
  <p><strong>Scrape G2 product details, reviews, pricing, and ratings — plus every product's website, emails, phones, and social profiles. Clean JSON, no blocks, no proxies.</strong></p>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="g2-scraper forks" src="https://img.shields.io/github/forks/omkarcloud/g2-scraper?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/g2-scraper?style=for-the-badge&color=yellow" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/g2-scraper.svg" width="80px" height="28px" alt="View" />
</p>

G2 Scraper turns any G2 product page into clean JSON without the headache of blocks or managing proxies. Feed it a product slug or URL and get 40+ fields including G2 product details, reviews, pricing, and ratings.

Every product also comes with its website and the contacts found on it — emails, phone numbers, social profiles, and the technologies it runs — extracted by our open-source [Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper). And since only ~2% of G2 products list a website on their profile, we use AI to find it for the rest (`likely_product_website`).

For reviews, G2 itself stops serving them after page 10 — when you paginate past that, we automatically combine multiple filters behind the scenes to keep the reviews coming, giving you more reviews than G2 provides on its own.

- **Rated Excellent — 4.6 based on 25 reviews** on [Trustpilot](https://www.trustpilot.com/review/omkar.cloud). Our open source work is sponsored by [1000+ devs on GitHub](https://github.com/sponsors/omkarcloud).

[![Try the G2 Scraper API in the live playground — free, no signup](https://img.shields.io/badge/%E2%96%B6%20Playground-Run%20a%20live%20request%2C%20free-brightgreen?style=for-the-badge)](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=badge)

[![Free Plan: 100 requests per month](https://img.shields.io/badge/Free%20tier-100%20requests%2Fmonth-blue?style=for-the-badge)](#pricing)

The same scraper is also available on **Apify** and **RapidAPI**:

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-blue)](https://apify.com/omkar-cloud/g2-product-scraper) [![Run on RapidAPI](https://img.shields.io/badge/Run%20on-RapidAPI-blue?logo=rapidapi)](https://rapidapi.com/pradeepbardiya13/api/g2-data-api/playground/apiendpoint_452c117f-94ea-4d03-a158-4953226954aa)

[![G2 Scraper API playground — run a live request in your browser, free, no signup](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/g2-scraper-playground.png)](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=hero-image)

## Example: G2 Product Data in One Request

One request to the G2 products API:

```
GET https://g2-scraper.omkar.cloud/g2/products?product=postman
```

```json
{
  "product_id": 20238,
  "product_name": "Postman",
  "rating": 4.6,
  "reviews": 1800,
  "product_website": null,
  "likely_product_website": "https://www.postman.com",
  "website_contacts": {
    "domain": "www.postman.com",
    "emails": [
      {
        "value": "info@postman.com",
        "sources": ["https://www.postman.com/company/contact-us/"],
        "is_likely_official": true
      },
      {
        "value": "help@postman.com",
        "sources": ["https://www.postman.com/company/contact-sales/"],
        "is_likely_official": false
      }
    ],
    "phones": [
      {
        "value": "+18886161665",
        "sources": ["https://www.postman.com/company/contact-sales/"],
        "is_likely_official": true
      }
    ],
    "linkedins": [
      { "value": "https://www.linkedin.com/company/postman-platform", "is_likely_official": true }
    ],
    "twitters": [
      { "value": "https://x.com/getpostman", "is_likely_official": true }
    ],
    "instagrams": [
      { "value": "https://www.instagram.com/getpostman", "is_likely_official": true }
    ],
    "discords": [
      { "value": "https://discord.gg/58aNNsRBGR", "is_likely_official": true }
    ],
    "githubs": [
      { "value": "https://github.com/postmanlabs", "is_likely_official": true }
    ],
    "technologies": [
      { "name": "Amazon Web Services", "categories": ["PaaS"] },
      { "name": "Cloudflare", "categories": ["CDN"] }
    ]
  },
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "seller": "Postman",
  "what_is": "Postman is the world's leading API platform, used by more than 30 million developers and 500,000 organizations worldwide for building and managing APIs.",
  "category": { "name": "API Platforms", "link": "https://www.g2.com/categories/api-platforms" },
  "company_location": "San Francisco, CA",
  "company_founded_year": 2014,
  "company_website": "https://www.postman.com",
  "number_of_employees_on_linkedin": 2305,
  "pricing_plans": [
    {
      "plan_name": "Free Plan",
      "plan_price": "Free",
      "plan_description": "For individuals or a small team of 3 or less to start testing APIs.",
      "plan_features": ["Up to 3 collaborators"]
    }
  ],
  "alternatives": [
    { "name": "MuleSoft Anypoint Platform", "link": "https://www.g2.com/products/mulesoft-anypoint-platform/reviews", "rating": 4, "reviews": 655 }
  ],
  "comparisons": [
    { "name": "SwaggerHub", "link": "https://www.g2.com/compare/postman-vs-swaggerhub" }
  ]
}
```

*Trimmed for readability — the full response has 40+ fields. See the [sample response](#product-details--reviews) in the API reference.*

Postman doesn't list a website on its G2 profile (`product_website: null`) — like ~98% of G2 products. We find it with AI (`likely_product_website`), then crawl it with our open-source **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)** to pull the emails, phone numbers, and social profiles you see above.

**[Run this exact request in the Playground — no signup, no key →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=example)**

The playground comes prefilled with this request and runs it against the live API in your browser. The JSON it returns is identical to what the API returns.

## Start Getting Data in Minutes

Python and Node.js integration examples are available for every endpoint in the playground, so you can get G2 data in minutes instead of days.

```python
import requests

# Scrape G2 reviews and pricing for a product
response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/products",
    params={"product": "postman"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

## API Reference

### Product Details & Reviews

▶ [Try it live in the Playground — no key needed →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-products)

```
GET https://g2-scraper.omkar.cloud/g2/products?product=postman
```

Accepts a G2 product slug (`postman`) or full product link. Optional `website_contacts_crawl_mode` controls contact enrichment: `homepage` (default — scan the website's homepage), `deep` (also crawl its top contact-like pages: contact, about, careers, blog), or `off`.

#### Response

Returns the product's website and the contacts found on it (emails, phone numbers, social profiles, and technologies as `website_contacts`), plus 40+ fields including rating, pricing plans, features, alternatives, comparisons, company details, and social profiles.

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "product_id": 20238,
  "product_name": "Postman",
  "rating": 4.6,
  "reviews": 1800,
  "product_website": null,
  "likely_product_website": "https://www.postman.com",
  "website_contacts": {
    "domain": "www.postman.com",
    "title": "Postman: The World's Leading API Platform | Sign Up for Free",
    "description": "Accelerate API development with Postman's all-in-one platform. Streamline collaboration and simplify the API lifecycle for faster, better results. Learn more.",
    "emails": [
      {
        "value": "info@postman.com",
        "sources": [
          "https://www.postman.com/company/contact-us/",
          "https://www.postman.com/company/about-postman/"
        ],
        "is_likely_official": true
      },
      {
        "value": "help@postman.com",
        "sources": ["https://www.postman.com/company/contact-sales/"],
        "is_likely_official": false
      }
    ],
    "phones": [
      {
        "value": "+18886161665",
        "sources": ["https://www.postman.com/company/contact-sales/"],
        "is_likely_official": true
      },
      {
        "value": "+14157966470",
        "sources": ["https://www.postman.com/company/contact-us/"],
        "is_likely_official": false
      }
    ],
    "linkedins": [
      {
        "value": "https://www.linkedin.com/company/postman-platform",
        "sources": ["https://www.postman.com/"],
        "is_likely_official": true
      }
    ],
    "twitters": [
      { "value": "https://x.com/getpostman", "sources": ["https://www.postman.com/"], "is_likely_official": true }
    ],
    "instagrams": [
      { "value": "https://www.instagram.com/getpostman", "sources": ["https://www.postman.com/"], "is_likely_official": true }
    ],
    "facebooks": [
      { "value": "https://www.facebook.com/getpostman", "sources": ["https://www.postman.com/company/contact-us/"], "is_likely_official": true }
    ],
    "youtubes": [
      { "value": "https://www.youtube.com/channel/UCocudCGVb3MmhWQ1aoIgUQw", "sources": ["https://blog.postman.com/"], "is_likely_official": true }
    ],
    "discords": [
      { "value": "https://discord.gg/58aNNsRBGR", "sources": ["https://www.postman.com/"], "is_likely_official": true }
    ],
    "githubs": [
      { "value": "https://github.com/postmanlabs", "sources": ["https://www.postman.com/"], "is_likely_official": true }
    ],
    "technologies": [
      { "name": "Amazon Cloudfront", "versions": [], "categories": ["CDN"] },
      { "name": "Amazon Web Services", "versions": [], "categories": ["PaaS"] },
      { "name": "Cloudflare", "versions": [], "categories": ["CDN"] }
    ],
    "error": null
  },
  "product_uuid": "06ab3e14-7ed4-4cc9-b6a6-12b92b7fe34c",
  "company_id": 16505,
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "category": {
    "name": "API Platforms",
    "link": "https://www.g2.com/categories/api-platforms"
  },
  "product_logo": "https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_fd527e1fc777d9e31b2a28e8d3c959a4/postman.jpg",
  "what_is": "Postman is the world's leading API platform, used by more than 30 million developers and 500,000 organizations worldwide for building and managing APIs.",
  "product_description": "Postman enables teams to efficiently collaborate at every stage of the API lifecycle while prioritizing quality, performance, and security.",
  "medal_image": "https://images.g2crowd.com/uploads/report_medal/image/1004859/medal.svg",
  "seller": "Postman",
  "company_location": "San Francisco, CA",
  "company_founded_year": 2014,
  "discussions_link": "https://community.postman.com/",
  "twitter": "https://twitter.com/getpostman",
  "number_of_followers_on_twitter": 51725,
  "linkedin": "https://www.linkedin.com/company/3795851/",
  "number_of_employees_on_linkedin": 2305,
  "company_website": "https://www.postman.com",
  "is_claimed": true,
  "categories": [
    { "name": "Software Testing", "link": "https://www.g2.com/categories/software-testing" },
    { "name": "Build Automation", "link": "https://www.g2.com/categories/build-automation" }
  ],
  "pricing_plans": [
    {
      "plan_name": "Free Plan",
      "plan_price": "Free",
      "plan_description": "For individuals or a small team of 3 or less to start testing APIs.",
      "plan_features": ["Up to 3 collaborators"]
    }
  ],
  "alternatives": [
    { "name": "MuleSoft Anypoint Platform", "link": "https://www.g2.com/products/mulesoft-anypoint-platform/reviews", "rating": 4, "reviews": 655 }
  ],
  "comparisons": [
    { "link": "https://www.g2.com/compare/postman-vs-swaggerhub", "name": "SwaggerHub", "logo": "https://images.g2crowd.com/uploads/product/image/small_square/small_square_7ca4052dc540756d666b98eb073a3e58/swaggerhub.png" }
  ],
  "features": [
    { "name": "API Construction", "features": ["API Testing"] }
  ],
  "detailed_features": [
    {
      "name": "API Construction",
      "features": [
        {
          "name": "API Testing",
          "content": "Based on 589 Postman reviews. Provides an environment for users to test their API's functionality, efficiency, and data accuracy.",
          "percentage": 94,
          "based_on_number_of_reviews": 589
        }
      ]
    }
  ],
  "g2_reviews_link": "https://www.g2.com/products/postman/reviews#reviews"
}
```

</details>

---

### Products by Category

▶ [Try it live in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-categories)

```
GET https://g2-scraper.omkar.cloud/g2/categories?category=marketing-automation
```

Accepts a G2 category slug (`marketing-automation`) or full category link. Optional: `page` (15 products per page) and `sort` (`g2-score` default, `popularity`, `satisfaction`).

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "category_link": "https://www.g2.com/categories/marketing-automation",
  "count": 408,
  "results": [
    {
      "name": "HubSpot Marketing Hub",
      "link": "https://www.g2.com/products/hubspot-marketing-hub/reviews",
      "users": ["Marketing Manager", "Marketing Coordinator"],
      "industries": ["Computer Software", "Marketing and Advertising"],
      "market_segments": ["54% Small-Business", "40% Mid-Market"]
    },
    {
      "name": "Insider",
      "link": "https://www.g2.com/products/insider/reviews",
      "users": ["Digital Marketing Manager", "Digital Marketing Specialist"],
      "industries": ["Retail", "Apparel & Fashion"],
      "market_segments": ["45% Mid-Market", "29% Small-Business"]
    }
  ]
}
```

</details>

---

### Category Links

Get every G2 category link — a directory of all 2,000+ categories you can feed into the Products by Category endpoint.

▶ [Try it live in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-category-links)

```
GET https://g2-scraper.omkar.cloud/g2/category-links
```

No parameters required.

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 2227,
  "links": [
    "https://www.g2.com/categories/zoho-consulting",
    "https://www.g2.com/categories/hr-analytics-consulting",
    "https://www.g2.com/categories/brand-advocacy-services"
  ]
}
```

</details>

---

### Product Links

Get every G2 product link — a directory of all 240,000+ products you can feed into the Product Details endpoint.

▶ [Try it live in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-product-links)

```
GET https://g2-scraper.omkar.cloud/g2/product-links
```

No parameters required.

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 240975,
  "links": [
    "https://www.g2.com/products/24sevenoffice/reviews",
    "https://www.g2.com/products/basecamp/reviews",
    "https://www.g2.com/products/adobe-acrobat-sign/reviews"
  ]
}
```

</details>

## Pricing

| Plan | Price | Requests/Month |
|------|-------|----------------|
| Free | $0 | 100 |
| Grow | $48 | 15,000 |
| Scale | $148 | 75,000 |

1 API call = 1 request

Free Plan Available — [create your API key →](https://www.omkar.cloud/auth/sign-up?redirect=/api-key&utm_source=github&utm_medium=cpc&utm_content=pricing-signup). No credit card for the free tier.

## G2 Dataset Downloads

Free to download, no signup: [240,975 G2 product links (4.8MB)](https://www.omkar.cloud/downloads/g2-products-links.json) · [2,227 G2 category links (128KB)](https://www.omkar.cloud/downloads/g2-categories-links.json)

The API serves pre-crawled data that may be a few months old — fine for competitive research, lead generation, and market analysis. If you need the newest reviews across all 240,975 products, the full refreshed dataset is available for purchase: [WhatsApp us](https://api.whatsapp.com/send?phone=918178804274&text=I%20want%20to%20buy%20the%20full%20G2%20dataset.) or [email us](mailto:happy.to.help@omkar.cloud?subject=Full%20G2%20Dataset).

## FAQs

### Can I try the API before signing up?

Yes. The playground runs live requests in your browser — free, no account, no API key. [Try it in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=faq)

### How does the API find product emails, phone numbers, and social profiles?

Only ~2% of G2 products list a website on their G2 profile. For the other 98%, we use AI to find the product's real website — returned as `likely_product_website`. That website is then crawled by our open-source **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)**, and every email, phone number, social profile, and technology it finds comes back as `website_contacts`, each with the source pages and an `is_likely_official` flag.

Want the same contact extraction for any website, free? **[Get the Website Email Contact Scraper on GitHub →](https://github.com/omkarcloud/website-email-contact-scraper)**

### How many reviews can I get per product?

Reviews come 10 per page. G2 itself caps every filter combination at 10 pages — but when you paginate past page 10, we automatically apply multiple filter combinations (stars, company segment, and more) behind the scenes and keep serving fresh reviews, giving you more than G2 provides on its own.

### How do I discover products and categories to scrape?

Use the **Product Links** and **Category Links** endpoints. They return the complete directory — 240,975 products and 2,227 categories — so you can crawl G2 end to end without guessing URLs.

Prefer files? Download the full directories directly, free: [240,975 G2 product links (4.8MB)](https://www.omkar.cloud/downloads/g2-products-links.json) · [2,227 G2 category links (128KB)](https://www.omkar.cloud/downloads/g2-categories-links.json)

### How do I scrape G2 reviews?

Call the reviews endpoint with a product slug or URL:

```
GET https://g2-scraper.omkar.cloud/g2/reviews?product=postman&page=1
```

It returns 10 reviews per page — full text, ratings, reviewer name, job title, company size, and publish date — and supports filters for stars, company segment, industry, reviewer role, region, keywords, and sort order.

G2 itself stops serving reviews after page 10. When you paginate past that, we automatically combine multiple filters behind the scenes to keep the reviews coming — so you get more reviews than G2 provides on its own.

### What data does the API return?

**Product Details & Reviews** returns 40+ fields per product:
- Product name, logo, description, and G2 link
- Overall rating and total review count
- The product's website — AI-found when the G2 profile doesn't list it (`likely_product_website`)
- Website contacts — emails, phone numbers, social profiles, and technologies, extracted by our open-source [Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)
- Pricing plans with features
- Features and detailed feature scores (with % and review counts)
- Alternatives and head-to-head comparisons
- Company info — seller, location, founded year, employee count
- Social profiles — Twitter, LinkedIn, follower counts
- Categories

**Products by Category** returns per product:
- Product name and G2 link
- Common user job titles
- Top industries
- Market segment split (Small-Business, Mid-Market, Enterprise)

**Category Links** and **Product Links** return the full directory of category and product URLs, with a total count.

### How accurate is the data?

The data comes straight from real G2 profiles — real ratings, reviews, pricing, and company details.

### How fresh is the data, and how do I get the newest?

API responses come from a pre-crawled dataset that may be a few months old. For the newest reviews across the full catalog, see [G2 Dataset Downloads](#g2-dataset-downloads).

### Will I get blocked or need proxies?

No. We handle the scraping infrastructure — you call a normal REST API and never touch G2 directly, so there are no proxies, headless browsers, or CAPTCHAs on your side.

### Can I pass a slug instead of a full URL?

Yes. Product Details and Products by Category accept either a slug (`postman`, `marketing-automation`) or a full G2 URL. Use whichever you have.

## More Review-Data Scrapers: Google Maps, Capterra & Trustpilot

- **[Google Maps Scraper (3,100+ GitHub Stars)](https://github.com/omkarcloud/google-maps-scraper)** — need tens of thousands ofleads?  Type a niche and a city ("dentists in New York") and get every matching business as a ready-to-call lead list — name, address, phone, website, emails, rating, and reviews. The free tier alone pulls up to 100K leads a month, enough to run your entire outreach pipeline on $0.

- **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)** — the same contact engine this API uses, free and open source: point it at any website and get every email, phone number, and social profile on it, each with source pages and an official/unofficial flag.

- **[Capterra Scraper API](https://github.com/omkarcloud/capterra-scraper)** — the same clean JSON, pointed at Capterra: 5-dimension rating breakdowns, pricing plans, integrations, pros/cons for 108,726 products.

- **[Trustpilot Scraper API](https://github.com/omkarcloud/trustpilot-scraper)** — real-time Trustpilot data for 1.6M+ companies: search companies by keyword, full profiles with rating distributions, every review for any domain. 200 free requests/month.

## Video Tutorial

Prefer a walkthrough? Watch the complete API demo:

[![G2 Scraper API Walkthrough](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/g2-scraper-youtube-video-preview.png)](https://www.youtube.com/watch?v=oo7OIek2WDY)

## Support

Built by developers, for developers — when you reach out, you talk to the engineers who built the API, not a support script. Message us anytime and we'll solve your query within 1 working day.


[![Contact Us on WhatsApp about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20G2%20Scraper%20API.)

Email: [happy.to.help@omkar.cloud](mailto:happy.to.help@omkar.cloud?subject=G2%20Scraper%20API%20Question)

[![Email Us about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=G2%20Scraper%20API%20Question)

## Love It? Star It! ⭐

From one developer to another: If the G2 Scraper API saved you time, please [star the repo](https://github.com/omkarcloud/g2-scraper).

Here's why it matters: most developers judge a scraper by its stars before trying it. Your star helps the next developer — someone deciding whether the G2 data here is real and reliable — try it with confidence.

It takes only 1 second, and means the world to me.

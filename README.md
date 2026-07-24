# G2 Scraper API

Scrape G2 product details, reviews, ratings, pricing, and full category listings via a simple REST API. Feed it a slug or URL, get clean structured JSON back — 40+ fields per product, including star distribution, pricing plans, features, alternatives, company info, and up to 2,500 reviews.

- **Rated Excellent — 4.6 based on 21 reviews** on [Trustpilot](https://www.trustpilot.com/review/omkar.cloud). Our open source work is sponsored by [1000+ devs on GitHub](https://github.com/sponsors/omkarcloud).

[![Try the G2 Scraper API in the live playground — free, no signup](https://img.shields.io/badge/%E2%96%B6%20Playground-Run%20a%20live%20request%2C%20free-brightgreen?style=for-the-badge)](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=badge)

[![Free Plan: 100 requests per month](https://img.shields.io/badge/Free%20tier-100%20requests%2Fmonth-blue?style=for-the-badge)](#pricing)

[![G2 Scraper API playground — run a live request in your browser, free, no signup](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/g2-scraper-playground.png)](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=hero-image)

## Example: G2 Product Data in One Request

One request to the G2 reviews API:

```
GET https://g2-scraper.omkar.cloud/g2/products?product=postman&max_reviews=100
```

```json
{
  "product_name": "Postman",
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "seller": "Postman",
  "what_is": "Postman is the world's leading API platform, used by more than 30 million developers and 500,000 organizations worldwide for building and managing APIs.",
  "product_description": "Postman enables teams to efficiently collaborate at every stage of the API lifecycle while prioritizing quality, performance, and security.",
  "rating": 4.6,
  "reviews": 1194,
  "star_distribution": { "1": 5, "2": 0, "3": 10, "4": 191, "5": 988 },
  "popular_mentions": ["Api development", "Api testing"],
  "category": { "name": "API Platforms", "link": "https://www.g2.com/categories/api-platforms" },
  "categories": [
    { "name": "Software Testing", "link": "https://www.g2.com/categories/software-testing" },
    { "name": "Build Automation", "link": "https://www.g2.com/categories/build-automation" }
  ],
  "company_location": "San Francisco, CA",
  "company_founded_year": 2014,
  "company_website": "https://www.postman.com",
  "number_of_employees_on_linkedin": 2305,
  "number_of_followers_on_twitter": 51725,
  "pricing_plans": [
    {
      "plan_name": "Free Plan",
      "plan_price": "Free",
      "plan_description": "For individuals or a small team of 3 or less to start testing APIs.",
      "plan_features": ["Up to 3 collaborators"]
    }
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
  "alternatives": [
    { "name": "MuleSoft Anypoint Platform", "link": "https://www.g2.com/products/mulesoft-anypoint-platform/reviews", "rating": 4, "reviews": 655 }
  ],
  "comparisons": [
    { "name": "SwaggerHub", "link": "https://www.g2.com/compare/postman-vs-swaggerhub" }
  ],
  "all_reviews": [
    {
      "review_title": "Great tool for API testing and managment",
      "review_content": "The postman gives feature of customer environment which really helps to manage your API's requirements and secure keys...",
      "review_question_answers": [
        {
          "question": "What do you like best about Postman?",
          "answer": "The postman gives feature of customer environment which really helps to manage your API's requirements and secure keys..."
        }
      ],
      "review_rating": 4.0,
      "reviewer": {
        "reviewer_name": "Chetan P.",
        "reviewer_job_title": "Fullstack Developer"
      },
      "reviewer_company_size": "Enterprise(> 1000 emp.)",
      "review_link": "https://www.g2.com/products/postman/reviews/postman-review-9712982"
    }
  ]
}
```

*Trimmed for readability — the full response has 40+ fields. See the [sample response](#product-details--reviews) in the API reference.*

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
GET https://g2-scraper.omkar.cloud/g2/products?product=postman&max_reviews=100
```

Accepts a G2 product slug (`postman`) or full product link. `max_reviews` is optional (default `2500`).

#### Response

Returns 40+ fields including rating, star distribution, up to 2,500 reviews, pricing plans, features, alternatives, comparisons, company details, and social profiles.

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "product_id": 20238,
  "product_name": "Postman",
  "product_logo": "https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_fd527e1fc777d9e31b2a28e8d3c959a4/postman.jpg",
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "what_is": "Postman is the world's leading API platform, used by more than 30 million developers and 500,000 organizations worldwide for building and managing APIs.",
  "product_description": "Postman enables teams to efficiently collaborate at every stage of the API lifecycle while prioritizing quality, performance, and security.",
  "reviews": 1194,
  "rating": 4.6,
  "medal_image": "https://images.g2crowd.com/uploads/report_medal/image/1004859/medal.svg",
  "category": {
    "name": "API Platforms",
    "link": "https://www.g2.com/categories/api-platforms"
  },
  "company_id": 16505,
  "seller": "Postman",
  "company_location": "San Francisco, CA",
  "company_founded_year": 2014,
  "discussions_link": "https://community.postman.com/",
  "twitter": "https://twitter.com/getpostman",
  "number_of_followers_on_twitter": 51725,
  "linkedin": "https://www.linkedin.com/company/3795851/",
  "number_of_employees_on_linkedin": 2305,
  "product_website": "https://www.postman.com/api-network/",
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
  "star_distribution": { "1": 5, "2": 0, "3": 10, "4": 191, "5": 988 },
  "popular_mentions": ["Api development", "Api testing"],
  "g2_reviews_link": "https://www.g2.com/products/postman/reviews#reviews",
  "all_reviews": [
    {
      "review_id": 9712982,
      "review_title": "Great tool for API testing and managment",
      "review_content": "What do you like best about Postman?\nThe postman gives feature of customer environment which really helps to manage your API's requirements and secure keys...",
      "review_question_answers": [
        {
          "question": "What do you like best about Postman?",
          "answer": "The postman gives feature of customer environment which really helps to manage your API's requirements and secure keys..."
        }
      ],
      "review_rating": 4.0,
      "reviewer": {
        "reviewer_name": "Chetan P.",
        "reviewer_job_title": "Fullstack Developer",
        "reviewer_link": "https://www.g2.com/users/9bcd50ba-ba77-46d4-9477-7dd15087e7ef"
      },
      "publish_date": "2024-06-09T00:00:00",
      "reviewer_company_size": "Enterprise(> 1000 emp.)",
      "video_link": null,
      "review_link": "https://www.g2.com/products/postman/reviews/postman-review-9712982"
    }
  ]
}
```

</details>

---

### Products by Category

▶ [Try it live in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-categories)

```
GET https://g2-scraper.omkar.cloud/g2/categories?category=marketing-automation
```

Accepts a G2 category slug (`marketing-automation`) or full category link. `max_reviews` is optional (default `2500`).

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
  "count": 2162,
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

Get every G2 product link — a directory of all 185,000+ products you can feed into the Product Details endpoint.

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
  "count": 185648,
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

1 API call = 1 request, regardless of `max_reviews` or how many results come back. Rate limits are monthly quotas per plan — there is no per-second throttling to engineer around.

Every plan starts free — [create your API key →](https://www.omkar.cloud/auth/sign-up?redirect=/api-key&utm_source=github&utm_medium=cpc&utm_content=pricing-signup). No credit card for the free tier.

## G2 Dataset Downloads

Free to download, no signup: [185,648 G2 product links](https://www.omkar.cloud/downloads/g2-products-links.json) · [2,162 G2 category links](https://www.omkar.cloud/downloads/g2-categories-links.json)

The API serves pre-crawled data that may be a few months old — fine for competitive research, lead generation, and market analysis. If you need the newest reviews across all 185,648 products, the full refreshed dataset is available for purchase: [WhatsApp us](https://api.whatsapp.com/send?phone=918178804274&text=I%20want%20to%20buy%20the%20full%20G2%20dataset.) or [email us](mailto:happy.to.help@omkar.cloud?subject=Full%20G2%20Dataset).

## FAQs

### Can I try the API before signing up?

Yes. The playground runs live requests in your browser — free, no account, no API key. [Try it in the Playground →](https://www.omkar.cloud/tools/g2-scraper/playground?utm_source=github&utm_medium=cpc&utm_content=faq)

### How do I scrape G2 reviews?

Call the [Product Details & Reviews](#product-details--reviews) endpoint with a product slug or URL. It returns up to 2,500 reviews per product — full text, ratings, reviewer name, job title, company size, and publish date. Control the volume with the `max_reviews` parameter.

### What data does the API return?

**Product Details & Reviews** returns 40+ fields per product:
- Product name, logo, description, and G2 link
- Overall rating, total review count, and star distribution
- Every review — title, full text, question/answer breakdown, rating, publish date, reviewer name, job title, and company size
- Pricing plans with features
- Features and detailed feature scores (with % and review counts)
- Alternatives and head-to-head comparisons
- Company info — seller, location, founded year, employee count
- Social profiles — Twitter, LinkedIn, follower counts
- Categories and popular mentions

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

### How many reviews can I get per product?

Up to 2,500 reviews per product. Control the volume with the `max_reviews` parameter — set it low for fast lookups, or leave it at the default to pull everything.

### How do I discover products and categories to scrape?

Use the **Product Links** and **Category Links** endpoints. They return the complete directory — 185,648 products and 2,162 categories — so you can crawl G2 end to end without guessing URLs.

Prefer files? Download the full directories directly, free: [185,648 G2 product links](https://www.omkar.cloud/downloads/g2-products-links.json) · [2,162 G2 category links](https://www.omkar.cloud/downloads/g2-categories-links.json)

## Video Tutorial

Prefer a walkthrough? Watch the complete API demo:

[![G2 Scraper API Walkthrough](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/g2-scraper-youtube-video-preview.png)](https://www.youtube.com/watch?v=oo7OIek2WDY)

## Support

Built by developers, for developers — when you reach out, you talk to the engineers who built the API, not a support script. Message us anytime and we'll solve your query within 1 working day.

[![Contact Us on WhatsApp about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20G2%20Scraper%20API.)

[![Contact Us on Email about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=G2%20Scraper%20API%20Question)

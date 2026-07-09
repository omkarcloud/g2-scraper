# G2 Scraper API

Scrape G2 product details, reviews, ratings, pricing, and full category listings via a simple REST API. Feed it a slug or URL, get clean structured JSON back. Start free with 100 requests/month — no credit card required.

## Key Features

- Get full G2 product profiles, browse products by category, and pull the complete product/category directory — all via 1 API.
- 100 free requests per month. No credit card required.

Here's a sample response for a **product details** request:

```json
{
  "product_name": "Postman",
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "seller": "Postman",
  "rating": 4.6,
  "reviews": 1194,
  "category": {
    "name": "API Platforms",
    "link": "https://www.g2.com/categories/api-platforms"
  },
  "star_distribution": { "1": 5, "2": 0, "3": 10, "4": 191, "5": 988 },
  "pricing_plans": [
    {
      "plan_name": "Free Plan",
      "plan_price": "Free",
      "plan_description": "For individuals or a small team of 3 or less to start testing APIs."
    }
  ]
}
```

## Get API Key

Create an account at [omkar.cloud](https://www.omkar.cloud/auth/sign-up?redirect=/api-key) to get your API key.

It takes just 2 minutes to sign up. You get 100 free requests every month for detailed G2 data.

This is a well built product, and your search for the best G2 Scraper API ends right here.

## Quick Start

```bash
curl -X GET "https://g2-scraper.omkar.cloud/g2/products?product=postman" \
  -H "API-Key: YOUR_API_KEY"
```

```json
{
  "product_name": "Postman",
  "g2_link": "https://www.g2.com/products/postman/reviews",
  "seller": "Postman",
  "rating": 4.6,
  "reviews": 1194,
  "category": {
    "name": "API Platforms",
    "link": "https://www.g2.com/categories/api-platforms"
  },
  "star_distribution": { "1": 5, "2": 0, "3": 10, "4": 191, "5": 988 }
}
```

## Quick Start (Python)

```bash
pip install requests
```

```python
import requests

# Get full product details
response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/products",
    params={"product": "postman"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

## API Reference

### Product Details

```
GET https://g2-scraper.omkar.cloud/g2/products
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `product` | Yes | — | G2 product slug (`postman`) or full product link (`https://www.g2.com/products/postman/reviews`). |
| `max_reviews` | No | `2500` | Maximum number of reviews to return. Integer between 0 and 2500. |

#### Example

```python
import requests

response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/products",
    params={"product": "postman", "max_reviews": 100},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

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

```
GET https://g2-scraper.omkar.cloud/g2/categories
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `category` | Yes | — | G2 category slug (`marketing-automation`) or full category link (`https://www.g2.com/categories/marketing-automation`). |
| `max_reviews` | No | `2500` | Maximum number of reviews to return per product. Integer between 0 and 2500. |

#### Example

```python
import requests

response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/categories",
    params={"category": "marketing-automation"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

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

```
GET https://g2-scraper.omkar.cloud/g2/category-links
```

No parameters required.

#### Example

```python
import requests

response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/category-links",
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

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

```
GET https://g2-scraper.omkar.cloud/g2/product-links
```

No parameters required.

#### Example

```python
import requests

response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/product-links",
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

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

## Error Handling

```python
response = requests.get(
    "https://g2-scraper.omkar.cloud/g2/products",
    params={"product": "postman"},
    headers={"API-Key": "YOUR_API_KEY"}
)

if response.status_code == 200:
    data = response.json()
elif response.status_code == 401:
    # Invalid API key
    pass
elif response.status_code == 429:
    # Rate limit exceeded
    pass
```

## FAQs

### What data does the API return?

**Product Details** returns 40+ fields per product:
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

All in structured JSON. Ready to use in your app.

### How accurate is the data?

Data is pulled from G2 in real time. Every API call fetches live data — not cached or stale results. Ratings, reviews, pricing, and company details reflect what's on G2 right now.

### Can I pass a slug instead of a full URL?

Yes. Product Details and Products by Category accept either a slug (`postman`, `marketing-automation`) or a full G2 URL. Use whichever you have.

### How many reviews can I get per product?

Up to 2,500 reviews per product. Control the volume with the `max_reviews` parameter — set it low for fast lookups, or leave it at the default to pull everything.

### How do I discover products and categories to scrape?

Use the **Product Links** and **Category Links** endpoints. They return the complete directory — 185,000+ products and 2,000+ categories — so you can crawl G2 end to end without guessing URLs.

## Rate Limits

| Plan | Price | Requests/Month |
|------|-------|----------------|
| Free | $0 | 100 |
| Grow | $48 | 15,000 |
| Scale | $148 | 75,000 |

## Questions? We have answers.

Reach out anytime. We will solve your query within 1 working day.

[![Contact Us on WhatsApp about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20G2%20Scraper%20API.)

[![Contact Us on Email about G2 Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=G2%20Scraper%20API%20Question)

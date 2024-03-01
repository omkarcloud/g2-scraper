![G2 Scraper Featured Image](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/images/g2-scraper-featured-image.png)

<div align="center" style="margin-top: 0;">
  <h1>✨ G2 Scraper 🚀</h1>
  <p>💦 Find G2 Product Details 💦</p>
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
  <a href="#">
    <img alt="g2-scraper License" src="https://img.shields.io/github/license/omkarcloud/g2-scraper?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/g2-scraper/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/g2-scraper?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/g2-scraper.svg" width="80px" height="28px" alt="View" />
</p>

<p align="center">
  <a href="https://gitpod.io/#https://github.com/omkarcloud/g2-scraper">
    <img alt="Open in Gitpod" src="https://gitpod.io/button/open-in-gitpod.svg" />
  </a>
</p>
  
---

## Disclaimer for G2 Scraper Project

> By using G2 Scraper, you agree to comply with all applicable local and international laws related to data scraping, copyright, and privacy. The developers of G2 Scraper will not be held liable for any misuse of this software. It is the user's sole responsibility to ensure adherence to all relevant laws regarding data scraping, copyright, and privacy, and to use G2 Scraper in an ethical and legal manner, in line with both local and international regulations.

We take concerns related to the G2 Scraper Project very seriously. If you have any inquiries or issues, please contact Chetan Jain at [chetan@omkar.cloud](mailto:chetan@omkar.cloud). We will take prompt and necessary action in response to your emails.

## 👉 Explore Our Other Awesome Products


- ✅ [Botasaurus](https://github.com/omkarcloud/botasaurus): The All-in-One Web Scraping Framework with Anti-Detection, Parallelization, Asynchronous, and Caching Superpowers.

- ✅ [Google Maps Scraper](https://github.com/omkarcloud/google-maps-scraper): Discover Search Results from Google Maps.

---

G2 Scraper helps you scrape G2 Products. 🚀

## 🚀 Getting Started

1️⃣ **Clone the Magic 🧙‍♀:**
```shell
git clone https://github.com/omkarcloud/g2-scraper
cd g2-scraper
```
2️⃣ **Install Dependencies 📦:**
```shell
python -m pip install -r requirements.txt
```
3️⃣ **Let the Rain of G2 Products Begin 😎**:
```shell
python main.py
```

Find 100 G2 Products in the `output` directory.

![G2 Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/images/g2-scraper-csv-result.png)

*Note: If you don't have Python installed. Follow this Simple FAQ [here](https://github.com/omkarcloud/g2-scraper/blob/master/advanced.md#-i-dont-have-python-installed-how-can-i-run-the-scraper) and you will have your g2 products in next 5 Minutes*

## 🤔 FAQs

### ❓ How to Get G2 Product Details for Specific Companies?

1. Open `main.py` file.
2. Update the `products` list to include the products you're interested in.

```python
products = [
  "github",
  "atom",
  "sublime-text",
]
G2.get_products(products)
```
3. Run it.
```bash
python main.py
```   

You can also pass the direct links:

```python
products = [
  "https://www.g2.com/products/github/reviews", 
  "https://www.g2.com/products/atom/reviews", 
  "https://www.g2.com/products/sublime-text/reviews",
]
G2.get_products(products)
```
### ❓ What Data Points Are Scraped?

We scrape over 35+ data points, notable among them are:
- Name
- Product Description
- Reviews
- Rating
- Comparisons
- Alternatives
- Reviews (up to 25 reviews)
- And many more...

For examples in CSV/JSON format, see [this file](https://drive.google.com/file/d/1y8z-enPJemBKIcRr98jgDSjC6ZJNP7ha/view?usp=sharing).

### How to Scrape More Products Using the G2 API?

To scrape additional products, follow these steps to use our G2 API with the Free Plan, allowing you to scrape 50 products at no cost:
1. Sign up on RapidAPI by visiting [this link](https://rapidapi.com/auth/sign-up).
   
![Sign Up on RapidAPI](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/sign-up.png)

2. Then, subscribe to our Free Plan by visiting [this link](https://rapidapi.com/Chetan11dev/api/g2-data-api/pricing).

![Subscribe to Free Plan](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/images/g2-free-subscription.png)

3. Now, copy the API key.
![Copy the API Key](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/images/g2-api-key.png)

4. Use it in the scraper as follows:
```python
products = [
  "my-awesome-product",
]
G2.get_products(products, key="YOUR_API_KEY")
```
5. Now, run the script, and you'll find G2 Products in the `output` folder.
```bash
python main.py
```   

The first 50 products are free. After that, you can upgrade to the Pro Plan to scrape 1,000 products for $9.

### ❓ How to get list of all g2 products?

Kindly run following command:
```sh
python products.py
```

### ❓ How Are You Different from Your Competitors?

- We provide over 35+ data points.
- Our pricing is highly competitive at $9 per 1,000 products, compared to competitors which starts at $20 per 1,000 products.
- We are focused on small businesses and startups, offering a free-to-start plan followed by $9 per 1,000 products, whereas competitors target enterprise customers with datasets priced in the thousands of dollars.

### ❓ Do You Offer Discounts for Scraping the Complete G2 Dataset?

If you're looking to scrape the entire G2 dataset, which includes over 100,000 products, we offer a special rate of $3.8 per 1,000 products.

The data will be freshly scraped and we will deliver the JSON/CSV files of the Complete G2 Dataset to you within 7 Days.

If you need the complete G2 dataset, kindly contact us on WhatsApp. We'll be happy to help you out.

[![Contact Us on WhatsApp](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/mwa.png)](https://api.whatsapp.com/send?phone=918295042963&text=Hi,%20I%20would%20like%20to%20learn%20more%20about%20your%20products.)

## Love It? [Star It! ⭐](https://github.com/omkarcloud/g2-scraper/stargazers)

## Made with ❤️ using [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)
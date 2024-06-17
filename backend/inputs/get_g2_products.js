/**
 * @typedef {import('../../frontend/node_modules/botasaurus-controls/dist/index').Controls} Controls
 */


function isValidHttpUrl(string) {
    let url
  
    try {
      url = new URL(string)
    } catch (_) {
      return false
    }
  
    return url.protocol === "http:" || url.protocol === "https:"
  }

  function isEmpty(x) {
    return (
      x === null || x === undefined || (typeof x == "string" && x.trim() === "")
    )
  }
  
function isNotEmpty(x) {
    return !isEmpty(x)
  }
  
/**
 * @param {Controls} controls
 */
function getInput(controls) {
    let validUrls = [
        "https://www.g2.com/categories/marketing-automation",
        "https://www.g2.com/products/jenkins/reviews",
        "postman",
    ];
    
    controls
        // Render a Link Input
        .listOfTexts('search_queries', { isRequired: true,
            placeholder: "https://www.g2.com/products/jenkins/reviews",
            validate:(value) => {
                for (let index = 0; index < value.length; index++) {

                    const element = value[index];

                    if (!isEmpty(element)) {
                        if (isValidHttpUrl(element)){
                            if (!element.includes('g2.com/categories/') && !element.includes('g2.com/products/')) {
                                return 'Must be a valid g2 product or category link';
                            }
                        } else if (element.includes('/')) {
                            return 'Must be a valid g2 product slug';
                        }
                    }
                   
                }
            },
            defaultValue: [
            "https://www.g2.com/categories/marketing-automation",
            "https://www.g2.com/products/jenkins/reviews",
            "postman",
        ]})
        .numberGreaterThanOrEqualToZero('max_reviews',
            {
                isShown: (x)=>false,
                placeholder: 25,
                max: 2500,
            }
        ).text('api_key', {
            placeholder: "2e5d346ap4db8mce4fj7fc112s9h26s61e1192b6a526af51n9",
            label: 'Rapid API Key',
            helpText: 'Enter your Rapid API key to extract g2 products.',
            validate:(x,data) =>{
                if (isEmpty(x)){
                    const ls = data['search_queries'].filter(isNotEmpty)
                
                    if (ls.length && !ls.every(query => validUrls.includes(query.trim()))) {
                        return 'To get different products, please enter your Rapid API Key. You can use the starter plan offers a generous 400 monthly searches.';
                    }
                }

            }
        })
}

from playwright.sync_api import sync_playwright

def get_html_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html_content = page.content()
        browser.close()
    return html_content

def parse_html(html_content):
    return html_content

def fetch_amazon_page():
    amazon_url = "https://www.amazon.in/ASUS-Vivobook-i3-1115G4-Transparent-X1400EA-EK322WS/dp/B0C3CNRQD1/?_encoding=UTF8&pd_rd_w=DaPLc&content-id=amzn1.sym.44901b9b-bd56-4240-8b6b-3ad72079fb43%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=44901b9b-bd56-4240-8b6b-3ad72079fb43&pf_rd_r=KXEDW7Z1136BS2JS7Q4C&pd_rd_wg=iLhP9&pd_rd_r=9eccd694-3ae2-4660-9276-a29855420faa&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
    
    html_content = get_html_content(amazon_url)
    return html_content

# Example usage
amazon_page_html = fetch_amazon_page()
print(amazon_page_html)

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(amazon_page_html)

import requests
import json
import pandas as pd


def payload_gen():
    search= input("Phone Name: ")
    items= input("no of item you want(default=15): ")
    payload = {
                    't': 1703178991854,
                    'q': search,
                    'limit': items,
                    'startRow': 0,
                }
    return payload
    
def data_gen():
    url = 'https://api.91mobiles.com/nm-community/api/searchPage/web'
    payload=payload_gen()
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        json_response = response.json()
        data_str= json.dumps(json_response, indent=6)
        data= json.loads(data_str)
        data= data['products']
        json_data = json.dumps(data, indent=4)
        with open('data.json','w') as f:
            f.write(json_data)
    # print("response: ",response)
    return data


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def clear_data():
    product_dicts_list=data_gen()
    product_dicts_list = [flatten_dict(i) for i in product_dicts_list]
    selected_keys =keys_list = ["productId", "productCategoryName", "productName", "alterProductName", "brandName","productStatus_price_app","productStatus_price_web","expectedPrice", "productImageSlug", "productUrl", "productQuickSpecs_0_displayValue", "productQuickSpecs_1_displayValue", "productQuickSpecs_2_displayValue", "productQuickSpecs_3_displayValue", "productQuickSpecs_4_displayValue", "productQuickSpecs_5_displayValue", "productQuickSpecs_6_displayValue", "productQuickSpecs_7_displayValue", "productQuickSpecs_8_displayValue", "productQuickSpecs_9_displayValue", "productGridViewFeatures_OS", "productGridViewFeatures_Battery", "productGridViewFeatures_Camera", "productGridViewFeatures_Performance", "productGridViewFeatures_Display", "wapFeatureSpecs_0_group_options_0_value", "wapFeatureSpecs_1_group_options_0_nm", "wapFeatureSpecs_1_group_options_0_value", "wapFeatureSpecs_2_group_options_0_nm", "wapFeatureSpecs_2_group_options_0_value", "wapFeatureSpecs_3_group_options_0_nm", "wapFeatureSpecs_3_group_options_0_value", "appFeatureSpecs_0_group_options_0_nm", "appFeatureSpecs_0_group_options_0_value", "appFeatureSpecs_1_group_options_0_nm", "appFeatureSpecs_1_group_options_0_value", "productAddDate", "priceDetails_storeDisplayName", "priceDetails_storeUrl", "productStatus_status_app", "productStatus_status_wap", "productStatus_display_status_app", "productStatus_display_status_wap", "id"]
    clean_data=  [({key: i[key] for key in selected_keys if key in i}) for i in product_dicts_list]
    return clean_data


def main():
    data_gen()
    data =clear_data()
    df = pd.DataFrame(data)
    df.to_csv('CSV_data_file.csv', index=False)

if __name__=="__main__":
    main()
    c=input("enter to exit")

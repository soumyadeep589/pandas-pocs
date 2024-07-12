import requests
import json
import pandas as pd
import xml.etree.ElementTree as ET

# Step 1: Fetch data from the API
# url = "https://weatherapi-com.p.rapidapi.com/current.json"

# querystring = {"q":"53.1,-0.13"}

# headers = {
# 	"x-rapidapi-key": "95e420e7f7msh618a511738c26e9p123bdfjsncc9e5fccb545",
# 	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# data = response.json()

with open('movies.json', 'r') as file:
    data = json.load(file)

# Access the movies list
movies = data['movies']
print(movies)

# Step 2: Load data into a DataFrame and manipulate it
df = pd.DataFrame(movies)
df_cleaned = df.dropna()
# df_filtered = df_cleaned[df_cleaned['column_name'] > some_value]
# df_grouped = df_filtered.groupby('another_column').sum()

# Step 3: Convert DataFrame to XML
def df_to_xml(df, root_tag, row_tag):
    root = ET.Element(root_tag)
    for _, row in df.iterrows():
        row_elem = ET.SubElement(root, row_tag)
        for field in df.columns:
            field_elem = ET.SubElement(row_elem, field)
            field_elem.text = str(row[field])
    return root

xml_root = df_to_xml(df_cleaned, 'imdb', 'movie')
tree = ET.ElementTree(xml_root)
tree.write('report.xml', encoding='utf-8', xml_declaration=True)

print('Report generated successfully.')


### Customization for Regulatory Specifications

# For regulatory reports, you may need to customize the XML structure further to meet specific guidelines. This can involve setting specific attributes, namespaces, or nested structures as required by the regulatory body.

#### Example: Customizing XML Structure
def df_to_custom_xml(df, root_tag, row_tag):
    root = ET.Element(root_tag)
    for _, row in df.iterrows():
        row_elem = ET.SubElement(root, row_tag)
        for field in df.columns:
            field_elem = ET.SubElement(row_elem, field)
            # Customize field element as per specifications
            field_elem.set('attribute', 'value')  # Example attribute
            field_elem.text = str(row[field])
    return root

xml_root = df_to_custom_xml(df_cleaned, 'imdb', 'movie')
tree = ET.ElementTree(xml_root)
tree.write('custom_report.xml', encoding='utf-8', xml_declaration=True)
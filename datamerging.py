import pandas as pd
df_amazon = pd.read_csv("Dataset files/export_dataframe.csv")
print(df_amazon.info())
df_Otto = pd.read_csv("Dataset files/LaptopsOtto.csv")
print(df_Otto.info())
List_Brand_Amazon = list(df_amazon["brand"])
List_Brand_Otto = list(df_Otto["name"])
print(List_Brand_Otto)
print(List_Brand_Amazon)
List_Price_Amazon1 = list(df_amazon["price"])
List_Price_Otto1 = list(df_Otto["price"])
List_Price_Amazon = []
for i in range(len(List_Price_Amazon1)):
    price = List_Price_Amazon1[i]
    price_modified = price[20:].replace(",","")
    List_Price_Amazon.append(float(price_modified))
print(List_Price_Amazon)
List_Price_Otto = []
for i in range(len(List_Price_Otto1)):
    price = List_Price_Otto1[i]
    price_modified = price[2:].replace(".","")
    price_modified1 = price_modified.replace(",",".")
    List_Price_Otto.append(float(price_modified1))
print(List_Price_Otto)
Brand_list = ["Otto","Amazon"]

name = ["Lenovo ideapad3","Lenovo Ideapad5","Hp pavillion","Hp Omen","Acer Aspire 3","Acer Aspire 5"]
for i in range(len(name)):
    Product_specs = List_Brand_Otto[i]
    Price = [str(List_Price_Otto[i])+" EUR",str(List_Price_Amazon[i])+" EUR"]
    df = pd.DataFrame([Brand_list,Price]).transpose()
    df.to_csv("Dataset files"+name[i]+".csv")
    df1 = pd.read_csv(name[i]+".csv")
    df2 = df1.drop("Unnamed: 0",axis=1)
    df2.columns=["Store","Price"]
    print(df2)


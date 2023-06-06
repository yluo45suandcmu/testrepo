# price_data = [['category', 'product', 'capacity', 'rating', 'price', 'price_size', 'supermarket', 'date']]
price_data = []
with open('C:/Users/Yan/Dropbox/Python/project/results.csv','r', encoding='utf-8') as Source_File3:
    lines = [x.rstrip() for x in Source_File3]
    line_count = 0
    for line in lines:
        if line_count >= 2:
            temp = line.split(':')
            price_data.append([temp[0].strip(), temp[1].strip(), temp[2].strip(),
                               temp[3].strip(), temp[4].strip(), temp[5].strip(),
                               temp[6].strip(), temp[7].strip()])
        line_count += 1

    # print(price_data)
    # print(type(price_data))
    # print(price_data)


    # print(line_count)
    # print(amazon_item)

    shopping_list = ['coke', 'whole milk', 'doritos',
                     'brown eggs', 'breakfast chreal', 'kit kat',
                     'string cheese', 'spring water', 'apple juice']


    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    special_situation = 0
    for i in range(len(price_data)):
        if line_count >= 2 and shopping_list[0] in price_data[i]:
            list_0.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[1] in price_data[i]:
            list_1.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[2] in price_data[i]:
            list_2.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[3] in price_data[i]:
            list_3.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[4] in price_data[i]:
            list_4.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[5] in price_data[i]:
            list_5.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[6] in price_data[i]:
            list_6.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[7] in price_data[i]:
            list_7.append(price_data[i])
            line_count += 1
        elif line_count >= 2 and shopping_list[8] in price_data[i]:
            list_8.append(price_data[i])
            line_count += 1
        else:
            special_situation += 1

    # print(list_0)
    # print(list_1)
    # print(list_2)
    # print(list_3)
    # print(list_4)
    # print(list_5)
    # print(list_6)
    # print(list_7)
    # print(list_8)
    
    # Amazon list 
    amazon_list_0 = []
    for i in list_0:
        if i[-2] == 'amazon':
            amazon_list_0.append(i)

    amazon_list_1 = []
    for i in list_1:
        if i[-2] == 'amazon':
            amazon_list_1.append(i)

    amazon_list_2 = []
    for i in list_2:
        if i[-2] == 'amazon':
            amazon_list_2.append(i)

    amazon_list_3 = []
    for i in list_3:
        if i[-2] == 'amazon':
            amazon_list_3.append(i)

    amazon_list_4 = []
    for i in list_4:
        if i[-2] == 'amazon':
            amazon_list_4.append(i)

    amazon_list_5 = []
    for i in list_5:
        if i[-2] == 'amazon':
            amazon_list_5.append(i)
            
    amazon_list_6 = []
    for i in list_6:
        if i[-2] == 'amazon':
            amazon_list_6.append(i)
            
    amazon_list_7 = []
    for i in list_7:
        if i[-2] == 'amazon':
            amazon_list_7.append(i)
            
    amazon_list_8 = []
    for i in list_8:
        if i[-2] == 'amazon':
            amazon_list_8.append(i)

    # print(amazon_list_8)
    
    # Walmart list    
    walmart_list_0 = []
    for i in list_0:
        if i[-2] == 'walmart':
            amazon_list_0.append(i)

    walmart_list_1 = []
    for i in list_1:
        if i[-2] == 'walmart':
            walmart_list_1.append(i)

    walmart_list_2 = []
    for i in list_2:
        if i[-2] == 'walmart':
            walmart_list_2.append(i)

    walmart_list_3 = []
    for i in list_3:
        if i[-2] == 'walmart':
            walmart_list_3.append(i)

    walmart_list_4 = []
    for i in list_4:
        if i[-2] == 'walmart':
            walmart_list_4.append(i)

    walmart_list_5 = []
    for i in list_5:
        if i[-2] == 'walmart':
            walmart_list_5.append(i)
            
    walmart_list_6 = []
    for i in list_6:
        if i[-2] == 'walmart':
            walmart_list_6.append(i)
            
    walmart_list_7 = []
    for i in list_7:
        if i[-2] == 'walmart':
            walmart_list_7.append(i)
            
    walmart_list_8 = []
    for i in list_8:
        if i[-2] == 'walmart':
            walmart_list_8.append(i)
            
    # print(walmart_list_8)

    from pandas.core.frame import DataFrame
    import pandas as pd
    #df = DataFrame(price_data)
    df = pd.DataFrame(price_data, columns=['category', 'product', 'capacity', 'rating', 'price', 'price_size', 'supermarket', 'date'])
    print(df)
    #print(df[df['supermarket'] == 'Amazon'])








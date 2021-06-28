models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1_data = {}

cars = {}
for model, qty2018, qty2017, qty2016 in zip(models, sales2018, sales2017, sales2016):
    qty2018 = qty2018.replace('NA' , '0')
    qty2017 = qty2017.replace('NA' , '0')
    qty2016 = qty2016.replace('NA' , '0')
    qty2018 = int(qty2018.replace(',' , ''))
    qty2017 = int(qty2017.replace(',' , ''))
    qty2016 = int(qty2016.replace(',' , ''))
    car = model.split(" - ")
    if not car[0] in cars.keys():
        cars[car[0]] = {car[1] : {"sales" : {"2016" : qty2016, "2017" : qty2017, "2018" : qty2018}}}
    else:
        cars[car[0]][car[1]] = {"sales" : {"2016" : qty2016, "2017" : qty2017, "2018" : qty2018}}
    answer1_data[model] = qty2017

print(cars)


def find_best_brand_2018():
    temp_dict = {}
    for brand, data in cars.items():
        temp = 0
        for model, sales in data.items():
            # print('{} {} in 2018: {}'.format(brand, model, sales['sales']['2018']))
            temp += sales['sales']['2018']
        temp_dict[brand] = temp
    return sorted(temp_dict.items(), key = lambda x: x[1], reverse = True)


def answer3():
    temp_list = []
    for brand, data in cars.items():
        for model, sales in data.items():
            if (sales['sales']['2016'] == 0) and (not sales['sales']['2017'] == 0):
                temp_list.append(model)
    return temp_list


def answer4():
    temp_dict = {}
    for brand, data in cars.items():
        for model, sales in data.items():
            temp = 0
            print('{} {} in 2018: {}'.format(brand, model, sales['sales']['2018']))
            temp += (sales['sales']['2016'] + sales['sales']['2017'] + sales['sales']['2018'])
        temp_dict[model] = temp
    print(temp_dict)
    return sorted(temp_dict.items(), key = lambda x: x[1])


def ford_sales_change():
    sales2018 = []
    sales2017 = []
    for brand, data in cars.items():
        if brand == 'Ford':
            for model, sales_data in data.items():
                for sales, quantities_per_year in sales_data.items():
                    for year, quantity in quantities_per_year.items():
                        if year == '2017':
                            sales2017.append(quantity)
                        if year == '2018':
                            sales2018.append(quantity)

    sales_yoy = sum(sales2018) - sum(sales2017)

    return (sales_yoy / sum(sales2017)) * 100


answer1 = max(answer1_data, key = answer1_data.get) # zostawiłem swoją wersję dla własnej referencji
answer2_list = find_best_brand_2018() # Adam
answer2 = answer2_list[0][0] # Adam
answer3 = answer3() # Adam
answer4_list = answer4() # Adam
answer4 = answer4_list[0][0] # Adam
print(answer4) 
answer5 = str(f"{round(ford_sales_change())}%")
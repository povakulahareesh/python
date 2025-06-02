cars=[{'model': 'maruthi', 'brand': 'swift', 'price':800000, 'color':'white'},

{'model': 'maruthi', 'brand': 'swift', 'price':800000,'color':'blue'},

{'model': ' RangeRover', 'brand': 'velar', 'price':10000000, 'color':'black'},

{'model':'maruthi', 'brand':'alto', 'price':200000,'color':'white'},

{'model':'tata', 'brand':'tiago', 'price':400000, 'color':'blue'},

{'model': 'kia', 'brand':'swift', 'price':4800000, 'color':'yellow'},

{'model': 'kai','brand':'swift', 'price':3800000, 'color': 'white'},

{'model':'mahindra', 'brand': 'Xuv700', 'price': 2800000, 'color': 'black'},

{'model': 'mahindra', 'brand': 'scorpio', 'price': 1800000, 'color': 'black'}]


# def filter_cars(car):
#     if car['price']>=100000:
#         return True
#     else:
#         return False
# below_100000_cars=list(filter(filter_cars,cars))
# print(below_100000_cars)


white_cars=list(filter(lambda car:car['color']=='white',cars))
print(white_cars)



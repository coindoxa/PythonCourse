# premium_shipping = 125
#
#
# def ground_shipping(weight):
#     """
#
#     :rtype: object
#     """
#     # weight= input("What is your weight?")
#     if weight <= 2:
#         price_per_pound = 1.5
#     elif weight <= 6:
#         price_per_pound = 3
#     elif weight <= 10:
#         price_per_pound = 4
#     else:
#         price_per_pound = 4.75
#     return 20 + (weight * price_per_pound)
#
#
# # print(ground_shipping(4.8))
#
#
# def drone_shipping(weight):
#     if weight <= 2:
#         price_per_pound = 4.5
#     elif weight <= 6:
#         price_per_pound = 9
#     elif weight <= 10:
#         price_per_pound = 12
#     else:
#         price_per_pound = 14.25
#     return (weight * price_per_pound)
#
#
# # print(drone_shipping(1.5))
#
# def shipping_cost(weight):
#     ground = ground_shipping(weight)
#     premium = premium_shipping
#     drone = drone_shipping(weight)
#
#     if ground < premium and ground < drone:
#         method = "Standard ground"
#         cost = ground
#     elif premium < ground and premium < drone:
#         method = "premium ground"
#         cost = premium
#     else:
#         method = "drone"
#         cost = drone
#     print ("The cheapest option available is $%.2F with %s shipping " % (cost, method))
#
#
# print(shipping_cost(4.8))
# print(shipping_cost(41.5))
#
#
#

# thread_sold_split = ['white', 'white', 'blue', 'white', 'blue', 'white ', 'white', 'yellow ', 'purple', 'white']
# # new = thread_sold_split.count('white')
# # print (new)
# def color_count(color):### NOT WORKING
#     for item in thread_sold_split:
#         new = item.count(color)
#         return new
#
# print(color_count("white"))





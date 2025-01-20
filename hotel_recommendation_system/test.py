from bundle_recommendation import bundle_recommendation, upsale

def submit_user_info(num_adults, num_children, num_infants, arrival_month, num_nights, weekend, holiday, customer_origin, hotel_name):
    print("Calling bundle_recommendation with:")
    print(f"hotel_name={hotel_name}, num_of_adults={num_adults}, num_of_childrens={num_children}, num_of_infants={num_infants}, arrival_month={arrival_month}, num_nights={num_nights}, weekend={weekend}, holiday={holiday}, customer_origin={customer_origin}")
    
    packages = bundle_recommendation(
        hotel_name=hotel_name,
        num_of_adults=num_adults,
        num_of_childrens=num_children,
        num_of_infants=num_infants,
        arrival_month=arrival_month,
        num_nights=num_nights,
        weekend=weekend,
        holiday=holiday,
        customer_origin=customer_origin
    )
    
    print("Packages:", packages)
    
    # recommended_bundles = bundle_recommendation(
    #     hotel_name='Vinpearl Wonderworld Phú Quốc', # refer to the cell belows for possible values
    #     num_of_adults=2,
    #     num_of_childrens=0,
    #     num_of_infants=0,
    #     arrival_month=4,
    #     num_nights=2,
    #     weekend=True,
    #     holiday=False,
    #     customer_origin='North' # or 'South', or 'Midle', or 'Oversea'
    # )
    
    # print("Recommended Bundles:", recommended_bundles)

hotel_name = 'Vinpearl Wonderworld Phú Quốc' # refer to the cell belows for possible values
num_adults = 2
num_children = 0
num_infants = 0
arrival_month = 4
num_nights = 2
weekend = True
holiday = False
customer_origin = 'North'

submit_user_info(num_adults, num_children, num_infants, arrival_month, num_nights, weekend, holiday, customer_origin, hotel_name)
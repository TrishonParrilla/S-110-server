def get_coupons():
    coupons = [
        {
            "_id":1,"code":"WELCOME10","discount":10
        },
        {
            "_id":2,"code":"SPOOKY25","discount":25
        },
        {
            "_id":3,"code":"VIP50","discount": 50
        }
    ]
    return(coupons)

def get_coupons_count(coupons):
    for coupon in coupons:
        print(coupon)

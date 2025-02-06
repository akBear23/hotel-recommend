import frappe
import pickle
# import numpy as np
from frappe import _
from hotel_recommendation_system.bundle_recommendation import bundle_recommendation, upsale

def load_model():
    try:
        with open(frappe.get_app_path('hotel_recommendation_system', 'toy_bundle_recommenders.pkl'), 'rb') as f:
            return pickle.load(f)
    except Exception:
        frappe.log_error(f"Error loading model: {str(e)}")
        return None

@frappe.whitelist(allow_guest=True)
def submit_user_info(num_adults, num_children, num_infants, arrival_month, num_nights, weekend, holiday, customer_origin, hotel_name):
    print(num_adults, num_children, num_infants, arrival_month, num_nights, weekend, holiday, customer_origin, hotel_name)

    # try:
        # Call the AI model to generate packages
    packages = bundle_recommendation(
                hotel_name=hotel_name,
                num_of_adults=int(num_adults),
                num_of_childrens=int(num_children),
                num_of_infants=int(num_infants),
                arrival_month=int(arrival_month),
                num_nights=int(num_nights),
                weekend=int(weekend),
                holiday=int(holiday),
                customer_origin=customer_origin
            )
    print(packages)
    if packages:
        return {"packages": packages}
    else:
        return {"error": _("No packages found.")}
    # except Exception as e:
    #     frappe.log_error(frappe.get_traceback(), _("User Info Submission Error"))
    #     return {"error": _("An error occurred. Please try again.")}
    
@frappe.whitelist(allow_guest=True)
def ping():
    return "pong"
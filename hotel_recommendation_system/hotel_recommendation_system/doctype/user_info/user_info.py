# Copyright (c) 2025, ankhanh and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
@frappe.whitelist(allow_guest=True)
def bundle_recommendation(
    hotel_name: str,
    num_of_adults: int,
    num_of_childrens: int,
    num_of_infants: int,
    arrival_month: int,
    num_nights: int,
    weekend: bool,
    holiday: bool,
    customer_origin: str
):
    # Replace this with your logic to generate recommendations
    recommendations = [
        {"package_name": "Family Package", "price": 200},
        {"package_name": "Weekend Getaway", "price": 150},
        {"package_name": "Holiday Special", "price": 250},
    ]
    print("Generated Recommendations:", recommendations)
    return recommendations

def before_load(doc, method):
    # Get the hotel reference from the query parameters
    hotel = frappe.local.form_dict.get("hotel_name")
    if hotel:
        doc.hotel_name = hotel

class UserInfo(WebsiteGenerator):
    def validate(self):
        print("validate method triggered!")  # Debugging
        super().validate()
    def before_submit(self):
        print("before_submit method triggered!")  # Debugging
    def on_submit(self):
        print("/n On_submit method triggered!/n")
        # Call the bundle_recommendation function
        recommendations = bundle_recommendation(
            hotel_name=self.hotel_name,
            num_of_adults=self.num_adults,
            num_of_childrens=self.num_children,
            num_of_infants=self.num_infants,
            arrival_month=self.arrival_month,
            num_nights=self.num_nights,
            weekend=self.weekend,
            holiday=self.holiday,
            customer_origin=self.customer_origin
        )
        print("Saving Recommendations:", recommendations)
        # Store the recommendations in the session or a new DocType
        frappe.session.data["recommendations"] = recommendations

        # Redirect the user to the packages page
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = "/packages"

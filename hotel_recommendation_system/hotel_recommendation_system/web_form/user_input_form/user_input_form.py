import frappe
# import requests

# @frappe.whitelist(allow_guest=True)
# def bundle_recommendation(
#     hotel_name: str,
#     num_of_adults: int,
#     num_of_childrens: int,
#     num_of_infants: int,
#     arrival_month: int,
#     num_nights: int,
#     weekend: bool,
#     holiday: bool,
#     customer_origin: str
# ):
#     # Replace this with your logic to generate recommendations
#     recommendations = [
#         {"package_name": "Family Package", "price": 200},
#         {"package_name": "Weekend Getaway", "price": 150},
#         {"package_name": "Holiday Special", "price": 250},
#     ]
#     print("Generated Recommendations:", recommendations)
#     return recommendations

def get_context(context):
    pass
    # def validate(self):
    #     print("validate method triggered!")  # Debugging
    #     super().validate()
    # def before_submit(self):
    #     print("before_submit method triggered!")  # Debugging
    # def on_submit(self):
    #     print("\nOn_submit method triggered!\n")
    #     # Call the API to get recommendations
    #     response = requests.post(
    #         "/api/method/hotel_recommendation_system.api.submit_user_info",
    #         json={
    #             "hotel_name": self.hotel_name,
    #             "num_of_adults": self.num_adults,
    #             "num_of_childrens": self.num_children,
    #             "num_of_infants": self.num_infants,
    #             "arrival_month": self.arrival_month,
    #             "num_nights": self.num_nights,
    #             "weekend": self.weekend,
    #             "holiday": self.holiday,
    #             "customer_origin": self.customer_origin
    #         }
    #     )
    #     recommendations = response.json().get("message", [])
    #     print("Saving Recommendations:", recommendations)
    #     # Store the recommendations in the session or a new DocType
    #     frappe.session.data["recommendations"] = recommendations
    #     # Redirect to the /packages page
    #     frappe.local.response["type"] = "redirect"
    #     frappe.local.response["location"] = "/packages"


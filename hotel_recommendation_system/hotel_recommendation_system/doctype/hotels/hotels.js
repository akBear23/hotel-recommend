// Copyright (c) 2025, ankhanh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Hotels", {
// 	refresh(frm) {
//         frm.add_custom_button(__("Get Hotel Recommendations"), function() {
//             frappe.call({
//                 method: "hotel_recommendation_system.hotel_recommendation_system.doctype.hotels.hotels.get_hotel_recommendations",
//                 args: {
//                     user_info: frm.doc.name
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frappe.msgprint(r.message);
//                     }
//                 }
//             });
//         });
// 	},
// });
// frappe.ui.form.on("Hotels", {
//     refresh: function(frm) {
//         frm.add_custom_button('Get Hotel Recommendations', () {
//             frappe.new_doc('User Info', {
//                 hotel_name: frm.doc.name
//             });
//     });
//     }
// });

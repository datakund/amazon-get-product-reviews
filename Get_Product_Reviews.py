from amazon_get_product_reviews import *

amazon.open("https://www.amazon.in/Intellilens%C2%AE-Spectacles-Anti-glare-Protection-Computer/product-reviews/B07JCKYCJ1/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews") # product reviews link

for i in range(0,5):
	response=amazon.get_reviews()
	data=response['body']
	amazon.click_next_reviews() # clicks on next button
  #data=[{"Stars": "Stars", "Review Link": "Review Link", "Review": "Review"}]

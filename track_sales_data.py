jeans_stock = 600
jeans_sold = 400
sales_target = 500


target_hit = jeans_sold == sales_target
if (target_hit == True ):
  print("Jeans sind ausverkauft (Ziel errreicht): ")
  print(target_hit)
else:
  print("Jeans in Stock :")
  print(jeans_stock - jeans_sold)

  

  
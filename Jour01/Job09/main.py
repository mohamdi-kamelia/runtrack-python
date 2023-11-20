nom_de_produit="robes"
prix_unitaire=100
quantité_en_stock= 30
print("Nom du produit :", nom_de_produit)
print("Prix unitaire :", prix_unitaire ,"euros" )
print("Quantité en stock :", quantité_en_stock)
quantite_achat = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock = quantité_en_stock - quantite_achat
print("Quantité en stock après achat :", quantite_en_stock)
prix_unitaire*=  1.10 
print("Prix unitaire après inflation :", prix_unitaire)
print("Après la mise à jour on a :")
print("Nom du produit :", nom_de_produit)
print("Prix unitaire :", prix_unitaire, "euros")
print("Quantité en stock :", quantite_en_stock)

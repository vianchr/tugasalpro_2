gaji=int(input("gaji per jam:"))
jam_kerja=int(input("jam kerja perminggu:"))
# output
print ()
total_uang = gaji*jam_kerja*5 #5 minggu kerja  
print (f"total uang Budi adalah {total_uang :,} Rupiah")
pajak = total_uang - 0.14*total_uang 
print (f"total uang setelah pajak {pajak:,} Rupiah")
biaya_baju = pajak*0.1
print (f"jadi biaya baju dan aksesoris nya {biaya_baju:,} Rupiah")
# sisa_baju=pajak-biaya_baju
biaya_pensil = 0.01 * pajak
print (f"jadi biaya peralatan tulisnya adalah {biaya_pensil:,} Rupiah")
setelah_baju= pajak-biaya_baju-biaya_pensil

sedekah=setelah_baju*0.25
print (f"jadi total yang Budi sedekahkan sebesar  : {sedekah:,} Rupiah")
yatim_awal = sedekah%1000 
yatim=(sedekah-yatim_awal) *0.3

print (f"jadi Budi sedekah ke anak yatim sebesar  : {yatim:,} Rupiah")
duafah_awal = sedekah%1000
duafah=(sedekah-duafah_awal) *0.7
print (f"jadi Budi sedekah ke kaum duafah sebesar : {duafah:,} Rupiah")


from flask import Blueprint, render_template, request
import math

bata = Blueprint("bata", __name__, static_folder="static", template_folder="templates")

@bata.route('/bata', methods=['GET','POST'])
def kebutuhan_bata():
    if request.method == 'POST':

        panjang = request.form['panjang']
        lebar = request.form['lebar']
        tinggi = request.form['tinggi']
        tebalMortar = request.form['tebalMortar']
        panjangDinding = request.form['panjangDinding']
        tinggiDinding = request.form['tinggiDinding']
        harga = request.form['harga']

        sum = math.ceil(((float(panjangDinding)*1000) * (float(tinggiDinding)*1000)) / ((float(panjang) + float(tebalMortar)) * (float(tinggi) + float(tebalMortar))))
        
        wastage = math.ceil(sum * 10/100)

        sum = sum + wastage
        
        amount = float(harga) *  (sum + wastage)
        price = "Rp {:,.2f}".format(amount)

        return render_template('bata.html', sum=sum, price=price, wastage=wastage)

    else:
        return render_template('bata.html')
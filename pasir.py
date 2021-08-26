from flask import Blueprint, render_template, request

pasir = Blueprint("pasir", __name__, static_folder="static", template_folder="templates")

@pasir.route('/pasir', methods=["GET","POST"])
def kebutuhan_pasir():
    if request.method == 'POST':
        panjang = request.form['panjang']
        lebar = request.form['lebar']
        dalam = request.form['dalam']
        bobot = request.form['bobot']
        harga = request.form['harga']

        _area = float(panjang) * float(lebar)
        _volume = _area * (float(dalam) * 0.01)
        _weight = float(bobot) * _volume
        _price = (float(harga) * _weight) / _volume
        
        price = "Rp {:,.2f}".format(_price)
        area = str(_area) + " m\u00b2"
        volume = str(_volume) + " m\u00b3"
        weight = str(_weight) + " kg"

        return render_template('pasir.html', area=area, volume=volume, weight=weight, price=price)
    else:
        return render_template('pasir.html')
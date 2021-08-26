from flask import Blueprint, render_template, request

semen = Blueprint("semen", __name__, static_folder="static", template_folder="templates")

@semen.route('/semen', methods=["GET","POST"])
def kebutuhan_semen():
    if request.method == "POST":
        cementPart = 0
        sandPart = 0
        volumeKerikil = 0
        totalPart = 1

        volumeBasah = request.form['volume_basah']
        harga = request.form['harga_semen']

        volumeKering = float(volumeBasah) * 1.54

        wastage = volumeKering * 10/100

        totalVolume = volumeKering + wastage

        if request.form.get('campuran') == '1:3':
            cementPart = 1
            sandPart = 3
            totalPart = cementPart + sandPart
        elif request.form.get('campuran') == '1:4':
            cementPart = 1
            sandPart = 4
            totalPart = cementPart + sandPart
        elif request.form.get('campuran') == '1:5':
            cementPart = 1
            sandPart = 5
            totalPart = cementPart + sandPart
        elif request.form.get('campuran') == '1:6':
            cementPart = 1
            sandPart = 6
            totalPart = cementPart + sandPart

        elif request.form.get('campuran') == '1:1:2':
            cementPart = 1
            sandPart = 1
            gravelPart = 2
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart
        elif request.form.get('campuran') == '1:1.5:3':
            cementPart = 1
            sandPart = 1.5
            gravelPart = 3
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart
        elif request.form.get('campuran') == '1:2:4':
            cementPart = 1
            sandPart = 2
            gravelPart = 4
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart
        elif request.form.get('campuran') == '1:3:6':
            cementPart = 1
            sandPart = 3
            gravelPart = 6
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart
        elif request.form.get('campuran') == '1:4:8':
            cementPart = 1
            sandPart = 4
            gravelPart = 8
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart
        elif request.form.get('campuran') == '1:5:10':
            cementPart = 1
            sandPart = 5
            gravelPart = 10
            totalPart = cementPart + sandPart + gravelPart
            volumeKerikil = volumeKering * gravelPart / totalPart

        print(request.form.get('campuran'))
        volumeSemen = volumeKering * cementPart / totalPart
        volumePasir = volumeKering * sandPart / totalPart

        isiSemen = request.form['isi_semen']

        if isiSemen == '':
            isiSemen = 50.0

        beratSemen = volumeSemen * 1440
        sak = beratSemen / float(isiSemen)


        amount = sak * float(harga) 
        price = "Rp {:,.2f}".format(amount)

        return render_template("semen.html", price=price, berat=beratSemen, sak=sak, wastage=wastage, volumeKering=volumeKering, totalVolume=totalVolume, volumeSemen=volumeSemen, volumePasir=volumePasir, volumeKerikil=volumeKerikil)
    else:
        return render_template("semen.html")
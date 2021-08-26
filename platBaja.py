from flask import Blueprint, render_template, request

platBaja = Blueprint("platBaja", __name__,
                     static_folder="static", template_folder="templates")


@platBaja.route('/platBaja', methods=["GET", "POST"])
def tebal_baja():


    if request.method == "POST":
        density = 0
        if request.form.get("density") == "1":
            density = 7715
        elif request.form.get("density") == "2":
            density = 7750
        elif request.form.get("density") == "3":
            density = 7820
        elif request.form.get("density") == "4":
            density = 7830
        elif request.form.get("density") == "5":
            density = 7840
        elif request.form.get("density") == "6":
            density = 7850
        elif request.form.get("density") == "7":
            density = 7860
        elif request.form.get("density") == "8":
            density = 7870
        elif request.form.get("density") == "9":
            density = 8030

        panjang = request.form['panjang']
        lebar = request.form['lebar']
        sisi = request.form['sisi']
        diameter = request.form['diameter']
        tebalPersegiPanjang = request.form['tebal_persegi_panjang']
        tebalPersegi = request.form['tebal_persegi']
        tebalLingkaran = request.form['tebal_lingkaran']
        tebalLainnya = request.form['tebal_lainnya']
        jumlah = request.form['quantity']

        phi = 3.14
        quantity = float(jumlah)

        if panjang != "":
            luas = float(panjang) * float(lebar)
            volume = luas * float(tebalPersegiPanjang)
            weight = ((volume * 0.000001) * density) * quantity
        elif sisi != "":
            luas = float(sisi) * float(sisi)
            volume = luas * float(tebalPersegi)
            weight = ((volume * 0.000001) * density) * quantity
        elif diameter != "":
            r = float(diameter) / 2
            luas = phi * r * r
            volume = luas * float(tebalLingkaran)
            weight = ((volume * 0.000001) * density) * quantity
        else:
            luas = float(request.form['luas_lainnya'])
            volume = luas * float(tebalLainnya)
            weight = ((volume * 0.000001) * density) * quantity

        luas = "{:.2f}".format(luas)
        volume = "{:.2f}".format(volume)
        berat = "{:.4f}".format(weight)
        return render_template('platBaja.html', luas=luas, volume=volume, berat=berat)
    else:
        return render_template("platBaja.html")

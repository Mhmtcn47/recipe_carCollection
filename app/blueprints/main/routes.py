from flask import render_template

from . import bp

@bp.route('/civic')
def civic():
   car={
        'Toyota' : ('Corolla', 'Tacoma', 'Raw', 'Camry'),
        'Honda': ['civic', 'Odesy', 'accord',]
    }
   return render_template("index.jinja", title='Home', honda=car['Honda'],toyota=car['Toyota'])


@bp.route('/about')
def about():
    car={
        "Bmw": ('325', 'X5', 'I8'),
        "Mercedes": ('Benz',' C-class', 'AmG')
    }
    return render_template('about.jinja', title='Home', Bmw=car['Bmw'], Mercedes=car['Mercedes'])

@bp.route('/jeep')
def jeep():
    car={
        "Jeep": ('Patriot', 'Compass', 'Grand-Cherokee'),
        "Lincoln": ('Continental', 'Mkc-reserve', 'Navigator')
    }
    return render_template('about.jinja', title='Home', Jeep=car['Jeep'], Lincoln=car['Lincoln'])


@bp.route('/recipe')
def recipe():
    bread={
        'flour': {550:'gr'},
        'yeast': {6:'gr'},
        'honey': {50:'gr'},
        'warm_water': {215:'gr'},
        'salt': {9:'gr'},
        'veg_oil': {40:'gr'},
        'eggs': {2:''}
    }
    return render_template('recipe.jinja', title='Home',recipe=bread)
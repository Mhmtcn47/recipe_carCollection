from flask import render_template

from . import bp

@bp.route('/signin')
def signin():
    return render_template('signin.jinja')


@bp.route('/register')
def register():
    return render_template('register.jinja')


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
    return render_template('recipe.jinja', title='Home',recipe=bread['recipe'])
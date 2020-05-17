from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os
from werkzeug.utils import secure_filename

from marketplace.auth import login_required, admin_only
from marketplace.db import get_db

bp = Blueprint('store', __name__)
UPLOAD_FOLDER = '/Users/sreeyasai/Documents/Github_Projects/flask-tutorial/marketplace/static/img'

@bp.route('/')
def index():
    if not g.user:
        return redirect(url_for('auth.login'))
    db = get_db()
    items = db.execute(
        'SELECT i.id, i.item_name, i.item_description, i.item_image, i.price'
        ' FROM item i'
    ).fetchall()
    return render_template('store/index.html', items=items)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
@admin_only
def create():
    if request.method == 'POST':
        item_name = request.form["name"]
        item_description = request.form["description"]
        item_image = request.files["image"]
        price = request.form["price"]

        if item_image:
            secure_filename(item_image.filename)
            item_image.save(os.path.join(UPLOAD_FOLDER, item_image.filename))

        if not item_name:
            error = 'Title is required.'
            flash(error)
        else :
            db = get_db()
            db.execute(
                'INSERT INTO item (item_name, item_description, item_image, price)'
                ' VALUES (?, ?, ?, ?)',
                (item_name, item_description, item_image.filename, price)
            )
            db.commit()
            flash(item_name + ' was added to the store', 'success')

    return render_template('store/create.html')


@bp.route('/delete_cart_item/<int:item_id>', methods=['POST'])
@login_required
@admin_only
def delete(item_id):
    db = get_db()
    db.execute('DELETE FROM item WHERE id = ?', [item_id])
    db.commit()
    return redirect(url_for('store.index'))
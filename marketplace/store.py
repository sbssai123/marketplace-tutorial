from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os
from werkzeug.utils import secure_filename

from marketplace.auth import login_required, admin_only
from marketplace.db import get_db

bp = Blueprint('store', __name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/static/img'

@bp.route('/')
def index():
    if not g.user:
        return redirect(url_for('auth.login'))
    # TODO: Select all of the items in the store and display
    # them on the homepage


@bp.route('/create', methods=['GET', 'POST'])
@login_required
@admin_only
def create():
    if request.method == 'POST':
        item_name = request.form["name"]
        item_description = request.form["description"]
        item_image = request.files["image"]
        price = request.form["price"]

        # Save image that we uploaded to a local file system
        if item_image:
            secure_filename(item_image.filename)
            item_image.save(os.path.join(UPLOAD_FOLDER, item_image.filename))

            # TODO: Add store item to the Item table in the DB
            flash(item_name + ' was added to the store', 'success')

    return render_template('store/create.html')


@bp.route('/delete_cart_item/<int:item_id>', methods=['POST'])
@login_required
@admin_only
def delete(item_id):
    # TODO: Delete an item from the database
    return redirect(url_for('store.index'))
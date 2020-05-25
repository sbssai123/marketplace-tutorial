from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from marketplace.db import get_db
from marketplace.auth import login_required

bp = Blueprint('cart', __name__)

@bp.route('/add_cart/<int:item_id>', methods=['POST'])
@login_required
def add_cart(item_id):
    # TODO: Add Item to the cart
    flash("Item successfully added to cart", 'success')
    return redirect(url_for('store.index'))

@bp.route('/checkout', methods=['GET'])
@login_required
def checkout():
    db = get_db()
    # TODO: Get all of the cart items
    # TODO: Calculate Total Price of items in the cart
    return render_template('cart/checkout.html')


@bp.route('/delete/<cart_item_id>', methods=['POST'])
@login_required
def delete_item(cart_item_id):
    db = get_db()
    db.execute('DELETE FROM cart WHERE cart_id = ?', [cart_item_id])
    db.commit()
    return redirect(url_for('cart.checkout'))

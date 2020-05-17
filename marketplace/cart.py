from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from marketplace.db import get_db
from marketplace.auth import login_required

bp = Blueprint('cart', __name__)

@bp.route('/add_cart/<int:item_id>', methods=['POST'])
@login_required
def add_cart(item_id):
    db = get_db()
    db.execute(
        'INSERT INTO cart (user_id, item_id)'
        ' VALUES (?, ?)',
        (g.user['id'], item_id)
    )
    db.commit()
    flash("Item successfully added to cart", 'success')
    return redirect(url_for('store.index'))

@bp.route('/checkout', methods=['GET'])
@login_required
def checkout():
    db = get_db()
    cart_items = db.execute(
        'SELECT cart_id, i.item_name, i.price, i.item_image FROM cart c'
        ' INNER JOIN item i ON c.item_id = i.id'
        ' WHERE c.user_id = ?',
        [g.user['id']]
    ).fetchall()
    total_price = 0
    for item in cart_items:
        total_price = total_price + item['price']
    return render_template('cart/checkout.html', cart_items=cart_items, total_price=total_price)


@bp.route('/delete/<cart_item_id>', methods=['POST'])
@login_required
def delete_item(cart_item_id):
    print("HERE")
    db = get_db()
    print(cart_item_id)
    db.execute('DELETE FROM cart WHERE cart_id = ?', [cart_item_id])
    db.commit()
    return redirect(url_for('cart.checkout'))

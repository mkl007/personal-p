from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from databs.database_setup import Base, Usuarios, Tareas
from sqlalchemy import inspect


app = Flask(__name__)

engine = create_engine('sqlite:///myDatabasepq.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()



# ----------------

@app.route('/')
@app.route('/inicio')
def mostraUsuario():
    usuario = session.query(Usuarios).filter_by(id=2).all()
    # return jsonify([i.serialize for i in usuario])
    return jsonify(usuario[0].serialize)
    # return(f"Estos son los datos sacados {usuario.name} {usuario.email}")
    
    
    
    
    
#  ----------------------------------------------------   
 

# @app.route('/restaurants/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(
#         restaurant_id=restaurant_id).all()
#     return jsonify(MenuItems=[i.serialize for i in items])



# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/menu/JSON')
# def restaurantMenuJSON_itemMenu(restaurant_id, menu_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(id=menu_id).all()
#     return jsonify(MenuItems=[i.serialize for i in items])



# @app.route('/restaurants/<int:restaurant_id>/')
# def restaurantMenu(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
#     return render_template('menu.html', restaurant=restaurant, items=items)


# @app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
# def newMenuItem(restaurant_id):

#     if request.method == 'POST' and request.form['name'] != '':
#         newItem = MenuItem(name=request.form['name'], description=request.form[
#                            'description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
#         session.add(newItem)
#         session.commit()
#         flash('New menu item created.')

#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         # return "Error when creating a new menu item"
#         return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',
#            methods=['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):

#     editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedItem.name = request.form['name']
#             editedItem.description=request.form['description'] 
#             editedItem.price = request.form['price']
#             editedItem.course = request.form['course']
#         session.add(editedItem)
#         session.commit()
#         flash('A menu item has been Edited')
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
#         # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
#         return render_template(
#             'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)
 

# #  DELETE MENU ITEM SOLUTION
# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',
#            methods=['GET', 'POST'])
# def deleteMenuItem(restaurant_id, menu_id):
#     itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         session.delete(itemToDelete)
#         session.commit()
#         flash('A menu item has been Deleted!')
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         return render_template('deletemenuitem.html', item=itemToDelete)




        
if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


    # Delete Menu Item
    # https://learn.udacity.com/courses/ud088/lessons/4fa83147-28e9-43de-b7c9-97a2c18f7d49/concepts/17be6ea6-76ad-4538-afcf-67e28000eddf/instructions
    # https://github.com/udacity/Full-Stack-Foundations/blob/master/Lesson-3/14_Delete-Menu-Item/deletemenuitem.html
import sqlite3
from sqlite3 import Error
from peewee import *


db = SqliteDatabase('test.sqlite')


class Client(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)

    class Meta:
        database = db


class Order(Model):
    id = AutoField(primary_key=True)
    cost = IntegerField()
    name = CharField(max_length=20)
    client = ForeignKeyField(Client, backref='orders')

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Client, Order])


def create_data():
    clients = [
        {'id': 1, 'name': 'Client1'},
        {'id': 2, 'name': 'Client2'},
        {'id': 3, 'name': 'Client3'},
        {'id': 4, 'name': 'Client4'}
    ]
    orders = [
        {'id': 1, 'cost': 100, 'name': 'Order1', 'client_id': 1},
        {'id': 2, 'cost': 200, 'name': 'Order2', 'client_id': 1},
        {'id': 3, 'cost': 300, 'name': 'Order3', 'client_id': 2},
        {'id': 4, 'cost': 400, 'name': 'Order4', 'client_id': 2},
        {'id': 5, 'cost': 500, 'name': 'Order5', 'client_id': 2},
        {'id': 6, 'cost': 600, 'name': 'Order6', 'client_id': 3},
        {'id': 7, 'cost': 700, 'name': 'Order7', 'client_id': 4},
        {'id': 8, 'cost': 800, 'name': 'Order8', 'client_id': 4},
        {'id': 9, 'cost': 900, 'name': 'Order9', 'client_id': 4},
        {'id': 10, 'cost': 1000, 'name': 'Order10', 'client_id': 4}
    ]
    
    with db.atomic():
        Client.bulk_create([
            Client(id=c['id'], name=c['name']) for c in clients
        ])
        Order.bulk_create([
            Order(id=o['id'], cost=o['cost'], name=o['name'], client_id=o['client_id']) for o in orders
        ])


def get_orders_using_orm():
    clients = Client.select()
    for client in clients:
        orders = client.orders
        print(f"Client {client.name} orders:")
        for order in orders:
            print(f"Order {order.name} cost: {order.cost}")


def get_orders_using_raw_sql():
    query = '''
    SELECT c.name AS client_name, o.name AS order_name, o.cost
    FROM Clients c
    INNER JOIN Orders o ON c.id = o.client_id;
    '''
    with db.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        order_dict = {}
        for row in results:
            client_name, order_name, cost = row
            if client_name not in order_dict:
                order_dict[client_name] = []
            order_dict[client_name].append({'name': order_name, 'cost': cost})
        
        for client_name, orders in order_dict.items():
            print(f"Client {client_name} orders:")
            for order in orders:
                print(f"Order {order['name']} cost: {order['cost']}")


create_tables()
create_data()


get_orders_using_orm()


get_orders_using_raw_sql()

import json

def load_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

def count_rooms(reservations):
    return len(reservations)

def count_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

def count_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

def total_paid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if reservation['paid'])

def total_unpaid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if not reservation['paid'])

def main():
    reservations = load_reservations('reservations.json')

    num_rooms = count_rooms(reservations)
    num_paid_reservations = count_paid_reservations(reservations)
    num_unpaid_reservations = count_unpaid_reservations(reservations)
    total_paid = total_paid_value(reservations)
    total_unpaid = total_unpaid_value(reservations)

    print("Number of rooms:", num_rooms)
    print("Number of paid reservations:", num_paid_reservations)
    print("Number of unpaid reservations:", num_unpaid_reservations)
    print("Total value of paid reservations:", total_paid)
    print("Total value of unpaid reservations:", total_unpaid)

if __name__ == '__main__':
    main()

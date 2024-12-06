import queue

q = queue.Queue()

def new_customer(ticket_number, q):
    customer = f"Customer {ticket_number}"
    q.put(customer)
    print(f"{customer} has been added to the queue.")
    ticket_number += 1
    return ticket_number

def serve_customer(q):
    if not q.empty():
        customer = q.get()
        print(f"{customer} is being served.")
    else:
        print("No customers in the queue.")

ticket_number = 1

ticket_number = new_customer(ticket_number, q)
ticket_number = new_customer(ticket_number, q)
ticket_number = new_customer(ticket_number, q)

serve_customer(q)
serve_customer(q)
serve_customer(q)
serve_customer(q)

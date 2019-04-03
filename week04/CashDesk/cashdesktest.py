from batchbill import *
values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)
desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()
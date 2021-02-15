from datetime import date


def server_cost(d1, m1, y1, d2, m2, y2):
    c_date = date(y1, m1, d1)
    d_date = date(y2, m2, d2)




    if c_date == d_date:
        cost = 20
        return cost
    else:
        num_days = (d_date - c_date).days
        num_months = (d_date.year - c_date.year) * 12 + (d_date. month - c_date. month)
        num_years = num_days/365.242
        

        if num_days <= 30:
            cost = 30 * num_days
            return cost
        elif  num_days >= 30 and num_years <= 1:
            cost = 1000 * num_months
            return cost
        else:
            cost = 20000
            return cost


server_created_date = input('Enter the data the server was created like (d m y): ')

server_deleted_date = input('Enter the data the server was deleted like (d m y): ')

if __name__ == '__main__':
    d1M1Y1 = server_created_date.split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])


    d2M2Y2 = server_deleted_date.split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')

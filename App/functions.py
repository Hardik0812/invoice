from datetime import date

def getcurrentfinancialyear():
    current_month = date.today().month
    current_year = date.today().year
    last_year = str(current_year - 1)
    next_year = str(current_year + 1)
    if current_month <= 3:
        return last_year[2:] + "/" + str(current_year)[2:]
    else:
        return str(current_year)[2:] + "/" + next_year[2:]


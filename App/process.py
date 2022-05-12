from .function import getcurrentfinancialyear
from .models import Invoice

def increment_invoice_number():
        last_invoice = Invoice.objects.all().order_by('invoice_id').last()
        if not last_invoice:
            return '01' + "-" + getcurrentfinancialyear()
        invoice_no = str(last_invoice)
        invoice_str = invoice_no.split('-')[:1]
        new_invoice_int = int(invoice_str[0])
        new_invoice_str = str(new_invoice_int + 1)
        if int(new_invoice_str)<10:
            new_invoice_no = str("0" + new_invoice_str + "-" + getcurrentfinancialyear())
        else:
            new_invoice_no = str(new_invoice_str + "-" + getcurrentfinancialyear())
        return new_invoice_no
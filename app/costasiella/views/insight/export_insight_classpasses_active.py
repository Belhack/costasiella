import io

from django.utils.translation import gettext as _
from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, FileResponse
from django.db.models import Q
from django.template.loader import get_template, render_to_string


# from django.template.loader import render_to_string
# rendered = render_to_string('my_template.html', {'foo': 'bar'})

import jwt
from .jwt_settings import jwt_settings

from ...modules.graphql_jwt_tools import get_user_from_cookie
from ...models import AppSettings
from ...dudes.insight_account_classpasses_dude import InsightAccountClasspassesDude
# from ..modules.gql_tools import require_login_and_permission, get_rid


# Create your views here.
def export_excel_insight_classpasses_active(request, year):
    """
    Export 

    :param: POST: year: int year (yyyy)
    """
    import openpyxl

    user = get_user_from_cookie(request)
    if not user.has_perm('costasiella.view_insight'):
        raise Http404("Permission denied")

    iac_dude = InsightAccountClasspassesDude()
    data = iac_dude.get_classpasses_active_year_data(year)

    wb = openpyxl.workbook.Workbook(write_only=True)
    ws_header = [
        _("Relation"),
        _("Classpass"),
        _("Start"),
        _("Expiration"),
        _("Price")
    ]

    for month in range(1, 13):
        month_data = data[month]
        ws = wb.create_sheet(title=_(str(year) + "-" + str(month)))
        ws.append(ws_header)

        for classpass in month_data:
            data_list = [
                classpass.account.full_name,
                classpass.organization_classpass.name,
                classpass.date_start,
                classpass.date_end,
                classpass.organization_classpass.price
            ]

            ws.append(data_list)

    # # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    wb.save(buffer)


    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)

    filename = _('classpasses_active') + '_' + str(year) + '.xlsx'

    return FileResponse(buffer, as_attachment=True, filename=filename)

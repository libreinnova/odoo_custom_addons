import logging
import pprint

from odoo import http
from odoo.http import request
from odoo.addons.payment_redsys.controllers.main import RedsysController

_logger = logging.getLogger(__name__)


class RedsysResult(RedsysController):

    @http.route(
        ['/payment/redsys/result/<page>'],
        type='http',
        auth='public',
        methods=['GET'],
        website=True,
    )
    def redsys_result(self, page, **vals):
        if page == 'redsys_result_ok' and vals:
            _logger.debug(
                'Redsys: entering form_feedback with post data %s', pprint.pformat(vals)
            )
            request.env['payment.transaction'].sudo().form_feedback(vals, 'redsys')
        return super(RedsysResult, self).redsys_result(page=page, **vals)

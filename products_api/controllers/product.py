# -*- coding: utf-8 -*-

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.exceptions import AccessError

import logging

_logger = logging.getLogger(__name__)


class ProductAPI(http.Controller):

    REQUIRED_API_KWARGS = []

    def _check_user_credentials(self, **kwargs):
        error_args = []
        error_msg = ''

        for arg in self.REQUIRED_API_KWARGS:
            if arg not in kwargs:
                error_args.append(arg)

        if not request.httprequest.headers.get('Api-Key'):
            error_args.append('api_key')

        if error_args:
            error_msg = "Mandatory argument not provided in request: %s"%(', '.join(error_args))
        else:
            user = request.env['res.users'].sudo().search([('api_key', '=', request.httprequest.headers.get('Api-Key'))])
            if not user:
                error_msg = 'API key is not valid. Please provide valid key.'

        return error_msg

    @http.route('/api/v1/product/<int:product_id>', methods=['GET'], type='json', auth='public', csrf=False)
    def product_details(self, product_id, **kwargs):
        product_obj = request.env['product.product']

        error = self._check_user_credentials(**kwargs)
        if error:
            _logger.error('Product details api called: %s', error)
            return {'error': error}

        _logger.info('Product details api called: %s', kwargs.get('api_key'))

        response = {}
        user = request.env['res.users'].sudo().search([('api_key', '=', request.httprequest.headers.get('Api-Key'))])

        try:
            product_data = product_obj.with_env(request.env(user=user.id)).search_read([('id', '=', product_id)],\
                ['name', 'list_price', 'standard_price', 'qty_available', 'categ_id'])
            if not product_data:
                response = {'error': 'Product ID provided not valid.'}
            else:
                response = product_data[0]
        except AccessError as e:
            response = {'error': "Sorry, you are not allowed to access documents of type 'Product'"}

        return response
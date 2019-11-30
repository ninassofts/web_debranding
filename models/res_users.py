from odoo import models, api, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    odoobot_state = fields.Selection(selection=[],string="Bot Status")


    def is_admin(self):
        # By default Python functions starting with _ are considered private methods.
        # Private methods (such as _is_admin) cannot be called remotely
        return self._is_admin()

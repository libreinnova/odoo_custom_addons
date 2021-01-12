
from odoo import api, fields, models, exceptions, _


class L10nEsAeatMod190Report(models.Model):
    _inherit = 'l10n.es.aeat.mod190.report'

    @api.multi
    def button_confirm(self):
        """
        Overwrite this method to fix rounding error on compute 'percepciones' and 'retenciones' validation
        """
        for report in self:
            valid, valid_error = True, ''
            if self.casilla_01 != len(report.partner_record_ids):
                valid = False

            percepciones = 0.0
            retenciones = 0.0
            for line in report.partner_record_ids:
                percepciones += \
                    line.percepciones_dinerarias + \
                    line.percepciones_en_especie + \
                    line.percepciones_dinerarias_incap + \
                    line.percepciones_en_especie_incap

                retenciones += \
                    line.retenciones_dinerarias + \
                    line.retenciones_dinerarias_incap

            if self.casilla_02 != round(percepciones, 4):
                valid = False
                valid_error += _('Percepciones: %s != %s\n' % (self.casilla_02, percepciones))

            if self.casilla_03 != round(retenciones, 4):
                valid = False
                valid_error += _('Retenciones: %s != %s\n' % (self.casilla_03, retenciones))

            if not valid:
                raise exceptions.UserError(
                    _("You have to recalculate the report before confirm it.\n%s") % valid_error)
        self._check_report_lines()
        return super(L10nEsAeatMod190Report, self).button_confirm()

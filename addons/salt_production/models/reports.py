from datetime import datetime, timedelta

from odoo import api, fields, models, tools


def get_periods_query(base_query, periods=None, group_by=''):
    periods = periods or [
        ("Today", "where date(time) = CURRENT_DATE"),
        (
            "This month to date",
            "where date(time) <= CURRENT_DATE and "
            f"date(time) >= '{(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')}'"
        ),
        (
            "This year to date",
            "where date(time) <= CURRENT_DATE and "
            f"date(time) >= '{(datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')}'"
        ),
        ("Overall to date", "where date(time) <= CURRENT_DATE"),
    ]



    queries = []
    id = 1
    for period_name, where_query in periods:
        query = base_query.replace("<PERIOD>", period_name)
        query = query.replace("<ID>", str(id))
        query = f'{query} {where_query} {group_by}'
        queries.append(query)
        id += 1

    return " UNION ALL ".join(queries)


class WashingReportPeriodsSummary(models.Model):
    _name = 'salt_production.washing_report_periods_summary'
    _description = 'salt_production.washing_report_periods_summary'
    _auto = False

    period = fields.Char(string="Period")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    effective_working_hours = fields.Float(string='Effective working hours')
    total_production = fields.Float(string='Total production')
    productivity_per_hour = fields.Float(string='Productivity per hour')
    total_washing_losses = fields.Float(string='Total washing losses')
    water_load_salt_losses = fields.Float(string='Water load salt losses')
    washing_losses = fields.Float(string='Washing losses')

    def init(self):

        base_query = """
        select CAST('<ID>' AS text) as "id",
        CAST('<PERIOD>' AS text) as "period",
        sum(effectivehr) as "effective_working_hours",
        salt_production_crystalizer.id as crystalizer_id,
        sum(rawsalt) as "total_production",
        sum(rawsalt)/sum(effectivehr) as "productivity_per_hour",
        sum(waterloadloss) + sum(washinglosscalc) as "total_washing_losses",
        sum(waterloadloss) as "water_load_salt_losses", sum(washinglosscalc)
         as "washing_losses"
        from salt_production_washing
        left join salt_production_crystalizer on
        salt_production_crystalizer.id = salt_production_washing.crystalizer_id
        """

        query = get_periods_query(
            base_query, None, 'group by salt_production_crystalizer.id')

        tools.drop_view_if_exists(
            self._cr, 'salt_production_washing_report_periods_summary')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_washing_report_periods_summary AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)


class RefinaryReportPeriodsSummary(models.Model):
    _name = 'salt_production.refinary_report_periods_summary'
    _description = 'salt_production.refinary_report_periods_summary'
    _auto = False

    period = fields.Char(string="Period")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    coarse_salt = fields.Float(string='Coarse salt (MTons)')
    fine_salt = fields.Float(string='Fine salt (MTons)')
    powder_salt = fields.Float(string='Powder salt (MTons)')
    total_production = fields.Float(string='Total production (MTons)')
    effective_working_hours = fields.Float(string='Effective working hours')
    productivity_per_hour = fields.Float(string='Productivity per hour')
    production_losses = fields.Float(string='Production losses')

    def init(self):

        base_query = """
        select CAST('<ID>' AS text) as "id",
         CAST('<PERIOD>' AS text) as "period", sum(effectivehr)
          as "effective_working_hours",
        salt_production_crystalizer.id as crystalizer_id,
        sum(coarse) as "coarse_salt",
        sum(finesalt) as "fine_salt",
        sum(powdersalt) as "powder_salt",
        sum(coarse)+sum(finesalt)+sum(powdersalt) as "total_production",
        (sum(coarse)+sum(finesalt)+sum(powdersalt))/sum(effectivehr)
         as "productivity_per_hour",
        sum(lossrefine) as "production_losses"
        from salt_production_refine
        left join salt_production_crystalizer on
        salt_production_crystalizer.id = salt_production_refine.crystalizer_id
        """

        query = get_periods_query(
            base_query, None, 'group by salt_production_crystalizer.id')

        tools.drop_view_if_exists(
            self._cr, 'salt_production_refinary_report_periods_summary')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_refinary_report_periods_summary AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)

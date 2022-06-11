from bdb import effective
from odoo import models, fields, api
from datetime import datetime


class WaterPump(models.Model):
    _name = 'salt_production.water_pump'
    _description = 'salt_production.water_pump'
    _rec_name = 'name'

    code = fields.Char(required=True)
    name = fields.Char(required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]

    def write(self, vals):
        # raise Exception('hello')
        print('hello hello')
        return super().write(vals)


class WaterContainer(models.Model):
    _name = 'salt_production.water_container'
    _description = 'salt_production.water_container'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    area = fields.Float("Area", digits=(12,3))

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]


class Crystalizer(models.Model):
    _name = 'salt_production.crystalizer'
    _description = 'salt_production.crystalizer'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    area = fields.Float("Area", digits=(12,3))

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name already exists!"),
        ('code_uniq', 'unique (code)', "Code already exists!"),
    ]


class FeedEvaporator(models.Model):
    _name = 'feedevaporator'
    _description = 'salt_production.feed_evaporate'


    time = fields.Datetime(string="Time" ,required=True)
    water_container_id = fields.Many2one("salt_production.water_container", string="Evaporator",required=True)
    no_nitrogen = fields.Char(string="Bags (Nitrogen)",required=True)
    no_tsp = fields.Char(string="Bags (TSP)",required=True)

    _sql_constraints = [
        # ('name_uniq', 'unique (name)', "Name already exists!"),
        # ('code_uniq', 'unique (wa)', "Code already exists!"),
    ]



class WidthSaltPlate(models.Model):
    _name = 'widthsaltplate'
    _description = 'salt_production.withsaltplate'


    time = fields.Datetime(string="Time" ,required=True)
    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystalizer",required=True)
    average= fields.Float('Average of Test (cm)', digits=(12,2),compute="_compute_average")
    timeperoid = fields.Char('Month Year')

    top1 = fields.Float('Top Point 1', digits=(12,3))
    btm1 = fields.Float('Btm Point 1', digits=(12,3))
    dif1 = fields.Float('Diff Point 1', digits=(12,3),compute="_compute_total")
    space1= fields.Char('sample 1', readonly=True)

    top2 = fields.Float('Top Point 2', digits=(12,3))
    btm2 = fields.Float('Btm Point 2', digits=(12,3))
    dif2 = fields.Float('dif Point 2', digits=(12,3),compute="_compute_total2")
    space2 = fields.Char('sample 2', readonly=True)

    top3 = fields.Float('Top Point 3', digits=(12,3))
    btm3 = fields.Float('Btm Point 3', digits=(12,3))
    dif3 = fields.Float('dif Point 3', digits=(12,3),compute="_compute_total3")
    space3 = fields.Char('sample 3', readonly=True)

    top4 = fields.Float('Top Point 4', digits=(12,3))
    btm4 = fields.Float('Btm Point 4', digits=(12,3))
    dif4 = fields.Float('dif Point 4', digits=(12,3),compute="_compute_total4")
    space4 = fields.Char('sample 4', readonly=True)

    top5 = fields.Float('Top Point 5', digits=(12,3))
    btm5 = fields.Float('Btm Point 5', digits=(12,3))
    dif5 = fields.Float('dif Point 5', digits=(12,3),compute="_compute_total5")
    space5 = fields.Char('sample 5', readonly=True)

    top6 = fields.Float('Top Point 6', digits=(12,3))
    btm6 = fields.Float('Btm Point 6', digits=(12,3))
    dif6 = fields.Float('dif Point 6', digits=(12,3),compute="_compute_total6")
    space6 = fields.Char('sample 6', readonly=True)

    top7 = fields.Float('Top Point 7', digits=(12,3))
    btm7 = fields.Float('Btm Point 7', digits=(12,3))
    dif7 = fields.Float('dif Point 7', digits=(12,3),compute="_compute_total7")
    space7 = fields.Char('sample 7', readonly=True)
    


    

    _sql_constraints = [
        # ('name_uniq', 'unique (name)', "Name already exists!"),
        # ('code_uniq', 'unique (wa)', "Code already exists!"),
    ]

    
    @api.depends("btm1")
    def _compute_total(self):
        for record in self:
            record.dif1 = record.top1 - record.btm1

    @api.depends("btm2")
    def _compute_total2(self):
        for record in self:
            record.dif2 = record.top2 - record.btm2

    @api.depends("btm3")
    def _compute_total3(self):
        for record in self:
            record.dif3 = record.top3 - record.btm3

    @api.depends("btm4")
    def _compute_total4(self):
        for record in self:
            record.dif4 = record.top4 - record.btm4

    @api.depends("btm5")
    def _compute_total5(self):
        for record in self:
            record.dif5 = record.top5 - record.btm5

    @api.depends("btm6")
    def _compute_total6(self):
        for record in self:
            record.dif6 = record.top6 - record.btm6

    @api.depends("btm7")
    def _compute_total7(self):
        for record in self:
            record.dif7 = record.top7 - record.btm7

    @api.depends("average")
    def _compute_average(self):
        for record in self:
            if(record.dif7 > 0):
                record.average = ((record.dif1 + record.dif2 +record.dif3 
                +record.dif4 +record.dif5 + record.dif6 + record.dif7)/7)*100

            elif(record.dif6 > 0):
                record.average = ((record.dif1 + record.dif2 +record.dif3 
                +record.dif4 +record.dif5 + record.dif6 )/6)*100

            elif(record.dif5 > 0):
                record.average = ((record.dif1 + record.dif2 +record.dif3 
                +record.dif4 +record.dif5  )/5)*100

            elif(record.dif4 > 0):
                record.average = ((record.dif1 + record.dif2 +record.dif3 
                +record.dif4   )/4)*100

            elif(record.dif3 > 0):
                record.average = ((record.dif1 + record.dif2 +record.dif3 
                   )/3)*100

            elif(record.dif2 > 0):
                record.average = ((record.dif1 + record.dif2 )/2)*100
            
            elif(record.dif1 > 0):
                record.average = (record.dif1  )*100

    
    
class ProjectedProd(models.Model):
    _name = 'salt_production.projectedprod'
    _description = 'salt_production.ProjectedProd'

    code = fields.Char('Code')
    # name = fields.Char(required=True)
    time = fields.Datetime(string="Time" ,required=True)
    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystalizer",required=True)
    cycle = fields.Selection([
        ('Cycle1/2022','Cycle1/2022'),('Cycle2/2022','Cycle2/2022'),('Cycle3/2022','Cycle3/2022'),
        ('Cycle1/2023','Cycle1/2023'),('Cycle2/2023','Cycle2/2023'),('Cycle3/2023','Cycle3/2023'),
        ('Cycle1/2024','Cycle1/2024'),('Cycle2/2024','Cycle2/2024'),('Cycle3/2024','Cycle3/2024'),
        ('Cycle1/2025','Cycle1/2025'),('Cycle2/2025','Cycle2/2025'),('Cycle3/2025','Cycle3/2025'),
        ], string="Cycle",required=True)

    stime = fields.Date(string="Start Time" )
    etime = fields.Date(string="End Time" )
    days = fields.Char(string="Days" , compute="_compute_total5")
    average = fields.Float(string= "Calc Average Layer(cm)")
    
    area = fields.Float("Area CR", digits=(12,3), related = "crystalizer_id.area")
    projected=fields.Integer(string="Projected Production", required=True)
    calcprod=fields.Integer(string="Calc Prod (area x avg)", compute="_compute_prod")
    vari=fields.Float(string="Prjected - Calc", compute="_compute_var")

    _sql_constraints = [
        # ('name_uniq', 'unique (name)', "Name already exists!"),
        # ('code_uniq', 'unique (code)', "Code already exists!"),
    ]
    # @api.depends("etime")
    def _compute_total5(self):
        for record in self:
            start=fields.Datetime.to_datetime(record.stime)
            end=fields.Datetime.to_datetime(record.etime)
            record.days = ( end - start).days


    @api.depends("average")
    def _compute_prod(self):
        for record in self:
            record.calcprod = record.average * record.area

    def _compute_var(self):
        for record in self:
            record.vari = record.projected - record.calcprod




    

    

class Washing(models.Model):
    _name = 'salt_production.washing'
    _description = 'salt_production.washing'

    time = fields.Datetime(string="Time" ,required=True)
    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystalizer",required=True)
    # average= fields.Float('Average of Test (cm)', digits=(12,2),compute="_compute_average")
    cycle = fields.Selection([
        ('Cycle1/2022','Cycle1/2022'),('Cycle2/2022','Cycle2/2022'),('Cycle3/2022','Cycle3/2022'),
        ('Cycle1/2023','Cycle1/2023'),('Cycle2/2023','Cycle2/2023'),('Cycle3/2023','Cycle3/2023'),
        ('Cycle1/2024','Cycle1/2024'),('Cycle2/2024','Cycle2/2024'),('Cycle3/2024','Cycle3/2024'),
        ('Cycle1/2025','Cycle1/2025'),('Cycle2/2025','Cycle2/2025'),('Cycle3/2025','Cycle3/2025'),
        ], string="Cycle",required=True)
    trips=fields.Integer(string="No of Trips")
    truckweight=fields.Float(string="Truck Estimated Wt")
    raw=fields.Float(string="Raw Incoming",compute="_compute_prod")
    belt1=fields.Float(string="Weigh Scale Belt Output")
    whicheverisless = fields.Float(string="Less above",compute="compareless")
    waterload=fields.Integer(string="Water Load %")
    waterloadloss=fields.Float(string="Water Load Loss", compute="waterloadlosscalc")
    rawsalt=fields.Float(string="Raw Salt Gross",compute="_compute_raw")
    cat = fields.Selection([
        ('Single','Single'),('Double','Double'),('Tripple','Tripple')
        ], string="Category of wash",required=True)
    
    washingloss=fields.Float(string="Washing Loss %")
    washinglosscalc=fields.Float(string="Washing Loss", compute="washingslosscalc")
    washedsalt=fields.Float(string="Raw Salt Net",compute="_compute_washed")
    belt2=fields.Float(string="Weigh Scale Belt 2")
    washedsalt2=fields.Float(string="Salt after belt 2",compute="_compute_washed2")
    belt3=fields.Float(string="Weigh Scale Belt 3")
    washedsalt3=fields.Float(string="Salt after belt 3",compute="_compute_washed3")
    stime = fields.Datetime(string="Start Time harvesting" )
    etime = fields.Datetime(string="End Time Harvesting" )
    hours = fields.Float(string="Hours" , compute="_compute_hours" , digits=(12,2))
    # days = fields.Char(string="Days" , compute="_compute_total5")
    interuption=fields.Integer(string="Interrupted Hrs")
    effectivehr=fields.Integer(string="effective Hrs",compute="_compute_effectivehr")
    perhrprod=fields.Float(string="Prod / Hr" , compute="_prodperhr")
    remarks=fields.Char(string="Remarks")

    @api.depends("belt1", "raw")
    def compareless(self):
        for record in self:
            belt1 = record.belt1 or 0
            raw = record.raw or 0
            less_value = belt1 if belt1 < raw else raw
            print(less_value)
            record.whicheverisless = less_value

    @api.depends("washingloss")
    def washingslosscalc(self):
        for record in self:
            
                record.washinglosscalc = record.rawsalt - record.washedsalt

    @api.depends("rawsalt")
    def waterloadlosscalc(self):
        for record in self:
            
                record.waterloadloss = record.whicheverisless - record.rawsalt
          

    @api.depends("effectivehr")
    def _prodperhr(self):
        for record in self:
            if(record.effectivehr > 0):
                record.perhrprod = record.washedsalt / record.effectivehr
            else:
                record.perhrprod = 0

    

    @api.depends("interuption")
    def _compute_effectivehr(self):
        for record in self:
            record.effectivehr = record.hours - record.interuption

    
    
    @api.depends("etime")
    def _compute_hours(self):
        for record in self:
            if(record.etime):
                start=fields.Datetime.to_datetime(record.stime)
                end=fields.Datetime.to_datetime(record.etime)
                record.hours = (end - start).total_seconds()/(60*60)
            else:
                record.hours=0
    
    
    
    


    @api.depends("truckweight")
    def _compute_prod(self):
        for record in self:
            record.raw = record.trips * record.truckweight

    @api.depends("waterload")
    def _compute_raw(self):
        for record in self:
            record.rawsalt = record.whicheverisless- (record.whicheverisless *  record.waterload /100)
    
    @api.depends("washingloss")
    def _compute_washed(self):
        for record in self:
            record.washedsalt =record.rawsalt- (record.rawsalt *  record.washingloss /100)
    
    @api.depends("belt3")
    def _compute_washed3(self):
        for record in self:
            record.washedsalt3 = record.washedsalt2  - record.belt3
    
    @api.depends("belt2")
    def _compute_washed2(self):
        for record in self:
            record.washedsalt2 = record.washedsalt  - record.belt2

    _sql_constraints = [
        # ('name_uniq', 'unique (name)', "Name already exists!"),
        # ('code_uniq', 'unique (code)', "Code already exists!"),
    ]



 
class Refine(models.Model):
    _name = 'salt_production.refine'
    _description = 'salt_production.refine'


    time = fields.Datetime(string="Time" ,required=True)

    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystalizer",required=True)
    customer= fields.Char(string="Customer")
    saleorder= fields.Char(string="Purchase Order")
    cycle = fields.Selection([
        ('Cycle1/2022','Cycle1/2022'),('Cycle2/2022','Cycle2/2022'),('Cycle3/2022','Cycle3/2022'),
        ('Cycle1/2023','Cycle1/2023'),('Cycle2/2023','Cycle2/2023'),('Cycle3/2023','Cycle3/2023'),
        ('Cycle1/2024','Cycle1/2024'),('Cycle2/2024','Cycle2/2024'),('Cycle3/2024','Cycle3/2024'),
        ('Cycle1/2025','Cycle1/2025'),('Cycle2/2025','Cycle2/2025'),('Cycle3/2025','Cycle3/2025'),
        ], string="Cycle",required=True)
    catincome = fields.Selection([
        ('Single','Single'),('Double','Double'),('Tripple','Tripple')
        ], string="Category Income",required=True)
    rawincome= fields.Float(string="Raw Incoming from wash")
    coarse= fields.Float(string="Coarse Salt (Mtons)")
    finesalt= fields.Float(string="Fine Salt (Mtons)")
    coarseAndFine= fields.Float(string="Coarse + Fine" , compute="_coarsefine")
    powdersalt= fields.Float(string="Powder Salt")
    totalrefine= fields.Float(string="Coarse + Fine + Powder", compute="_totalrefinesalt")
    lossrefine= fields.Float(string="Loss on Refine", compute="refineloss")
    lossrefinePerc= fields.Float(string="Loss Refine %", compute="refinelossPerc")
    
    stime = fields.Datetime(string="Start Time" )
    etime = fields.Datetime(string="End Time " )
    hours = fields.Float(string="Hours worked" , compute="_compute_hours" , digits=(12,2))
    # days = fields.Char(string="Days" , compute="_compute_total5")
    interuption=fields.Float(string="Interrupted Hrs")
    effectivehr=fields.Integer(string="effective Hrs", compute="_compute_effectivehr")
    perhrprod=fields.Float(string="Prod / Hr" , compute="_prodperhr")
    coarsePerc=fields.Float(string="Coarse Salt %", compute="_coarse")
    finePerc=fields.Float(string="Fine Salt %" , compute="_fine")
    powderPerc=fields.Float(string="Powder Salt %" , compute="_powder")
    totalPerc=fields.Float(string="Total %" , compute="_totalPerc")

    remarks=fields.Char(string="Remarks")

    @api.depends("lossrefine")
    def refinelossPerc(self):
        for record in self:
            if(record.rawincome):
                record.lossrefinePerc = (   record.totalrefine/ record.rawincome *100 )
            else:
                record.lossrefinePerc = 0


    @api.depends("totalrefine")
    def refineloss(self):
        for record in self:
            record.lossrefine = record.rawincome - record.totalrefine

    

    @api.depends("totalrefine")
    def _totalPerc(self):
        for record in self:
            record.totalPerc = (record.coarsePerc +
             record.finePerc +record.powderPerc)


    @api.depends("totalrefine")
    def _powder(self):
        for record in self:
            if(record.totalrefine > 0):
                record.powderPerc = (record.powdersalt / record.totalrefine)*100
            else:
                record.powderPerc = 0

    @api.depends("totalrefine")
    def _fine(self):
        for record in self:
            if(record.totalrefine > 0):
                record.finePerc = (record.finesalt / record.totalrefine)*100
            else:
                record.finePerc = 0

    @api.depends("totalrefine")
    def _coarse(self):
        for record in self:
            if(record.totalrefine > 0):
                record.coarsePerc = (record.coarse / record.totalrefine)*100
            else:
                record.coarsePerc = 0
    

           

    @api.depends("effectivehr")
    def _prodperhr(self):
        for record in self:
            if(record.effectivehr > 0):
                record.perhrprod = record.totalrefine / record.effectivehr
            else:
                record.perhrprod = 0


    @api.depends("powdersalt")
    def _totalrefinesalt(self):
        for record in self:
            record.totalrefine = record.coarseAndFine + record.powdersalt

    @api.depends("interuption")
    def _compute_effectivehr(self):
        for record in self:
            if(record.interuption > 0):
                record.effectivehr = record.hours - record.interuption
            else:
                record.effectivehr= record.hours
    
    @api.depends("finesalt")
    def _coarsefine(self):
        for record in self:
            record.coarseAndFine = record.coarse + record.finesalt

    @api.depends("etime")
    def _compute_hours(self):
        for record in self:
            if(record.etime):
                start=fields.Datetime.to_datetime(record.stime)
                end=fields.Datetime.to_datetime(record.etime)
                record.hours = (end - start).total_seconds()/(60*60)
            else:
                record.hours=0
    





class Productionconsume(models.Model):
    _name = 'salt_production.productionconsume'
    _description = 'salt_production.refine'


    time = fields.Datetime(string="Time" ,required=True)
    cycle = fields.Selection([
        ('Cycle1/2022','Cycle1/2022'),('Cycle2/2022','Cycle2/2022'),('Cycle3/2022','Cycle3/2022'),
        ('Cycle1/2023','Cycle1/2023'),('Cycle2/2023','Cycle2/2023'),('Cycle3/2023','Cycle3/2023'),
        ('Cycle1/2024','Cycle1/2024'),('Cycle2/2024','Cycle2/2024'),('Cycle3/2024','Cycle3/2024'),
        ('Cycle1/2025','Cycle1/2025'),('Cycle2/2025','Cycle2/2025'),('Cycle3/2025','Cycle3/2025'),
        ], string="Cycle")
    petrol= fields.Float(string="Petrol (Galons)")
    diesel= fields.Float(string="Diesel (Galons)")
    water= fields.Float(string="Water (Galons)")
    electricity= fields.Float(string="Electricity (KW)")
    additives=fields.Float(string="Additives ")
    production = fields.Integer(string="Total Production")
    consume = fields.Float(string="Consumption/Mton", compute="_consume")

    @api.depends("production")
    def _consume(self):
        for record in self:
            if (record.petrol > 0):
                record.consume = record.production / record.petrol
            elif(record.diesel > 0):
                record.consume = record.production / record.diesel
            else:
                record.consume = record.consume



class Burnerconsume(models.Model):
    _name = 'salt_production.burnerconsume'
    _description = 'salt_production.refine'


    time = fields.Datetime(string="Time" ,required=True)
    cycle = fields.Selection([
       ('Cycle1/2022','Cycle1/2022'),('Cycle2/2022','Cycle2/2022'),('Cycle3/2022','Cycle3/2022'),
        ('Cycle1/2023','Cycle1/2023'),('Cycle2/2023','Cycle2/2023'),('Cycle3/2023','Cycle3/2023'),
        ('Cycle1/2024','Cycle1/2024'),('Cycle2/2024','Cycle2/2024'),('Cycle3/2024','Cycle3/2024'),
        ('Cycle1/2025','Cycle1/2025'),('Cycle2/2025','Cycle2/2025'),('Cycle3/2025','Cycle3/2025'),
        ], string="Cycle")
    petrol= fields.Float(string="Petrol")
    diesel= fields.Float(string="Diesel")
    water= fields.Float(string="water")
    electricity= fields.Float(string="Electricity")
    additives=fields.Float(string="Additives")
    production = fields.Integer(string="Total Production")

    consume = fields.Float(string="Consumption/Mton", compute="_consume")

    @api.depends("production")
    def _consume(self):
        for record in self:
            if (record.petrol > 0):
                record.consume = record.production / record.petrol
            elif(record.diesel > 0):
                record.consume = record.production / record.diesel
            else:
                record.consume = record.consume

     
  

class Pump(models.Model):
    _name = 'salt_production.pump'
    _description = 'salt_production.pump'


    time = fields.Datetime(string="Date of Entry" ,required=True)
    water_pump_id = fields.Many2one("salt_production.water_pump", string="Water Pump",required=True)
    
    stime = fields.Datetime(string="Start Time Pump" )
    etime = fields.Datetime(string="End Time Pump" )
    hours = fields.Float(string="Hours worked" , compute="_compute_hours" , digits=(12,2))
    statusOP = fields.Selection([
        ('Operating','Operating'),('Non-Operating','Non-Operating')
        ], string="Status")
    remarks = fields.Char(string="Remarks")
    volume = fields.Float(string="Volume (m^3)")
    capacity = fields.Float(string="Capacity (m^3/h)", compute="_compute_capacity")



    @api.depends("etime")
    def _compute_hours(self):
        for record in self:
            if(record.etime):
                start=fields.Datetime.to_datetime(record.stime)
                end=fields.Datetime.to_datetime(record.etime)
                record.hours = (end - start).total_seconds()/(60*60)
            else:
                record.hours=0

    @api.depends("volume")
    def _compute_capacity(self):
        for record in self:
            if(record.hours):
                
                record.capacity = record.volume/record.hours
            else:
                record.capacity=0


class Analysis(models.Model):
    _name = 'salt_production.analysis'
    _description = 'salt_production.analysis'


    time = fields.Datetime(string="Date of Entry" ,required=True)
    sampletime = fields.Date(string="Sample Taken at" )
    testperf = fields.Date(string="Test Performed at" )
    crystalizer_id = fields.Many2one("salt_production.crystalizer", string="Crystalizer",required=True)

    cat = fields.Selection([
        ('Raw Salt','Raw Salt'),('Washed-1','Washed-1'),('Washed-2','Washed-2'),('Washed-3','Washed-3')
        ,('Washed-4','Washed-4')
        ], string="Category")
    
    analysis_line_ids = fields.One2many('analysis.lines', 'analysis_id', string="Analysis Uper Lines")


class Analysislines(models.Model):
    _name = 'analysis.lines'
    _description = 'salt_production analysislines'

    tests = fields.Char(string="Tests")
    unit = fields.Char(string="Unit")
    testmethod = fields.Char(string="Test Method")
    scoretest= fields.Char(string="Score")
    remarks = fields.Char(string="Remarks")

    analysis_id = fields.Many2one('salt_production.analysis', string="analysis below line")



  


 

    


   
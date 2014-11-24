from openerp.osv import osv
from openerp.osv import fields
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import time

class Vehicle(osv.osv):

    _name = 'vehicle.vehicle'
     
    _columns = {
            'name':fields.char('Model Name', size=64, required=False, readonly=False),
            'frame_no':fields.char('Frame Number',size=64,required=False),
            
        }
Vehicle()

class Sms(osv.osv):

    _name = 'sms.sms'
    
    def on_change_sms(self, cr, uid, ids, partner, context=None):
        values = {}
        if partner:
            res_partner=self.pool.get('res.partner').browse(cr,uid,partner)
            phone=res_partner.phone
            mobile=res_partner.mobile
            street= res_partner.street
            street2=res_partner.street2
            city=res_partner.city
            state=res_partner.state_id.name
            pin=res_partner.zip
            if not street:
                street=""
            if not street2:
                street2=""
            if not city:
                city=""
            if not state:
                state=""
            if not pin:
                pin=""
            #===================================================================
            # if street or street2 or city or state or pin:
            address= street+'\n'+street2+'\n'+city+'\n'+state+'\n'+pin
            # else:
            #     address=False
            #===================================================================
            model=res_partner.model
            frame=res_partner.frame_no
            reg_no=res_partner.reg_no
                   
            values={'ph_no':phone,
                        'mobile_no':mobile,
                        'address':address,
                        'model':model,
                        'frame_no':frame,
                        'reg_no':reg_no
                        }
        return {'value' :values}
    
        
     
    _columns = {
            'model':fields.many2one('vehicle.vehicle','Model Name',required=False, readonly=False),
            'frame_no':fields.char('Frame Number',size=64,required=False),
            'reg_no':fields.char('Registration Number',size=64),
            'partner':fields.many2one('res.partner','Customer',required=False),
            'address':fields.text('Address',size=256),
            'ph_no':fields.char('Phone Number',size=64),
            'mobile_no':fields.char('Mobile No:',size=64),
            'service_due':fields.char('Type Of Service Due',size=128),
            'due_from':fields.date('Due From:'),
            'due_to':fields.date('Due To:'),
            
        }
    _defaults ={
                'due_from': lambda *a: time.strftime(DEFAULT_SERVER_DATE_FORMAT),
                }
Sms()

class sale(osv.osv):
    
    _inherit = 'res.partner'
    
    _columns = {
            
            'frame_no':fields.char('Frame Number',size=64),
            'model':fields.many2one('vehicle.vehicle','Model Name',required=False, readonly=False),     
            'reg_no':fields.char('Registration Number',size=64),
        }
sale()


class settings(osv.osv):
    
    _name='sms.settings'
    
    _columns = {
            
            'url':fields.char('URL',size=64),
            'sender_id':fields.char('Sender ID',size=64),
            'password':fields.char('Password',size=64),
            'user_name':fields.char('User Name',size=64),
        }
settings()
    
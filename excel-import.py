import openerp.osv
import xlrd

class ExcelImport(osv.osv_memory):
    _name = "excel.import"
    _columns = {
                
                'data_file': fields.binary('File Excel', required=True, filters='*.xls'),
                
                }   
    
    
    def import_excel(self, cr, uid, ids, context=None):
        val = self.browse(cr, uid, ids)[0]
       
        data = base64.decodestring(val.data_file)      
        
        excel = xlrd.open_workbook(file_contents = data)    
        
        sh = excel.sheet_by_index(0) 
         
        
        print sh.name, sh.nrows, sh.ncols 
         
       
        for rx in range(sh.nrows): 
            print [sh.cell(rx, ry).value for ry in range(sh.ncols)] 
     
   
 
    return {}    

ExcelImport()
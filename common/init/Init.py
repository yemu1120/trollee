from common.init.InitConfig import InitConfig
from common.init.InitExcel import InitExcel
'''
@初始化用例文件和配置文件
'''
class Init(InitConfig,InitExcel):
    column=''     
    '''
    @各关键字的列号在很多地方会用到
    '''                                                                                                                                                                                                                                                           
    nameCol,urlCol,methodCol,paramCol,fileCol,headerCol,part101Col,part201Col,part301Col,section101Col,\
    section201Col,section301Col,resTextCol,resHeaderCol,statusCodeCol,expressionCol,statusCol,timeCol,\
    init001Col,restore001Col,dyparam001Col,key001Col,value001Col,headerManagerCol,DBCol,IterationCol=\
    '','','','','','','','','','','','','','','','','','','','','','','','','',''
    fileData,email,userParams,userParamsValue='','','',''
    ncols=''
    '''
    @初始化用例文件和配置文件
    @param reportDate: 
    @param path:
    @param file:
    @param sheetName:   
    '''
    def initFile(self,reportDate,path,file,sheetName):      
        self.fileData,self.email,self.userParams,self.userParamsValue=self.initConfig(path)
        book=self.getBook(path,file)  
        sheet,nrows,self.ncols=self.getSheet(reportDate,path,sheetName,file,book)     
        self.column=self.getColumn(file,sheet)    
        self.nameCol=self.column[0]
        self.urlCol=self.column[1]
        self.methodCol=self.column[2]
        self.paramCol=self.column[3]
        self.fileCol=self.column[4]
        self.headerCol=self.column[5]
        self.part101Col=self.column[6]
        self.part201Col=self.column[7]
        self.part301Col=self.column[8]
        self.section101Col=self.column[9]
        self.section201Col=self.column[10]
        self.section301Col=self.column[11]
        self.resTextCol=self.column[12]
        self.resHeaderCol=self.column[13]
        self.statusCodeCol=self.column[14]
        self.expressionCol=self.column[15]
        self.statusCol=self.column[16]
        self.timeCol=self.column[17]
        self.init001Col=self.column[18]
        self.restore001Col=self.column[19]
        self.dyparam001Col=self.column[20]
        self.key001Col=self.column[21]
        self.value001Col=self.column[22]
        self.headerManagerCol=self.column[23]
        self.DBCol=self.column[24]
        self.IterationCol=self.column[25]                                                                                                                                                                                                                                   
        return sheet,nrows   
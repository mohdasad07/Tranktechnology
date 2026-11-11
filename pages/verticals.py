class vertical:
    def __init__(self, page):
        self.page = page

        # verticals locator
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')

        self.trading = page.locator('//li[@data-id="trading"]')

        self.stock = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')

        self.pap = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')

        self.cfd = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')

        self.mas = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        
        self.tsd = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')

        self.wtd = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_options = [self.stock,self.pap,self.cfd,self.mas,self.tsd,self.wtd]

        # Retail and ecom
        self.retail_ecom = page.locator('//li[@data-id="retailEcommerce"]')

        self.web_dev= page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
   
        self.app_dev= page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_options =[self.web_dev,self.app_dev]

        # Health

        self.health= page.locator('(//strong[text() ="Healthcare"])[1]')

        self.diet= page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthapp= page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_options =[self.diet,self.healthapp]

        # Fintech

        self.fintech= page.locator('(//strong[text() ="Fintech"])[1]')
        self.pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto= page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        
        self.fintect_options =[self.pos,self.crypto]

        # Custom App
        self.custom = page.locator('//strong[text()="Custom App"]')
        self.desk = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.mad = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.dad = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.cc = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erp = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.elm = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.real = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.ccd = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_options = [self.desk,self.hrm,self.mad,self.dad,self.cc,self.erp,self.elm,self.real,self.ccd]



    def trading_options_clicking(self):
        for i in self.trading_options:
            self.vertical.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def retail_ecom_clicking(self):
        for i in self.retail_options:
            self.vertical.hover()
            self.retail_ecom.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def health_options_clicking(self):
        for i in self.health_options:
           self.vertical.hover()
           self.health.hover()
           i.click()
           self.page.wait_for_load_state('load')
           self.page.go_back()

    def fintech_options_selction(self):
        for i in self.fintect_options:
            self.vertical.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    
    
        



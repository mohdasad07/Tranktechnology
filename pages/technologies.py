class technology:
    def __init__(self, page):
        self.page = page

        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.md=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.cd=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.bc=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.np=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ld=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.dd=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.jd=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.ed=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.od=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.wpd=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.sd=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nd=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.wcd=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.pd=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.wid=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.rd=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.ecomm_options=[self.md,self.cd,self.bc,self.cs,self.np,self.ld,self.dd,self.jd,self.ed,self.od,self.wpd,self.sd,self.nd,self.wcd,self.pd,self.wid,self.rd]



        # mobileapp development

        self.mobileapp = page.locator('//li[@data-id="mobileApp"]')
        self.rnat = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.emp = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xmd = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kmd = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.fmd = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.imd = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.smd = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.abd = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobapp_options= [self.rnat,self.emp,self.xmd,self.kmd,self.fmd,self.imd,self.smd,self.abd]

        self.ai = page.locator('(//a[.//strong[text()="Artificial Intelligence"]])[1]')

    def ecomm_options_clicking(self):
        for i in self.ecomm_options:
            self.tech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def mobapp_options_clicking(self):
        for i in self.mobapp_options:
            self.tech.hover()
            self.mobileapp.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    # Artifical development
    def ai_options_clicking(self):
       self.tech.hover()
       self.ai.hover()
       self.ai.click()
       self.page.wait_for_load_state('load')
       self.page.go_back()

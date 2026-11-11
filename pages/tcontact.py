class contact:
    def __init__(self, page):
        self.page = page

        self.contact= page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.contact.click()

        self.name= page.locator('(//input[@placeholder="Your Name"])[2]')
        self.name.fill("Asad khan")
        self.email= page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.email.fill('asad@gmail.com')
        self.otp= page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.otp.fill('2564')
        self.com= page.locator('(//input[@placeholder="Your Company"])[2]')
        self.com.fill('wipro')
        self.cser= page.locator('(//select[@name="service"])[2]')
        self.cser.select_option('Web Development')
        self.phn= page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.phn.fill('9880918566')
        self.mess= page.locator('(//textarea[@placeholder="Message"])[2]')
        self.mess.fill('Automation')
        self.sub = page.locator('//input[@type="submit" and @name="contact"]')

        self.contact_options= [self.name,self.email,self.otp,self.com,self.cser,self.phn,self.mess,self.sub]

    def contact_clicking(self):
            self.contact.click()
            self.page.wait_for_load_state('load')
    
            for i in self.contact_options:
                print(i.count())
                

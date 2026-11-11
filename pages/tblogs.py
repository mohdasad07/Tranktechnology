class blog:
    def __init__(self, page):
        self.page = page

        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.ap=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[1]')
        self.ari=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.cm=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.cd=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.dm=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ec=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.em=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.gd=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.sc=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.sd=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.ud=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.wed=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.blog_elements=[ self.ap, self.ari, self.cm, self.cd, self.dm, self.ec, self.em, self.gd, self.sc, self.sd, self.ud, self.wed]

    def blogs_elements_clicking(self):
        self.blog.click()
        self.page.wait_for_load_state('load')

        for b in self.blog_elements:
            b.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
             

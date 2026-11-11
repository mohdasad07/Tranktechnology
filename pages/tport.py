class tport:
    def __init__(self, page):
        self.page = page

        self.port = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')

    def port_clicking(self):
        self.port.click()
        self.page.wait_for_load_state('load')
        print(self.page.url)
        
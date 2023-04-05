from BaseApp import SeleniumActions


class BasePageHelpers(SeleniumActions):

    def find_link(self, link, text_option):
        self.loadUrl()
        assert self.find_elements(link)[0].text == text_option

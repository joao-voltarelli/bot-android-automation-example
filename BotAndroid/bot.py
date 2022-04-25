from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution=None):
        
        # Start process
        self.start_emulator()

    def start_emulator(self):
        # Open blue stacks app
        self.execute("C:\\Program Files\\BlueStacks_nxt\\HD-Player")

        # Open the form app inside blue stacks emulator
        self.open_form()

        # Fill the example form
        self.fill_form("Joao Victor", "Voltarelli", "joao@email.com", "19", "123456789", 
                       "I need information about Python and BotCity.")

        # Back to android home screen
        self.home_screen()

        # Close all open apps
        self.close_all_apps()

    def home_screen(self):
        # Use blue stacks shortcut to get back to home screen
        self.type_keys(['ctrl', 'shift', '1'])

    def close_all_apps(self):
        # Use bluestacks shortcut to see all open apps
        self.type_keys(['ctrl', 'shift', '5'])

        # Find the "clear all" option and click to close all apps
        if not self.find_text( "clear_all", matching=0.95, waiting_time=10000):
            self.not_found("clear_all")
        self.click()

    def open_form(self):
        # Find and click to open forms app
        if not self.find( "app_form", matching=0.97, waiting_time=60000):
            self.not_found("app_form")
        self.click_relative(20, -35)
        
        # Select the form to be filled
        if not self.find( "form", matching=0.97, waiting_time=30000):
            self.not_found("form")
        self.click()
        
        # Click on fill option
        if not self.find( "fill_out", matching=0.97, waiting_time=10000):
            self.not_found("fill_out")
        self.click()

    def fill_form(self, first_name, last_name, email, phone_ddd, phone_number, information):
        # Find and fill the name field
        if not self.find( "name", matching=0.97, waiting_time=10000):
            self.not_found("name")
        self.click_relative(272, 7)
        self.paste(first_name)
        self.tab(1000)
        self.paste(last_name)

        # Find and fill the email field
        if not self.find( "email", matching=0.97, waiting_time=10000):
            self.not_found("email")
        self.click_relative(284, 7)
        self.paste(email, 1000)

        # Find and fill the phone field
        if not self.find( "phone", matching=0.97, waiting_time=10000):
            self.not_found("phone")
        self.click_relative(271, 6)
        self.paste(phone_ddd)
        self.tab(1000)
        self.paste(phone_number)

        self.page_down()

        # Find and fill the requesting field
        if not self.find( "requesting", matching=0.97, waiting_time=10000):
            self.not_found("requesting")
        self.click_relative(288, 21)
        self.paste(information, 1000)

        # Submit the form at final
        if not self.find( "submit_form", matching=0.97, waiting_time=10000):
            self.not_found("submit_form")
        self.click(5000)


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

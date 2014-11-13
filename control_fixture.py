from controller import Controller

# Initialize the control fixture
class ControlFixture(object):
    """Control Fixture for the controller in the DRL fridges"""
    def __init__(self, update_period):
        """Constructor for ControlFixture
        Arguments:
        - update_period: Period between updates in seconds in soft real time.
        """
        super(ControlFixture, self).__init__()
        self.update_period = update_period

if __name__ == '__main__':
    control_fixture = ControlFixture(10)
    c = Controller()
    

# # Run the controller
# while (True):
#     c.update()
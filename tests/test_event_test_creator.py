import datetime
import unittest2

from google.appengine.ext import testbed

from helpers.event.event_test_creator import EventTestCreator

from models.event import Event
from models.team import Team

class TestEventTeamCreator(unittest2.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        for team_number in range(7):
            Team(id = "frc%s" % team_number,
                 team_number = team_number).put()
        
    def tearDown(self):
        self.testbed.deactivate()

    def testCreates(self):
        EventTestCreator.createPastEvent()
        EventTestCreator.createFutureEvent()
        EventTestCreator.createPresentEvent()

        #TODO: assert the events got created properly -gregmarra 20130416



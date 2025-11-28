from ddt import ddt, data, unpack
from frameworkproj.Util import Util
import pytest
import softest
from testcase.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerify(softest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_objects(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Util()

    @data(*Util.readdata_from_csv(
        r"C:\Users\Fleek\PycharmProjects\PythonProjectwithpomandunittest\testcase\tdata.csv"
    ))
    @unpack
    def test_search_flight(self, departlocation, gotolocation, stop1, stop2, stop3):

        # SEARCH
        search_flight_result = self.lp.searchflight(departlocation, gotolocation)
        self.lp.pagescroll()

        # FILTER RESULTS
        nonstop_list = search_flight_result.filter_flights(stop1)
        onestop_list = search_flight_result.filter_flights(stop2)
        twostop_list = search_flight_result.filter_flights(stop3)

        # ASSERTIONS
        self.ut.assertListItems(nonstop_list, stop1)
        self.ut.assertListItems(onestop_list, stop2)
        self.ut.assertListItems(twostop_list, stop3)

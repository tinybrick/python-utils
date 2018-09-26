from unittest import TestCase

class testProperties(TestCase):
    def test_string_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf")
        self.assertEquals("testString", PROPS.getString("test.string.key"))

    def test_int_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf")
        self.assertEquals(100, PROPS.getInt("test.int.key"))

    def test_boolean_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf")
        self.assertEquals(False, PROPS.getBoolean("test.boolean.key"))

    def test_password_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf")
        self.assertEquals("P@550rd", PROPS.getPassword("test.password.username"))

    def test_env_properties(self):
        """ Demo for usage """
        from utils import Properties
        import os
        os.environ["PROFILE"] = "test"
        self.assertEquals("test", Properties.getEnv("PROFILE"))

    def test_date_properties(self):
        """ Demo for usage """
        from utils import Properties
        from utils import YearMonth
        self.assertEquals(YearMonth().format(), Properties.getCurrentYearMonth().format())

    def test_other_string_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf", environment="other")
        self.assertEquals("otherTestString", PROPS.getString("test.other.string.key"))

    def test_other_int_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf", environment="other")
        self.assertEquals(100, PROPS.getInt("test.int.key"))

    def test_other_boolean_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf", environment="other")
        self.assertEquals(True, PROPS.getBoolean("test.other.boolean.key"))

    def test_other_password_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf", environment="other")
        self.assertEquals("P@550rd", PROPS.getPassword("test.other.password.username"))

    def test_non_existing_properties(self):
        """ Demo for usage """
        from utils import Properties
        PROPS = Properties("utils/tests/test.conf")
        self.assertEquals("Non-existing", PROPS.getString("test.none", "Non-existing"))

    def test_non_existing_properties_with_exception(self):
        """ Demo for usage """
        from utils import Properties
        import configparser
        PROPS = Properties("utils/tests/test.conf")
        try:
            self.assertEquals("Non-existing", PROPS.getString("test.none"))
        except configparser.NoOptionError as e:
            print("Cache you!")
            return
        self.fail()


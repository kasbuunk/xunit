class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1
        self.log += "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "

class TestCaseTest(TestCase):
    def setUp(self):
        self.test= WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 1

    def summary(self):
        return "%d run, 0 failed" % self.runCount

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
